from datetime import datetime

import amazon_sp_api_clients
from tests.client_config import *


def test_get_orders():
    clients = amazon_sp_api_clients.AmazonSpApiClients(**client_config_v1)
    orders = clients.orders_v0.getOrders(
        MarketplaceIds=[marketplace.market_place],
        CreatedAfter=datetime(2000, 1, 1).isoformat()
    ).payload.Orders
    for order in orders:
        print(order.AmazonOrderId, order.LastUpdateDate)
