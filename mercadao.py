from order_processor import process_orders
from configuration import Configuration
from request_service import fetch_orders


def mercadao():
    try:

        setup = Configuration()
    
        print("dentro do mercadao")

        data = fetch_orders(setup)

        print("a seguir ao primeiro request")

        process_orders(data, setup.topic)
    except Exception as e:
        print(f"Error {e}")
mercadao()
