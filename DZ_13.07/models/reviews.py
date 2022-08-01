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


class ReviewBaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    is_landlord = Column(Boolean)
    review = Column(Text)
    added_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    apartment = relationship('ApartmentModel', foreign_keys='ReviewModel.apartment_id') #,  back_populates='reviews'
    your_user = relationship('UserModel', foreign_keys='ReviewModel.user_id') #, back_populates='your_reviews'
    user = relationship('UserModel', foreign_keys='ReviewModel.user_id') #, back_populates='reviews_about'

    def __repr__(self) -> str:
        return f'<From {self.user_id.nickname} to {self.him_user_id.nickname}>'


class LandlordReviewModel(ReviewBaseModel):
    __tablename__ = 'landlord_reviews'

    score = Column(Enum(ScoreEnum), nullable=True)
    renter_id = Column(Integer, ForeignKey("users.id"), nullable=True)


class RenterReviewModel(ReviewBaseModel):
    __tablename__ = 'renter_reviews'

    score = Column(Enum(ScoreEnum), nullable=True)
    apartment_id = Column(Integer, ForeignKey("apartments.id"), nullable=True)
