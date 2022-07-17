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

def generate_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = 'users'
    #metadata
    id = Column(Integer, primary_key=True, autoincrement=True, default=generate_uuid)
    email = Column(String, unique=True)
    nickname = Column(String, unique=True)
    password = Column(String)
    phone_number = Column(Integer, unique=True)
    raiting = Column(Float)
    is_landlord = Column(Boolean)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    apartments = relationship('Apatment',  back_populates="user")
    your_feedback = relationship('Reviews', back_populates="user")
    feedback_about_you = relationship('Reviews', back_populates="user")

    def __repr__(self) -> str:
        return f'<User {self.nickname}>'