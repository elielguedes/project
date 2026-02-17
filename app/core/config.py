from fastapi import Depends , HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from dotenv import load_dotenv
from ..models.user import User
from ..database import pegar_sessao
from jose import jwt , JWTError
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY") 
ALGORITHM = os.getenv("ALGORITHM")
ACESS_TOKEN_MIN = int(os.getenv("ACESS_TOKEN_MIN" , 30))

oauth2_schemes = OAuth2PasswordBearer(tokenUrl = "auth/loguin-form", scopes = {})
bcrypt_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

def verificar_token(token: str = Depends(oauth2_schemes), db: Session = Depends(pegar_sessao)):
    try:
        payload = jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code = 401 , detail = "Acess not authorization")
    except JWTError as e:
        raise HTTPException(status_code = 401 , detail = "Acess not authorization")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code = 401 , detail = "Acess not authorization")
    return user