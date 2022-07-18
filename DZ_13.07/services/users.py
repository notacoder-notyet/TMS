import datetime
from typing import List, Optional

from models.users import User as UserModel
from schemas.user import User, UserIn
from core.security import hash_password
from .base import BaseServices

class UserServices(BaseServices):
    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        query = UserModel.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[User]:
        query = UserModel.select().where(UserModel.c.id==id)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def create(self, u: UserIn) -> User:
        user = User(
            id=0,
            nickname=u.nickname,
            email=u.email,
            hashed_password=hash_password(u.password),
            phone_number=u.phone_number,
            is_landlord=u.is_landlord,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )
        values = {**user.dict()}
        values.pop('id', None)
        query = UserModel.insert().values(**values)
        user.id = await self.database.execute(query)
        return user

    async def update(self, id: int, u: UserIn) -> User:
        user = User(
            id=id,
            nickname=u.nickname,
            email=u.email,
            hashed_password=hash_password(u.password),
            phone_number=u.phone_number,
            is_landlord=u.is_landlord,
            updated_at=datetime.datetime.utcnow(),
        )
        values = {**user.dict()}
        values.pop('id', None)
        values.pop('created_at', None)
        query = UserModel.update().where(UserModel.c.id==id).values(**values)
        await self.database.execute(query)
        return user

    async def get_by_email(self, email: str) -> Optional[User]:
        query = UserModel.select().where(UserModel.c.email==email)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)