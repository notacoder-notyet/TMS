import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    Text,
    String
)
from sqlalchemy.orm import relationship

from db.base import Base
from enums.enums import AmenitiesEnum, StatusEnum


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
    status = Column(Enum(StatusEnum))
    raiting = Column(Float, nullable=True)
    renter_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    added_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    building = relationship('BuildingModel', foreign_keys='ApartmentModel.building_id') #, back_populates='apartments'
    owner = relationship('UserModel', foreign_keys='ApartmentModel.owner_id') #, back_populates='your_apartments'
    renter = relationship('UserModel', foreign_keys='ApartmentModel.renter_id') #, back_populates='rented_apartments'
    # reviews = relationship('ReviewModel', back_populates='apartment', viewonly=True)

    def __repr__(self) -> str:
        return f'<Building {self.building_id.address}>'
