import datetime
from fastapi import HTTPException, status
from typing import List
from sqlalchemy import delete, select, insert, update


from models.reviews import ReviewModel
from schemas.review import Review, RenterReview, LandlordReview
from .base import BaseServices

class ReviewServices(BaseServices):
    async def create_landlord(self, schema: LandlordReview, user_id: int) -> Review:
        data = schema.dict()
        data['user_id'] = user_id
        data['added_at'] = datetime.datetime.utcnow()
        data['updated_at'] = datetime.datetime.utcnow()
        query = insert(ReviewModel).values(**data)
        review = await self.database.execute(query=query)
        return review


    async def create_renter(self, schema: RenterReview, user_id: int) -> Review:
        data = schema.dict()
        data['user_id'] = user_id
        data['added_at'] = datetime.datetime.utcnow()
        data['updated_at'] = datetime.datetime.utcnow()
        query = insert(ReviewModel).values(**data)
        review = await self.database.execute(query=query)
        return review


    async def update_landlord(self, schema: LandlordReview, id: int) -> Review:
        data = schema.dict()
        data['updated_at'] = datetime.datetime.utcnow()
        query = update(ReviewModel).where(ReviewModel.id==id).values(**data)
        review = await self.database.execute(query=query)
        return review


    async def update_renter(self, schema: RenterReview, id: int) -> Review:
        data = schema.dict()
        data['updated_at'] = datetime.datetime.utcnow()
        query = update(ReviewModel).where(ReviewModel.id==id).values(**data)
        review = await self.database.execute(query=query)
        return review


    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Review]:
        query = select(ReviewModel).limit(limit).offset(skip)
        get_reviews = await self.database.fetch_all(query=query)
        return get_reviews


    async def delete(self, id: int):
        query = delete(ReviewModel).where(ReviewModel.id==id)
        review_delete = await self.database.execute(query=query)
        return review_delete

 
    async def get_by_id(self, id: int) -> Review:
        query = select(ReviewModel).where(ReviewModel.id==id)
        review = await self.database.fetch_one(query=query)
        return Review.parse_obj(review)
