from fastapi import Depends, HTTPException, status

from core.security import JWTBearer, decode_access_token
from db.base import database, SessionLocal


#[Users]
from services.users import UserServices
from schemas.user import User

def get_user_services() -> UserServices:
    return UserServices(database)

async def get_current_user(
    users: UserServices = Depends(get_user_services),
    token: str = Depends(JWTBearer())
) -> User:
    cred_exeption = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid credentials')
    payload = decode_access_token(token)
    if payload is None:
        raise cred_exeption
    email: str = payload.get('sub')
    if email is None:
        raise cred_exeption
    user = await users.get_by_email(email=email)
    if user is None:
        raise cred_exeption
    return user


#[Apartments]
from services.apartments import ApartmentServices

def get_apartment_services() -> ApartmentServices:
    return ApartmentServices(database)


#[Buildings]
from services.buildings import BuildingServices

def get_building_services() -> BuildingServices:
    return BuildingServices(database)


#[Reviews]
from services.reviews import ReviewServices

def get_review_services() -> ReviewServices:
    return ReviewServices(database)


#[Database]
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()