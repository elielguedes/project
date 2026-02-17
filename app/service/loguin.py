from fastapi import HTTPException
from ..models.user import User
from sqlalchemy.orm import Session
from ..schemas.loguin import LoguinCreate
from ..core.config import bcrypt_context , ACESS_TOKEN_MIN , SECRET_KEY , ALGORITHM
from datetime import timedelta , datetime , timezone
from jose import jwt

def LoguinService(senha , email, db: Session):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return False
    elif not bcrypt_context.verify(senha , user.senha):
        return False
    return user

def criar_token(id_user , dur_token: timedelta = timedelta(minutes = ACESS_TOKEN_MIN)):
    date_expire = datetime.now(timezone.utc) + dur_token
    payload = {"sub": str(id_user) , "exp": date_expire}
    jwt_codificado = jwt.encode(payload , SECRET_KEY , algorithm = ALGORITHM)
    return jwt_codificado

