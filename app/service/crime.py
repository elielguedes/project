from fastapi import HTTPException
from ..schemas.crime import CrimeCreate
from sqlalchemy.orm import Session
from ..models.crime import Crime

def Create_Crime(db: Session , data: CrimeCreate):
    crime = Crime(nome = data.nome)
    if not crime:
        raise HTTPException(status_code = 400 , detail = "Crime não registrado")
    
    db.add(crime)
    db.commit()
    return crime

def Update_Crime(db: Session , data: CrimeCreate , id: str):
    crime = db.query(Crime).filter(Crime.id == id).first()
    if not crime:
        raise HTTPException(status_code = 400 , detail = "Crime incorreto")
    crime.nome = str(data.nome)

    db.commit()
    db.refresh(crime)
    return crime

def Get_Crime(db: Session):
    crime = db.query(Crime).all()
    if not crime:
        raise HTTPException(status_code = 400 , detail = "Banco de dados vazio")
    return crime

def Get_Crime_id(db: Session , id: str):
    crime = db.query(Crime).filter(Crime.id == id).all()
    if not crime:
        raise HTTPException(status_code = 400 , detail = "Cadastro não encontrado ")
    return crime

def Delete_Crime(db: Session , id: str):
    crime = db.query(Crime).filter(Crime.id == id).first()
    if not crime:
        raise HTTPException(status_code = 400 , detail = "Cadastro não encontrado ")
    
    db.delete(crime)
    db.commit()
    return crime