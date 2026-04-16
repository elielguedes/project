from sqlalchemy.orm import Session
from ..models.location import Location

class LocationRepository:
    def __init__(self , db: Session):
        self.db = db
    
    def create(self , location: Location) -> Location:
        self.db.add(location)
        self.db.commit()
        self.db.refresh(location)
        return location
    
    def get_by_loc(self , id: str) -> list[Location]:
        return self.db.query(Location).filter(Location.id == id).first()
    
    def update(self , location: Location) -> Location:
        self.db.commit()
        self.db.refresh(location)
        return location
    
    def gets(self) -> list[Location]:
        return self.db.query(Location).all()
    
    def get_by_id(self , id: str)-> list[Location]:
        return self.db.query(Location).filter(Location.id == id).all()
    
    def delete_by_id(self , id: str) -> list[Location]:
        return self.db.query(Location).filter(Location.id == id).first()
    
    def delete(self , location: Location) -> Location:
        self.db.delete(location)
        self.db.commit()
        return location

