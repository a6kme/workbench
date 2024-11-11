from fastapi import APIRouter

from api.forge.sdk.schemas.models import UserPublic
from api.forge.sdk.services.deps import CurrentUser

router = APIRouter()


@router.get("/profile/", response_model=UserPublic)
async def get_user_profile(user: CurrentUser):
    return user
