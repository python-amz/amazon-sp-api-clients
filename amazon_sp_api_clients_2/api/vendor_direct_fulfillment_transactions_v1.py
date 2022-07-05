"""
Selling Partner API for Direct Fulfillment Transaction Status
=============================================================================================

The Selling Partner API for Direct Fulfillment Transaction Status provides programmatic access to a direct fulfillment vendor's transaction status.
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

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _error_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Error(**data)

    code: str = attrs.field(
        default=None,
    )
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field(
        default=None,
    )
    """
    A message that describes the error condition.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetTransactionResponse:
    """
    The response schema for the getTransactionStatus operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_transaction_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return GetTransactionResponse(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["TransactionStatus"] = attrs.field(
        default=None,
    )
    """
    The payload for the getTransactionStatus operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Transaction:
    """
    The transaction status details.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _transaction_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Transaction(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    status: Union[Literal["Failure"], Literal["Processing"], Literal["Success"]] = attrs.field(
        default=None,
    )
    """
    Current processing status of the transaction.
    """

    transaction_id: str = attrs.field(
        default=None,
    )
    """
    The unique identifier sent in the 'transactionId' field in response to the post request of a specific transaction.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransactionStatus:
    """
    The payload for the getTransactionStatus operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _transaction_status_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return TransactionStatus(**data)

    transaction_status: Optional["Transaction"] = attrs.field(
        default=None,
    )
    """
    The transaction status details.
    """


_error_name_convert = {
    "code": "code",
    "details": "details",
    "message": "message",
}

_get_transaction_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_transaction_name_convert = {
    "errors": "errors",
    "status": "status",
    "transactionId": "transaction_id",
}

_transaction_status_name_convert = {
    "transactionStatus": "transaction_status",
}


class VendorDirectFulfillmentTransactionsV1Client(BaseClient):
    def get_transaction_status(
        self,
        transaction_id: str,
    ) -> Union[GetTransactionResponse]:
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_transaction_status_params,
            self._get_transaction_status_responses,
        )
        return response

    _get_transaction_status_params = (("transactionId", "path"),)  # name, param in

    _get_transaction_status_responses = {
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
