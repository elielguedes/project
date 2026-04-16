from fastapi import APIRouter , Depends , Path , Request , HTTPException
from ..schemas.crime import CrimeCreate , CrimeResponse
from sqlalchemy.orm import Session
from ..database import pegar_sessao
from ..core.config import verificar_token
from ..core.dependecies import Validator_Adm
from ..service.crime import CrimeService
from ..repositories.crime import CrimeRepository


RouterCrime = APIRouter(prefix = "/Crimes", tags=["Crimes"])

@RouterCrime.post("/CreateCrimes", response_model = CrimeResponse)
async def createcrimes(data: CrimeCreate , db: Session = Depends(pegar_sessao), user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not authenticator")
    repository = CrimeRepository(db)
    service = CrimeService(repository)
    return service.create_cri(data)

@RouterCrime.put("/Update/{id}", response_model = CrimeResponse)
async def UpdateCrime(id: str , data: CrimeCreate , db: Session = Depends(pegar_sessao), user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not authenticator")
    repository = CrimeRepository(db)
    service = CrimeService(repository)
    return service.Update_Crime(id , data)

@RouterCrime.get("/lista/crime")
async def ListCrime(db: Session = Depends(pegar_sessao) , user = Depends(verificar_token) , adm = Depends(Validator_Adm)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not authenticator")
    repository = CrimeRepository(db)
    service = CrimeService(repository)
    return service.Get_Crime()

@RouterCrime.get("/listar/{id}")
async def ListCrimeId(id: str , db: Session = Depends(pegar_sessao), user = Depends(verificar_token), adm = Depends(Validator_Adm)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "user not authrozation")
    repository = CrimeRepository(db)
    service = CrimeService(repository)
    return service.Get_Crime_id(id)

@RouterCrime.delete("/delete/{id}")
async def DeleteCrime(id: str , db: Session = Depends(pegar_sessao), user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not authenticator")
    repository = CrimeRepository(db)
    service = CrimeService(repository)
    return service.Delete_Crime(id)