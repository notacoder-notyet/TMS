from fastapi import Depends, HTTPException, status
from sqlalchemy.sql import func
from sqlalchemy.orm import Session

from core.security import JWTBearer, decode_access_token
from db.base import database, SessionLocal
from models.reviews import ReviewModel


#[Database]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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
from schemas.apartment import Apartment


def get_apartment_services() -> ApartmentServices:
    return ApartmentServices(database)


async def get_user(id: int, users: UserServices = Depends(get_user_services)) -> User:
    user = await users.get_by_id(id=id)
    return user


async def get_apartment(id: int, apartments: ApartmentServices = Depends(get_apartment_services)) -> Apartment:
    apartment = await apartments.get_by_id(id=id)
    return apartment


#[Buildings]
from services.buildings import BuildingServices


def get_building_services() -> BuildingServices:
    return BuildingServices(database)


#[Reviews]
from services.reviews import ReviewServices


def get_review_services() -> ReviewServices:
    return ReviewServices(database)


async def raiting_calculate(score, object_id, id: int, db: Session = Depends(get_db)):
    avg_val = await db.query(func.avg(score)).filter(object_id==id)
    return avg_val


async def update_raiting(obj, avg_value):
    setattr(obj, 'raiting', avg_value)
