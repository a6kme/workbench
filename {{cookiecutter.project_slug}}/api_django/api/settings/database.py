# Database configuration
import os

import dj_database_url

try:
    DATABASE_URL = os.environ["DATABASE_URL"]
except KeyError:
    raise Exception("DATABASE_URL environment variable not set")


DATABASES = {"default": dj_database_url.config(default=DATABASE_URL)}
