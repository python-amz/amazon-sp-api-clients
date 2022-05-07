"""
Selling Partner API for Tokens 
=============================================================================================

The Selling Partner API for Tokens provides a secure way to access a customer's PII (Personally Identifiable Information). You can call the Tokens API to get a Restricted Data Token (RDT) for one or more restricted resources that you specify. The RDT authorizes subsequent calls to restricted operations that correspond to the restricted resources that you specified.

For more information, see the [Tokens API Use Case Guide](doc:tokens-api-use-case-guide).
API Version: 2021-03-01
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateRestrictedDataTokenRequest:
    """
    The request schema for the createRestrictedDataToken operation.
    """

    restricted_resources: List["RestrictedResource"] = attrs.field()
    """
    A list of restricted resources.
        Maximum: 50
    """

    target_application: Optional[str] = attrs.field(
        default=None,
    )
    """
    The application ID for the target application to which access is being delegated.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateRestrictedDataTokenResponse:
    """
    The response schema for the createRestrictedDataToken operation.
    """

    expires_in: Optional[int] = attrs.field()
    """
    The lifetime of the Restricted Data Token, in seconds.
    """

    restricted_data_token: Optional[str] = attrs.field()
    """
    A Restricted Data Token (RDT). This is a short-lived access token that authorizes calls to restricted operations. Pass this value with the x-amz-access-token header when making subsequent calls to these restricted resources.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    An error response returned when the request is unsuccessful.
    """

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
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

    errors: Optional[List["Error"]] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class RestrictedResource:
    """
    Model of a restricted resource.
    """

    data_elements: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    Indicates the type of Personally Identifiable Information requested. This parameter is required only when getting an RDT for use with the getOrder, getOrders, or getOrderItems operation of the Orders API. For more information, see the [Tokens API Use Case Guide](doc:tokens-api-use-case-guide). Possible values include:
        - **buyerInfo**. On the order level this includes general identifying information about the buyer and tax-related information. On the order item level this includes gift wrap information and custom order information, if available.
        - **shippingAddress**. This includes information for fulfilling orders.
        - **buyerTaxInformation**. This includes information for issuing tax invoices.
    """

    method: Union[Literal["GET"], Literal["PUT"], Literal["POST"], Literal["DELETE"]] = attrs.field()
    """
    The HTTP method in the restricted resource.
    """

    path: str = attrs.field()
    """
    The path in the restricted resource. Here are some path examples:
        - ```/orders/v0/orders```. For getting an RDT for the getOrders operation of the Orders API. For bulk orders.
        - ```/orders/v0/orders/123-1234567-1234567```. For getting an RDT for the getOrder operation of the Orders API. For a specific order.
        - ```/orders/v0/orders/123-1234567-1234567/orderItems```. For getting an RDT for the getOrderItems operation of the Orders API. For the order items in a specific order.
        - ```/mfn/v0/shipments/FBA1234ABC5D```. For getting an RDT for the getShipment operation of the Shipping API. For a specific shipment.
        - ```/mfn/v0/shipments/{shipmentId}```. For getting an RDT for the getShipment operation of the Shipping API. For any of a selling partner's shipments that you specify when you call the getShipment operation.
    """


class Tokens20210301Client(BaseClient):
    def create_restricted_data_token(
        self,
        restricted_resources: List["RestrictedResource"],
        target_application: str = None,
    ) -> Union[CreateRestrictedDataTokenResponse, ErrorList]:
        """
        Returns a Restricted Data Token (RDT) for one or more restricted resources that you specify. A restricted resource is the HTTP method and path from a restricted operation that returns Personally Identifiable Information (PII), plus a dataElements value that indicates the type of PII requested. See the Tokens API Use Case Guide for a list of restricted operations. Use the RDT returned here as the access token in subsequent calls to the corresponding restricted operations.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 1 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            restricted_resources: A list of restricted resources.
                Maximum: 50
            target_application: The application ID for the target application to which access is being delegated.
        """
        url = "/tokens/2021-03-01/restrictedDataToken"
        values = (
            restricted_resources,
            target_application,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_restricted_data_token_params,
        )
        klass = self._create_restricted_data_token_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _create_restricted_data_token_params = (  # name, param in
        ("restrictedResources", "body"),
        ("targetApplication", "body"),
    )

    _create_restricted_data_token_responses = {
        200: CreateRestrictedDataTokenResponse,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }
