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
    print("Accessed target page successfully response")
else:
    print(f"Failed response to access target page {response.status_code} url: {url_available}")
    sys.exit(1)

def send_notification(topic):    
    try:
        requests.post("https://ntfy.sh/"+topic, 
    data="Trabalha boi".encode(encoding='utf-8'))
        print("Notification sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
        sys.exit(1)

def writeTofile(filename, list):
    for item in list:
        with open(filename, 'a') as file:
            file.write(f"{item}\n")

def clear_file_content(file_path):
    with open(file_path, 'w') as file:
        # Opening a file in 'w' mode truncates the file and overwrites its content with nothing.
        pass

data = response.json()

if data['count'] != 0:
    print("Processing orders...")

    cenas = data
    
    orders = []
    flag = 0
    with open('order_track.txt', 'r') as file:
        lines = file.readlines()
    
    print("Output from read file:", lines)

    if lines.count != 0:
        current_orders = [int(line.strip()) for line in lines]
    print("Current orders:", current_orders)

    for item in data['orders']:  
        order_id = item['identifier']  
        orders.append(order_id)
        print(f"Processing order {order_id}...")
        if order_id not in current_orders:
            current_orders.append(order_id)  
            flag = 1
    
    if flag == 1:
        print("Sending notification....")
        send_notification(topic)

    clear_file_content('order_track.txt')
    orders_to_keep = [order for order in orders if order in current_orders]
    print("Orders to keep:", orders_to_keep)
    writeTofile('order_track.txt', orders_to_keep)
else:
    cenas = "Não tem"
    print("Não tem")


with open('results.log', 'a') as file:
    file.write(f"{datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.000Z')} {cenas} \n")