from configuration import Configuration
from specs import payload_login, headers_login, headers_available
import requests
from log_handler import request_log
from file_handler import read_file, clear_file_content, write_to_file

#TODO break this method
def fetch_orders(setup):

    token = read_file("token.txt")

    headers_available["authorization"] = token[0].strip()

    #resquest
    response = requests.request("GET", setup.url_available, headers=headers_available)

    request_log(response.status_code, "fetch_records")

    if response.status_code == 401:
        print("Token expired....")
        clear_file_content("token.txt")
        payload = payload_login.replace("$USERNAME", setup.username).replace("$PASSWORD", setup.password)

        #request
        response_login = requests.request("POST", setup.url, headers=headers_login, data=payload) 
        request_log(response_login.status_code, "login")

        data = response_login.json()
        
        write_to_file("token.txt", list([data["id"]]))
        
        headers_available["authorization"] = data["id"]

        #resquest
        response = requests.request("GET", setup.url_available, headers=headers_available)

        request_log(response.status_code, "fetch_records")    

    return response.json() 