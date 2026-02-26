from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..schemas.registros import RegistrosCreate
from ..models.registros import Registros

def CreateRecords(db: Session, data: RegistrosCreate):
    new_record = Registros(qtd=data.qtd,mes=data.mes,ano=data.ano,crime_id=str(data.crime_id),location_id=str(data.location_id) if data.location_id else None,user_id=str(data.user_id) if data.user_id else None)
    if not new_record:
        raise HTTPException(status_code = 400 , detail = "Dados incorretos tente novamente")
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

def get_res(db: Session):
    records = db.query(Registros).all()
    if not records:
        raise HTTPException(status_code = 400 , detail = "Dados não encontrados")
    return records