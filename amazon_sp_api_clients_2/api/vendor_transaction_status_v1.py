"""
Selling Partner API for Retail Procurement Transaction Status
=============================================================================================

The Selling Partner API for Retail Procurement Transaction Status provides programmatic access to status information on specific asynchronous POST transactions for vendors.
API Version: v1
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
    An error code that identifies the type of error that occurred.
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


@attrs.define
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    pass


@attrs.define
class GetTransactionResponse:
    """
    The response schema for the getTransaction operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "TransactionStatus" = attrs.field(
        kw_only=True,
    )


@attrs.define
class Transaction:
    """
    The transaction status.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    status: Union[Literal["Failure"], Literal["Processing"], Literal["Success"]] = attrs.field(
        kw_only=True,
    )
    """
    Current processing status of the transaction.
    """

    transaction_id: str = attrs.field(
        kw_only=True,
    )
    """
    The unique identifier returned in the 'transactionId' field in response to the post request of a specific transaction.
    """


@attrs.define
class TransactionStatus:

    transaction_status: "Transaction" = attrs.field(
        kw_only=True,
    )


class VendorTransactionStatusV1Client(BaseClient):
    def get_transaction(
        self,
        transaction_id: str,
    ):
        """
        Returns the status of the transaction that you specify.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            transaction_id: The GUID provided by Amazon in the 'transactionId' field in response to the post request of a specific transaction.
        """
        url = "/vendor/transactions/v1/transactions/{transactionId}"
        values = (transaction_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_transaction_params)
        return response

    _get_transaction_params = (("transactionId", "path"),)  # name, param in
