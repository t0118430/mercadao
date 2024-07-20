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

        self.url = "http://localhost:5000/token"
        url_raw = "localhost:5000"
        self.url_available = "http://localhost:5000/orders"
        self.topic = "trabalhaboidevizUmS9N1lPsQJpN"
        self.username = "os.getenv('USERNAME')"
        self.password = "os.getenv('PASSWORD')"