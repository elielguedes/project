from fastapi import APIRouter , Path , Depends , Request , HTTPException
from ..database import pegar_sessao
from ..core.config import verificar_token
from ..core.dependecies import Validator_Adm
from sqlalchemy.orm import Session
from ..schemas.registros import RegistrosCreate , RegistrosResponse
from ..service.registros import RegistrosService
from ..repositories.registros import RecordsRepository

RouterRecords = APIRouter(prefix="/resgistros" , tags=["registros"])

@RouterRecords.post("/create_records", response_model = RegistrosResponse)
async def create_recor(Data: RegistrosCreate , db: Session = Depends(pegar_sessao), user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not autheticator")
    repository = RecordsRepository(db)
    service = RegistrosService(repository)
    return service.create_reg(Data)

@RouterRecords.put("/update_records/{id}" , response_model = RegistrosResponse)
async def update_records(id: str , data: RegistrosCreate , db: Session = Depends(pegar_sessao), user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "Not auutheticator")
    repository = RecordsRepository(db)
    service = RegistrosService(repository)
    return service.update_reg_id(id, data)

@RouterRecords.get("/get_records")
async def get_records(db: Session = Depends(pegar_sessao), user = Depends(verificar_token) , adm = Depends(Validator_Adm)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autheticator")
    if not adm:
        raise HTTPException(status_code = 400 , detail = "Not authorizator ")
    repository = RecordsRepository(db)
    service = RegistrosService(repository)
    return service.get_res()

@RouterRecords.get("/records/{id}")
async def get_records_id(id: str , db: Session = Depends(pegar_sessao), user = Depends(verificar_token), adm = Depends(Validator_Adm)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not autheticator")
    if not adm:
        raise HTTPException(status_code = 401 , detail = "Acesso restrito ")
    repository = RecordsRepository(db)
    service = RegistrosService(repository)
    return service.get_recor_id(id)

@RouterRecords.delete("/delete/{id_records}")
async def delete_id(id: str , db: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not authenticator")
    repository = RecordsRepository(db)
    service = RegistrosService(repository)
    return service.delete_record_id(id)
    