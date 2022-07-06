import json
from datetime import datetime
from pathlib import Path

import cattrs

import amazon_sp_api_clients_2
from amazon_sp_api_clients_2.api.orders_v0 import GetOrdersResponse
from .client_config import client_config, marketplace

clients = amazon_sp_api_clients_2.AmazonSpApiClients(**client_config)


def test_download_orders():
    response = clients.request("/orders/v0/orders", params={
        'MarketplaceIds': marketplace.market_place,
        'CreatedAfter': datetime(2000, 1, 1).isoformat(),
    })
    data = response.json()
    path = Path(__file__).parent / 'orders.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def test_get_orders():
    debug = True
    if debug:
        path = Path(__file__).parent / 'orders.json'
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # orders = cattrs.structure(data, GetOrdersResponse)
        orders = GetOrdersResponse.from_json(data)
    else:
        orders = clients.orders_v0.get_orders(
            marketplace_ids=[marketplace.market_place],
            created_after=datetime(2000, 1, 1).isoformat(),
        )
    for o in orders.payload.orders:
        print(f'{o.amazon_order_id} | {o.purchase_date} | {o.buyer_info}')
