from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..schemas.registros import RegistrosCreate
from ..models.registros import Registros

def CreateRecords(db: Session , data: RegistrosCreate):
    records = Registros(qtd = data.qtd ,mes = data.mes , ano = data.ano)
    if not records:
        raise HTTPException(status_code = 400 , detail = "Records not")
    db.add(records)
    db.commit()
    return records