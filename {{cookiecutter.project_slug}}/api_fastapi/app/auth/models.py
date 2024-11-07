from pydantic import EmailStr
from sqlalchemy import BigInteger, Column

# https://github.com/fastapi/sqlmodel/discussions/828
from sqlmodel import Field, SQLModel  # type: ignore[reportUnknownVariableType]


# Shared properties
class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = Field(default=None, max_length=255)
    federated_user_id: str | None = Field(default=None, max_length=255)
    avatar_url: str | None = Field(default=None, max_length=255)


# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: int = Field(
        sa_column=Column(BigInteger, primary_key=True, autoincrement=True),
    )


# Properties to return via API, id is always required
class UserPublic(UserBase):
    id: int
