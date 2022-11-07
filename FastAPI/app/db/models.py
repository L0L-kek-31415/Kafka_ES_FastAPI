from sqlalchemy import Column, Integer, Boolean, String

from app.db.session import Base


class User(Base):
    __tablename__ = "fuck_users"
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(30), index=True, nullable=False, unique=True)
    email = Column(String(30), unique=True)
    hashed_password = Column(String(300))
