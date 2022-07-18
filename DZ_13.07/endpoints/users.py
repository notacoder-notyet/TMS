from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from services.users import UserServices
from schemas.user import User, UserIn
from .depends import get_user_services, get_current_user

router = APIRouter()

@router.get('/', response_model=List[User], response_model_exclude={"hashed_password"})
async def read_users(
    limit: int = 100,
    skip: int = 100,
    users: UserServices = Depends(get_user_services)
):
    return await users.get_all(limit=limit, skip=0)

@router.post('/', response_model=User)
async def create_user(
    user: UserIn,
    users: UserServices = Depends(get_user_services)
):
    return await users.create(u=user)

@router.put('/', response_model=User)
async def update_user(
    id: int,
    user: UserIn,
    users: UserServices = Depends(get_user_services),
    current_user: User = Depends(get_current_user)
):
    old_user = await users.get_by_id(id=id)
    if old_user is None or old_user.email != current_user.email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details='User not found')
    return await users.update(id=id, u=user)


