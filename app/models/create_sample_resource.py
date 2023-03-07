from uuid import UUID

from .sample_resource_common import SampleResourceBase, to_lower_camel_case
from .mongo_model import MongoModel


class CreateSampleResourceReq(SampleResourceBase):
    class Config:
        alias_generator = to_lower_camel_case


class CreateSampleResourceResp(MongoModel):
    id: UUID
