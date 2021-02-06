from peewee import *


class Database:

    def __init__(self, url):
        database_proxy = DatabaseProxy()
        self._db = SqliteDatabase(url)
        database_proxy.initialize(self._db)

    @property
    def db(self):
        return self._db

# db = Database(url=DATABASE_PATH)
