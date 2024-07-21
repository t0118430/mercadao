import requests
from specs import payload_login, headers_login, headers_available
from order_processor import process_orders
from configuration import Configuration
from log_handler import request_log

def mercadao():
    setup = Configuration()

    payload = payload_login.replace("$USERNAME", setup.username).replace("$PASSWORD", setup.password)

    #request
    response_login = requests.request("POST", setup.url, headers=headers_login, data=payload)

    # Check if the page is accessible
    request_log(response_login.status_code, "login")

    data = response_login.json()

    headers_available["authorization"] = data["id"]
    #resquest
    response = requests.request("GET", setup.url_available, headers=headers_available)

    request_log(response_login.status_code, "fetch_records")

    #pass to method
    data = response.json()

    process_orders(data, setup.topic)

mercadao()