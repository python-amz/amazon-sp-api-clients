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

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occured.
    """

    details: Optional[str] = attrs.field()
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

    errors: List["Error"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GenerateOrderScenarioRequest:
    """
    The request body for the generateOrderScenarios operation.
    """

    orders: Optional[List["OrderScenarioRequest"]] = attrs.field()
    """
    The list of test orders requested as indicated by party identifiers.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderScenarioRequest:
    """
    The party identifiers required to generate the test data.
    """

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

    next_token: Optional[str] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartyIdentification:
    """
    The identification object for the party information. For example, warehouse code or vendor code. Please refer to specific party for more details.
    """

    party_id: str = attrs.field()
    """
    Assigned identification for the party. For example, warehouse code or vendor code. Please refer to specific party for more details.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Scenario:
    """
    A scenario test case response returned when the request is successful.
    """

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

    scenarios: Optional[List["Scenario"]] = attrs.field()
    """
    Set of use cases that describes the possible test scenarios.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TestOrder:
    """
    Error response returned when the request is unsuccessful.
    """

    order_id: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Transaction:
    """
    The transaction details including the status. If the transaction was successful, also includes the requested test order data.
    """

    status: Union[Literal["FAILURE"], Literal["PROCESSING"], Literal["SUCCESS"]] = attrs.field()
    """
    The current processing status of the transaction.
    """

    test_case_data: Optional["TestCaseData"] = attrs.field()
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

    transaction_id: Optional[str] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransactionStatus:
    """
    The payload for the getOrderScenarios operation.
    """

    transaction_status: Optional["Transaction"] = attrs.field()
    """
    The transaction details including the status. If the transaction was successful, also includes the requested test order data.
    """


class VendorDirectFulfillmentSandboxTestData20211028Client(BaseClient):
    def generate_order_scenarios(
        self,
        orders: List["OrderScenarioRequest"] = None,
    ):
        """
        Submits a request to generate test order data for Vendor Direct Fulfillment API entities.

        Args:
            orders: The list of test orders requested as indicated by party identifiers.
        """
        url = "/vendor/directFulfillment/sandbox/2021-10-28/orders"
        values = (orders,)
        response = self._parse_args_and_request(url, "POST", values, self._generate_order_scenarios_params)
        return response

    _generate_order_scenarios_params = (("orders", "body"),)  # name, param in

    def get_order_scenarios(
        self,
        transaction_id: str,
    ):
        """
        Returns the status of the transaction indicated by the specified transactionId. If the transaction was successful, also returns the requested test order data.

        Args:
            transaction_id: The transaction identifier returned in the response to the generateOrderScenarios operation.
        """
        url = "/vendor/directFulfillment/sandbox/2021-10-28/transactions/{transactionId}"
        values = (transaction_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_order_scenarios_params)
        return response

    _get_order_scenarios_params = (("transactionId", "path"),)  # name, param in
