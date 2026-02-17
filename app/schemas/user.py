from pydantic import BaseModel, Field, EmailStr
from typing import Annotated
from uuid import UUID

class UserBase(BaseModel):
    name: str = Field(..., max_length=100)
    email: EmailStr
    adm: bool = Field(default = False)

class UserCreate(UserBase):
    senha: Annotated[str, Field(max_length = 100)]

class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    adm: bool
