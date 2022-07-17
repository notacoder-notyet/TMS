from re import U
from typing import List
from fastapi import APIRouter, Depends

from services.users import UserServices
from schemas.user import User, UserIn
from .depends import get_user_services

router = APIRouter()

@router.get('/', response_model=List[User])
async def read_users(
    users: UserServices = Depends(get_user_services),
    limit: int = 100,
    skip: int = 100):
    return await users.get_all(limit=limit, skip=0)

@router.post('/', response_model=User)
async def create(
    user: UserIn,
    users: UserServices = Depends(get_user_services)):
    return await users.create(u=user)
