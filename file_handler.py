from datetime import datetime
import os

def resolve_path(filename):
    return os.path.join("/home/sinister/mercadao/prod/",filename)

def write_to_file(filename, list):
    try:
        filename = resolve_path(filename)
        for item in list:
            with open(filename, 'a') as file:
                file.write(f"{item}\n")
    except Exception as e:
        print(f"Error {e}")

def clear_file_content(filename): 
    filename = resolve_path(filename)
    with open(filename, 'w') as file:
        # Opening a file in 'w' mode truncates the file and overwrites its content with nothing.
        pass   

def print_to_file(filename, data):
    filename = resolve_path(filename)
    with open(filename, 'a') as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000Z')} {data}\n")

def read_file(filename):
    filename = resolve_path(filename)
    with open(filename, 'r') as file:
        return file.readlines()

