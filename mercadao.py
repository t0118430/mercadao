import requests
import sys
from specs import payload_login, headers_login, headers_available
from order_processor import OrderProcessor
from datetime import datetime
import os

def mercadao():
    order_processor = OrderProcessor()

    midnight_utc = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    formatted_date = midnight_utc.strftime('%Y-%m-%dT%H:%M:%S.000Z')

    url = os.getenv('URL')
    url_raw = os.getenv('URL_AVAILABLE')
    url_available = url_raw + formatted_date
    topic = os.getenv('TOPIC')
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    payload_login["username"] = username
    payload_login["password"] = password
    print(f"url avalable {payload_login}")
    print(f"url avalable {headers_login}")

    #request
    response_login = requests.request("POST", url, headers=headers_login, data=payload_login)

    # Check if the page is accessible
    #log
    if response_login.status_code == 200:
        print("Accessed target page successfully")
    else:
        print(f"Failed to access target page {response_login.status_code} url:{url}")
        sys.exit(1)

    print(f"url avalable {url_available}")
    #resquest
    response = requests.request("GET", url_available, headers=headers_available)

    #log
    if response.status_code == 200:
        print("Accessed target page successfully response")
    else:
        print(f"Failed response to access target page {response.status_code} url: {setUp.url_available}")
        sys.exit(1)

    #pass to method
    data = response.json()

    order_processor.process_orders(data, topic)


mercadao()