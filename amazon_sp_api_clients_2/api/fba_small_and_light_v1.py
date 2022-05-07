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

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field()
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

    errors: Optional[List["Error"]] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class FeeLineItem:
    """
    Fee details for a specific fee.
    """

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

    pass


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
class SellerSKU:
    """
    Identifies an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class SmallAndLightEligibility:
    """
    The Small and Light eligibility status of the item indicated by the specified seller SKU.
    """

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

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class SmallAndLightEnrollment:
    """
    The Small and Light enrollment status of the item indicated by the specified seller SKU.
    """

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

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class SmallAndLightFeePreviewRequest:
    """
    Request schema for submitting items for which to retrieve fee estimates.
    """

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

    data: Optional[List["FeePreview"]] = attrs.field()
    """
    A list of fee estimates for the requested items. The order of the fee estimates will follow the same order as the items in the request, with duplicates removed.
    """


class FbaSmallAndLightV1Client(BaseClient):
    def delete_small_and_light_enrollment_by_seller_sku(
        self,
        seller_sku: str,
        marketplace_ids: List[str],
    ):
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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _delete_small_and_light_enrollment_by_seller_sku_params = (  # name, param in
        ("sellerSKU", "path"),
        ("marketplaceIds", "query"),
    )

    _delete_small_and_light_enrollment_by_seller_sku_responses = {
        (400, "application/json"): ErrorList,
        (403, "application/json"): ErrorList,
        (404, "application/json"): ErrorList,
        (413, "application/json"): ErrorList,
        (415, "application/json"): ErrorList,
        (429, "application/json"): ErrorList,
        (500, "application/json"): ErrorList,
        (503, "application/json"): ErrorList,
    }

    def get_small_and_light_eligibility_by_seller_sku(
        self,
        seller_sku: str,
        marketplace_ids: List[str],
    ):
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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _get_small_and_light_eligibility_by_seller_sku_params = (  # name, param in
        ("sellerSKU", "path"),
        ("marketplaceIds", "query"),
    )

    _get_small_and_light_eligibility_by_seller_sku_responses = {
        (200, "application/json"): SmallAndLightEligibility,
        (400, "application/json"): ErrorList,
        (403, "application/json"): ErrorList,
        (404, "application/json"): ErrorList,
        (413, "application/json"): ErrorList,
        (415, "application/json"): ErrorList,
        (429, "application/json"): ErrorList,
        (500, "application/json"): ErrorList,
        (503, "application/json"): ErrorList,
    }

    def get_small_and_light_enrollment_by_seller_sku(
        self,
        seller_sku: str,
        marketplace_ids: List[str],
    ):
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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _get_small_and_light_enrollment_by_seller_sku_params = (  # name, param in
        ("sellerSKU", "path"),
        ("marketplaceIds", "query"),
    )

    _get_small_and_light_enrollment_by_seller_sku_responses = {
        (200, "application/json"): SmallAndLightEnrollment,
        (400, "application/json"): ErrorList,
        (403, "application/json"): ErrorList,
        (404, "application/json"): ErrorList,
        (413, "application/json"): ErrorList,
        (415, "application/json"): ErrorList,
        (429, "application/json"): ErrorList,
        (500, "application/json"): ErrorList,
        (503, "application/json"): ErrorList,
    }

    def get_small_and_light_fee_preview(
        self,
        items: List["Item"],
        marketplace_id: str,
    ):
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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _get_small_and_light_fee_preview_params = (  # name, param in
        ("items", "body"),
        ("marketplaceId", "body"),
    )

    _get_small_and_light_fee_preview_responses = {
        (200, "application/json"): SmallAndLightFeePreviews,
        (400, "application/json"): ErrorList,
        (401, "application/json"): ErrorList,
        (403, "application/json"): ErrorList,
        (404, "application/json"): ErrorList,
        (429, "application/json"): ErrorList,
        (500, "application/json"): ErrorList,
        (503, "application/json"): ErrorList,
    }

    def put_small_and_light_enrollment_by_seller_sku(
        self,
        seller_sku: str,
        marketplace_ids: List[str],
    ):
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
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _put_small_and_light_enrollment_by_seller_sku_params = (  # name, param in
        ("sellerSKU", "path"),
        ("marketplaceIds", "query"),
    )

    _put_small_and_light_enrollment_by_seller_sku_responses = {
        (200, "application/json"): SmallAndLightEnrollment,
        (400, "application/json"): ErrorList,
        (403, "application/json"): ErrorList,
        (404, "application/json"): ErrorList,
        (413, "application/json"): ErrorList,
        (415, "application/json"): ErrorList,
        (429, "application/json"): ErrorList,
        (500, "application/json"): ErrorList,
        (503, "application/json"): ErrorList,
    }
