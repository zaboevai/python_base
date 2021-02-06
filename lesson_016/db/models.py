from lesson_016 import *


class Forecast(db.Model):
    date = DateField(unique=True)
    temp = CharField()
    desc = CharField()

    class Meta:
        database = db


@db.connection_context()
def create_tables():
    db.create_tables([Forecast])
