import datetime
from pyexpat import model
from fastapi import HTTPException, status
from typing import List
from sqlalchemy import delete, select, insert, update


from models.reviews import LandlordReviewModel, RenterReviewModel
from schemas.review import Review, RenterReview, LandlordReview
from .base import BaseServices

class ReviewServices(BaseServices):

    async def create_review(self, schema, model, user_id: int) -> Review:
        data = schema.dict()
        data['user_id'] = user_id
        data['added_at'] = datetime.datetime.utcnow()
        data['updated_at'] = datetime.datetime.utcnow()
        query = insert(model).values(**data)
        review = await self.database.execute(query=query)
        return review


    async def update_review(self, schema, model, id: int) -> Review:
        data = schema.dict()
        data['updated_at'] = datetime.datetime.utcnow()
        query = update(model).where(model.id==id).values(**data)
        review = await self.database.execute(query=query)
        return review


    async def delete_review(self, model, id: int):
        query = delete(model).where(model.id==id)
        review = await self.database.execute(query=query)
        return review


    # async def get_all(self, limit: int = 100, skip: int = 0) -> List[Review]:
    #     query = select(ReviewModel).limit(limit).offset(skip)
    #     reviews = await self.database.fetch_all(query=query)
    #     return reviews

 
    async def get_by_id(self, model, id: int) -> Review:
        query = select(model).where(model.id==id)
        review = await self.database.fetch_one(query=query)
        return review
