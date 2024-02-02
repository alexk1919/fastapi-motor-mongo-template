from pydantic import BaseModel


class GetSampleResourceResp(BaseModel):
    name: str
