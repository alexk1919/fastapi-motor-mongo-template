import pytest_asyncio
from fastapi.testclient import TestClient
import os

from .mongo_client import MongoClient


@pytest_asyncio.fixture()
def env_setup():
    os.environ["MONGODB_DBNAME"] = os.environ.get("TEST_DB_NAME")
    os.environ["MONGODB_URL"] = os.environ.get("TEST_MONGODB_URL")


@pytest_asyncio.fixture()
def test_client(env_setup):
    from app.main import app
    with TestClient(app) as test_client:
        yield test_client


@pytest_asyncio.fixture()
async def mongo_client(env_setup):
    print('\033[92mSetting test db\033[0m')
    async with MongoClient(
        os.environ.get("TEST_DB_NAME"),
        'sample_resource'
    ) as mongo_client:
        yield mongo_client
