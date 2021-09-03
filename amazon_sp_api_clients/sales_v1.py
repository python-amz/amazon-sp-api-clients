from .base import BaseClient as __BaseClient
from typing import List as _List


class GetOrderMetricsResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: OrderMetricsList = OrderMetricsList(data["payload"])
        else:
            self.payload: OrderMetricsList = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class OrderMetricsInterval:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "interval" in data:
            self.interval: str = str(data["interval"])
        else:
            self.interval: str = None
        if "unitCount" in data:
            self.unitCount: int = int(data["unitCount"])
        else:
            self.unitCount: int = None
        if "orderItemCount" in data:
            self.orderItemCount: int = int(data["orderItemCount"])
        else:
            self.orderItemCount: int = None
        if "orderCount" in data:
            self.orderCount: int = int(data["orderCount"])
        else:
            self.orderCount: int = None
        if "averageUnitPrice" in data:
            self.averageUnitPrice: Money = Money(data["averageUnitPrice"])
        else:
            self.averageUnitPrice: Money = None
        if "totalSales" in data:
            self.totalSales: Money = Money(data["totalSales"])
        else:
            self.totalSales: Money = None


class Error:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "code" in data:
            self.code: str = str(data["code"])
        else:
            self.code: str = None
        if "message" in data:
            self.message: str = str(data["message"])
        else:
            self.message: str = None
        if "details" in data:
            self.details: str = str(data["details"])
        else:
            self.details: str = None


class Money:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "currencyCode" in data:
            self.currencyCode: str = str(data["currencyCode"])
        else:
            self.currencyCode: str = None
        if "amount" in data:
            self.amount: Decimal = Decimal(data["amount"])
        else:
            self.amount: Decimal = None


class OrderMetricsList(list, _List["OrderMetricsInterval"]):
    def __init__(self, data):
        super().__init__([OrderMetricsInterval(datum) for datum in data])
        self.data = data


class ErrorList(list, _List["Error"]):
    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class Decimal(str):
    pass


class SalesV1Client(__BaseClient):
    def getOrderMetrics(
        self,
        marketplaceIds: _List[str],
        interval: str,
        granularity: str,
        granularityTimeZone: str = None,
        buyerType: str = None,
        fulfillmentNetwork: str = None,
        firstDayOfWeek: str = None,
        asin: str = None,
        sku: str = None,
    ):
        url = "/sales/v1/orderMetrics".format()
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if interval is not None:
            params["interval"] = (interval,)
        if granularityTimeZone is not None:
            params["granularityTimeZone"] = (granularityTimeZone,)
        if granularity is not None:
            params["granularity"] = (granularity,)
        if buyerType is not None:
            params["buyerType"] = (buyerType,)
        if fulfillmentNetwork is not None:
            params["fulfillmentNetwork"] = (fulfillmentNetwork,)
        if firstDayOfWeek is not None:
            params["firstDayOfWeek"] = (firstDayOfWeek,)
        if asin is not None:
            params["asin"] = (asin,)
        if sku is not None:
            params["sku"] = (sku,)
        response = self.request(url, method="GET", params=params)
        return {
            200: GetOrderMetricsResponse,
            400: GetOrderMetricsResponse,
            403: GetOrderMetricsResponse,
            404: GetOrderMetricsResponse,
            413: GetOrderMetricsResponse,
            415: GetOrderMetricsResponse,
            429: GetOrderMetricsResponse,
            500: GetOrderMetricsResponse,
            503: GetOrderMetricsResponse,
        }[response.status_code](self._get_response_json(response))
