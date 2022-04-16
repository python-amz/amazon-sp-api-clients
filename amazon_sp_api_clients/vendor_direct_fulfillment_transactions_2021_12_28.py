from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class TransactionStatus(__BaseDictObject):
    """
    The payload for the getTransactionStatus operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "transactionStatus" in data:
            self.transactionStatus: Transaction = self._get_value(Transaction, "transactionStatus")
        else:
            self.transactionStatus: Transaction = None


class Transaction(__BaseDictObject):
    """
    The transaction status details.
    """

    def __init__(self, data):
        super().__init__(data)
        if "transactionId" in data:
            self.transactionId: str = self._get_value(str, "transactionId")
        else:
            self.transactionId: str = None
        if "status" in data:
            self.status: str = self._get_value(str, "status")
        else:
            self.status: str = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class ErrorList(__BaseDictObject):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: _List[Error] = [Error(datum) for datum in data["errors"]]
        else:
            self.errors: _List[Error] = []


class Error(__BaseDictObject):
    """
    Error response returned when the request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        if "code" in data:
            self.code: str = self._get_value(str, "code")
        else:
            self.code: str = None
        if "message" in data:
            self.message: str = self._get_value(str, "message")
        else:
            self.message: str = None
        if "details" in data:
            self.details: str = self._get_value(str, "details")
        else:
            self.details: str = None


class VendorDirectFulfillmentTransactions20211228Client(__BaseClient):
    def getTransactionStatus(
        self,
        transactionId: str,
    ):
        """
                Returns the status of the transaction indicated by the specified transactionId.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/vendor/directFulfillment/transactions/2021-12-28/transactions/{transactionId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: TransactionStatus,
            400: ErrorList,
            401: Error,
            403: Error,
            404: Error,
            415: Error,
            429: Error,
            500: Error,
            503: Error,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
