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
from typing import Any, List, Dict, Union, Literal
from datetime import date, datetime


@attrs.define
class Error:

    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field(
        kw_only=True,
    )
    """
    An error code that identifies the type of error that occured.
    """

    details: str = attrs.field(
        kw_only=True,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field(
        kw_only=True,
    )
    """
    A message that describes the error condition.
    """

    pass


@attrs.define
class ErrorList:

    """
    A list of error responses returned when a request is unsuccessful.
    """

    errors: List["Error"] = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GenerateOrderScenarioRequest:

    """
    The request body for the generateOrderScenarios operation.
    """

    orders: List["OrderScenarioRequest"] = attrs.field(
        kw_only=True,
    )
    """
    The list of test orders requested as indicated by party identifiers.
    """

    pass


@attrs.define
class OrderScenarioRequest:

    """
    The party identifiers required to generate the test data.
    """

    selling_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    ship_from_party: "PartyIdentification" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Pagination:

    """
    A generated string used to pass information to your next request. If NextToken is returned, pass the value of NextToken to the next request. If NextToken is not returned, there are no more order items to return.
    """

    next_token: str = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class PartyIdentification:

    """
    The identification object for the party information. For example, warehouse code or vendor code. Please refer to specific party for more details.
    """

    party_id: str = attrs.field(
        kw_only=True,
    )
    """
    Assigned identification for the party. For example, warehouse code or vendor code. Please refer to specific party for more details.
    """

    pass


@attrs.define
class Scenario:

    """
    A scenario test case response returned when the request is successful.
    """

    orders: List["TestOrder"] = attrs.field(
        kw_only=True,
    )
    """
    A list of orders that can be used by the caller to test each life cycle or scenario.
    """

    scenario_id: str = attrs.field(
        kw_only=True,
    )
    """
    An identifier that identifies the type of scenario that user can use for testing.
    """

    pass


@attrs.define
class TestCaseData:

    """
    The set of test case data returned in response to the test data request.
    """

    scenarios: List["Scenario"] = attrs.field(
        kw_only=True,
    )
    """
    Set of use cases that describes the possible test scenarios.
    """

    pass


@attrs.define
class TestOrder:

    """
    Error response returned when the request is unsuccessful.
    """

    order_id: str = attrs.field(
        kw_only=True,
    )
    """
    An error code that identifies the type of error that occurred.
    """

    pass


@attrs.define
class Transaction:

    """
    The transaction details including the status. If the transaction was successful, also includes the requested test order data.
    """

    status: Union[Literal["FAILURE"], Literal["PROCESSING"], Literal["SUCCESS"]] = attrs.field(
        kw_only=True,
    )
    """
    The current processing status of the transaction.
    """

    transaction_id: str = attrs.field(
        kw_only=True,
    )
    """
    The unique identifier returned in the response to the generateOrderScenarios request.
    """

    test_case_data: "TestCaseData" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class TransactionReference:

    """
    A GUID assigned by Amazon to identify this transaction.
    """

    transaction_id: str = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class TransactionStatus:

    """
    The payload for the getOrderScenarios operation.
    """

    transaction_status: "Transaction" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


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
