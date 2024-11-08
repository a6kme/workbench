from loguru import logger
from pydantic import EmailStr
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import Session

from api.forge.sdk.db.converter import convert_to_user
from api.forge.sdk.db.models import UserModel
from api.forge.sdk.schemas.models import User
from api.settings import settings


class DBClient:
    def __init__(self) -> None:
        self.engine = create_engine(str(settings.DATABASE_URL))

    def create_user(
        self,
        email: EmailStr,
        full_name: str,
        federated_user_id: str,
        avatar_url: str | None,
        is_active: bool = True,
        is_superuser: bool = False,
    ) -> User:
        try:
            with Session(self.engine) as session:
                new_user = UserModel(
                    email=email,
                    is_active=is_active,
                    is_superuser=is_superuser,
                    full_name=full_name,
                    federated_user_id=federated_user_id,
                    avatar_url=avatar_url,
                )
                session.add(new_user)
                session.commit()
                session.refresh(new_user)
                return convert_to_user(new_user)
        except SQLAlchemyError:
            logger.exception("SQLAlchemyError")
            raise
        except Exception:
            logger.exception("UnexpectedError")
            raise


db_client = DBClient()
