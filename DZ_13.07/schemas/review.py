import datetime
from typing import List
from pydantic import BaseModel, constr

from enums.enums import ScoreEnum

from .apartment import Apartment
from .user import User


class Review(BaseModel):
    id: int
    apartment_id: int
    review: str
    is_landlord: bool
    renter_score: ScoreEnum
    apartment_score: ScoreEnum
    user_id: int
    renter_id: int
    added_at: datetime.datetime
    updated_at: datetime.datetime
    apartment: List[Apartment] = []
    your_user: List[User] = []
    renter: List[User] = []


class RenterReview(BaseModel):
    review: constr(max_lenght=500)
    apartment_score: ScoreEnum
    apartment: List[Apartment] = []
    is_landlord: bool = False


class LandlordReview(BaseModel):
    review: constr(max_lenght=500)
    renter_score: ScoreEnum
    renter: List[User] = []
    is_landlord: bool = True
