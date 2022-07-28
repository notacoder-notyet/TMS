from http.client import HTTPException
from fastapi import APIRouter, Depends, HTTPException, status

from core.security import verify_password, create_access_token
from schemas.token import Token, Login
from services.users import UserServices
from .depends import get_user_services

router = APIRouter()

@router.post('/', response_model=Token)
async def login(login: Login, users: UserServices = Depends(get_user_services)):
    user = await users.get_by_email(login.email)
    if user is None and verify_password(login.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect email or password')

    return Token(
        access_token=create_access_token({'sub': user.email}),
        token_type='Bearer'
    )
