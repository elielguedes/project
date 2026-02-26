from fastapi import APIRouter , Path , Depends , Request , HTTPException
from ..database import pegar_sessao
from ..core.config import verificar_token
from ..core.dependecies import Validator_Adm
from sqlalchemy.orm import Session
from ..schemas.registros import RegistrosCreate , RegistrosResponse
from ..service.registros import CreateRecords , get_res


RouterRecords = APIRouter(prefix="/resgistros" , tags=["registros"])

@RouterRecords.post("/create_records", response_model = RegistrosResponse)
async def create_recor(Data: RegistrosCreate , db: Session = Depends(pegar_sessao), user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not autheticator")
    Create = CreateRecords(db , Data)
    return Create

@RouterRecords.get("/get_records")
async def get_records(db: Session = Depends(pegar_sessao), user = Depends(verificar_token) , adm = Depends(Validator_Adm)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autheticator")
    if not adm:
        raise HTTPException(status_code = 400 , detail = "Not authorizator ")
    get_record = get_res(db)
    return get_record