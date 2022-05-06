"""
Selling Partner API for Product Fees
=============================================================================================

The Selling Partner API for Product Fees lets you programmatically retrieve estimated fees for a product. You can then account for those fees in your pricing.
API Version: v0
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal
from datetime import date, datetime


@attrs.define
class Error:

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
    Additional information that can help the caller understand or fix the issue.
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
class FeeDetail:
    """
    The type of fee, fee amount, and other details.
    """

    fee_amount: "MoneyType" = attrs.field(
        kw_only=True,
    )

    fee_promotion: "MoneyType" = attrs.field(
        kw_only=True,
    )

    fee_type: str = attrs.field(
        kw_only=True,
    )
    """
    The type of fee charged to a seller.
    """

    final_fee: "MoneyType" = attrs.field(
        kw_only=True,
    )

    included_fee_detail_list: "IncludedFeeDetailList" = attrs.field(
        kw_only=True,
    )

    tax_amount: "MoneyType" = attrs.field(
        kw_only=True,
    )


@attrs.define
class FeeDetailList:
    """
    A list of other fees that contribute to a given fee.
    """

    pass


@attrs.define
class FeesEstimate:
    """
    The total estimated fees for an item and a list of details.
    """

    fee_detail_list: "FeeDetailList" = attrs.field(
        kw_only=True,
    )

    time_of_fees_estimation: datetime = attrs.field(
        kw_only=True,
    )
    """
    The time at which the fees were estimated. This defaults to the time the request is made.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    total_fees_estimate: "MoneyType" = attrs.field(
        kw_only=True,
    )


@attrs.define
class FeesEstimateError:
    """
    An unexpected error occurred during this operation.
    """

    code: str = attrs.field(
        kw_only=True,
    )
    """
    An error code that identifies the type of error that occurred.
    """

    detail: "FeesEstimateErrorDetail" = attrs.field(
        kw_only=True,
    )

    message: str = attrs.field(
        kw_only=True,
    )
    """
    A message that describes the error condition.
    """

    type: str = attrs.field(
        kw_only=True,
    )
    """
    An error type, identifying either the receiver or the sender as the originator of the error.
    """


@attrs.define
class FeesEstimateErrorDetail:
    """
    Additional information that can help the caller understand or fix the issue.
    """

    pass


@attrs.define
class FeesEstimateErrorDetailItem:

    pass


@attrs.define
class FeesEstimateIdentifier:
    """
    An item identifier, marketplace, time of request, and other details that identify an estimate.
    """

    id_type: str = attrs.field(
        kw_only=True,
    )
    """
    The type of item identifier specified.
    """

    id_value: str = attrs.field(
        kw_only=True,
    )
    """
    The item identifier.
    """

    is_amazon_fulfilled: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, the offer is fulfilled by Amazon.
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    A marketplace identifier.
    """

    optional_fulfillment_program: "OptionalFulfillmentProgram" = attrs.field(
        kw_only=True,
    )

    price_to_estimate_fees: "PriceToEstimateFees" = attrs.field(
        kw_only=True,
    )

    seller_id: str = attrs.field(
        kw_only=True,
    )
    """
    The seller identifier.
    """

    seller_input_identifier: str = attrs.field(
        kw_only=True,
    )
    """
    A unique identifier provided by the caller to track this request.
    """


@attrs.define
class FeesEstimateRequest:

    identifier: str = attrs.field(
        kw_only=True,
    )
    """
    A unique identifier provided by the caller to track this request.
    """

    is_amazon_fulfilled: bool = attrs.field(
        kw_only=True,
    )
    """
    When true, the offer is fulfilled by Amazon.
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    A marketplace identifier.
    """

    optional_fulfillment_program: "OptionalFulfillmentProgram" = attrs.field(
        kw_only=True,
    )

    price_to_estimate_fees: "PriceToEstimateFees" = attrs.field(
        kw_only=True,
    )


@attrs.define
class FeesEstimateResult:
    """
    An item identifier and the estimated fees for the item.
    """

    error: "FeesEstimateError" = attrs.field(
        kw_only=True,
    )

    fees_estimate: "FeesEstimate" = attrs.field(
        kw_only=True,
    )

    fees_estimate_identifier: "FeesEstimateIdentifier" = attrs.field(
        kw_only=True,
    )

    status: str = attrs.field(
        kw_only=True,
    )
    """
    The status of the fee request. Possible values: Success, ClientError, ServiceError.
    """


@attrs.define
class GetMyFeesEstimateRequest:
    """
    Request schema.
    """

    fees_estimate_request: "FeesEstimateRequest" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetMyFeesEstimateResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "GetMyFeesEstimateResult" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetMyFeesEstimateResult:
    """
    Response schema.
    """

    fees_estimate_result: "FeesEstimateResult" = attrs.field(
        kw_only=True,
    )


@attrs.define
class IncludedFeeDetail:
    """
    The type of fee, fee amount, and other details.
    """

    fee_amount: "MoneyType" = attrs.field(
        kw_only=True,
    )

    fee_promotion: "MoneyType" = attrs.field(
        kw_only=True,
    )

    fee_type: str = attrs.field(
        kw_only=True,
    )
    """
    The type of fee charged to a seller.
    """

    final_fee: "MoneyType" = attrs.field(
        kw_only=True,
    )

    tax_amount: "MoneyType" = attrs.field(
        kw_only=True,
    )


@attrs.define
class IncludedFeeDetailList:
    """
    A list of other fees that contribute to a given fee.
    """

    pass


@attrs.define
class MoneyType:

    amount: float = attrs.field(
        kw_only=True,
    )
    """
    The monetary value.
    """

    currency_code: str = attrs.field(
        kw_only=True,
    )
    """
    The currency code in ISO 4217 format.
    """


@attrs.define
class OptionalFulfillmentProgram:
    """
    An optional enrollment program to return the estimated fees when the offer is fulfilled by Amazon (IsAmazonFulfilled is set to true).
    """

    pass


@attrs.define
class Points:

    points_monetary_value: "MoneyType" = attrs.field(
        kw_only=True,
    )

    points_number: int = attrs.field(
        kw_only=True,
    )
    """

    Extra fields:
    {'schema_format': 'int32'}
    """


@attrs.define
class PriceToEstimateFees:
    """
    Price information for an item, used to estimate fees.
    """

    listing_price: "MoneyType" = attrs.field(
        kw_only=True,
    )

    points: "Points" = attrs.field(
        kw_only=True,
    )

    shipping: "MoneyType" = attrs.field(
        kw_only=True,
    )


class ProductFeesV0Client(BaseClient):
    def get_my_fees_estimate_for_asin(
        self,
        asin: str,
        fees_estimate_request: Dict[str, Any] = None,
    ):
        """
        Returns the estimated fees for the item indicated by the specified Asin in the marketplace specified in the request body.

        You can call getMyFeesEstimateForASIN for an item on behalf of a selling partner before the selling partner sets the item's price. They can then take estimated fees into account. With each product fees request, you must include an original identifier. This identifier is included in the fees estimate so you can correlate a fees estimate with the original request.

        **Note:** This value is only an estimate, actual costs may vary. Search "fees" in [Seller Central](https://sellercentral.amazon.com/) and consult the store-specific fee schedule for the most up-to-date information.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 20 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            asin: The Amazon Standard Identification Number (ASIN) of the item.
            fees_estimate_request: no description.
        """
        url = "/products/fees/v0/items/{Asin}/feesEstimate"
        values = (
            asin,
            fees_estimate_request,
        )
        response = self._parse_args_and_request(url, "POST", values, self._get_my_fees_estimate_for_asin_params)
        return response

    _get_my_fees_estimate_for_asin_params = (  # name, param in
        ("Asin", "path"),
        ("FeesEstimateRequest", "body"),
    )

    def get_my_fees_estimate_for_sku(
        self,
        seller_sku: str,
        fees_estimate_request: Dict[str, Any] = None,
    ):
        """
        Returns the estimated fees for the item indicated by the specified seller SKU in the marketplace specified in the request body.

        You can call getMyFeesEstimateForSKU for an item on behalf of a selling partner before the selling partner sets the item's price. They can then take estimated fees into account. With each fees estimate request, you must include an original identifier. This identifier is included in the fees estimate so you can correlate a fees estimate with the original request.

        **Note:** This value is only an estimate, actual costs may vary. Search "fees" in [Seller Central](https://sellercentral.amazon.com/) and consult the store-specific fee schedule for the most up-to-date information.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 20 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            seller_sku: Used to identify an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.
            fees_estimate_request: no description.
        """
        url = "/products/fees/v0/listings/{SellerSKU}/feesEstimate"
        values = (
            seller_sku,
            fees_estimate_request,
        )
        response = self._parse_args_and_request(url, "POST", values, self._get_my_fees_estimate_for_sku_params)
        return response

    _get_my_fees_estimate_for_sku_params = (  # name, param in
        ("SellerSKU", "path"),
        ("FeesEstimateRequest", "body"),
    )
