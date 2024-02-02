from fastapi import APIRouter, Depends, Response
import logging
from uuid import UUID

from app.db.db import get_db, AsyncIOMotorClient
from app.schemas.sample_resource import create_sample_resource
from app.schemas.sample_resource import get_sample_resource
from app.schemas.sample_resource import update_sample_resource
from app.schemas.sample_resource import delete_sample_resource

from app.common.util import uuid_masker
from app.common.error import UnprocessableError

from app.models.create_sample_resource import \
    CreateSampleResourceReq, CreateSampleResourceResp
from app.models.get_sample_resource import GetSampleResourceResp

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

    sample_resource_db = await create_sample_resource(
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
        f'Receive get sample resource {uuid_masker(resource)} request'
    )

    sample_resource = await get_sample_resource(
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
        f'Receive update sample resource {uuid_masker(resource_id)} request'
    )

    sample_resource = await update_sample_resource(
        db,
        resource_id,
        sample_resource_data.dict()
    )
    if None is sample_resource:
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
        f'Receive delete sample resource {uuid_masker(resource_id)} request'
    )

    sample_resource = await delete_sample_resource(
        db,
        resource_id,
    )
    if None is sample_resource:
        raise UnprocessableError([])

    return {}
