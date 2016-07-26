from connect import db
from Ad_model import MatchingAd
from scraper import *
from config import Config



if MatchingAd.table_exists():
    pass
else:
    db.create_tables([MatchingAd], safe=True)



my = HardverScraper("http://hardverapro.hu")
x = my.transform()

z = SmallAd.factory(x)
for i in z:
    if not MatchingAd.is_existing(i.title):
        MatchingAd.create(title=i.title,url=i.link,price=int(i.price.replace("Ft","").replace(" ","")),date=i.date)
