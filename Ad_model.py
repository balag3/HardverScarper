from  peewee import *
from connect import db

class BaseModel(Model):
    class Meta:
        database = db

class MatchingAd(BaseModel):
    title = CharField()
    url = CharField()
    price = IntegerField()
    date = DateTimeField()


    def is_existing(ad):
        return len(MatchingAd.select().where(MatchingAd.title == ad)) != 0
