from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List


class GetOrderMetricsResponse:
    """
    The response schema for the getOrderMetrics operation.
    """

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
    """
    Contains order metrics.
    """

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
    """
    Error response returned when the request is unsuccessful.
    """

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
    """
    The currency type and the amount.
    """

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
    """
    A set of order metrics, each scoped to a particular time interval.
    """

    def __init__(self, data):
        super().__init__([OrderMetricsInterval(datum) for datum in data])
        self.data = data


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class Decimal(str):
    """
    A decimal number with no loss of precision. Useful when precision loss is unnaceptable, as with currencies. Follows RFC7159 for number representation.
    """


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
        """
                Returns aggregated order metrics for given interval, broken down by granularity, for given buyer type.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | .5 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/sales/v1/orderMetrics"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if interval is not None:
            params["interval"] = interval
        if granularityTimeZone is not None:
            params["granularityTimeZone"] = granularityTimeZone
        if granularity is not None:
            params["granularity"] = granularity
        if buyerType is not None:
            params["buyerType"] = buyerType
        if fulfillmentNetwork is not None:
            params["fulfillmentNetwork"] = fulfillmentNetwork
        if firstDayOfWeek is not None:
            params["firstDayOfWeek"] = firstDayOfWeek
        if asin is not None:
            params["asin"] = asin
        if sku is not None:
            params["sku"] = sku
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
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
