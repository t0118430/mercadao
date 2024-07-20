import requests
import sys
from specs import payload_login, headers_login, headers_available
from order_processor import OrderProcessor
from configuration import Configuration
from log_handler import Log

def mercadao():
    order_processor = OrderProcessor()
    setup = Configuration()
    logging = Log()

    print(setup.username)
    print(setup.password)
    payload = payload_login.replace("$USERNAME", setup.username).replace("$PASSWORD", setup.password)

    #request
    response_login = requests.request("POST", setup.url, headers=headers_login, data=payload)

    # Check if the page is accessible
    logging.request_log(response_login.status_code, "login")

    data = response_login.json()

    headers_available["authorization"] = data["id"]

    print(f"url avalable {setup.url_available}")
    #resquest
    response = requests.request("GET", setup.url_available, headers=headers_available)

    logging.request_log(response_login.status_code, "fetch_records")

    #pass to method
    data = response.json()

    order_processor.process_orders(data, setup.topic)

mercadao()