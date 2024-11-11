from typing import Annotated

from fastapi import Depends, Header, HTTPException, status

from api.forge.sdk.schemas.models import User
from api.forge.sdk.services.supabase import supabase_service


async def get_current_user(authorization: Annotated[str | None, Header()] = None) -> User:
    """
    Marking authorization as optional here so that its not marked as required in the OpenAPI spec. Doing 
    this since the generated client SDK will not have headers as required parameter. If the header
    is required parameter in the generated typescript sdk, we will have to pass the authorization header
    in every request which leads to duplication of code. We would ideally want to pass the token only once
    when initializing the client. 

    Look at client.ts in ui for more details.
    """
    if authorization is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="missing authentication header",
        )

    token = authorization.split("Bearer ")[1]
    user = await supabase_service.get_authenticated_user(token)
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]
