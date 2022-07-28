from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from schemas.review import Review, RenterReview, LandlordReview
from schemas.user import User
from services.reviews import ReviewServices
from .depends import get_review_services, get_current_user

router = APIRouter()

exc_not_found = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review not found')

@router.get('/', response_model=List[Review])
async def read_reviews(
    limit: int = 100,
    skip: int = 0,
    reviews: ReviewServices = Depends(get_review_services)
):
    get_reviews = await reviews.get_all(limit=limit, skip=skip)
    return get_reviews


@router.post('/1/', response_model=Review)
async def create_landlord_review(
    schema: LandlordReview,
    current_user: User = Depends(get_current_user),
    reviews: ReviewServices = Depends(get_review_services)
):
    review_create = await reviews.create_landlord(schema, user_id=current_user.id)
    return review_create


@router.post('/2/', response_model=Review)
async def create_renter_review(
    schema: RenterReview,
    current_user: User = Depends(get_current_user),
    reviews: ReviewServices = Depends(get_review_services)
):
    review_create = await reviews.create_renter(schema, user_id=current_user.id)
    return review_create


@router.put('/3/', response_model=Review)
async def update_landlord_review(
    schema: LandlordReview,
    id: int,
    current_user: User = Depends(get_current_user),
    reviews: ReviewServices = Depends(get_review_services)
):
    review = await reviews.get_by_id(id=id)
    if review is None or review.user_id != current_user.id:
        raise exc_not_found
    review_update = await reviews.update_landlord(schema, id=id)
    return review_update


@router.put('/4/', response_model=Review)
async def update_renter_review(
    schema: RenterReview,
    id: int,
    current_user: User = Depends(get_current_user),
    reviews: ReviewServices = Depends(get_review_services)
):
    review = await reviews.get_by_id(id=id)
    if review is None or review.user_id != current_user.id:
        raise exc_not_found
    review_update = await reviews.update_renter(schema, id=id)
    return review_update


@router.delete('/', response_model=Review)
async def delete_review(
    id: int,
    current_user: User = Depends(get_current_user),
    reviews: ReviewServices = Depends(get_review_services)
):
    review = await reviews.get_by_id(id=id)
    if review is None or review.user_id != current_user.id:
        raise exc_not_found
    result = await reviews.delete(id=id)
    return {'status': True}
