from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    refresh_token: str


class User(BaseModel):
    username: str
    email: str | None = None

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str
