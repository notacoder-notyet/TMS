from services.users import UserServices
from db.base import database

def get_user_services() -> UserServices:
    return UserServices(database)