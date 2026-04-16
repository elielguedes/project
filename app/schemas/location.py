from pydantic import BaseModel , Field 
from typing import Annotated
from enum import Enum
from uuid import UUID

class Municipio(str , Enum):
    BELOHORIZONTE = "Belo Horizonte"
    BRASILIA = "Brasilia"
    MONTESCLAROS = "Montes Claros"
    
class LocationBase(BaseModel):
    cod_municipio: Annotated[int , Field(...,le = 999999)]
    risp: Annotated[str , Field(..., max_length = 6)]
    rmbh: Annotated[str , Field(...,max_length = 100)]
    nome_municipio: Municipio = Municipio.BRASILIA

class LocationCreate(LocationBase):
    pass

class LocationResponse(BaseModel):
    id: UUID
    cod_municipio: Annotated[int, Field(description="Código do município", le=999999)]
    risp: Annotated[str, Field(max_length=6)]
    rmbh: Annotated[str, Field(max_length=100)]
    nome_municipio: Municipio
