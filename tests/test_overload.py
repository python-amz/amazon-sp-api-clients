from datetime import datetime
from threading import Thread

from amazon_sp_api_clients import OrdersV0Client
from .client_config import client_config, marketplace

client = OrdersV0Client(**client_config)


def worker():
    orders = client.getOrders(
        MarketplaceIds=[marketplace.market_place],
        CreatedAfter=datetime(2000, 1, 1).isoformat()).payload.Orders
    print(len(orders))


def main():
    for _ in range(30):
        Thread(target=worker).start()
