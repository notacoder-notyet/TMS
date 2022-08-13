from databases import Database
from db.base import database

class BaseServices:
    def __init__(self, database: Database):
        self.database = database