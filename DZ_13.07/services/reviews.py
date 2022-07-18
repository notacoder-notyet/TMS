import datetime
from fastapi import HTTPException, status
from typing import List


from models.reviews import Review as ReviewModel
from schemas.review import Review, RenterReview, LandlordReview
from .base import BaseServices

class ReviewServices(BaseServices):

    exc_not_found = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Review not found')

    '''Наверное надо использовать шаблонизатор и подставлять в аргумент небходимую
    схему. Т.к. они разняться объектом отзыва. Мысли есть, но времени нету,
    если можно, то давай обсудим как тут можно сделать на занятии. Предварительно
    запилю один из. Т.к. создавать два create только из-за различия в один параметр
    не правильно.
    Верно?
    Опять траблы из-за, вероятнее всего, неправильной компоновки моделей и их связей
    или неверного использования typing.List
    is_landlord наверн надо задавать автоматом, только я все так же не понимаю как
    сделать реквест на авторизованного юзера. Вообще этот collumn мне нужен был для
    фильтрации отзывов от домовладельцев и арендаторов'''
    async def create(self, user_id: int, apartment_id: int, renter_id:int, r: LandlordReview) -> Review:
        review = Review(
            id=0,
            user_id=user_id,
            apartment=r.apartment, #Это List, логика в том что и жилец и владелец пишут отзыв исходя от апартоментов
            apartment_id=apartment_id, #Соответственно надо задавать выбранный в List Apartment.id
            review=r.review,
            renter_score=r.renter_score, #Enum
            renter=r.renter, #Тоже List из схем
            renter_id=renter_id, #И тот же вопрос с id. Ps. их юзер видеть не должен
            added_at=datetime.datetime.utcnow(),
        )
        values = {**review.dict()}
        values.pop('id', None)
        values.pop('apartment_score', None)
        query = review.insert().values(**values)
        review.id = await self.database.execute(query=query)
        return review

    async def update(self, id: int, user_id: int, apartment_id: int, renter_id:int, r: LandlordReview) -> Review:
        '''Та же история что и с create
        Тоже про id. Меняться должен обзор, а обозреваемая квартира или рентер.
        В итоге оставлять renter_id=renter_id? Или стирать это из дикта и
        добавлять в pop как None?'''
        review = Review(
            id=id,
            user_id=user_id,
            apartment=r.apartment,
            apartment_id=apartment_id,
            review=r.review,
            renter_score=r.renter_score,
            renter=r.renter,
            renter_id=renter_id,
            added_at=datetime.datetime.utcnow(),
        )
        values = {**review.dict()}
        values.pop('id', None)
        values.pop('added_at', None)
        values.pop('apartment_score', None)
        query = ReviewModel.update().where(ReviewModel.c.id==id).values(**values)
        await self.database.execute(query=query)
        return review

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Review]:
        query = ReviewModel.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def delete(self, id: int):
        query = ReviewModel.delete().where(ReviewModel.c.id==id)
        return await self.database.execute(query=query)

    async def get_by_id(self, id: int) -> Review:
        query = ReviewModel.select().where(ReviewModel.c.id==id)
        review = await self.database.fetch_one(query=query)
        return Review.parse_obj(review)