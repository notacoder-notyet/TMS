import datetime
from fastapi import HTTPException, status
from typing import List, Optional
from sqlalchemy import insert, select, update, delete

from models.apartments import ApartmentModel
from schemas.apartment import Apartment, ApartmentIn

from .base import BaseServices


class ApartmentServices(BaseServices):

    async def create(self, schema: ApartmentIn, owner_id: int) -> Apartment:
        data = schema.dict()
        data['owner_id'] = owner_id
        data['status'] = 'Freely'
        data['added_at'] = datetime.datetime.utcnow()
        data['updated_at'] = datetime.datetime.utcnow()
        query = insert(ApartmentModel).values(**data)
        apartment = await self.database.execute(query=query)
        return apartment


    async def update(self, schema: ApartmentIn, id: int) -> Apartment:
        data = schema.dict()
        data['updated_at'] = datetime.datetime.utcnow()
        query = update(ApartmentModel).where(ApartmentModel.id==id).values(**data)
        apartment = await self.database.execute(query=query)
        return apartment


    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Apartment]:
        query = select(ApartmentModel).limit(limit).offset(skip)
        apartments = await self.database.fetch_all(query=query)
        return apartments


    async def delete(self, id: int):
        query = delete(ApartmentModel).where(ApartmentModel.id==id)
        deleted_apartment = await self.database.execute(query=query)
        return deleted_apartment


    async def get_by_id(self, id: int) -> Optional[Apartment]:
        query = select(ApartmentModel).where(ApartmentModel.id==id)
        apartment = await self.database.fetch_one(query=query)
        if apartment is None:
            return None
        return apartment


    async def reservation(self, apartment_for_booking, renter_id: int):
        setattr(apartment_for_booking, 'renter_id', renter_id)
        setattr(apartment_for_booking, 'status', 'Booked')
        apartment = await self.database.execute(apartment_for_booking)
        return apartment

    async def rental_confirmation(self, apartment):
        setattr(apartment, 'status', 'Rented')
        apartment = await self.database.execute(apartment)
        return apartment