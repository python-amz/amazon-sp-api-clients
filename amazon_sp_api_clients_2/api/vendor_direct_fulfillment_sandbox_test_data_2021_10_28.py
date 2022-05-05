"""
Selling Partner API for Vendor Direct Fulfillment Sandbox Test Data
=============================================================================================

The Selling Partner API for Vendor Direct Fulfillment Sandbox Test Data provides programmatic access to vendor direct fulfillment sandbox test data.
API Version: 2021-10-28
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class GenerateOrderScenarioRequest:
    pass


class OrderScenarioRequest:
    pass


class PartyIdentification:
    pass


class Pagination:
    pass


class TransactionReference:
    pass


class TransactionStatus:
    pass


class Transaction:
    pass


class TestCaseData:
    pass


class Scenario:
    pass


class TestOrder:
    pass


class ErrorList:
    pass


class Error:
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
