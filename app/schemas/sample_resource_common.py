from pydantic import constr
from datetime import datetime
from uuid import UUID

from .mongo_model import MongoModel


def to_lower_camel_case(string: str) -> str:
    split_str = string.split('_')
    return split_str[0] + ''.join(word.capitalize() for word in split_str[1:])


class SampleResourceBase(MongoModel):
    name: constr(max_length=255)


class SampleResource(SampleResourceBase):
    id: UUID
    create_time: datetime
    update_time: datetime
    deleted: bool
