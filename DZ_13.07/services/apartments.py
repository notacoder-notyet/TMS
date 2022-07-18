from datetime import datetime
from fastapi import HTTPException, status
from typing import List, Optional

from models.apartments import Apartment as ApartmentModel
from schemas.apartment import Apartment, ApartmentIn

from .base import BaseServices


class ApartmentServices(BaseServices):

    exc_not_found = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Apartment not found')

    async def create(self, owner_id: int, building_id: int, a: ApartmentIn) -> Apartment: #дополнение к коментарию снизу b: BuildingIn
        '''Тут какая-то ошибка, видимо не признает List от typing.
        В мыслях было добавить сюда поля из двух схем(buildings&apartments),
        а ниже сделать проверку, если есть,
        то не добавлять в бд и записать как вложенный объект
        по схожестям(аля автозаполнение), если есть но отличаеться
        то перезаписать. Или сделать цикл if adress==b.adress, то присвоить
        одноименный id'''
        apartment = Apartment(
            id=0,
            owner_id=owner_id, #или тут user_id, мб напутал со связями m2o, тут должно быть o2m
            building=a.building, # typing.List из schemas
            building_id=building_id, #тоже, может должно быть building.id? исходя из выбора выше
            square=a.square,
            floor=a.floor,
            rooms=a.rooms,
            pet_friendly=a.pet_friendly,
            amenities=a.amenities, #Enum
            description=a.description,
            price=a.price,
            added_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )
        values = {**apartment.dict()}
        values.pop('id', None)
        query = apartment.insert().values(**values)
        apartment.id = await self.database.execute(query=query)
        return apartment

    async def update(self, id: int, owner_id: int, building_id: int, a: ApartmentIn) -> Apartment:
        '''Та же история что и с create
        Вопрос. Надо ли отсюда вычеркивать owner_id? Записывать в pop как None
        Тип меняться должно описание, а как поменяеться владелец? Непонял тут'''
        apartment = Apartment(
            id=id,
            owner_id=owner_id,
            building_id=building_id,
            building=a.building,
            square=a.square,
            floor=a.floor,
            rooms=a.rooms,
            pet_friendly=a.pet_friendly,
            amenities=a.amenities,
            description=a.description,
            price=a.price,
            updated_at=datetime.datetime.utcnow(),
        )
        values = {**apartment.dict()}
        values.pop('id', None)
        values.pop('added_at', None)
        query = ApartmentModel.update().where(ApartmentModel.c.id==id).values(**values)
        await self.database.execute(query=query)
        return apartment

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Apartment]:
        query = ApartmentModel.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def delete(self, id: int):
        query = ApartmentModel.delete().where(ApartmentModel.c.id==id)
        return await self.database.execute(query=query)

    async def get_by_id(self, id: int) -> Optional[Apartment]:
        query = ApartmentModel.select().where(ApartmentModel.c.id==id)
        apartment = await self.database.fetch_one(query=query)
        if apartment is None:
            return None
        return Apartment.parse_obj(apartment)