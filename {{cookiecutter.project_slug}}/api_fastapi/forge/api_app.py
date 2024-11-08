import sentry_sdk
from starlette.middleware.cors import CORSMiddleware

from api.forge import app as forge_app
from api.forge.sdk.routes.main import api_router
from fastapi import FastAPI
from fastapi.routing import APIRoute


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


if (
    forge_app.SETTINGS_MANAGER.SENTRY_DSN
    and forge_app.SETTINGS_MANAGER.ENVIRONMENT != "local"
):
    sentry_sdk.init(dsn=str(forge_app.SETTINGS_MANAGER.SENTRY_DSN), enable_tracing=True)

app = FastAPI(
    title=forge_app.SETTINGS_MANAGER.PROJECT_NAME,
    openapi_url=f"{forge_app.SETTINGS_MANAGER.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

# Set all CORS enabled origins
if forge_app.SETTINGS_MANAGER.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=forge_app.SETTINGS_MANAGER.all_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=forge_app.SETTINGS_MANAGER.API_V1_STR)
