import requests
from datetime import datetime
import os
import sys

# Example URL (replace with the actual URL)
midnight_utc = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
formatted_date = midnight_utc.strftime('%Y-%m-%dT%H:%M:%S.000Z')

url = os.getenv('URL')
url_raw = os.getenv('URL_AVAILABLE')
url_available = url_raw + formatted_date
topic = os.getenv('TOPIC')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

payload_login = f"{{\"email\":\"{username}\",\"password\":\"{password}\"}}"
headers_login = {
  'Content-Type': 'text/plain'
}

response_login = requests.request("POST", url, headers=headers_login, data=payload_login)

# Check if the page is accessible
if response_login.status_code == 200:
    print("Accessed target page successfully")
else:
    print(f"Failed to access target page {response_login.status_code} url:{url}")
    sys.exit(1)

headers_available = {
  'authorization': f'{response_login.json()['id']}'
}

response = requests.request("GET", url_available, headers=headers_available)

if response.status_code == 200:
    print("Accessed target page successfully respose")
else:
    print(f"Failed response to access target page {response.status_code}")
    sys.exit(1)

def send_notification(topic):    
    try:
        requests.post("https://ntfy.sh/"+topic, 
    data="Trabalha boi".encode(encoding='utf-8'))
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
        sys.exit(1)

data = response.json()

# Check if datatable-selection tag is found
if data['count'] != 0:
    print("cenas")
    cenas = data
    send_notification(topic)    
else:
    cenas = "Não tem"
    print("Não tem")


with open('results.log', 'a') as file:
    file.write(f"{datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.000Z')} {cenas} \n")