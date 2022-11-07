from typing import List

from fastapi import status, HTTPException, Depends, APIRouter, Query
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.crud import create_user_func, get_user_by_username, get_users
from app.db.schemas import Token, UserInDB, User as UserSchema
from app.db.session import get_db

from app.utils import (
    create_access_token,
    verify_password,
    create_refresh_token,
)


router = APIRouter(
    prefix='',
    tags=['jwt']
)


@router.post("/user/", response_model=UserInDB)
async def create_user(user: UserInDB, db: Session = Depends(get_db)):
    return create_user_func(db=db, user=user)


@router.get("/users/", response_model=List[UserSchema])
async def list_users(db: Session = Depends(get_db)):
    return get_users(db)


@router.get("/", response_class=RedirectResponse,
            include_in_schema=False)
async def docs():
    return RedirectResponse(url="/docs")


@router.post('/login', summary="Create access and refresh tokens for user", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_username(db=db, username=form_data.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = user.hashed_password
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    return {
        "access_token": create_access_token(user.username),
        "refresh_token": create_refresh_token(user.username),
    }
