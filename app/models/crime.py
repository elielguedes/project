from ..database import Base 
from sqlalchemy.orm import Mapped , mapped_column , relationship
from sqlalchemy import Integer, String , Boolean
import uuid

class Crime(Base):
    __tablename__ = "Crime"

    id: Mapped[str] = mapped_column(String(36), primary_key = True , default = lambda: str(uuid.uuid4()))
    nome: Mapped[str] = mapped_column(String(100), nullable = False)

    registros = relationship("Registros", back_populates = "crime", cascade = "all , delete-orphan")