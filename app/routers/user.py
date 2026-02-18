from fastapi import APIRouter , Depends , HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from ..schemas.user import UserCreate , UserResponse
from ..schemas.loguin import LoguinCreate , LoguinResponse
from ..database import pegar_sessao
from sqlalchemy.orm import Session
from ..models.user import User
from ..service.user import CreateService
from ..service.loguin import LoguinService
from ..core.config import verificar_token
from ..service.loguin import criar_token , LoguinService

router = APIRouter(prefix = "/auth" , tags=["auth"])


@router.post("/create" , response_model = UserResponse)
async def CreateLoguin(data: UserCreate , db: Session = Depends(pegar_sessao)):
    user = CreateService(db , data)
    return user

@router.post("/loguin", response_model = LoguinResponse)
async def Loguin(data: LoguinCreate , db: Session = Depends(pegar_sessao)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not authenticator")
    access_token = criar_token(user.id)
    refresh_token = criar_token(user.id)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }

@router.post("/loguin-form")
async def LoguinForm(dados_formulario: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(pegar_sessao)):
    user = LoguinService(dados_formulario.password , dados_formulario.username , db)
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not authorization")
    access_token = criar_token(user.id)
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("refresh") 
async def refresh(user: User = Depends(verificar_token)):
    access_token = criar_token(user.id)
    return {"access_token": access_token , "token_type": "bearer"}