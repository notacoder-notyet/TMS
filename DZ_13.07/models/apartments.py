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

from db.base import Base, metadata
from enums.enums import AmenitiesEnum

from .buildings import Building
from .reviews import Review
from .users import User

class Apartment(Base):
    __tablename__ = 'apartments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    building_id = Column(Integer, ForeignKey('buildings.id'))
    price = Column(Integer)
    square = Column(Integer)
    description = Column(Text(500))
    floor = Column(Integer)
    rooms = Column(Integer)
    pet_friendly = Column(Boolean)
    amenities = Column(Enum(AmenitiesEnum))
    owner_id = Column(Integer, ForeignKey('users.id'))
    added_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    building = relationship('Building', back_populates="apartments")
    owner = relationship('User', back_populates="apartments")
    reviews = relationship('Review', back_populates='reviews')

    def __repr__(self) -> str:
        return f'<Building {self.building_id.address}>'