import smtplib
from config import Config
from email.mime.text import MIMEText

class Mail():
    fromaddr = Config.load("sender")
    toaddrs  = Config.load("receiver")
    username = Config.load("mail_username")
    password = Config.load("mail_password")
    subject = "hardverapro"


    @classmethod
    def send(cls,message):
        msg = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (cls.fromaddr, ", ".join(cls.toaddrs), cls.subject, message)
        server = smtplib.SMTP(Config.load("server"))
        server.ehlo()
        server.starttls()
        server.login(cls.username, cls.password)
        server.sendmail(cls.fromaddr, cls.toaddrs, msg.encode("UTF-8"))
        server.quit()

    @staticmethod
    def format(ad_objects_list):
        return str("The following newly published ads correspond to your search criterias:" + "\n" + "\n".join(i.link + "\n" + str(i.title) + ' ----- ' + i.price + '\n'+str(i.date) + "\n"  for i in ad_objects_list))
