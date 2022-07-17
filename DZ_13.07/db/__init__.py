from .base import Base, engine, metadata
from models.apartments import Apartment, Building
from models.reviews import Review
from models.users import User

Base.metadata.create_all(bind=engine)