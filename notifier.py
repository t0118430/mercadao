import requests
import sys

def send_notification(topic):    
    try:
        requests.post("https://ntfy.sh/"+topic, 
            data="Trabalha boi".encode(encoding='utf-8'))
        print("Notification sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
        sys.exit(1)