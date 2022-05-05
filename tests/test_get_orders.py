from datetime import datetime

import amazon_sp_api_clients_2
from .client_config import client_config, marketplace

clients = amazon_sp_api_clients_2.AmazonSpApiClients(**client_config)


def test_get_orders():
    orders = clients.orders_v0.get_orders(
        marketplace_ids=[marketplace.market_place],
        created_after=datetime.utcnow().isoformat(),
    )
    print(orders)
