import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Text,
    String
)
from sqlalchemy.orm import relationship

from db.base import Base
from enums.enums import AmenitiesEnum


class ApartmentModel(Base):
    __tablename__ = 'apartments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    building_id = Column(Integer, ForeignKey('buildings.id'))
    owner_id = Column(Integer, ForeignKey('users.id'))
    price = Column(Integer)
    square = Column(Integer)
    description = Column(Text(500))
    floor = Column(Integer)
    rooms = Column(Integer)
    pet_friendly = Column(Boolean)
    amenities = Column(Enum(AmenitiesEnum))
    added_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    building = relationship('BuildingModel', back_populates='apartments', foreign_keys='ApartmentModel.building_id')
    owner = relationship('UserModel', back_populates='apartments', foreign_keys='ApartmentModel.owner_id')
    reviews = relationship('ReviewModel', back_populates='apartment', viewonly=True)

    def __repr__(self) -> str:
        return f'<Building {self.building_id.address}>'
