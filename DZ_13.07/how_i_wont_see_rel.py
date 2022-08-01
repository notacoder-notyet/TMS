from sqlalchemy import (Column, ForeignKey, Integer)
from sqlalchemy.orm import relationship
from db.base import Base

class ApartmentModel(Base):
    __tablename__ = 'apartments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('users.id')) # Landlord id
    # renter_id = Column(Integer, ForeignKey('users.id'), nullable=True) # If be rented

    owner = relationship('UserModel', back_populates='your_apartments', foreign_keys='ApartmentModel.owner_id')
    # renters = relationship('UserModel', back_populates='rented_apartments', foreign_keys='ApartmentModel.renter_id')
    reviews = relationship('ReviewModel', back_populates='apartment', viewonly=True)

class Rent(Base): 
    id = Column(Integer, primary_key=True, autoincrement=True)
    renter_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    apartment_id = Column(Integer, ForeignKey("apartments.id"), nullable=True)

    renters = relationship('UserModel', back_populates='renter')
    apartment = relationship('ApartmentModel',  back_populates='reviews')


class ReviewModel(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column(Integer, ForeignKey("users.id")) #Current user
    renter_id = Column(Integer, ForeignKey("users.id"), nullable=True) #If writing landlord
    apartment_id = Column(Integer, ForeignKey("apartments.id"), nullable=True) #If writing renter

    apartment = relationship('ApartmentModel',  back_populates='reviews', foreign_keys='ReviewModel.apartment_id')
    your_user = relationship('UserModel', back_populates='your_reviews', foreign_keys='ReviewModel.user_id')
    renter = relationship('UserModel', back_populates='renter_reviews', foreign_keys='ReviewModel.user_id')

class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)

    your_apartments = relationship('ApartmentModel',  back_populates='owner', viewonly=True)
    # rented_apartments = relationship('ApartmentModel',  back_populates='renters', viewonly=True)
    your_reviews = relationship('ReviewModel', back_populates='your_user', viewonly=True)
    renter_review = relationship('ReviewModel', back_populates='renter', viewonly=True)