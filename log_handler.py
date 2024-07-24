def request_log(status_code, action):
    if status_code == 200:
        print(f"Accessed target page successfully action: {action}")
    else:
        print(f"Failed to access target page {status_code} action: {action}")