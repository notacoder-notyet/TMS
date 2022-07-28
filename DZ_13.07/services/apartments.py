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
        get_apartments = await self.database.fetch_all(query=query)
        return get_apartments


    async def delete(self, id: int):
        query = delete(ApartmentModel).where(ApartmentModel.id==id)
        apartment_delete = await self.database.execute(query=query)
        return apartment_delete


    async def get_by_id(self, id: int) -> Optional[Apartment]:
        query = select(ApartmentModel).where(ApartmentModel.id==id)
        apartment = await self.database.fetch_one(query=query)
        if apartment is None:
            return None
        return Apartment.parse_obj(apartment)
