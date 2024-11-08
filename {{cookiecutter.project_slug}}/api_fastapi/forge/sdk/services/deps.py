from typing import Annotated

from api.forge.sdk.schemas.models import User
from api.forge.sdk.services.supabase import supabase_service
from fastapi import Depends, Header


async def get_current_user(authorization: Annotated[str, Header()]) -> User:
    token = authorization.split("Bearer ")[1]
    user = await supabase_service.get_authenticated_user(token)
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]
