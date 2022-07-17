from email.policy import default
from starlette.config import Config

config = Config('.env')

SQLALCHEMY_DATABASE_URL = config('RENT_APPARTMENTS_DB', cast=str, default='')