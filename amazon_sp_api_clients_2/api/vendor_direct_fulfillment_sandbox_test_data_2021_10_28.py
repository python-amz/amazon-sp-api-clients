"""
Selling Partner API for Vendor Direct Fulfillment Sandbox Test Data
=============================================================================================

The Selling Partner API for Vendor Direct Fulfillment Sandbox Test Data provides programmatic access to vendor direct fulfillment sandbox test data.
API Version: 2021-10-28
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _error_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Error(**data)

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occured.
    """

    details: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _error_list_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ErrorList(**data)

    errors: List["Error"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GenerateOrderScenarioRequest:
    """
    The request body for the generateOrderScenarios operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _generate_order_scenario_request_name_convert
        data = {name_convert[k]: v for k, v in data}
        return GenerateOrderScenarioRequest(**data)

    orders: Optional[List["OrderScenarioRequest"]] = attrs.field()
    """
    The list of test orders requested as indicated by party identifiers.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderScenarioRequest:
    """
    The party identifiers required to generate the test data.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _order_scenario_request_name_convert
        data = {name_convert[k]: v for k, v in data}
        return OrderScenarioRequest(**data)

    selling_party: "PartyIdentification" = attrs.field()
    """
    The identification object for the party information. For example, warehouse code or vendor code. Please refer to specific party for more details.
    """

    ship_from_party: "PartyIdentification" = attrs.field()
    """
    The identification object for the party information. For example, warehouse code or vendor code. Please refer to specific party for more details.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Pagination:
    """
    A generated string used to pass information to your next request. If NextToken is returned, pass the value of NextToken to the next request. If NextToken is not returned, there are no more order items to return.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _pagination_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Pagination(**data)

    next_token: Optional[str] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartyIdentification:
    """
    The identification object for the party information. For example, warehouse code or vendor code. Please refer to specific party for more details.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _party_identification_name_convert
        data = {name_convert[k]: v for k, v in data}
        return PartyIdentification(**data)

    party_id: str = attrs.field()
    """
    Assigned identification for the party. For example, warehouse code or vendor code. Please refer to specific party for more details.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Scenario:
    """
    A scenario test case response returned when the request is successful.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _scenario_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Scenario(**data)

    orders: List["TestOrder"] = attrs.field()
    """
    A list of orders that can be used by the caller to test each life cycle or scenario.
    """

    scenario_id: str = attrs.field()
    """
    An identifier that identifies the type of scenario that user can use for testing.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TestCaseData:
    """
    The set of test case data returned in response to the test data request.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _test_case_data_name_convert
        data = {name_convert[k]: v for k, v in data}
        return TestCaseData(**data)

    scenarios: Optional[List["Scenario"]] = attrs.field()
    """
    Set of use cases that describes the possible test scenarios.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TestOrder:
    """
    Error response returned when the request is unsuccessful.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _test_order_name_convert
        data = {name_convert[k]: v for k, v in data}
        return TestOrder(**data)

    order_id: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Transaction:
    """
    The transaction details including the status. If the transaction was successful, also includes the requested test order data.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _transaction_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Transaction(**data)

    status: Union[Literal["FAILURE"], Literal["PROCESSING"], Literal["SUCCESS"]] = attrs.field()
    """
    The current processing status of the transaction.
    """

    test_case_data: Optional["TestCaseData"] = attrs.field(
        default=None,
    )
    """
    The set of test case data returned in response to the test data request.
    """

    transaction_id: str = attrs.field()
    """
    The unique identifier returned in the response to the generateOrderScenarios request.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransactionReference:
    """
    A GUID assigned by Amazon to identify this transaction.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _transaction_reference_name_convert
        data = {name_convert[k]: v for k, v in data}
        return TransactionReference(**data)

    transaction_id: Optional[str] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransactionStatus:
    """
    The payload for the getOrderScenarios operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _transaction_status_name_convert
        data = {name_convert[k]: v for k, v in data}
        return TransactionStatus(**data)

    transaction_status: Optional["Transaction"] = attrs.field()
    """
    The transaction details including the status. If the transaction was successful, also includes the requested test order data.
    """


_error_name_convert = {
    "code": "code",
    "details": "details",
    "message": "message",
}

_error_list_name_convert = {
    "errors": "errors",
}

_generate_order_scenario_request_name_convert = {
    "orders": "orders",
}

_order_scenario_request_name_convert = {
    "sellingParty": "selling_party",
    "shipFromParty": "ship_from_party",
}

_pagination_name_convert = {
    "nextToken": "next_token",
}

_party_identification_name_convert = {
    "partyId": "party_id",
}

_scenario_name_convert = {
    "orders": "orders",
    "scenarioId": "scenario_id",
}

_test_case_data_name_convert = {
    "scenarios": "scenarios",
}

_test_order_name_convert = {
    "orderId": "order_id",
}

_transaction_name_convert = {
    "status": "status",
    "testCaseData": "test_case_data",
    "transactionId": "transaction_id",
}

_transaction_reference_name_convert = {
    "transactionId": "transaction_id",
}

_transaction_status_name_convert = {
    "transactionStatus": "transaction_status",
}


class VendorDirectFulfillmentSandboxTestData20211028Client(BaseClient):
    def generate_order_scenarios(
        self,
        orders: List["OrderScenarioRequest"] = None,
    ) -> Union[ErrorList, TransactionReference]:
        """
        Submits a request to generate test order data for Vendor Direct Fulfillment API entities.

        Args:
            orders: The list of test orders requested as indicated by party identifiers.
        """
        url = "/vendor/directFulfillment/sandbox/2021-10-28/orders"
        values = (orders,)
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._generate_order_scenarios_params,
            self._generate_order_scenarios_responses,
        )
        return response

    _generate_order_scenarios_params = (("orders", "body"),)  # name, param in

    _generate_order_scenarios_responses = {
        202: TransactionReference,
        400: ErrorList,
        403: ErrorList,
        404: ErrorList,
        413: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def get_order_scenarios(
        self,
        transaction_id: str,
    ) -> Union[ErrorList, TransactionStatus]:
        """
        Returns the status of the transaction indicated by the specified transactionId. If the transaction was successful, also returns the requested test order data.

        Args:
            transaction_id: The transaction identifier returned in the response to the generateOrderScenarios operation.
        """
        url = "/vendor/directFulfillment/sandbox/2021-10-28/transactions/{transactionId}"
        values = (transaction_id,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_order_scenarios_params,
            self._get_order_scenarios_responses,
        )
        return response

    _get_order_scenarios_params = (("transactionId", "path"),)  # name, param in

    _get_order_scenarios_responses = {
        200: TransactionStatus,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }
