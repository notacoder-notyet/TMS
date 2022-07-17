from typing import List

from pydantic import BaseModel, validator, Field


#Арендодатель, Апартаменты, Пользователь (снимает жилье), Оценка

class User(BaseModel): #Landlord
    nickname: str
    phone_number: int  = Field(min_lenght=11, max_lenght=11)
    email: str
    rating: float
    role: list


# class Renter(BaseModel):
#     nickname: str
#     phone_number: int = Field(min_lenght=11, max_lenght=11)
#     email: str
#     rating: float


class Building(BaseModel):
    address: str
    year: int
    floors: int #этажность
    elevator: bool
    MTA: int # сколько метров до метро


class Apartments(BaseModel):
    address: List[Building]
    price: int
    square: int
    floor: int
    rooms: int
    pet_friendly: bool
    amenities: list #услуги. прим: ванна, микроволновка, стиралка и тд
    owner: str


class Feedback(BaseModel):
    nickname: str
    address: str
    role: list #арендатор или арендодатель
    review: str
    score: int = Field(..., gt=1,le=5, description='Insert score in range 1-5')

    # @validator('score')
    # def check_score(cls,v):
    #     if v < 1 and v > 5:
    #         raise ValueError('Insert score in range 1-5')
    #     return v