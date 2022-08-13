from sqlalchemy import (Column, ForeignKey, Integer)
from sqlalchemy.orm import relationship
from db.base import Base

class Apartment(Base):
    __tablename__ = 'apartments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('users.id')) # Landlord id

    owner = relationship('User', back_populates='your_apartments', foreign_keys='Apartment.owner_id')
    renter = relationship('Rent', back_populates='rented_apartment', viewonly=True)
    reviews = relationship('Review', back_populates='apartment', viewonly=True)

class Rent(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    renter_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    apartment_id = Column(Integer, ForeignKey("apartments.id"), nullable=True)

    user = relationship('User', back_populates='rented', foreign_keys='Rent.renter_id')
    rented_apartment = relationship('Apartment',  back_populates='renter', foreign_keys='Rent.apartment_id')


class Review(Base): #abstract
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column(Integer, ForeignKey("users.id")) #Current user

    your_user = relationship('User', back_populates='your_reviews', foreign_keys='Review.user_id')


class ReviewLL(Review):
    __tablename__ = 'rl'
    renter_id = Column(Integer, ForeignKey("r.id"), nullable=True) #If writing landlord

    renter = relationship('User', back_populates='reviews_of_landlords', foreign_keys='Review.user_id')


class ReviewR(Review):
    __tablename__ = 'rr'
    apartment_id = Column(Integer, ForeignKey("apartments.id"), nullable=True) #If writing renter

    apartment = relationship('Apartment',  back_populates='reviews', foreign_keys='Review.apartment_id')


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    your_reviews = relationship('Review', back_populates='your_user', viewonly=True)

class Landlord(User):
    __tablename__ = 'l'

    your_apartments = relationship('Apartment',  back_populates='owner', viewonly=True)

class Renter(User):
    __tablename__ = 'r'

    rented = relationship('Rent',  back_populates='user', viewonly=True)
    reviews_of_landlords = relationship('Review', back_populates='renter', viewonly=True)