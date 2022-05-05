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


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class FeeDetail:

    fee_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'string'}

    fee_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/MoneyType'}
    fee_promotion: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/MoneyType'}
    final_fee: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/MoneyType'}
    included_fee_detail_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/IncludedFeeDetailList'}
    tax_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/MoneyType'}
    pass


@attrs.define
class FeeDetailList:

    pass


@attrs.define
class FeesEstimate:

    time_of_fees_estimation: str
    # {'schema_format': 'date-time', 'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'string'}

    fee_detail_list: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/FeeDetailList'}
    total_fees_estimate: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/MoneyType'}
    pass


@attrs.define
class FeesEstimateError:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'string'}
    type: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'string'}

    detail: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/FeesEstimateErrorDetail'}
    pass


@attrs.define
class FeesEstimateErrorDetail:

    pass


@attrs.define
class FeesEstimateIdentifier:

    id_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'string'}
    id_value: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'string'}
    is_amazon_fulfilled: bool
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'boolean'}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'string'}
    seller_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'string'}
    seller_input_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'string'}

    optional_fulfillment_program: Union[Literal["FBA_CORE"], Literal["FBA_SNL"], Literal["FBA_EFN"]]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/OptionalFulfillmentProgram'}
    price_to_estimate_fees: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/PriceToEstimateFees'}
    pass


@attrs.define
class FeesEstimateRequest:

    identifier: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'string'}
    is_amazon_fulfilled: bool
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'boolean'}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'string'}

    optional_fulfillment_program: Union[Literal["FBA_CORE"], Literal["FBA_SNL"], Literal["FBA_EFN"]]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/OptionalFulfillmentProgram'}
    price_to_estimate_fees: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/PriceToEstimateFees'}
    pass


@attrs.define
class FeesEstimateResult:

    status: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'string'}

    error: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/FeesEstimateError'}
    fees_estimate: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/FeesEstimate'}
    fees_estimate_identifier: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/FeesEstimateIdentifier'}
    pass


@attrs.define
class GetMyFeesEstimateRequest:

    fees_estimate_request: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/FeesEstimateRequest'}
    pass


@attrs.define
class GetMyFeesEstimateResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/GetMyFeesEstimateResult'}
    pass


@attrs.define
class GetMyFeesEstimateResult:

    fees_estimate_result: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/FeesEstimateResult'}
    pass


@attrs.define
class IncludedFeeDetail:

    fee_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'string'}

    fee_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/MoneyType'}
    fee_promotion: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/MoneyType'}
    final_fee: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/MoneyType'}
    tax_amount: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/MoneyType'}
    pass


@attrs.define
class IncludedFeeDetailList:

    pass


@attrs.define
class MoneyType:

    amount: Union[float, int]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'number'}
    currency_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'string'}

    pass


@attrs.define
class OptionalFulfillmentProgram:

    pass


@attrs.define
class Points:

    points_number: int
    # {'schema_format': 'int32', 'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'type': 'integer'}

    points_monetary_value: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/MoneyType'}
    pass


@attrs.define
class PriceToEstimateFees:

    listing_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/MoneyType'}
    points: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/Points'}
    shipping: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x0000028D733230A0>, 'ref': '#/components/schemas/MoneyType'}
    pass


class ProductFeesV0Client(BaseClient):
    def get_my_fees_estimate_for_asin(
        self,
        asin: str,
        fees_estimate_request: dict[str, Any] = None,
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
        fees_estimate_request: dict[str, Any] = None,
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
