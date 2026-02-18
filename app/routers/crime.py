from fastapi import APIRouter , Depends , Path , Request , HTTPException
from ..schemas.crime import CrimeCreate , CrimeResponse
from sqlalchemy.orm import Session
from ..database import pegar_sessao
from ..core.config import verificar_token
from ..core.dependecies import Validator_Adm
from ..service.crime import Create_Crime , Update_Crime , Get_Crime ,Get_Crime_id , Delete_Crime

RouterCrime = APIRouter(prefix = "/Crimes", tags=["Crimes"])

@RouterCrime.post("/CreateCrimes", response_model = CrimeResponse)
async def createcrimes(data: CrimeCreate , db: Session = Depends(pegar_sessao), user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not authenticator")
    crime = Create_Crime(db , data)
    return crime 

@RouterCrime.put("/Update/{id}", response_model = CrimeResponse)
async def UpdateCrime(id: str , data: CrimeCreate , db: Session = Depends(pegar_sessao), user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not authenticator")
    crime = Update_Crime(db , data , id)
    return crime

@RouterCrime.get("/lista/crime")
async def ListCrime(db: Session = Depends(pegar_sessao) , user = Depends(verificar_token) , adm = Depends(Validator_Adm)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not authenticator")
    crime = Get_Crime(db)
    return crime

@RouterCrime.get("/listar/{id}")
async def ListCrimeId(id: str , db: Session = Depends(pegar_sessao), user = Depends(verificar_token), adm = Depends(Validator_Adm)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "user not authrozation")
    crime = Get_Crime_id(db , id)
    return crime

@RouterCrime.delete("/delete/{id}")
async def DeleteCrime(id: str , db: Session = Depends(pegar_sessao), user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 401 , detail = "User not authenticator")
    crime = Delete_Crime(db , id)
    return crime 