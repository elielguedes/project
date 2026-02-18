from fastapi import Depends , HTTPException
from ..core.config import verificar_token
from ..models.user import User

def Validator_Adm(user: User = Depends(verificar_token)):
    if not user.adm:
        raise HTTPException(status_code = 403 , detail = "User not authorization")
    return user