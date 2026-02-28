from pydantic import BaseModel , Field , field_validator
from typing import Annotated
from enum import Enum
from uuid import UUID

class municipio(Enum):
    BELOHORIZONTE = "Belo Horizonte"
    BRASILIA = "Brasilia"
    MONTESCLAROS = "Montes Claros"
    
class LocationBase(BaseModel):
    cod_municipio = Annotated[int , Field(ge = 6 , le = 6)]
    risp: Annotated[str , Field(ge = 6 , le = 6)]
    rmbh: Annotated[str , Field(max_length = 100)]
    nome_municipio: Annotated[str , Field(max_length = 100 , default_factory = municipio)]

class LocationCreate(LocationBase):
    pass

class LocationResponse(BaseModel):
    id: UUID
    cod_municipio = Annotated[int , Field(ge = 6 , le = 6)]
    risp: Annotated[str , Field(ge = 6 , le = 6)]
    rmbh: Annotated[str , Field(max_length = 100)]
    nome_municipio: Annotated[str , Field(max_length = 100 , default_factory = municipio)]
