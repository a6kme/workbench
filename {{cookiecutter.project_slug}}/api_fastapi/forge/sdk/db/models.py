"""
Adding models here will allow Alembic to autogenerate migrations for them. The configuration
in `api/alembic/env.py` will use the `SQLModel.metadata` to generate the migrations.
"""

from datetime import datetime

from pydantic import EmailStr
from sqlalchemy import BigInteger, Column, DateTime, func

# https://github.com/fastapi/sqlmodel/discussions/828
from sqlmodel import Field, SQLModel  # type: ignore[reportUnknownVariableType]


class UserModel(SQLModel, table=True):
    __tablename__ = "auth_user"  # type: ignore

    id: int | None = Field(
        sa_column=Column(BigInteger, primary_key=True, autoincrement=True),
        default=None,
    )
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str = Field(default=None, max_length=255)
    federated_user_id: str = Field(default=None, max_length=255)
    avatar_url: str | None = Field(default=None, max_length=255)
    created_at: datetime = Field(
        default_factory=datetime.now, sa_column=Column(DateTime, default=func.now())
    )
    updated_at: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column(DateTime, default=func.now(), onupdate=func.now()),
    )
