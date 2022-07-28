import datetime
import uuid
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    Integer,
    String
)
from sqlalchemy.orm import relationship

from db.base import Base

# from sqlalchemy.dialects.postgresql import UUID
# from flask_sqlalchemy import SQLAlchemy
# import uuid

# db = SQLAlchemy()

# class Foo(db.Model):
# id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 

def generate_uuid():
    return str(uuid.uuid4())


class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True)
    nickname = Column(String, unique=True)
    password = Column(String)
    phone_number = Column(Integer, unique=True)
    raiting = Column(Float, nullable=True)
    is_landlord = Column(Boolean)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    apartments = relationship('ApartmentModel',  back_populates='owner', viewonly=True)
    your_reviews = relationship('ReviewModel', back_populates='your_user', foreign_keys='ReviewModel.user_id', viewonly=True)
    reviews_about = relationship('ReviewModel', back_populates='user', foreign_keys='ReviewModel.user_id', viewonly=True)

    def __repr__(self) -> str:
        return f'<User {self.nickname}>'
