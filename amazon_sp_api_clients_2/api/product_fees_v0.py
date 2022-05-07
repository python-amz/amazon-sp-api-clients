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
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime
import cattrs


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional information that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FeeDetail:
    """
    The type of fee, fee amount, and other details.
    """

    fee_amount: "MoneyType" = attrs.field()

    fee_promotion: Optional["MoneyType"] = attrs.field(
        default=None,
    )

    fee_type: str = attrs.field()
    """
    The type of fee charged to a seller.
    """

    final_fee: "MoneyType" = attrs.field()

    included_fee_detail_list: Optional[List["IncludedFeeDetail"]] = attrs.field(
        default=None,
    )
    """
    A list of other fees that contribute to a given fee.
    """

    tax_amount: Optional["MoneyType"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class FeesEstimate:
    """
    The total estimated fees for an item and a list of details.
    """

    fee_detail_list: Optional[List["FeeDetail"]] = attrs.field(
        default=None,
    )
    """
    A list of other fees that contribute to a given fee.
    """

    time_of_fees_estimation: datetime = attrs.field()
    """
    The time at which the fees were estimated. This defaults to the time the request is made.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    total_fees_estimate: Optional["MoneyType"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class FeesEstimateError:
    """
    An unexpected error occurred during this operation.
    """

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    detail: List["FeesEstimateErrorDetailItem"] = attrs.field()
    """
    Additional information that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition.
    """

    type: str = attrs.field()
    """
    An error type, identifying either the receiver or the sender as the originator of the error.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FeesEstimateErrorDetailItem:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class FeesEstimateIdentifier:
    """
    An item identifier, marketplace, time of request, and other details that identify an estimate.
    """

    id_type: Optional[str] = attrs.field()
    """
    The type of item identifier specified.
    """

    id_value: Optional[str] = attrs.field()
    """
    The item identifier.
    """

    is_amazon_fulfilled: Optional[bool] = attrs.field()
    """
    When true, the offer is fulfilled by Amazon.
    """

    marketplace_id: Optional[str] = attrs.field()
    """
    A marketplace identifier.
    """

    optional_fulfillment_program: Optional["OptionalFulfillmentProgram"] = attrs.field()
    """
    An optional enrollment program to return the estimated fees when the offer is fulfilled by Amazon (IsAmazonFulfilled is set to true).
    """

    price_to_estimate_fees: Optional["PriceToEstimateFees"] = attrs.field()
    """
    Price information for an item, used to estimate fees.
    """

    seller_id: Optional[str] = attrs.field()
    """
    The seller identifier.
    """

    seller_input_identifier: Optional[str] = attrs.field()
    """
    A unique identifier provided by the caller to track this request.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FeesEstimateRequest:

    identifier: str = attrs.field()
    """
    A unique identifier provided by the caller to track this request.
    """

    is_amazon_fulfilled: Optional[bool] = attrs.field(
        default=None,
    )
    """
    When true, the offer is fulfilled by Amazon.
    """

    marketplace_id: str = attrs.field()
    """
    A marketplace identifier.
    """

    optional_fulfillment_program: Optional["OptionalFulfillmentProgram"] = attrs.field(
        default=None,
    )
    """
    An optional enrollment program to return the estimated fees when the offer is fulfilled by Amazon (IsAmazonFulfilled is set to true).
    """

    price_to_estimate_fees: "PriceToEstimateFees" = attrs.field()
    """
    Price information for an item, used to estimate fees.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FeesEstimateResult:
    """
    An item identifier and the estimated fees for the item.
    """

    error: Optional["FeesEstimateError"] = attrs.field()
    """
    An unexpected error occurred during this operation.
    """

    fees_estimate: Optional["FeesEstimate"] = attrs.field()
    """
    The total estimated fees for an item and a list of details.
    """

    fees_estimate_identifier: Optional["FeesEstimateIdentifier"] = attrs.field()
    """
    An item identifier, marketplace, time of request, and other details that identify an estimate.
    """

    status: Optional[str] = attrs.field()
    """
    The status of the fee request. Possible values: Success, ClientError, ServiceError.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetMyFeesEstimateRequest:
    """
    Request schema.
    """

    fees_estimate_request: Optional["FeesEstimateRequest"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetMyFeesEstimateResponse:

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["GetMyFeesEstimateResult"] = attrs.field()
    """
    Response schema.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetMyFeesEstimateResult:
    """
    Response schema.
    """

    fees_estimate_result: Optional["FeesEstimateResult"] = attrs.field()
    """
    An item identifier and the estimated fees for the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class IncludedFeeDetail:
    """
    The type of fee, fee amount, and other details.
    """

    fee_amount: "MoneyType" = attrs.field()

    fee_promotion: Optional["MoneyType"] = attrs.field(
        default=None,
    )

    fee_type: str = attrs.field()
    """
    The type of fee charged to a seller.
    """

    final_fee: "MoneyType" = attrs.field()

    tax_amount: Optional["MoneyType"] = attrs.field(
        default=None,
    )


@attrs.define(kw_only=True, frozen=True, slots=True)
class MoneyType:

    amount: Optional[float] = attrs.field()
    """
    The monetary value.
    """

    currency_code: Optional[str] = attrs.field()
    """
    The currency code in ISO 4217 format.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OptionalFulfillmentProgram:
    """
    An optional enrollment program to return the estimated fees when the offer is fulfilled by Amazon (IsAmazonFulfilled is set to true).
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Points:

    points_monetary_value: Optional["MoneyType"] = attrs.field()

    points_number: Optional[int] = attrs.field()
    """

    Extra fields:
    {'schema_format': 'int32'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PriceToEstimateFees:
    """
    Price information for an item, used to estimate fees.
    """

    listing_price: "MoneyType" = attrs.field()

    points: Optional["Points"] = attrs.field(
        default=None,
    )

    shipping: Optional["MoneyType"] = attrs.field(
        default=None,
    )


class ProductFeesV0Client(BaseClient):
    def get_my_fees_estimate_for_asin(
        self,
        asin: str,
        fees_estimate_request: Dict[str, Any] = None,
    ) -> Union[GetMyFeesEstimateResponse]:
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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._get_my_fees_estimate_for_asin_params,
        )
        klass = self._get_my_fees_estimate_for_asin_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = cattrs.structure(response.json(), klass)
        return obj

    _get_my_fees_estimate_for_asin_params = (  # name, param in
        ("Asin", "path"),
        ("FeesEstimateRequest", "body"),
    )

    _get_my_fees_estimate_for_asin_responses = {
        200: GetMyFeesEstimateResponse,
        400: GetMyFeesEstimateResponse,
        401: GetMyFeesEstimateResponse,
        403: GetMyFeesEstimateResponse,
        404: GetMyFeesEstimateResponse,
        429: GetMyFeesEstimateResponse,
        500: GetMyFeesEstimateResponse,
        503: GetMyFeesEstimateResponse,
    }

    def get_my_fees_estimate_for_sku(
        self,
        seller_sku: str,
        fees_estimate_request: Dict[str, Any] = None,
    ) -> Union[GetMyFeesEstimateResponse]:
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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._get_my_fees_estimate_for_sku_params,
        )
        klass = self._get_my_fees_estimate_for_sku_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = cattrs.structure(response.json(), klass)
        return obj

    _get_my_fees_estimate_for_sku_params = (  # name, param in
        ("SellerSKU", "path"),
        ("FeesEstimateRequest", "body"),
    )

    _get_my_fees_estimate_for_sku_responses = {
        200: GetMyFeesEstimateResponse,
        400: GetMyFeesEstimateResponse,
        401: GetMyFeesEstimateResponse,
        403: GetMyFeesEstimateResponse,
        404: GetMyFeesEstimateResponse,
        429: GetMyFeesEstimateResponse,
        500: GetMyFeesEstimateResponse,
        503: GetMyFeesEstimateResponse,
    }
