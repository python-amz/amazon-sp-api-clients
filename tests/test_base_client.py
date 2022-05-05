from datetime import datetime

from amazon_sp_api_clients.utils.base_client import BaseClient
from tests.client_config import client_config, marketplace

base_client = BaseClient(**client_config)


def test_request():
    response = base_client.request('/orders/v0/orders', params={
        'MarketplaceIds': marketplace.market_place,
        'CreatedAfter': datetime(2000, 1, 1).isoformat(),
    })
    json = response.json()
    keys = ('MarketplaceId', 'AmazonOrderId', 'OrderStatus', 'LastUpdateDate')
    print()
    print(' '.join((f'{k:>30}' for k in keys)))
    for order in json['payload']['Orders']:
        print(' '.join((f'{order[k]:>30}' for k in keys)))
    assert json['payload']['Orders']
