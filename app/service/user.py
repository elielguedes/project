from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user import UserCreate
from ..core.config import bcrypt_context

def CreateService(db: Session , data: UserCreate):
    user = db.query(User).filter(User.email == data.email).first()
    if user:
        raise HTTPException(status_code = 401 , detail = "E-mail já cadastrado")
    
    senha_crypt = bcrypt_context.hash(data.senha)
    NovoUser = User(name = data.name ,email = data.email, senha = senha_crypt, adm = data.adm)
    db.add(NovoUser)
    db.commit()
    db.refresh(NovoUser)
    return NovoUser