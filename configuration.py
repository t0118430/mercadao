from datetime import datetime
import os

class Configuration:
    def __init__(self):
        midnight_utc = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
        formatted_date = midnight_utc.strftime('%Y-%m-%dT%H:%M:%S.000Z')

        #envs
        #self.url = os.getenv('URL')
        #self.url_raw = os.getenv('URL_AVAILABLE')
        #self.url_available = self.url_raw + formatted_date
        #self.topic = os.getenv('TOPIC')
        #self.username = os.getenv('USERNAME')
        #self.password = os.getenv('PASSWORD')
        #self.token = os.getenv('TOKEN)
#
        self.url = "https://admin.mercadao.pt/api/shoppers/login"
        self.url_raw = "https://admin.mercadao.pt/api/shoppers/orders/available?limit=10&deliveryFrom="
        self.url_available = self.url_raw+formatted_date
        self.topic = "trabalhaboidevizUmS9N1lPsQJpN"
        self.username = "daniel.ribeiro4@hotmail.com"
        self.password = "Mercadao1904."
        self.token = "xqxT8FeyrM9Z9KrXBf1CtpYqo3V9bg19K6CUo88WIK03GtPggyp0uqDUcq2K2EO5"