from .base import BaseClient as __BaseClient
from typing import List as _List


class GetTransactionResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: TransactionStatus = TransactionStatus(data["payload"])
        else:
            self.payload: TransactionStatus = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class TransactionStatus:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "transactionStatus" in data:
            self.transactionStatus: Transaction = Transaction(data["transactionStatus"])
        else:
            self.transactionStatus: Transaction = None


class Transaction:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "transactionId" in data:
            self.transactionId: str = str(data["transactionId"])
        else:
            self.transactionId: str = None
        if "status" in data:
            self.status: str = str(data["status"])
        else:
            self.status: str = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


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


class ErrorList(list, _List["Error"]):
    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class VendorTransactionStatusV1Client(__BaseClient):
    def getTransaction(
        self,
        transactionId: str,
    ):
        url = "/vendor/transactions/v1/transactions/{transactionId}".format(
            transactionId=transactionId,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetTransactionResponse,
            400: GetTransactionResponse,
            401: GetTransactionResponse,
            403: GetTransactionResponse,
            404: GetTransactionResponse,
            415: GetTransactionResponse,
            429: GetTransactionResponse,
            500: GetTransactionResponse,
            503: GetTransactionResponse,
        }[response.status_code](self._get_response_json(response))
