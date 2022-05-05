"""
Selling Partner API for Vendor Direct Fulfillment Sandbox Test Data
=============================================================================================

The Selling Partner API for Vendor Direct Fulfillment Sandbox Test Data provides programmatic access to vendor direct fulfillment sandbox test data.
API Version: 2021-10-28
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from typing import Union, Literal

import attrs

from ..utils.base_client import BaseClient


@attrs.define
class Error:
    code: str = attrs.field()
    details: str = attrs.field()
    message: str = attrs.field()

    pass


@attrs.define
class ErrorList:
    errors: list["Error"] = attrs.field()

    pass


@attrs.define
class GenerateOrderScenarioRequest:
    orders: list["OrderScenarioRequest"] = attrs.field()

    pass


@attrs.define
class OrderScenarioRequest:
    selling_party: "PartyIdentification" = attrs.field()
    ship_from_party: "PartyIdentification" = attrs.field()
    pass


@attrs.define
class Pagination:
    next_token: str = attrs.field()

    pass


@attrs.define
class PartyIdentification:
    party_id: str = attrs.field()

    pass


@attrs.define
class Scenario:
    orders: list["TestOrder"] = attrs.field()
    scenario_id: str = attrs.field()

    pass


@attrs.define
class TestCaseData:
    scenarios: list["Scenario"] = attrs.field()

    pass


@attrs.define
class TestOrder:
    order_id: str = attrs.field()

    pass


@attrs.define
class Transaction:
    status: Union[Literal["FAILURE"], Literal["PROCESSING"], Literal["SUCCESS"]] = attrs.field()
    transaction_id: str = attrs.field()

    test_case_data: "TestCaseData" = attrs.field()
    pass


@attrs.define
class TransactionReference:
    transaction_id: str = attrs.field()

    pass


@attrs.define
class TransactionStatus:
    transaction_status: "Transaction" = attrs.field()
    pass


class VendorDirectFulfillmentSandboxTestData20211028Client(BaseClient):
    def generate_order_scenarios(
            self,
    ):
        """
        Submits a request to generate test order data for Vendor Direct Fulfillment API entities.

        Args:
        """
        url = "/vendor/directFulfillment/sandbox/2021-10-28/orders"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._generate_order_scenarios_params)
        return response

    _generate_order_scenarios_params = ()  # name, param in

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
