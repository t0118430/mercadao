from datetime import datetime

def write_to_file(filename, list):
    for item in list:
        with open(filename, 'a') as file:
            file.write(f"{item}\n")

def clear_file_content(file_path):
    with open(file_path, 'w') as file:
        # Opening a file in 'w' mode truncates the file and overwrites its content with nothing.
        pass   

def print_logs(data):
    with open('results.log', 'a') as file:
        file.write(f"{datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.000Z')} {data}\n")

def read_file():
    with open("order_track.txt", 'r') as file:
        lines = file.readlines()       
    return lines  
        
