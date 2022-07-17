import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Text,
)
from sqlalchemy.orm import relationship

from db.base import Base
from apartments import Apartment
from users import User

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    is_landlord = Column(Boolean)
    apartments_id = Column(Integer, ForeignKey("apartments.id"))
    review = Column(Text)
    renter_score = Column(Integer)
    apartment_score = Column(Integer)
    your_user_id = Column(Integer, ForeignKey("users.id"))
    him_user_id = Column(Integer, ForeignKey("users.id"))
    added_at = Column(DateTime, default=datetime.datetime.utcnow)

    apartments = relationship('Apatment',  back_populates="reviews")
    your_user = relationship('User', back_populates="reviews")
    him_user = relationship('User', back_populates="reviews")

    def __repr__(self) -> str:
        return f'<From {self.your_user_id.nickname} to {self.him_user_id.nickname}>'