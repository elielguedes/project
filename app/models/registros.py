from ..database import Base
from sqlalchemy.orm import Mapped , mapped_column , relationship
from sqlalchemy import String , Integer , Boolean , ForeignKey
import uuid

class Registros(Base):
    __tablename__ = "registros"

    id: Mapped[str] = mapped_column(String(36), primary_key = True , default = lambda: str(uuid.uuid4()))
    qtd: Mapped[int] = mapped_column(Integer , nullable = True)
    mes: Mapped[int] = mapped_column(Integer , nullable = False)
    ano: Mapped[int] = mapped_column(Integer , nullable = False)
    crime_id: Mapped[str] = mapped_column(String(36) , ForeignKey("Crime.id"))
    location_id: Mapped[str] = mapped_column(String(36), ForeignKey("Location.id"))
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("User.id"))

    location = relationship("Location" , back_populates = "registros")
    crime = relationship("Crime" , back_populates = "registros")
    user = relationship("User" , back_populates = "registros")

