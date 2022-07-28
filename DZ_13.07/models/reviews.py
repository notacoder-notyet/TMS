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


class ReviewModel(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    is_landlord = Column(Boolean)
    review = Column(Text)
    renter_score = Column(Enum(ScoreEnum), nullable=True)
    renter_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    apartment_score = Column(Enum(ScoreEnum), nullable=True)
    apartment_id = Column(Integer, ForeignKey("apartments.id"), nullable=True)
    added_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    apartment = relationship('ApartmentModel',  back_populates='reviews', foreign_keys='ReviewModel.apartment_id')
    your_user = relationship('UserModel', back_populates='your_reviews', foreign_keys='ReviewModel.user_id')
    user = relationship('UserModel', back_populates='reviews_about', foreign_keys='ReviewModel.user_id')

    def __repr__(self) -> str:
        return f'<From {self.user_id.nickname} to {self.him_user_id.nickname}>'
