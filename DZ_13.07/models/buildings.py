from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String
)
from sqlalchemy.orm import relationship

from db.base import Base, metadata


class Building(Base):
    __tablename__ = 'buildings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(100), unique=True)
    year = Column(Integer)
    floors = Column(Integer)
    elevator = Column(Boolean)
    MTA = Column(Integer)

    apartment = relationship('Apartment', back_populates="building")

    def __repr__(self) -> str:
        return f'<Building {self.address}>'