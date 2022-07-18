from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from schemas.review import Review, LandlordReview
from schemas.user import User
from services.reviews import ReviewServices
from .depends import get_review_services, get_current_user

router = APIRouter()

@router.get('/', response_model=List[Review])
async def read_reviews(
    limit: int = 100,
    skip: int = 0,
    reviews: ReviewServices = Depends(get_review_services)
):
    return await reviews.get_all(limit=limit, skip=skip)

@router.post('/', response_model=Review)
async def create_review(
    id: int,
    r: LandlordReview,
    reviews: ReviewServices = Depends(get_review_services),
    current_user: User = Depends(get_current_user)
):
    return reviews.create(user_id=current_user.id, r=r)
    #здесь надо еще передавать апартаменты по выбору из List? и юзера как из endpoints.apartments

@router.put('/', response_model=Review)
async def update_review(
    id: int,
    r: LandlordReview,
    reviews: ReviewServices = Depends(get_review_services),
    current_user: User = Depends(get_current_user)
):
    review = await reviews.get_by_id(id=id)
    if review is None or review.user_id != current_user.id:
        raise exc_not_found
    return await reviews.update(id=id, owner_id=current_user.id, r=r)

@router.delete('/', response_model=Review)
async def delete_review(
    id: int,
    reviews: ReviewServices = Depends(get_review_services),
    current_user: User = Depends(get_current_user)
):
    review = await reviews.get_by_id(id=id)
    if review is None or review.owner_id != current_user.id:
        raise exc_not_found
    result = await reviews.delete(id=id)
    return {'status': True}
