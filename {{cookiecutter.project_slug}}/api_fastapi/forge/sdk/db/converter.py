"""
We would not like to have the db model floating across in the services layer. We would
convert the db models to schema models in the converter layer. This would help in
decoupling the db layer from the services layer. Any property can be defined in the
pydantic schema model.
"""

from api.forge.sdk.db.models import UserModel
from api.forge.sdk.schemas.models import User


def convert_to_user(user: UserModel) -> User:
    return User(
        id=user.id,
        email=user.email,
        full_name=user.full_name,
        federated_user_id=user.federated_user_id,
        avatar_url=user.avatar_url,
        is_active=user.is_active,
        is_superuser=user.is_superuser,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )
