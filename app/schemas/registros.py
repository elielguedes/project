from pydantic import BaseModel , Field , field_validator
from typing import Annotated
from datetime import datetime
from uuid import UUID , uuid4

class RegistrosBase(BaseModel):
    crime_id: UUID
    location_id: UUID |None = None
    user_id: UUID |None = None
    qtd: Annotated[int , Field(ge = 1 , le = 10000)]
    mes: Annotated[int , Field(ge = 1 , le = 12)]
    ano: Annotated[int , Field(ge = 1900 , le= 2100)]

    @field_validator("mes")
    @classmethod
    def validator_mes(cls , v):
        if not 1 <= v <= 12:
            raise ValueError("O mês deve estar entre 1 e 12")
        return v

class RegistrosCreate(RegistrosBase):
    pass

class RegistrosResponse(BaseModel):
    id: UUID 
    qtd: Annotated[int , Field(ge = 1 , le = 10000)]
    mes: Annotated[int , Field(ge = 1 , le = 12)]
    ano: Annotated[int , Field(ge = 1900 , le= 2100)]