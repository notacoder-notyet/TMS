from typing import List
from unittest import result
from fastapi import APIRouter, Depends, HTTPException, status

from schemas.apartment import Apartment, ApartmentIn
from schemas.user import User
from services.apartments import ApartmentServices
from .depends import get_apartment_services, get_current_user

router = APIRouter()

@router.get('/', response_model=List[Apartment])
async def read_apartments(
    limit: int = 100,
    skip: int = 0,
    apartments: ApartmentServices = Depends(get_apartment_services)
):
    return await apartments.get_all(limit=limit, skip=skip)

@router.post('/', response_model=Apartment)
async def create_apartment(
    a: ApartmentIn,
    apartments: ApartmentServices = Depends(get_apartment_services),
    current_user: User = Depends(get_current_user)
):
    return await apartments.create(owner_id=current_user.id, a=a)

@router.put('/', response_model=Apartment)
async def update_apartment(
    id: int,
    a: ApartmentIn,
    apartments: ApartmentServices = Depends(get_apartment_services),
    current_user: User = Depends(get_current_user)
):
    apartment = await apartments.get_by_id(id=id)
    if apartment is None or apartment.owner_id != current_user.id:
        raise exc_not_found
    return await apartments.update(id=id, owner_id=current_user.id, a=a)

@router.delete('/', response_model=Apartment)
async def delete_apartment(
    id: int,
    apartments: ApartmentServices = Depends(get_apartment_services),
    current_user: User = Depends(get_current_user)
):
    apartment = await apartments.get_by_id(id=id)
    if apartment is None or apartment.owner_id != current_user.id:
        raise exc_not_found
    result = await apartments.delete(id=id)
    return {'status': True}
