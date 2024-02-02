from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import logging

from app.conf.config import Config

load_dotenv()

db_client: AsyncIOMotorClient


async def get_db() -> AsyncIOMotorClient:
    db_name = Config.app_settings.get('db_name')
    return db_client[db_name]


async def connect_and_init_db():
    global db_client
    try:
        db_client = AsyncIOMotorClient(
            Config.app_settings.get('mongodb_url'),
            username=Config.app_settings.get('db_username'),
            password=Config.app_settings.get('db_password'),
            maxPoolSize=Config.app_settings.get('max_db_conn_count'),
            minPoolSize=Config.app_settings.get('min_db_conn_count'),
            uuidRepresentation="standard",
        )
        logging.info('Connected to mongo.')
    except Exception as e:
        logging.exception(f'Could not connect to mongo: {e}')
        raise


async def close_db_connect():
    global db_client
    db_client.close()
    logging.info('Mongo connection closed.')
