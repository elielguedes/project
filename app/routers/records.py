from fastapi import APIRouter , Path , Depends , Request , HTTPException
from ..database import pegar_sessao
from ..core.config import verificar_token
from sqlalchemy.orm import Session
from ..schemas.registros import RegistrosCreate , RegistrosResponse
from ..service.registros import CreateRecords


RouterRecords = APIRouter(prefix="/resgistros" , tags=["registros"])

