from sqlalchemy.orm import Session
from ..models.location import Location

class LocationRepository:
    def __init__(self , db: Session):
        self.db = db
    
    def create(self , location: Location)-> Location:
        self.db.add(location)
        self.db.commit()
        self.db.refresh(location)
        return location
    
    def get_by_loc(self , id: str)-> str | None:
        return self.db.query(Location).filter(Location.id == id).first()
    
    def update(self , location: Location):
        self.db.commit()
        self.db.refresh(location)
        return location
    
    def gets(self):
        return self.db.query(Location).all()
    
    def get_by_id(self , id: str)-> str:
        return self.db.query(Location).filter(Location.id == id).all()
    
    def delete_by_id(self , id: str) -> Location |None :
        return self.db.query(Location).filter(Location.id == id).first()
    
    def delete(self , location: Location)-> None:
        self.db.delete(location)
        self.db.commit()

