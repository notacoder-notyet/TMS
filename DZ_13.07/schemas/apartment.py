import datetime
from typing import Optional
from pydantic import BaseModel, conint, constr

from enums.enums import AmenitiesEnum, StatusEnum


class BaseApartment(BaseModel):
    '''Костыль с optional, т.к. с orm_mode = True плевалась ошибками
     на каждое поле:
    `pydantic.error_wrappers.ValidationError: 12 validation errors for Apartment
    response -> pet_friendly
    field required (type=value_error.missing)
    и остальные 11...`
    А c False то же, только value_error.dict однократно
    '''
    pet_friendly: Optional[bool]
    amenities: Optional[AmenitiesEnum]
    building_id: Optional[int]


class Apartment(BaseApartment):
    id: Optional[int] = None
    price: Optional[conint(ge=1)]
    square: Optional[conint(ge=15, le=255)]
    description: Optional[constr(max_length=500)]
    floor: Optional[conint(ge=1, le=33)]
    rooms: Optional[conint(ge=1, le=10)]
    owner_id: Optional[int]
    status: Optional[StatusEnum]
    raiting: Optional[float]
    renter_id: Optional[int]
    added_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class ApartmentIn(BaseApartment):
    price: conint(ge=1)
    square: conint(ge=15, le=255)
    description: constr(max_length=500)
    floor: conint(ge=1, le=33)
    rooms: conint(ge=1, le=10)
