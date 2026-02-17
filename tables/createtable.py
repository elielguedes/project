from app.database import engine , Base
from app.models.location import Location
from app.models.registros import Registros
from app.models.user import User
from app.models.crime import Crime

Base.metadata.create_all(bind = engine)
print("Tabelas criadas")
