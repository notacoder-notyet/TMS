import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, validator, constr


class BaseUser(BaseModel):
    email: EmailStr
    nickname: str
    phone_number: int
    is_landlord: bool = False


class User(BaseUser):
    id: Optional[int] = None
    # password: Optional[str]
    raiting: Optional[float]
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True


class UserIn(BaseUser):
    password: constr(min_length=8)

    @validator('password')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError("Password don't match")
        return v
