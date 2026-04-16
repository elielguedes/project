from sqlalchemy.orm import Session
from ..models.registros import Registros

class RecordsRepository:
    def __init__(self , db: Session):
        self.db = db
    
    def create_registro(self , registro: Registros) -> Registros:
        self.db.add(registro)
        self.db.commit()
        return registro
    
    def get_by_id(self, id: str) -> list[Registros]:
        return self.db.query(Registros).filter(Registros.id == id).first()
    
    def update(self , registros: Registros) -> Registros:
        self.db.commit()
        self.db.refresh(registros)
        return registros
    
    def get_reg(self) -> list[Registros]:
        return self.db.query(Registros).all()
    
    def get_by_ip(self , id: str) -> list[Registros]:
        return self.db.query(Registros).filter(Registros.id == id).all()
    
    def delete_by_id(self , id: str) -> list[Registros]:
        return self.db.query(Registros).filter(Registros.id == id).first()
    
    def delete(self , registros: Registros) -> list[Registros]:
        self.db.delete(registros)
        self.db.commit()
        return registros