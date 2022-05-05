"""
Selling Partner API for Vendor Direct Fulfillment Sandbox Test Data
=============================================================================================
The Selling Partner API for Vendor Direct Fulfillment Sandbox Test Data provides programmatic access to vendor direct fulfillment sandbox test data.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: 2021-10-28
"""
from ..utils.base_client import BaseClient


class VendorDirectFulfillmentSandboxTestData20211028Client(BaseClient):
    def generate_order_scenarios(
        self,
    ):
        """
        Submits a request to generate test order data for Vendor Direct Fulfillment API entities.

        Args:
        """
        url = "/vendor/directFulfillment/sandbox/2021-10-28/orders"

    def get_order_scenarios(
        self,
        transaction_id,
    ):
        """
        Returns the status of the transaction indicated by the specified transactionId. If the transaction was successful, also returns the requested test order data.

        Args:
            transaction_id: The transaction identifier returned in the response to the generateOrderScenarios operation.
        """
        url = "/vendor/directFulfillment/sandbox/2021-10-28/transactions/{transactionId}"
