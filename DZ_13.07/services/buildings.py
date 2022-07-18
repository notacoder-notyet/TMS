from fastapi import HTTPException, status
from typing import List, Optional

from models.buildings import Building as BuildingModel
from schemas.building import Building, BuildingIn
from .base import BaseServices

class BuildingServices(BaseServices):

    exc_not_found = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Building not found')

    async def create(self, b: BuildingIn) -> Building:
        building = Building(
            id=0,
            address=b.address,
            elevator=b.elevator,
            year=b.year,
            floors=b.floors,
            MTA=b.MTA,
        )
        values = {**building.dict()}
        values.pop('id', None)
        query = building.insert().values(**values)
        building.id = await self.database.execute(query=query)
        return building

    async def update(self, id: int, b: BuildingIn) -> Building:
        building = Building(
            id=id,
            address=b.address,
            elevator=b.elevator,
            year=b.year,
            floors=b.floors,
            MTA=b.MTA,
        )
        values = {**building.dict()}
        values.pop('id', None)
        values.pop('added_at', None)
        query = BuildingModel.update().where(BuildingModel.c.id==id).values(**values)
        await self.database.execute(query=query)
        return building

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Building]:
        query = BuildingModel.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def delete(self, id: int):
        query = BuildingModel.delete().where(BuildingModel.c.id==id)
        return await self.database.execute(query=query)

    async def get_by_id(self, id: int) -> Optional[Building]:
        query = BuildingModel.select().where(BuildingModel.c.id==id)
        building = await self.database.fetch_one(query=query)
        if building is None:
            return None
        return Building.parse_obj(building)