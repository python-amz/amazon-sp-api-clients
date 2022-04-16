from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class GenerateOrderScenarioRequest(__BaseDictObject):
    """
    The request body for the generateOrderScenarios operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "orders" in data:
            self.orders: _List[OrderScenarioRequest] = [OrderScenarioRequest(datum) for datum in data["orders"]]
        else:
            self.orders: _List[OrderScenarioRequest] = []


class OrderScenarioRequest(__BaseDictObject):
    """
    The party identifiers required to generate the test data.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = self._get_value(PartyIdentification, "sellingParty")
        else:
            self.sellingParty: PartyIdentification = None
        if "shipFromParty" in data:
            self.shipFromParty: PartyIdentification = self._get_value(PartyIdentification, "shipFromParty")
        else:
            self.shipFromParty: PartyIdentification = None


class PartyIdentification(__BaseDictObject):
    """
    The identification object for the party information. For example, warehouse code or vendor code. Please refer to specific party for more details.
    """

    def __init__(self, data):
        super().__init__(data)
        if "partyId" in data:
            self.partyId: str = self._get_value(str, "partyId")
        else:
            self.partyId: str = None


class Pagination(__BaseDictObject):
    """
    A generated string used to pass information to your next request. If NextToken is returned, pass the value of NextToken to the next request. If NextToken is not returned, there are no more order items to return.
    """

    def __init__(self, data):
        super().__init__(data)
        if "nextToken" in data:
            self.nextToken: str = self._get_value(str, "nextToken")
        else:
            self.nextToken: str = None


class TransactionReference(__BaseDictObject):
    """
    A GUID assigned by Amazon to identify this transaction.
    """

    def __init__(self, data):
        super().__init__(data)
        if "transactionId" in data:
            self.transactionId: str = self._get_value(str, "transactionId")
        else:
            self.transactionId: str = None


class TransactionStatus(__BaseDictObject):
    """
    The payload for the getOrderScenarios operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "transactionStatus" in data:
            self.transactionStatus: Transaction = self._get_value(Transaction, "transactionStatus")
        else:
            self.transactionStatus: Transaction = None


class Transaction(__BaseDictObject):
    """
    The transaction details including the status. If the transaction was successful, also includes the requested test order data.
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
        if "testCaseData" in data:
            self.testCaseData: TestCaseData = self._get_value(TestCaseData, "testCaseData")
        else:
            self.testCaseData: TestCaseData = None


class TestCaseData(__BaseDictObject):
    """
    The set of test case data returned in response to the test data request.
    """

    def __init__(self, data):
        super().__init__(data)
        if "scenarios" in data:
            self.scenarios: _List[Scenario] = [Scenario(datum) for datum in data["scenarios"]]
        else:
            self.scenarios: _List[Scenario] = []


class Scenario(__BaseDictObject):
    """
    A scenario test case response returned when the request is successful.
    """

    def __init__(self, data):
        super().__init__(data)
        if "scenarioId" in data:
            self.scenarioId: str = self._get_value(str, "scenarioId")
        else:
            self.scenarioId: str = None
        if "orders" in data:
            self.orders: _List[TestOrder] = [TestOrder(datum) for datum in data["orders"]]
        else:
            self.orders: _List[TestOrder] = []


class TestOrder(__BaseDictObject):
    """
    Error response returned when the request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        if "orderId" in data:
            self.orderId: str = self._get_value(str, "orderId")
        else:
            self.orderId: str = None


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


class VendorDirectFulfillmentSandboxTestData20211028Client(__BaseClient):
    def generateOrderScenarios(
        self,
        data: GenerateOrderScenarioRequest,
    ):
        """
        Submits a request to generate test order data for Vendor Direct Fulfillment API entities.
        """
        url = f"/vendor/directFulfillment/sandbox/2021-10-28/orders"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            202: TransactionReference,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getOrderScenarios(
        self,
        transactionId: str,
    ):
        """
        Returns the status of the transaction indicated by the specified transactionId. If the transaction was successful, also returns the requested test order data.
        """
        url = f"/vendor/directFulfillment/sandbox/2021-10-28/transactions/{transactionId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: TransactionStatus,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
