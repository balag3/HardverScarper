import peewee

class BaseModel(Model):
    class Meta:
        database = db

class SmallAd(BaseModel):
    title = Charfield()
    url = Charfield()
    price = IntegerField()
    date = DateTimeField()

    def existing_ads():
        return SmallAd.select(title)
