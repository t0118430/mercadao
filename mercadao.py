import requests
import sys
from specs import payload_login, headers_login, headers_available
from order_processor import OrderProcessor
from configuration import Configuration

def mercadao():
    order_processor = OrderProcessor()
    setup = Configuration()

    print(setup.username)
    print(setup.password)
    payload = payload_login.replace("$USERNAME", setup.username).replace("$PASSWORD", setup.password)

    #payload_login = f"{{\"email\":\"{setup.username}\",\"password\":\"{setup.password}\"}}"
    print(payload)

    #request
    response_login = requests.request("POST", setup.url, headers=headers_login, data=payload)

    # Check if the page is accessible
    #log
    if response_login.status_code == 200:
        print("Accessed target page successfully")
    else:
        print(f"Failed to access target page {response_login.status_code} url:{setup.url}")
        sys.exit(1)

    data = response_login.json()

    headers_available["authorization"] = data["id"]

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