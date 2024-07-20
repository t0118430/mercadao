from datetime import datetime
import os

class Configuration:
    def __init__(self):
        midnight_utc = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
        formatted_date = midnight_utc.strftime('%Y-%m-%dT%H:%M:%S.000Z')

        #envs
        self.url = os.getenv('URL')
        url_raw = os.getenv('URL_AVAILABLE')
        self.url_available = url_raw + formatted_date
        self.topic = os.getenv('TOPIC')
        self.username = os.getenv('USERNAME')
        self.password = os.getenv('PASSWORD')