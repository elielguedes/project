from pydantic import BaseModel, Field, EmailStr
from typing import Annotated

class UserBase(BaseModel):
    name: str = Field(..., max_length=100)
    email: EmailStr

class UserCreate(UserBase):
    senha: Annotated[str, Field(max_length = 100)]

class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    adm: bool

