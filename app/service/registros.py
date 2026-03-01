from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..schemas.registros import RegistrosCreate
from ..models.registros import Registros
from ..repositories.registros import RecordsRepository

class RegistrosService:
    def __init__(self , repository: RecordsRepository):
        self.repository = repository
    
    def create_reg(self , data: RegistrosCreate):
        records = Registros(crime_id = str(data.crime_id) , qtd = data.qtd , mes = data.mes , ano = data.ano, location_id = str(data.location_id) , user_id = str(data.user_id))
        if not records:
            raise HTTPException(status_code = 404 , detail = "cadastro não realizado tente novamente !")
        return self.repository.create_registro(records)
        
    def update_reg_id(self, id: str , data: RegistrosCreate):
        records = self.repository.get_by_id(id)
        if not records:
            raise HTTPException(status_code = 404 , detail = "Registro não encontrado")
        records.qtd = int(data.qtd)
        records.mes = int(data.mes.value)
        records.ano = int(data.ano)
        return self.repository.update(records)

    def get_res(self):
        records = self.repository.get_reg()
        if not records:
            raise HTTPException(status_code = 404 , detail = "Regitros não encontrados")
        return records

    def get_recor_id(self, id: str):
        records = self.repository.get_by_ip(id)
        if not records:
            raise HTTPException(status_code = 404 , detail = "Registro não encontrado")
        return records

    def delete_record_id(self, id: str):
        records = self.repository.delete_by_id(id)
        if not records:
            raise HTTPException(status_code = 401 ,detail = "Registro não encontrado")
        
        self.repository.delete(records)
        return {"Mensagem": "Registro deletado com sucesso !"}