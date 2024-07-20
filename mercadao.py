import requests
import sys
from specs import payload_login, headers_login, headers_available
from order_processor import OrderProcessor
from datetime import datetime
import os
from configuration import Configuration

def mercadao():
    order_processor = OrderProcessor()
    setup = Configuration()

    #payload_login["email"] = setup.username
    #payload_login["password"] = setup.password
    #print(f"url avalable {payload_login}")
    #print(f"url avalable {headers_login}")

    payload_login = f"{{\"email\":\"{setup.username}\",\"password\":\"{setup.password}\"}}"

    #request
    response_login = requests.request("POST", setup.url, headers=headers_login, data=payload_login)

    # Check if the page is accessible
    #log
    if response_login.status_code == 200:
        print("Accessed target page successfully")
    else:
        print(f"Failed to access target page {response_login.status_code} url:{setup.url}")
        sys.exit(1)

    headers_available["authorization"] = response_login.json()["id"]

    print(f"url avalable {setup.url_available}")
    #resquest
    response = requests.request("GET", setup.url_available, headers=headers_available)

    #log
    if response.status_code == 200:
        print("Accessed target page successfully response")
    else:
        print(f"Failed response to access target page {response.status_code} url: {setup.url_available}")
        sys.exit(1)

    #pass to method
    data = response.json()

    order_processor.process_orders(data, setup.topic)


mercadao()