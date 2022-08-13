from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from schemas.building import Building, BuildingIn
from schemas.user import User
from services.buildings import BuildingServices
from .depends import get_building_services, get_current_user, get_db

router = APIRouter()

exc_not_found = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Building not found')

@router.get('/', response_model=List[Building])
async def read_buildings(
    limit: int = 100,
    skip: int = 0,
    buildings: BuildingServices = Depends(get_building_services)
):
    get_buildings = await buildings.get_all(limit=limit, skip=skip)
    return get_buildings


@router.post('/', response_model=Building)
async def create_building(
    schema: BuildingIn,
    buildings: BuildingServices = Depends(get_building_services),
    db: Session = Depends(get_db)
):
    building = await buildings.create(db, schema)
    return building


@router.put('/', response_model=Building)
async def update_building(
    schema: BuildingIn,
    id: int,
    buildings: BuildingServices = Depends(get_building_services)
):
    building = await buildings.get_by_id(id=id)
    if building is None:
        raise exc_not_found
    building = await buildings.update(schema, id)
    return building


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
