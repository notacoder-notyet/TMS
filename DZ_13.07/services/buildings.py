from distutils.command.build import build
from fastapi import HTTPException, status
from typing import List, Optional
from sqlalchemy import select, delete, update

from models.buildings import BuildingModel
from schemas.building import Building, BuildingIn
from .base import BaseServices


class BuildingServices(BaseServices):

    async def create(self, db, schema: BuildingIn) -> Building:
        building = BuildingModel(**schema.dict())
        db.add(building)
        db.commit()
        db.refresh(building)
        return building


    async def update(self, schema: BuildingIn, id: int) -> Building: # Осилил асинк БД на 50%, без async_engine и пр.
        query = update(BuildingModel).where(BuildingModel.id==id).values(**schema.dict())
        building = await self.database.execute(query=query)
        return building


    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Building]:
        query = select(BuildingModel).limit(limit).offset(skip)
        buildings = await self.database.fetch_all(query=query)
        return buildings


    async def delete(self, id: int):
        query = delete(BuildingModel).where(BuildingModel.id==id)
        deleted_building = await self.database.execute(query=query)
        return deleted_building


    async def get_by_id(self, id: int) -> Optional[Building]:
        query = select(BuildingModel).where(BuildingModel.id==id)
        building = await self.database.fetch_one(query=query)
        if building is None:
            return None
        return building
