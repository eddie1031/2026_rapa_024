from pydantic import BaseModel, Field

from datetime import datetime

class BoardUpsertRequest(BaseModel):
    name: str = Field(min_length=1)


class BoardResponse(BaseModel):
    name: str
    created_at: datetime
    updated_at: datetime





