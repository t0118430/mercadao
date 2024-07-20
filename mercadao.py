import requests
import sys
from specs import payload_login, headers_login, headers_available
from configuration import Configuration
from order_processor import OrderProcessor

def mercadao():
    setUp = Configuration()
    order_processor = OrderProcessor()

    payload_login["email"] = setUp.username
    payload_login["password"] = setUp.password

    #request
    response_login = requests.request("POST", setUp.url, headers=headers_login, data=payload_login)

    # Check if the page is accessible
    #log
    if response_login.status_code == 200:
        print("Accessed target page successfully")
    else:
        print(f"Failed to access target page {response_login.status_code} url:{setUp.url}")
        sys.exit(1)

    print(f"url avalable {setUp.url_available}")
    #resquest
    response = requests.request("GET", setUp.url_available, headers=headers_available)

    #log
    if response.status_code == 200:
        print("Accessed target page successfully response")
    else:
        print(f"Failed response to access target page {response.status_code} url: {setUp.url_available}")
        sys.exit(1)

    #pass to method
    data = response.json()

    order_processor.process_orders(data, setUp.topic)


mercadao()