from sqlalchemy.orm import Session
from ..models.crime import Crime

class CrimeRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create_crime(self , crime: Crime):
        self.db.add(crime)
        self.db.commit()
        return crime
    
    def get_by_id(self , id: str):
        return self.db.query(Crime).filter(Crime.id == id).first()
    
    def get_by_nome(self, nome: str):
        return self.db.query(Crime).filter(Crime.nome == nome).first()
    
    def update(self , crime: Crime):
        self.db.commit()
        self.db.refresh(crime)
        return crime
    
    def get_by_crime(self):
        return self.db.query(Crime).all()
    
    def get_by_ip(self , id: str):
        return self.db.query(Crime).filter(Crime.id == id).all()
    
    def delete_by_id(self , id: str):
        return self.db.query(Crime).filter(Crime.id == id).first()
    
    def delete(self , crime: Crime):
        self.db.delete(crime)
        self.db.commit()
        return crime