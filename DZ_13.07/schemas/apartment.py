import datetime
from typing import List
from pydantic import BaseModel, conint, constr

from enums.enums import AmenitiesEnum

from .building import Building
from .review import Review
from .user import User

class BaseApartment(BaseModel): #абстрактный класс?
    pet_friendly: bool
    amenities: AmenitiesEnum
    building: List[Building] = []

class Apartment(BaseApartment):
    id: int
    price: int
    square: int
    description: str
    floor: int
    rooms: int
    owner: List[User] = []
    building_id: int
    owner_id: int
    added_at: datetime.datetime
    updated_at: datetime.datetime
    reviews: List[Review] = []

class ApartmentIn(BaseApartment):
    price: conint(ge=1)
    square: conint(ge=15, le=255)
    description: constr(max_lenght=500)
    floor: conint(ge=1, le=33)
    rooms: conint(ge=1, le=10)