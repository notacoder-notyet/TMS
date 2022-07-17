import datetime
from typing import List, Optional
from pydentic import BaseModel, EmailStr, validator, constr

from review import Review

class User(BaseModel):
    id: Optional[str] = None
    email: EmailStr
    nickname: str
    hashed_password: str
    phone_number: int
    raiting: float
    is_landlord: bool
    your_feedback: List[Review] = []
    feedback_about_you: List[Review] = []
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UserIn(BaseModel):
    email: EmailStr
    nickname: str
    password: constr(min_lenght=8)
    password2: str
    phone_number: int
    is_landlord: bool = False

    @validator('password2')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError("Password don't match")
        return v
