from fastapi import APIRouter , Path , Depends , Request , HTTPException
from ..database import pegar_sessao
from ..core.config import verificar_token
from ..core.dependecies import Validator_Adm
from sqlalchemy.orm import Session
from ..schemas.registros import RegistrosCreate , RegistrosResponse
from ..service.registros import CreateRecords , get_res , get_recor_id , update_reg_id , delete_record_id


RouterRecords = APIRouter(prefix="/resgistros" , tags=["registros"])

@RouterRecords.post("/create_records", response_model = RegistrosResponse)
async def create_recor(Data: RegistrosCreate , db: Session = Depends(pegar_sessao), user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not autheticator")
    Create = CreateRecords(db , Data)
    return Create

@RouterRecords.put("/update_records/{id}" , response_model = RegistrosResponse)
async def update_records(id: str , data: RegistrosCreate , db: Session = Depends(pegar_sessao), user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "Not auutheticator")
    records_update = update_reg_id(db , id , data)
    return records_update

@RouterRecords.get("/get_records", response_model = RegistrosResponse)
async def get_records(db: Session = Depends(pegar_sessao), user = Depends(verificar_token) , adm = Depends(Validator_Adm)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autheticator")
    if not adm:
        raise HTTPException(status_code = 400 , detail = "Not authorizator ")
    get_record = get_res(db)
    return get_record

@RouterRecords.get("/records/{id}")
async def get_records_id(id: str , db: Session = Depends(pegar_sessao), user = Depends(verificar_token), adm = Depends(Validator_Adm)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not autheticator")
    if not adm:
        raise HTTPException(status_code = 401 , detail = "Acesso restrito ")
    records_id =  get_recor_id(db , id)
    return records_id

@RouterRecords.delete("/delete/{id_records}")
async def delete_id(id: str , db: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not authenticator")
    delete = delete_record_id(db , id)
    return delete
    