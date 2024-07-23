from order_processor import process_orders
from configuration import Configuration
from request_service import fetch_orders


def mercadao():
    setup = Configuration()

    data = fetch_orders(setup)

    process_orders(data, setup.topic)

mercadao()