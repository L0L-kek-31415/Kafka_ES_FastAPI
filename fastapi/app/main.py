from fastapi import FastAPI

from app.db.session import Base
from app.db.session import engine
from app.api.routers import router


app = FastAPI(reload=True)
app.include_router(router)
Base.metadata.create_all(bind=engine)
