from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from schemas.review import Review, RenterReview, LandlordReview
from schemas.user import User
from services.reviews import ReviewServices
from models.reviews import LandlordReviewModel, RenterReviewModel
from .depends import (
    get_apartment,
    get_review_services,
    get_current_user,
    get_user, update_raiting,
    raiting_calculate)

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
    model: LandlordReviewModel,
    current_user: User = Depends(get_current_user),
    reviews: ReviewServices = Depends(get_review_services)
):
    review = await reviews.create_review(schema, model, user_id=current_user.id)
    obj = get_user(id=review.renter_id) #Подразумеваеться объект обзора(апартаменты или рентер)
    avg_value = raiting_calculate(score=model.score, object_id=model.renter_id, id=review.renter_id)
    updated_raiting = update_raiting(obj, avg_value)
    return review


@router.post('/2/', response_model=Review)
async def create_renter_review(
    schema: RenterReview,
    model: RenterReviewModel,
    current_user: User = Depends(get_current_user),
    reviews: ReviewServices = Depends(get_review_services)
):
    review = await reviews.create_review(schema, model, user_id=current_user.id)
    obj = get_apartment(id=review.apartment_id)
    avg_value = raiting_calculate(score=model.score, object_id=model.apartment_id, id=review.apartment_id)
    updated_raiting = update_raiting(obj, avg_value)
    return review


@router.put('/3/', response_model=Review)
async def update_landlord_review(
    schema: LandlordReview,
    model: LandlordReviewModel,
    id: int,
    current_user: User = Depends(get_current_user),
    reviews: ReviewServices = Depends(get_review_services)
):
    review = await reviews.get_by_id(id=id, model=model)
    if review is None or review.user_id != current_user.id:
        raise exc_not_found
    updated_review = await reviews.update_review(schema, id=id)
    obj = get_user(id=review.renter_id)
    avg_value = raiting_calculate(score=model.score, object_id=model.renter_id, id=review.renter_id)
    updated_raiting = update_raiting(obj, avg_value)
    return updated_review


@router.put('/4/', response_model=Review)
async def update_renter_review(
    schema: RenterReview,
    model: RenterReviewModel,
    id: int,
    current_user: User = Depends(get_current_user),
    reviews: ReviewServices = Depends(get_review_services)
):
    review = await reviews.get_by_id(id=id, model=model)
    if review is None or review.user_id != current_user.id:
        raise exc_not_found
    updated_review = await reviews.update_review(schema, id=id)
    obj = get_apartment(id=review.apartment_id)
    avg_value = raiting_calculate(score=model.score, object_id=model.apartment_id, id=review.apartment_id)
    updated_raiting = update_raiting(obj, avg_value)
    return updated_review


@router.delete('/5/', response_model=Review)
async def delete_landlord_review(
    id: int,
    model: LandlordReviewModel,
    current_user: User = Depends(get_current_user),
    reviews: ReviewServices = Depends(get_review_services)
):
    review = await reviews.get_by_id(id=id, model=model)
    if review is None or review.user_id != current_user.id:
        raise exc_not_found
    result = await reviews.delete_review(id=id)
    obj = get_user(id=review.renter_id) # Пройдет ли здесь операция, если объект уже будет удален выше
    avg_value = raiting_calculate(score=model.score, object_id=model.renter_id, id=review.renter_id)
    updated_raiting = update_raiting(obj, avg_value)
    return {'status': True}


@router.delete('/5/', response_model=Review)
async def delete_renter_review(
    id: int,
    model: RenterReviewModel,
    current_user: User = Depends(get_current_user),
    reviews: ReviewServices = Depends(get_review_services)
):
    review = await reviews.get_by_id(id=id, model=model)
    if review is None or review.user_id != current_user.id:
        raise exc_not_found
    result = await reviews.delete_review(id=id)
    obj = get_apartment(id=review.apartment_id)
    avg_value = raiting_calculate(score=model.score, object_id=model.apartment_id, id=review.apartment_id)
    updated_raiting = update_raiting(obj, avg_value)
    return {'status': True}
