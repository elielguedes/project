from ..database import Base 
from sqlalchemy.orm import Mapped , mapped_column , relationship
from sqlalchemy import Integer , String , Boolean
import uuid

class Location(Base):
    __tablename__ = "Location"

    id: Mapped[str] = mapped_column(String(36), primary_key = True , default = lambda: str(uuid.uuid4()))
    cod_municipio: Mapped[int] = mapped_column(Integer, nullable = False)
    risp: Mapped[str] = mapped_column(String(6), nullable = False)
    rmbh: Mapped[str] = mapped_column(String(100), nullable = False)
    nome_municipio: Mapped[str] = mapped_column(String(100), nullable = False)

    # o cascade inclui todas operações possiveis de crud já o delete-orphan garante que a classe filho fique orfã automatico
    registros = relationship("Registros", back_populates = "location", cascade = "all , delete-orphan")
