from fastapi import HTTPException
from ..repositories.location import LocationRepository
from ..schemas.location import LocationCreate
from ..models.location import Location

class LocationService:
    def __init__(self , repository: LocationRepository):
        self.repository = repository
    
    def create_location(self , data: LocationCreate):
        location = Location(cod_municipio = data.cod_municipio ,risp = data.risp ,rmbh = data.rmbh , nome_municipio = data.nome_municipio)
        if not location:
            raise HTTPException(status_code = 404 ,detail = "Registro não realizado tente novamente !")
        return self.repository.create(location)
    
    def update_location(self , id: str , data: LocationCreate) -> Location:
        location: Location |None = self.repository.get_by_loc(id)
        if location is None:
            raise HTTPException(status_code = 404 , detail = "Registro não encontrado")
        for field , value in data.model_dump().items():
            setattr(location, field , value)
        
        return self.repository.update(location)
    
    def get_loc(self):
        location = self.repository.gets
        if not location:
            raise HTTPException(status_code = 404 , detail = "Dados não encontrados")
        return location()
    
    def get_loc_id(self , id: str) -> str:
        location = self.repository.get_by_id(id)
        if not location:
            raise HTTPException(status_code = 401 ,detail = "id não encontrado")
        return location
    
    def delete_loc(self , id: str)-> None:
        location: Location | None = self.repository.delete_by_id(id)
        if location is None:
            raise HTTPException(status_code = 404 , detail = "Registro não encontrado ! ")
        self.repository.delete(location)
        