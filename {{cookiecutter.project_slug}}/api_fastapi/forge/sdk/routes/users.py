from api.forge.sdk.schemas.models import UserPublic
from api.forge.sdk.services.deps import CurrentUser
from fastapi import APIRouter

router = APIRouter()


@router.get("/user/profile", response_model=UserPublic)
async def get_user_profile(user: CurrentUser):
    return user
