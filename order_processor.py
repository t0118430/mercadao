from file_handler import FileHandler
from notifier import Notifier

class OrderProcessor:
    def __init__(self, file_handler, notifier):
        self.file_handler = file_handler
        self.notifier = notifier

    def process_orders(self, data):
        if data['count'] != 0:
            print("Processing orders...")
            
            orders = []
            self.file_handler.read_file()

            with open('order_track.txt', 'r') as file:
                lines = file.readlines()

            if lines.count != 0:
                current_orders = [int(line.strip()) for line in lines]
            print("Current orders:", current_orders)

            orders_to_keep = []
            for item in data['orders']:  
                order_id = item['identifier']  
                orders.append(order_id)
                print(f"Processing order {order_id}...")
                if order_id not in current_orders:
                    print("Sending notification....")
                    orders_to_keep.append(order_id)  
                    
            if orders_to_keep.count != 0:
                print("Sending notification....")
                send_notification(topic)

            print("Orders to keep:", orders_to_keep)
            clear_file_content('order_track.txt')
            writeTofile('order_track.txt', orders_to_keep)
        else:
            cenas = "Não tem"
            print("Não tem")        