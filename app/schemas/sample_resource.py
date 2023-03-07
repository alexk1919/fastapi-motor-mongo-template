from uuid import uuid4, UUID
from datetime import datetime
import logging
from pymongo import ReturnDocument

from app.conf.config import Config
from app.db.db import AsyncIOMotorClient
from app.models.sample_resource_common import SampleResourceDB
from app.common.util import uuid_masker


__db_name = Config.app_settings.get('db_name')
__db_collection = 'sample_resource'


async def create_sample_resource(
    conn: AsyncIOMotorClient,
    name: str
) -> SampleResourceDB:
    new_sample_resource = SampleResourceDB(
        id=uuid4(),
        name=name,
        create_time=datetime.utcnow(),
        update_time=datetime.utcnow(),
        deleted=False,
    )
    logging.info(
        f'Inserting sample resource {name} into db...'
    )
    await conn[__db_name][__db_collection].insert_one(
        new_sample_resource.mongo()
    )
    logging.info(
        f"Sample resource {name} has inserted into db"
    )
    return new_sample_resource


async def get_sample_resource(
    conn: AsyncIOMotorClient,
    resource_id: UUID
) -> SampleResourceDB | None:
    logging.info(f"Getting sample resource {uuid_masker(resource_id)}...")
    sample_resource = await conn[__db_name][__db_collection].find_one(
        {"$and": [
            {'_id': resource_id},
            {'deleted': False},
        ]},
    )
    if None is sample_resource:
        logging.info(f"Resource {uuid_masker(resource_id)} is None")
    return sample_resource


async def update_sample_resource(
    conn: AsyncIOMotorClient,
    resource_id: UUID,
    resource_data: dict
) -> SampleResourceDB | None:
    logging.info(
        f'Updating sample resource {uuid_masker(str(resource_id))}...'
    )
    sample_resource = \
        await conn[__db_name][__db_collection].find_one_and_update(
            {"$and": [
                {'_id': resource_id},
                {'deleted': False},
            ]},
            {'$set': {
                **resource_data,
                "update_time": datetime.utcnow(),
            }},
            return_document=ReturnDocument.AFTER,
        )
    if None is sample_resource:
        logging.error(
            f"Sample resource {uuid_masker(str(resource_id))} not exist"
        )
    else:
        logging.info(
            f'Sample resource {uuid_masker(str(resource_id))} updated'
        )
    return sample_resource


async def delete_sample_resource(
    conn: AsyncIOMotorClient,
    resource_id: UUID,
) -> SampleResourceDB | None:
    logging.info(
        f"Deleting sample resource {uuid_masker(str(resource_id))}..."
    )

    sample_resource = await conn[__db_name][__db_collection].\
        find_one_and_update(
        {"$and": [
            {'_id': resource_id},
            {'deleted': False},
        ]},
        {'$set': {
            "deleted": True,
            "update_time": datetime.utcnow(),
        }},
        return_document=ReturnDocument.AFTER,
    )

    if None is sample_resource:
        logging.error(
            f"Sample resource {uuid_masker(str(resource_id))} not exist"
        )
    else:
        logging.info(
            f'Sample resource {uuid_masker(str(resource_id))} deleted'
        )
    return sample_resource
