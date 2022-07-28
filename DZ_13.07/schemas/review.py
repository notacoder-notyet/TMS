import datetime
from typing import Optional
from pydantic import BaseModel, constr

from enums.enums import ScoreEnum


class BaseReview(BaseModel):
    review: constr(max_length=500)

class Review(BaseReview):
    id: Optional[int] = None
    user_id: int
    is_landlord: Optional[bool]
    apartment_id: Optional[int]
    apartment_score: Optional[ScoreEnum]
    renter_id: Optional[int]
    renter_score: Optional[ScoreEnum]
    added_at: Optional[datetime.datetime]
    updated_at: datetime.datetime

    class Config:
        orm_mode = True


class RenterReview(BaseReview):
    apartment_score: ScoreEnum
    apartment_id: int
    is_landlord: bool = False


class LandlordReview(BaseReview):
    renter_score: ScoreEnum
    renter_id: int
    is_landlord: bool = True
