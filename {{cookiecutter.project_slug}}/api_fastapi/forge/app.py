from pathlib import Path

from api.forge.logger import get_logger
from api.forge.sdk.db.client import db_client
from api.settings import settings

SETTINGS_MANAGER = settings
LOGGER = get_logger(Path(settings.BASE_DIR).parent)
DATABASE = db_client
