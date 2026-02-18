from pydantic import BaseModel , Field
from typing import Annotated
from uuid import UUID

class CrimeBase(BaseModel):
    nome: Annotated[str , Field(max_length = 10000)] |None = None

class CrimeCreate(CrimeBase):
    pass

class CrimeResponse(BaseModel):
    id: UUID
    nome: Annotated[str , Field(max_length = 10000)]