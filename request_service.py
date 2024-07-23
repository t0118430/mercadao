from configuration import Configuration
from specs import payload_login, headers_login, headers_available
import requests
from log_handler import request_log

#TODO break this method
def fetch_orders(setup):
    headers_available["authorization"] = setup.token

    #resquest
    response = requests.request("GET", setup.url_available, headers=headers_available)

    request_log(response.status_code, "fetch_records")

    if response.status_code == 401:
        print("Token expired....")
        payload = payload_login.replace("$USERNAME", setup.username).replace("$PASSWORD", setup.password)

        #request
        response_login = requests.request("POST", setup.url, headers=headers_login, data=payload) 
        request_log(response_login.status_code, "login")

        data = response_login.json()
        print(data["id"])
        headers_available["authorization"] = data["id"]

        #resquest
        response = requests.request("GET", setup.url_available, headers=headers_available)

        request_log(response.status_code, "fetch_records")    

    return response.json() 