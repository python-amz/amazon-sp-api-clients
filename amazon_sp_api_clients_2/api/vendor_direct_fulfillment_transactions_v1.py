"""
Selling Partner API for Direct Fulfillment Transaction Status
=============================================================================================

The Selling Partner API for Direct Fulfillment Transaction Status provides programmatic access to a direct fulfillment vendor's transaction status.
API Version: v1
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
    pass


@attrs.define
class GetTransactionResponse:
    errors: "ErrorList" = attrs.field()
    payload: "TransactionStatus" = attrs.field()
    pass


@attrs.define
class Transaction:
    status: Union[Literal["Failure"], Literal["Processing"], Literal["Success"]] = attrs.field()
    transaction_id: str = attrs.field()

    errors: "ErrorList" = attrs.field()
    pass


@attrs.define
class TransactionStatus:
    transaction_status: "Transaction" = attrs.field()
    pass


class VendorDirectFulfillmentTransactionsV1Client(BaseClient):
    def get_transaction_status(
            self,
            transaction_id: str,
    ):
        """
        Returns the status of the transaction indicated by the specified transactionId.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            transaction_id: Previously returned in the response to the POST request of a specific transaction.
        """
        url = "/vendor/directFulfillment/transactions/v1/transactions/{transactionId}"
        values = (transaction_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_transaction_status_params)
        return response

    _get_transaction_status_params = (("transactionId", "path"),)  # name, param in
