from fastapi import APIRouter , HTTPException , Depends
from ..schemas.location import LocationCreate , LocationResponse
from sqlalchemy.orm import Session
from ..database import pegar_sessao
from ..core.config import verificar_token
from ..repositories.location import LocationRepository
from ..service.location import LocationService

RouterLoc = APIRouter(prefix = "/Location", tags = ["location"])

@RouterLoc.post("/create", response_model = LocationResponse)
async def create(data: LocationCreate , db: Session = Depends(pegar_sessao), user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not authenticator")
    repository = LocationRepository(db)
    service = LocationService(repository)
    return service.create_location(data)

@RouterLoc.put("/update", response_model = LocationResponse)
async def update(id: str , data: LocationCreate, db: Session = Depends(pegar_sessao), user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not authenticator")
    repository = LocationRepository(db)
    service = LocationService(repository)
    return service.update_location(id , data)

@RouterLoc.get("/get")
async def get_location(db: Session = Depends(pegar_sessao), user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not autheticator")
    repository = LocationRepository(db)
    service = LocationService(repository)
    return service.get_loc()

@RouterLoc.get("/get/{id}")
async def get_id(id: str , db: Session = Depends(pegar_sessao), user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not authenticator")
    repository = LocationRepository(db)
    service = LocationService(repository)
    return service.get_loc_id(id)

@RouterLoc.delete("/delete/{id}")
async def delete_location(id: str , db: Session = Depends(pegar_sessao), user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 401 ,detail = "User not authenticator")
    repository = LocationRepository(db)
    service = LocationService(repository)
    service.delete_loc(id)
    return {"Mnesagem": "Registro deletado com sucesso "}