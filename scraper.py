import requests
from bs4 import BeautifulSoup as bs
import datetime
from config import Config



class HardverScraper():

    def __init__(self,url):
        self.url = url

    def transform(self):
        page = self.url + "/?&kezdo=0&lista_perpage=200"
        scraped_page  = requests.get(page)
        soup_object = bs(scraped_page.text,"lxml")
        small_ads_first = soup_object.find_all("div",class_="left")
        small_ads_second = soup_object.find_all("div",class_="right")
        small_ads = list(zip(small_ads_first,small_ads_second))
        new_ads = [i for i in small_ads if i[0].find_all("h5")[0].attrs]
        return new_ads



class SmallAd():

    def __init__(self,title,link,price,date):
        self.title = title
        self.link = link
        self.price = price
        self.date = date


    @classmethod
    def factory(cls,new_ads):
        ad_objects = []
        for i in new_ads:
            title = i[0].get_text()
            link = "http://hardverapro.hu/"+i[0].find_all('a')[0]["href"]
            price = i[1].find_all("span",class_="price")[0].get_text()
            date = datetime.datetime.now()
            for term in Config.load("search_terms"):
                if term in title.lower():
                    ad_objects.append(SmallAd(title,link,price,date))
        return ad_objects




#
#
# my = HardverScraper("http://hardverapro.hu")
# x = my.transform()
#
# z = SmallAd.factory(x)
# for i in z:
#     print(i.title,i.link,i.price,i.date)


# x = datetime.date.today()
# print(x)
#
# for i in my.transform():
#     print(i[1].find_all("span",class_="price")[0].get_text())
# # print(my.transform().get_text())




# pattern = r"^apro"
#
#
#
# main = 'http://hardverapro.hu/'
#
#
#
# req = requests.get('http://hardverapro.hu/?&kezdo=200')
# soup = bs(req.text,"lxml")
# some = soup.find_all("div",class_="left")
# two = soup.find_all("div",class_="right")
# three = list(zip(some,two))
# if three[0][0].find_all("h5")[0].attrs:
#     print("yessss")


# # for i in some:
# #     print(i.div['global_list'])
# i = some[3]
# x = i.find_all("h5")
# print(x[0].attrs)
#
#
#
#
#
#
#
# # z = i.find_all("span",class_="price")
#
#
#
# # link = i.find_all('a')
# # a = link[0]
# # if re.match(pattern,a["href"]):
# #     print("yesssss")
# # print(a["href"])
