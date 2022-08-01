from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session


from schemas.user import User, UserIn
from services.notification import send_notification
from services.users import UserServices
from .depends import get_user_services, get_current_user, get_db


router = APIRouter()

@router.get('/', response_model=List[User], response_model_exclude={"hashed_password"})
async def read_users(
    limit: int = 100,
    skip: int = 100,
    users: UserServices = Depends(get_user_services)
):
    get_users = await users.get_all(limit=limit, skip=0)
    return get_users


@router.post('/', response_model=User)
async def create_user(
    schema: UserIn,
    background_tasks: BackgroundTasks,
    user_service: UserServices = Depends(get_user_services),
    db: Session = Depends(get_db),
):
    user = await user_service.create(db, schema)
    background_tasks.add_task(
        send_notification,
        email=user.email,
        message=f"Hello {user.nickname}, Welcome!"
    )
    return user


@router.put('/', response_model=User)
async def update_user(
    id: int,
    schema: UserIn,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    userservice: UserServices = Depends(get_user_services)
):
    old_user = await userservice.get_by_id(db, id=id)
    if old_user is None or old_user.email != current_user.email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details='User not found')
    updated_user = await userservice.update(db, old_user, schema)
    return updated_user
