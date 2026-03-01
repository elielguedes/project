from fastapi import HTTPException
from ..schemas.crime import CrimeCreate
from sqlalchemy.orm import Session
from ..models.crime import Crime
from ..repositories.crime import CrimeRepository

class CrimeService:
    def __init__(self , repository: CrimeRepository):
        self.repository = repository
    
    def create_cri(self , data: CrimeCreate):
        new_crime = Crime(nome = data.nome)
        if not new_crime:
            raise HTTPException(status_code = 400 , detail = "Ocorrêcia não criada")
        return self.repository.create_crime(new_crime)

    def Update_Crime(self ,id: str , data):
        crime = self.repository.get_by_id(id)
        if not crime:
            raise HTTPException(status_code = 404 ,detail = "Crime não encontrado")
        crime_exist = self.repository.get_by_nome(data.nome)
        if crime_exist and crime_exist.id != id:
            raise HTTPException(status_code = 400 ,detail = "Name já cadastrado")
        crime.nome = data.nome
        return self.repository.update(crime)

    def Get_Crime(self):
        crime = self.repository.get_by_crime()
        if not crime:
            raise HTTPException(status_code = 404 , detail = "Banco de dados vazio")
        return crime

    def Get_Crime_id(self , id: str):
        crime = self.repository.get_by_ip(id)
        if not crime:
            raise HTTPException(status_code = 404 , detail = "Cadastro não encontrado ")
        return crime

    def Delete_Crime(self, id: str):
        crime = self.repository.delete_by_id(id)
        if not crime:
            raise HTTPException(status_code = 404 , detail = "Cadastro não encontrado ")
        self.repository.delete(crime)

        return {"Mensagem": "Crime deletado com sucesso !"}