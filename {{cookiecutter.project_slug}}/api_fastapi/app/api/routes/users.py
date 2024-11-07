from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def hello() -> dict[str, str]:
    return {"Hello": "World"}
