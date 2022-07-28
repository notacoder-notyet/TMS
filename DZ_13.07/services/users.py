import datetime
from typing import List, Optional
from sqlalchemy import select

from models.users import UserModel
from schemas.user import User, UserIn
from core.security import hash_password
from .base import BaseServices
# from db.base import db


class UserServices(BaseServices):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        query = select(UserModel).limit(limit).offset(skip)
        get_users = await self.database.fetch_all(query=query)
        return get_users


    async def get_by_id(self, db, id: int) -> Optional[User]:
        user = db.query(UserModel).filter_by(id=id).first()
        if user is None:
            return None
        return user


    async def create(self, db, schema) -> User:
        data = schema.dict()
        data['password'] = hash_password(schema.password)
        data['created_at'] = datetime.datetime.utcnow()
        data['updated_at'] = datetime.datetime.utcnow()
        user = UserModel(**data)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user


    async def update(self, db, old_user, schema) -> User:
        for key, value in schema.dict().items():
            setattr(old_user, key, value)
        setattr(old_user, 'password', hash_password(schema.password))
        setattr(old_user, 'updated_at', datetime.datetime.utcnow())
        db.commit()
        db.refresh(old_user)
        return old_user


    async def get_by_email(self, email: str) -> Optional[User]:
        query = select(UserModel).where(UserModel.email==email)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)
