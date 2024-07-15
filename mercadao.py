import requests
from datetime import datetime
import os

# Example URL (replace with the actual URL)
midnight_utc = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
formatted_date = midnight_utc.strftime('%Y-%m-%dT%H:%M:%S.000Z')

url_raw = os.getenv('URL')
url = url_raw + formatted_date
url_available = os.getenv('URL_AVAILABLE')
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
    print(f"Failed to access target page {response_login.status_code}")
    exit()

headers_available = {
  'authorization': f'{response_login.json()['id']}'
}

response = requests.request("GET", url_available, headers=headers_available)

if response.status_code == 200:
    print("Accessed target page successfully respose")
else:
    print(f"Failed response to access target page {response.status_code}")
    exit()

def send_notification(topic):    
    try:
        requests.post("https://ntfy.sh/"+topic, 
    data="Trabalha boi".encode(encoding='utf-8'))
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

data = response.json()

# Check if datatable-selection tag is found
if data['count'] != 0:
    print("cenas")
    send_notification(topic)    
else:
    print("Não tem")

