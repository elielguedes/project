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

def update_reg_id(db: Session , id: str , data: RegistrosCreate):
    records = db.query(Registros).filter(Registros.id == id).first()
    if not records:
        raise HTTPException(status_code = 400 , detail = "Registro não encontrado")
    records.qtd = int(data.qtd)
    records.mes = int(data.mes.value)
    records.ano = int(data.ano)
    db.commit()
    db.refresh(records)
    return records

def get_res(db: Session):
    records = db.query(Registros).all()
    if not records:
        raise HTTPException(status_code = 400 , detail = "Regitros não encontrados")
    return records

def get_recor_id(db: Session , id: str):
    records = db.query(Registros).filter(Registros.id == id).all()
    if not records:
        raise HTTPException(status_code = 400 , detail = "Registro não encontrado")
    return records

def delete_record_id(db: Session , id: str):
    records = db.query(Registros).filter(Registros.id == id).first()
    if not records:
        raise HTTPException(status_code = 401 ,detail = "Registro não encontrado")
    db.delete(records)
    db.commit()
    return records