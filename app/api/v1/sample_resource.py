from fastapi import APIRouter, Depends, Response
import logging
from uuid import UUID

from app.db.db import get_db, AsyncIOMotorClient
from app.crud.sample_resource import create_sample_resource as db_create_sample_resource
from app.crud.sample_resource import get_sample_resource_by_id as db_get_sample_resource
from app.crud.sample_resource import update_sample_resource as db_update_sample_resource
from app.crud.sample_resource import delete_sample_resource as db_delete_sample_resource
from app.common.util import mask_uuid
from app.common.error import UnprocessableError

from app.schemas.create_sample_resource import \
    CreateSampleResourceReq, CreateSampleResourceResp
from app.schemas.get_sample_resource import GetSampleResourceResp

router = APIRouter()


@router.post('/', include_in_schema=False, status_code=201)
@router.post('', response_model=CreateSampleResourceResp, status_code=201,
             responses={
                 400: {}
             }
             )
async def create_sample_resource(
    sample_resource_data: CreateSampleResourceReq,
    db: AsyncIOMotorClient = Depends(get_db)
):
    logging.info('Receive create sample resource request')

    sample_resource_db = await db_create_sample_resource(
        db,
        sample_resource_data.name
    )

    return CreateSampleResourceResp(id=sample_resource_db.id)


@router.get('/', include_in_schema=False, status_code=200)
@router.get('', response_model=GetSampleResourceResp, status_code=200,
            responses={
                400: {}
            }
            )
async def get_sample_resource(
    resource: UUID,
    db: AsyncIOMotorClient = Depends(get_db),
):
    logging.info(
        f'Receive get sample resource {mask_uuid(resource)} request'
    )

    sample_resource = await db_get_sample_resource(
        db,
        resource
    )

    if None is sample_resource:
        return Response(status_code=204)

    return GetSampleResourceResp(name=sample_resource.get("name"))


@router.put('/{resource_id}', include_in_schema=False, status_code=200)
@router.put('/{resource_id}', status_code=200,
            responses={
                400: {}
            }
            )
async def update_sample_resource(
    resource_id: UUID,
    sample_resource_data: CreateSampleResourceReq,
    db: AsyncIOMotorClient = Depends(get_db),
):
    logging.info(
        f'Receive update sample resource {mask_uuid(resource_id)} request'
    )

    try:
        await db_update_sample_resource(
            db,
            resource_id,
            sample_resource_data.dict()
        )
    except RuntimeError:
        raise UnprocessableError([])

    return {}


@router.delete('/{resource_id}', include_in_schema=False, status_code=200)
@router.delete('/{resource_id}', status_code=200,
               responses={
                   400: {}
               }
               )
async def delete_sample_resource(
    resource_id: UUID,
    db: AsyncIOMotorClient = Depends(get_db),
):
    logging.info(
        f'Receive delete sample resource {mask_uuid(resource_id)} request'
    )

    try:
        await db_delete_sample_resource(
            db,
            resource_id,
        )
    except RuntimeError:
        raise UnprocessableError([])

    return {}
