from ..database import Base 
from sqlalchemy.orm import  Mapped , mapped_column , relationship
from sqlalchemy import String , Integer , Boolean
import uuid

class User(Base):
    __tablename__ = "User"

    id: Mapped[str] = mapped_column(String(36), primary_key = True , default = lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String(100), nullable = False)
    email: Mapped[str] = mapped_column(String(100), nullable = False, unique = True)
    senha: Mapped[str] = mapped_column(String(100), nullable = False)
    adm: Mapped[bool] = mapped_column(Boolean, nullable = False , default = False)

    registros = relationship("Registros", back_populates = "user", cascade = "all , delete-orphan")