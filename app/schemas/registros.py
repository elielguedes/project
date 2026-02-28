from pydantic import BaseModel , Field 
from pydantic.dataclasses import dataclass
from typing import Annotated
from datetime import datetime
from uuid import UUID , uuid4
from dataclasses import field
from enum import Enum

class Mes(int, Enum):
    JANEIRO = 1
    FEVEREIRO = 2
    MARCO = 3
    ABRIL = 4
    MAIO = 5
    JUNHO = 6 
    JULHO = 7 
    AGOSTO = 8
    SETEMBRO = 9
    OUTUBRO = 10
    NOVEMBRO = 11
    DEZEMBRO = 12
    
@dataclass
class RegistrosBase:
    crime_id: UUID
    mes: Mes
    location_id: UUID |None = None
    user_id: UUID |None = None
    qtd: int = 1
    ano: int = field(default_factory = lambda: datetime.now().year)

    def __post_init__(self):
        if not isinstance(self.mes , Mes):
            raise ValueError("Mês deve estar entre 1 e 12")
        
        if not 1 <= self.qtd <= 1000:
            raise ValueError("quantidade deve ser entre 1 a 1000")
             
        if self.ano < 1900:
            raise ValueError("Ano inválido")

class RegistrosCreate(RegistrosBase):
    pass

class RegistrosResponse(BaseModel):
    id: UUID 
    qtd: Annotated[int , Field(ge = 1 , le = 10000)]
    mes: Annotated[int , Field(ge = 1 , le = 12)]
    ano: Annotated[int , Field(ge = 1900 , le= 2100)]