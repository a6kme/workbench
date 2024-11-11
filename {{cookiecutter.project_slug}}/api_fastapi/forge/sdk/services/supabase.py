from fastapi import HTTPException, status
from gotrue.types import User as GoTrueUser  # type: ignore
from loguru import logger
from supabase._async.client import AsyncClient as SupabaseClient
from supabase._async.client import create_client

from api.forge import app as forge_app
from api.forge.sdk.schemas.models import User


class SupabaseService:
    def __init__(self) -> None:
        self.supabase_client: SupabaseClient | None = None

    async def create_supabase(self) -> SupabaseClient:
        return await create_client(
            forge_app.SETTINGS_MANAGER.SUPABASE_URL,
            forge_app.SETTINGS_MANAGER.SUPABASE_ANON_KEY,
        )

    async def get_authenticated_user(self, token: str) -> User:
        if not self.supabase_client:
            self.supabase_client = await self.create_supabase()

        try:
            response = await self.supabase_client.auth.get_user(token)
            if response and response.user:
                # Return a User object from database
                return self.get_or_create_user_object_from_db(user=response.user)
        except Exception as e:
            logger.info(f"Error verifying token: {str(e)}")

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="bad authentication token",
        )

    def get_or_create_user_object_from_db(self, user: GoTrueUser) -> User:
        assert user.email is not None

        # Check if user exists in database
        existing_user = forge_app.DATABASE.get_user(federated_user_id=user.id)

        if existing_user:
            return existing_user

        return forge_app.DATABASE.create_user(
            email=user.email,
            federated_user_id=user.id,
            full_name=user.user_metadata.get("full_name", ""),
            avatar_url=user.user_metadata.get("avatar_url", ""),
            federated_provider_response_data=user.user_metadata,
        )


supabase_service = SupabaseService()
