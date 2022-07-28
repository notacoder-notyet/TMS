import datetime
from typing import Optional
from pydantic import BaseModel, conint, confloat


class BaseBuilding(BaseModel):    
    address: str = None
    elevator: bool = False


class Building(BaseBuilding):
    id: Optional[int] = None
    year: conint(ge=1800, le=datetime.datetime.today().year) = None
    floors: conint(ge=1, le=33) = None
    MTA: confloat(ge=0.1, le=5.0) = None

    class Config:
        orm_mode = True


class BuildingIn(BaseBuilding):
    year: conint(ge=1800, le=datetime.datetime.today().year)
    floors: conint(ge=1, le=33)
    MTA: confloat(ge=0.1, le=5.0) = None
