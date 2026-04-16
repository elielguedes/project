from sqlalchemy.orm import Session
from ..models.user import User

class UserRepo:

    def __init__(self , db: Session):
        self.db = db

    def get_by_email(self , email: str) -> list[User]:
        return self.db.query(User).filter(User.email == email).first()
    
    def create(self , user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user