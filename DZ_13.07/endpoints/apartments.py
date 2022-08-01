from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status
from typing import List

from schemas.apartment import Apartment, ApartmentIn
from schemas.user import User
from services.apartments import ApartmentServices
from services.notification import send_notification
from .depends import get_apartment_services, get_current_user, get_user


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


@router.put('/1', response_model=Apartment, status_code=200)
async def reservetion(
    id: int,
    background_tasks: BackgroundTasks,
    renter: User = Depends(get_current_user),
    apartments: ApartmentServices = Depends(get_apartment_services),
):
    apartment_for_booking = await apartments.get_by_id(id=id)
    if apartment_for_booking is None:
        raise exc_not_found
    if apartment_for_booking.owner_id == renter.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You cant book your own apartment')
    apartment_reserved = await apartments.reservation(apartment_for_booking, renter_id=renter.id)
    owner = get_user(id=apartment_for_booking.owner_id)
    background_tasks.add_task(
        send_notification,
        email=owner.email,
        message=f"Your apartment id: {apartment_for_booking.id} was booked by {renter.nickname}.\
        Renter data: {renter.phone_number} and {renter.email}."
    )
    return apartment_reserved


@router.put('/2', response_model=Apartment, status_code=200)
async def rental_confirmation(
    id: int,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
    apartments: ApartmentServices = Depends(get_apartment_services),
):
    apartment = await apartments.get_by_id(id=id)
    if apartment is None or apartment.owner_id != current_user.id:
        raise exc_not_found
    apartment_rented = await apartments.reservation(apartment)
    renter = get_user(id=apartment.renter_id)
    background_tasks.add_task(
        send_notification,
        email=renter.email,
        message=f"The owner confirmed the rental of the apartment.\
            Contact the owner if you haven't already: {current_user.phone_number}"
    )
    return apartment_rented
