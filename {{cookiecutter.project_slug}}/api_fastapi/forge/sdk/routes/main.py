from fastapi import APIRouter

from api.forge.sdk.routes import users

api_router = APIRouter()
api_router.include_router(users.router, prefix="/user", tags=["users"])
