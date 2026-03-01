from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user import UserCreate
from ..core.config import bcrypt_context
from ..repositories.user import UserRepo

class UserService:

    def __init__(self , repository: UserRepo):
        self.repository = repository
    
    def create_user(self , data: UserCreate):
        User_exist = self.repository.get_by_email(data.email)
        if User_exist:
            raise HTTPException(status_code = 401 ,detail = "User Not autheticator")
        
        senha_cript = bcrypt_context.hash(data.senha)
        new_user = User(name = data.name , email = data.email , senha = senha_cript , adm = data.adm)

        return self.repository.create(new_user)