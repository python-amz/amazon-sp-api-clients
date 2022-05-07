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
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
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
class GetTransactionResponse:
    """
    The response schema for the getTransaction operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["TransactionStatus"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Transaction:
    """
    The transaction status.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    status: Union[Literal["Failure"], Literal["Processing"], Literal["Success"]] = attrs.field()
    """
    Current processing status of the transaction.
    """

    transaction_id: str = attrs.field()
    """
    The unique identifier returned in the 'transactionId' field in response to the post request of a specific transaction.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransactionStatus:

    transaction_status: Optional["Transaction"] = attrs.field()
    """
    The transaction status.
    """


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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_transaction_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _get_transaction_params = (("transactionId", "path"),)  # name, param in

    _get_transaction_responses = {
        200: GetTransactionResponse,
        400: GetTransactionResponse,
        401: GetTransactionResponse,
        403: GetTransactionResponse,
        404: GetTransactionResponse,
        415: GetTransactionResponse,
        429: GetTransactionResponse,
        500: GetTransactionResponse,
        503: GetTransactionResponse,
    }
