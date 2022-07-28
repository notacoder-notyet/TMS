from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from schemas.apartment import Apartment, ApartmentIn
from schemas.user import User
from services.apartments import ApartmentServices
from .depends import get_apartment_services, get_current_user


router = APIRouter()

exc_not_found = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Apartment not found')


@router.get('/', response_model=List[Apartment])
async def read_apartments(
    limit: int = 100,
    skip: int = 0,
    apartments: ApartmentServices = Depends(get_apartment_services)
):
    get_apartments = await apartments.get_all(limit=limit, skip=skip)
    return get_apartments


@router.post('/', response_model=Apartment, status_code=200)
async def create_apartment(
    schema: ApartmentIn,
    current_user: User = Depends(get_current_user),
    apartments: ApartmentServices = Depends(get_apartment_services)
):
    apartment = await apartments.create(schema, owner_id=current_user.id)
    return apartment


@router.put('/', response_model=Apartment, status_code=200)
async def update_apartment(
    schema: ApartmentIn,
    id: int,
    current_user: User = Depends(get_current_user),
    apartments: ApartmentServices = Depends(get_apartment_services)
):
    apartment = await apartments.get_by_id(id=id)
    if apartment is None or apartment.owner_id != current_user.id:
        raise exc_not_found
    apartment_update = await apartments.update(schema, id=id)
    return apartment_update


@router.delete('/', response_model=Apartment, status_code=200)
async def delete_apartment(
    id: int,
    current_user: User = Depends(get_current_user),
    apartments: ApartmentServices = Depends(get_apartment_services)
):
    apartment = await apartments.get_by_id(id=id)
    if apartment is None or apartment.owner_id != current_user.id:
        raise exc_not_found
    result = await apartments.delete(id=id)
    return {'status': True}
