import datetime
from typing import List, Optional
from pydentic import BaseModel, EmailStr, validator, constr

from .review import Review

class BaseUser(BaseModel):
    email: EmailStr
    nickname: str
    phone_number: int
    is_landlord: bool


class User(BaseUser):
    id: Optional[str] = None
    hashed_password: str
    raiting: float
    your_feedback: List[Review] = []
    feedback_about_you: List[Review] = []
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UserIn(BaseUser):
    password: constr(min_lenght=8)
    password2: str

    @validator('password2')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError("Password don't match")
        return v
