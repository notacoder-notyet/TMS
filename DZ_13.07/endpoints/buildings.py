from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from schemas.building import Building, BuildingIn
from schemas.user import User
from services.buildings import BuildingServices
from .depends import get_building_services, get_current_user

router = APIRouter()

@router.get('/', response_model=List[Building])
async def read_buildings(
    limit: int = 100,
    skip: int = 0,
    buildings: BuildingServices = Depends(get_building_services)
):
    return await buildings.get_all(limit=limit, skip=skip)

@router.post('/', response_model=Building)
async def create_building(
    id: int,
    b: BuildingIn,
    buildings: BuildingServices = Depends(get_building_services),
):
    return await buildings.create(b)

@router.put('/', response_model=Building)
async def update_building(
    id: int,
    b: BuildingIn,
    buildings: BuildingServices = Depends(get_building_services)
):
    building = await buildings.get_by_id(id=id)
    if building is None:
        raise exc_not_found
    return await buildings.update(id=id, b=b)

@router.delete('/')
async def delete_building(
    id: int,
    buildings: BuildingServices = Depends(get_building_services)
):
    building = await buildings.get_by_id(id=id)
    if building is None:
        raise exc_not_found
    result = await buildings.delete(id=id)
    return {'status': True}
