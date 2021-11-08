import gzip
from datetime import datetime, timedelta

import chardet
import requests

import amazon_sp_api_clients
from . import client_config

reports_client = amazon_sp_api_clients.Reports20210630Client(**client_config.client_config)
orders_client = amazon_sp_api_clients.OrdersV0Client(**client_config.client_config)


def test_get_orders():
    for order in orders_client.getOrders(
            [client_config.marketplace.market_place],
            CreatedAfter=(datetime.now() - timedelta(days=1000)).isoformat()
    ).payload.Orders:
        print(order.AmazonOrderId)


def test_get_inventory_report():
    report_id = reports_client.createReport(
        amazon_sp_api_clients.reports_2021_06_30.CreateReportSpecification({
            'reportType': 'GET_MERCHANT_LISTINGS_ALL_DATA',
            'marketplaceIds': [client_config.marketplace.market_place],
        })).reportId
    while True:
        response = reports_client.getReport(report_id)
        if response.processingStatus not in ('IN_QUEUE', 'IN_PROGRESS'):
            break
    document_id = response.reportDocumentId
    response = reports_client.getReportDocument(reportDocumentId=document_id)
    assert response.compressionAlgorithm == 'GZIP'
    data = requests.get(response.url).content
    data = gzip.decompress(data)
    encoding = chardet.detect(data)['encoding']
    lines = data.decode(encoding).splitlines()
    lines = [line.split('\t') for line in lines]
    columns = ('asin1', 'item-name', 'seller-sku', 'listing-id', 'price', 'quantity', 'product-id', 'status')
    indexes = [lines[0].index(f) for f in columns]
    data = [[line[i] for i in indexes] for line in lines[1:]]
    for line in data:
        print(line)


def test_get_and_delete_report():
    report_id = reports_client.createReport(
        amazon_sp_api_clients.reports_2021_06_30.CreateReportSpecification({
            'reportType': 'GET_MERCHANT_LISTINGS_ALL_DATA',
            'marketplaceIds': [client_config.marketplace.market_place],
        })).reportId
    print(report_id)
    response = reports_client.cancelReport(report_id)
    assert response is None
    response = reports_client.getReport(report_id)
    print(response.data)
