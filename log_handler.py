import sys

def request_log(status_code, action):
    if status_code == 200:
        print("Accessed target page successfully")
    else:
        print(f"Failed to access target page {status_code} action: {action}")
        sys.exit(1)