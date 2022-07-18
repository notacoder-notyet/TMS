from starlette.config import Config

config = Config('.env')

SQLALCHEMY_DATABASE_URL = config("RENT_APPARTMENTS_DB", cast=str, default='')
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("RA_SECRET_KEY", cast=str, default="0b26d37f996a5d2adf6278d1303c484ec9d26ad2322ee564ee285806a43936e5")