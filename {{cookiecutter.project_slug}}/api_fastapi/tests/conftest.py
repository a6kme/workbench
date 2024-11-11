import re

import psycopg
import pytest
from alembic import command
from alembic.config import Config
from httpx import ASGITransport, AsyncClient
from sqlalchemy import create_engine

from api.forge.api_app import app
from api.forge.sdk.db.client import db_client
from api.settings import settings


@pytest.fixture(scope="session")
def setup_test_database():
    """
    Create a test database and run migrations before running tests
    After test session is complete, drop the test database
    """
    # Connect to the main database and create test database
    database_url = str(settings.DATABASE_URL)
    database_url = re.sub(r"\+psycopg", "", database_url)
    try:
        with psycopg.connect(database_url, autocommit=True) as conn:
            with conn.cursor() as cur:
                cur.execute("CREATE DATABASE test_db")
        old_db_exists = False
    except psycopg.ProgrammingError:
        print("Test database already exists. Recreating...")
        old_db_exists = True

    if old_db_exists:
        # ask for permission from the user to drop the existing test database
        # TODO: Unable to do this from shell script. Need to find a way to do this
        # response = input(
        #     "Test database already exists. Do you want to drop and recreate it? (y/n): ").strip().lower()

        # if response not in ["y", "yes"]:
        #     raise Exception("Test database setup aborted by user.")

        try:
            with psycopg.connect(database_url, autocommit=True) as conn:
                with conn.cursor() as cur:
                    cur.execute("DROP DATABASE IF EXISTS test_db WITH (FORCE)")

            with psycopg.connect(database_url, autocommit=True) as conn:
                with conn.cursor() as cur:
                    cur.execute("CREATE DATABASE test_db")
        except psycopg.ProgrammingError:
            print("Error creating test database")
            raise Exception("Error creating test database")

    # Update db client with connection to test database
    test_database_url: str = re.sub(r"\/[\w]+$", "/test_db", str(settings.DATABASE_URL))
    db_client.engine = create_engine(str(test_database_url))

    # Run Alembic migrations to set up the database schema
    alembic_cfg = Config("api/alembic.ini")  # Path to your alembic.ini file
    alembic_cfg.set_main_option("sqlalchemy.url", str(test_database_url))
    command.upgrade(alembic_cfg, "head")

    yield  # Run tests

    db_client.engine.dispose()

    # Reconnect to the main database to drop the test database
    with psycopg.connect(database_url, autocommit=True) as conn:
        with conn.cursor() as cur:
            cur.execute("DROP DATABASE IF EXISTS test_db WITH (FORCE)")


# This fixture will run before every test
@pytest.fixture
async def async_client(setup_test_database):  # type: ignore
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://localhost:8000"
    ) as client:
        yield client


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"
