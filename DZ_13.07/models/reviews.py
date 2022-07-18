import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Text,
)
from sqlalchemy.orm import relationship

from db.base import Base
from enums.enums import ScoreEnum

from apartments import Apartment
from users import User

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    is_landlord = Column(Boolean)
    apartment_id = Column(Integer, ForeignKey("apartments.id"))
    review = Column(Text)
    renter_score = Column(Enum(ScoreEnum))
    apartment_score = Column(Enum(ScoreEnum))
    user_id = Column(Integer, ForeignKey("users.id"))
    renter_id = Column(Integer, ForeignKey("users.id"))
    added_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    apartment = relationship('Apatment',  back_populates="reviews")
    your_user = relationship('User', back_populates="reviews")
    renter = relationship('User', back_populates="reviews")

    def __repr__(self) -> str:
        return f'<From {self.your_user_id.nickname} to {self.him_user_id.nickname}>'