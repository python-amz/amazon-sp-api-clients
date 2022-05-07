"""
Selling Partner API for FBA Small And Light
=============================================================================================

The Selling Partner API for FBA Small and Light lets you help sellers manage their listings in the Small and Light program. The program reduces the cost of fulfilling orders for small and lightweight FBA inventory. You can enroll or remove items from the program and check item eligibility and enrollment status. You can also preview the estimated program fees charged to a seller for items sold while enrolled in the program.
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
        data = {name_convert[k]: v for k, v in data}
        return Error(**data)

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
    A message that describes the error condition in a human-readable form.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _error_list_name_convert
        data = {name_convert[k]: v for k, v in data}
        return ErrorList(**data)

    errors: Optional[List["Error"]] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class FeeLineItem:
    """
    Fee details for a specific fee.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _fee_line_item_name_convert
        data = {name_convert[k]: v for k, v in data}
        return FeeLineItem(**data)

    fee_charge: "MoneyType" = attrs.field()

    fee_type: Union[
        Literal["FBAWeightBasedFee"],
        Literal["FBAPerOrderFulfillmentFee"],
        Literal["FBAPerUnitFulfillmentFee"],
        Literal["Commission"],
    ] = attrs.field()
    """
    The type of fee charged to the seller.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class FeePreview:
    """
    The fee estimate for a specific item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _fee_preview_name_convert
        data = {name_convert[k]: v for k, v in data}
        return FeePreview(**data)

    asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) value used to identify the item.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    One or more unexpected errors occurred during the getSmallAndLightFeePreview operation.
    """

    fee_breakdown: Optional[List["FeeLineItem"]] = attrs.field()
    """
    A list of the Small and Light fees for the item.
    """

    price: Optional["MoneyType"] = attrs.field()

    total_fees: Optional["MoneyType"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Item:
    """
    An item to be sold.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _item_name_convert
        data = {name_convert[k]: v for k, v in data}
        return Item(**data)

    asin: str = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) value used to identify the item.
    """

    price: "MoneyType" = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class MarketplaceId:
    """
    A marketplace identifier.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _marketplace_id_name_convert
        data = {name_convert[k]: v for k, v in data}
        return MarketplaceId(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class MoneyType:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _money_type_name_convert
        data = {name_convert[k]: v for k, v in data}
        return MoneyType(**data)

    amount: Optional[float] = attrs.field()
    """
    The monetary value.
    """

    currency_code: Optional[str] = attrs.field()
    """
    The currency code in ISO 4217 format.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SellerSKU:
    """
    Identifies an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _seller_sku_name_convert
        data = {name_convert[k]: v for k, v in data}
        return SellerSKU(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class SmallAndLightEligibility:
    """
    The Small and Light eligibility status of the item indicated by the specified seller SKU.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _small_and_light_eligibility_name_convert
        data = {name_convert[k]: v for k, v in data}
        return SmallAndLightEligibility(**data)

    marketplace_id: "MarketplaceId" = attrs.field()
    """
    A marketplace identifier.
    """

    seller_sku: "SellerSKU" = attrs.field()
    """
    Identifies an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.
    """

    status: "SmallAndLightEligibilityStatus" = attrs.field()
    """
    The Small and Light eligibility status of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SmallAndLightEligibilityStatus:
    """
    The Small and Light eligibility status of the item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _small_and_light_eligibility_status_name_convert
        data = {name_convert[k]: v for k, v in data}
        return SmallAndLightEligibilityStatus(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class SmallAndLightEnrollment:
    """
    The Small and Light enrollment status of the item indicated by the specified seller SKU.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _small_and_light_enrollment_name_convert
        data = {name_convert[k]: v for k, v in data}
        return SmallAndLightEnrollment(**data)

    marketplace_id: "MarketplaceId" = attrs.field()
    """
    A marketplace identifier.
    """

    seller_sku: "SellerSKU" = attrs.field()
    """
    Identifies an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.
    """

    status: "SmallAndLightEnrollmentStatus" = attrs.field()
    """
    The Small and Light enrollment status of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SmallAndLightEnrollmentStatus:
    """
    The Small and Light enrollment status of the item.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _small_and_light_enrollment_status_name_convert
        data = {name_convert[k]: v for k, v in data}
        return SmallAndLightEnrollmentStatus(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class SmallAndLightFeePreviewRequest:
    """
    Request schema for submitting items for which to retrieve fee estimates.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _small_and_light_fee_preview_request_name_convert
        data = {name_convert[k]: v for k, v in data}
        return SmallAndLightFeePreviewRequest(**data)

    items: List["Item"] = attrs.field()
    """
    A list of items for which to retrieve fee estimates (limit: 25).

    Extra fields:
    {'maxItems': 25}
    """

    marketplace_id: "MarketplaceId" = attrs.field()
    """
    A marketplace identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SmallAndLightFeePreviews:
    @classmethod
    def from_json(cls, data: dict):
        name_convert = _small_and_light_fee_previews_name_convert
        data = {name_convert[k]: v for k, v in data}
        return SmallAndLightFeePreviews(**data)

    data: Optional[List["FeePreview"]] = attrs.field()
    """
    A list of fee estimates for the requested items. The order of the fee estimates will follow the same order as the items in the request, with duplicates removed.
    """


_error_name_convert = {
    "code": "code",
    "details": "details",
    "message": "message",
}

_error_list_name_convert = {
    "errors": "errors",
}

_fee_line_item_name_convert = {
    "feeCharge": "fee_charge",
    "feeType": "fee_type",
}

_fee_preview_name_convert = {
    "asin": "asin",
    "errors": "errors",
    "feeBreakdown": "fee_breakdown",
    "price": "price",
    "totalFees": "total_fees",
}

_item_name_convert = {
    "asin": "asin",
    "price": "price",
}

_marketplace_id_name_convert = {}

_money_type_name_convert = {
    "amount": "amount",
    "currencyCode": "currency_code",
}

_seller_sku_name_convert = {}

_small_and_light_eligibility_name_convert = {
    "marketplaceId": "marketplace_id",
    "sellerSKU": "seller_sku",
    "status": "status",
}

_small_and_light_eligibility_status_name_convert = {}

_small_and_light_enrollment_name_convert = {
    "marketplaceId": "marketplace_id",
    "sellerSKU": "seller_sku",
    "status": "status",
}

_small_and_light_enrollment_status_name_convert = {}

_small_and_light_fee_preview_request_name_convert = {
    "items": "items",
    "marketplaceId": "marketplace_id",
}

_small_and_light_fee_previews_name_convert = {
    "data": "data",
}


class FbaSmallAndLightV1Client(BaseClient):
    def delete_small_and_light_enrollment_by_seller_sku(
        self,
        seller_sku: str,
        marketplace_ids: List[str],
    ) -> Union[ErrorList]:
        """
        Removes the item indicated by the specified seller SKU from the Small and Light program in the specified marketplace. If the item is not eligible for disenrollment, the ineligibility reasons are returned.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            seller_sku: The seller SKU that identifies the item.
            marketplace_ids: The marketplace in which to remove the item from the Small and Light program. Note: Accepts a single marketplace only.
        """
        url = "/fba/smallAndLight/v1/enrollments/{sellerSKU}"
        values = (
            seller_sku,
            marketplace_ids,
        )
        response = self._parse_args_and_request(
            url,
            "DELETE",
            values,
            self._delete_small_and_light_enrollment_by_seller_sku_params,
            self._delete_small_and_light_enrollment_by_seller_sku_responses,
        )
        return response

    _delete_small_and_light_enrollment_by_seller_sku_params = (  # name, param in
        ("sellerSKU", "path"),
        ("marketplaceIds", "query"),
    )

    _delete_small_and_light_enrollment_by_seller_sku_responses = {
        400: ErrorList,
        403: ErrorList,
        404: ErrorList,
        413: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def get_small_and_light_eligibility_by_seller_sku(
        self,
        seller_sku: str,
        marketplace_ids: List[str],
    ) -> Union[ErrorList, SmallAndLightEligibility]:
        """
        Returns the Small and Light program eligibility status of the item indicated by the specified seller SKU in the specified marketplace. If the item is not eligible, the ineligibility reasons are returned.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            seller_sku: The seller SKU that identifies the item.
            marketplace_ids: The marketplace for which the eligibility status is retrieved. NOTE: Accepts a single marketplace only.
        """
        url = "/fba/smallAndLight/v1/eligibilities/{sellerSKU}"
        values = (
            seller_sku,
            marketplace_ids,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_small_and_light_eligibility_by_seller_sku_params,
            self._get_small_and_light_eligibility_by_seller_sku_responses,
        )
        return response

    _get_small_and_light_eligibility_by_seller_sku_params = (  # name, param in
        ("sellerSKU", "path"),
        ("marketplaceIds", "query"),
    )

    _get_small_and_light_eligibility_by_seller_sku_responses = {
        200: SmallAndLightEligibility,
        400: ErrorList,
        403: ErrorList,
        404: ErrorList,
        413: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def get_small_and_light_enrollment_by_seller_sku(
        self,
        seller_sku: str,
        marketplace_ids: List[str],
    ) -> Union[ErrorList, SmallAndLightEnrollment]:
        """
        Returns the Small and Light enrollment status for the item indicated by the specified seller SKU in the specified marketplace.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            seller_sku: The seller SKU that identifies the item.
            marketplace_ids: The marketplace for which the enrollment status is retrieved. Note: Accepts a single marketplace only.
        """
        url = "/fba/smallAndLight/v1/enrollments/{sellerSKU}"
        values = (
            seller_sku,
            marketplace_ids,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_small_and_light_enrollment_by_seller_sku_params,
            self._get_small_and_light_enrollment_by_seller_sku_responses,
        )
        return response

    _get_small_and_light_enrollment_by_seller_sku_params = (  # name, param in
        ("sellerSKU", "path"),
        ("marketplaceIds", "query"),
    )

    _get_small_and_light_enrollment_by_seller_sku_responses = {
        200: SmallAndLightEnrollment,
        400: ErrorList,
        403: ErrorList,
        404: ErrorList,
        413: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def get_small_and_light_fee_preview(
        self,
        items: List["Item"],
        marketplace_id: str,
    ) -> Union[ErrorList, SmallAndLightFeePreviews]:
        """
        Returns the Small and Light fee estimates for the specified items. You must include a marketplaceId parameter to retrieve the proper fee estimates for items to be sold in that marketplace. The ordering of items in the response will mirror the order of the items in the request. Duplicate ASIN/price combinations are removed.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 3 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            items: A list of items for which to retrieve fee estimates (limit: 25).
            marketplace_id: A marketplace identifier.
        """
        url = "/fba/smallAndLight/v1/feePreviews"
        values = (
            items,
            marketplace_id,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._get_small_and_light_fee_preview_params,
            self._get_small_and_light_fee_preview_responses,
        )
        return response

    _get_small_and_light_fee_preview_params = (  # name, param in
        ("items", "body"),
        ("marketplaceId", "body"),
    )

    _get_small_and_light_fee_preview_responses = {
        200: SmallAndLightFeePreviews,
        400: ErrorList,
        401: ErrorList,
        403: ErrorList,
        404: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }

    def put_small_and_light_enrollment_by_seller_sku(
        self,
        seller_sku: str,
        marketplace_ids: List[str],
    ) -> Union[ErrorList, SmallAndLightEnrollment]:
        """
        Enrolls the item indicated by the specified seller SKU in the Small and Light program in the specified marketplace. If the item is not eligible, the ineligibility reasons are returned.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 5 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            seller_sku: The seller SKU that identifies the item.
            marketplace_ids: The marketplace in which to enroll the item. Note: Accepts a single marketplace only.
        """
        url = "/fba/smallAndLight/v1/enrollments/{sellerSKU}"
        values = (
            seller_sku,
            marketplace_ids,
        )
        response = self._parse_args_and_request(
            url,
            "PUT",
            values,
            self._put_small_and_light_enrollment_by_seller_sku_params,
            self._put_small_and_light_enrollment_by_seller_sku_responses,
        )
        return response

    _put_small_and_light_enrollment_by_seller_sku_params = (  # name, param in
        ("sellerSKU", "path"),
        ("marketplaceIds", "query"),
    )

    _put_small_and_light_enrollment_by_seller_sku_responses = {
        200: SmallAndLightEnrollment,
        400: ErrorList,
        403: ErrorList,
        404: ErrorList,
        413: ErrorList,
        415: ErrorList,
        429: ErrorList,
        500: ErrorList,
        503: ErrorList,
    }
