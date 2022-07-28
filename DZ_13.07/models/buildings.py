from sqlalchemy import (
    Boolean,
    Column,
    Float,
    ForeignKey,
    Integer,
    String
)
from sqlalchemy.orm import relationship

from db.base import Base


class BuildingModel(Base):
    __tablename__ = 'buildings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(100), unique=True)
    year = Column(Integer, nullable=True)
    floors = Column(Integer, nullable=True)
    elevator = Column(Boolean, nullable=True)
    MTA = Column(Float, nullable=True)

    apartments = relationship('ApartmentModel', back_populates='building', viewonly=True)

    def __repr__(self) -> str:
        return f'<Building {self.address}>'
