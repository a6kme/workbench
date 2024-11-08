from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    id: int | None
    email: str
    full_name: str
    avatar_url: str | None
    is_active: bool
    created_at: datetime


class User(UserBase):
    is_superuser: bool
    federated_user_id: str
    updated_at: datetime


class UserPublic(UserBase): ...
