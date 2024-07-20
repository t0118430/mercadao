from file_handler import FileHandler
from notifier import Notifier
import sys

notificationService = Notifier()
file_handler = FileHandler()

class OrderProcessor:

    def process_orders(self, data, topic):
        if data['count'] != 0:
            try:
                print("Processing orders...")                
                orders = []
                flag = 0

                lines = file_handler.read_file()

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
                    notificationService.send_notification(topic)
                    file_handler.print_logs("Sent notification....")

                file_handler.clear_file_content('order_track.txt')
                orders_to_keep = [order for order in orders if order in current_orders]
                print("Orders to keep:", orders_to_keep)
                file_handler.writeTofile('order_track.txt', orders_to_keep)
            except Exception as e:
                print(f"Failed to process orders: {e}")
                sys.exit(1)
        else:
            file_handler.print_logs("Não tem.")
            print("Não tem")        