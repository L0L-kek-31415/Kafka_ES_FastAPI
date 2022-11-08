from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.db.models import User
import app.db.schemas
from app.authservice import AuthService


class UserService:
    def __init__(self):
        self.auth = AuthService()

    @staticmethod
    def get_user_by_username(db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    @staticmethod
    def get_users(db: Session):
        return db.query(User).all()

    def create_user_func(self, db: Session, user: app.db.schemas.UserInDB):
        db_user = User(
            username=user.username,
            email=user.email,
            hashed_password=self.auth.get_password_hash(user.hashed_password),
        )
        if UserService.get_user_by_username(db, db_user.username):
            raise HTTPException(
                status_code=401,
                detail="User with this username already exists",
                headers={"WWW-Authenticate": "Bearer"},
            )
        try:
            db.add(db_user)
            db.commit()
        except:
            raise HTTPException(
                status_code=401,
                detail="User with this email already exists",
                headers={"WWW-Authenticate": "Bearer"},
            )
        db.refresh(db_user)
        return db_user
