from pprint import pprint

import amazon_sp_api_clients
from .client_config import client_config, marketplace

reports_client = amazon_sp_api_clients.Reports20210630Client(**client_config)
orders_client = amazon_sp_api_clients.OrdersV0Client(**client_config)
upload_client = amazon_sp_api_clients.Uploads20201101Client(**client_config)


def test_upload():
    response = upload_client.createUploadDestinationForResource(
        resource='aplus/2020-11-01/contentDocuments',
        marketplaceIds=[marketplace.market_place],
        contentMD5='9e92dc1ed22ffc814f063f02b1c0f233',
        contentType='image/jpeg',
    )
    pprint(response.data)
