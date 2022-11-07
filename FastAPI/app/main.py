from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

from app.db.session import Base
from app.db.session import engine
from app.api.routers import router


def include_router(app):
    app.include_router(router)


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(reload=True)
    include_router(app)
    create_tables()
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    return app


app = start_application()
