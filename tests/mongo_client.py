from motor.motor_asyncio import AsyncIOMotorClient
import os
from uuid import UUID
import logging
import json
from datetime import datetime


class MongoHandler():
    def __init__(self, db_name: str, collection_name: str):
        self.__db_name = db_name
        self.__collection_name = collection_name
        self.__db_client = AsyncIOMotorClient(
            os.environ.get('TEST_MONGODB_URL')
        )

    async def get_sample_resource(self, resource_id: UUID):
        return await self.__db_client[self.__db_name][self.__collection_name]\
            .find_one({'_id': UUID(resource_id)})

    async def insert_sample_resource(self, sample_resource: dict):
        await self.__db_client[self.__db_name][self.__collection_name]\
            .insert_one(sample_resource)

    async def drop_database(self):
        await self.__db_client.drop_database(self.__db_name)

    def close_conn(self):
        self.__db_client.close()


class MongoClient():
    def __init__(self, db_name: str, collection_name: str):
        self.__db_handler = MongoHandler(db_name, collection_name)

    async def __aenter__(self):
        await self.__create_mock_data()
        return self.__db_handler

    async def __create_mock_data(self):
        with open('tests/mock_data/sample_resource.json', 'r') as f:
            sample_resource_json = json.load(f)
            for sample_resource in sample_resource_json:
                sample_resource['create_time'] = datetime.strptime(
                    sample_resource['create_time'], '%Y-%m-%d %H:%M:%S'
                )
                sample_resource['update_time'] = datetime.strptime(
                    sample_resource['update_time'], '%Y-%m-%d %H:%M:%S'
                )
                sample_resource['_id'] = UUID(sample_resource['_id'])
                await self.__db_handler.insert_sample_resource(sample_resource)

    async def __aexit__(
        self, exception_type,
        exception_value, exception_traceback
    ):
        if exception_type:
            logging.error(exception_value)

        await self.__db_handler.drop_database()
        self.__db_handler.close_conn()
        return False
