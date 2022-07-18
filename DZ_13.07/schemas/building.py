import datetime
from typing import List
from pydantic import BaseModel, conint, confloat

from .apartment import Apartment

class BaseBuilding(BaseModel):    
    address: str
    elevator: bool

class Building(BaseBuilding):
    id: int
    year: int
    floors: int
    MTA: float
    apartments: List[Apartment]

class BuildingIn(BaseBuilding):
    year: conint(ge=1800, le=datetime.datetime.today().year)
    floors: conint(ge=1, le=33)
    MTA: confloat(ge=0.1, le=5) = None  #дистанция в км

