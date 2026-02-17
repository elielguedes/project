from pydantic import BaseModel , EmailStr , Field
from typing import Annotated
from uuid import UUID

class LoguinBase(BaseModel):
    email: EmailStr
    senha: Annotated[str , Field(max_length = 100)]

class LoguinCreate(LoguinBase):
    senha: Annotated[str , Field(max_length = 100)]

class LoguinResponse(BaseModel):
    acess_token: str
    refresh_token: str
