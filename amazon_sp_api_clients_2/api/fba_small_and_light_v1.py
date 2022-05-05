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
from typing import Any, List, Dict, Union, Literal


@attrs.define
class Error:

    code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}
    details: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}
    message: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}

    pass


@attrs.define
class ErrorList:

    errors: list[dict[str, Any]]
    # {'type': 'array', 'items': Reference(ref='#/components/schemas/Error'), 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}

    pass


@attrs.define
class FeeLineItem:

    fee_type: Union[
        Literal["FBAWeightBasedFee"],
        Literal["FBAPerOrderFulfillmentFee"],
        Literal["FBAPerUnitFulfillmentFee"],
        Literal["Commission"],
    ]
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E78613B310>, 'enum': ['FBAWeightBasedFee', 'FBAPerOrderFulfillmentFee', 'FBAPerUnitFulfillmentFee', 'Commission']}

    fee_charge: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}
    pass


@attrs.define
class FeePreview:

    asin: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}
    errors: list[dict[str, Any]]
    # {'type': 'array', 'items': Reference(ref='#/components/schemas/Error'), 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}
    fee_breakdown: list[dict[str, Any]]
    # {'type': 'array', 'items': Reference(ref='#/components/schemas/FeeLineItem'), 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}

    price: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}
    total_fees: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}
    pass


@attrs.define
class Item:

    asin: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}

    price: dict[str, Any]
    # {'ref': '#/components/schemas/MoneyType', 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}
    pass


@attrs.define
class MarketplaceId:

    pass


@attrs.define
class MoneyType:

    amount: Union[float, int]
    # {'type': 'number', 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}
    currency_code: str
    # {'type': 'string', 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}

    pass


@attrs.define
class SellerSKU:

    pass


@attrs.define
class SmallAndLightEligibility:

    marketplace_id: str
    # {'ref': '#/components/schemas/MarketplaceId', 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}
    seller_sku: str
    # {'ref': '#/components/schemas/SellerSKU', 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}
    status: Union[Literal["ELIGIBLE"], Literal["NOT_ELIGIBLE"]]
    # {'ref': '#/components/schemas/SmallAndLightEligibilityStatus', 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}
    pass


@attrs.define
class SmallAndLightEligibilityStatus:

    pass


@attrs.define
class SmallAndLightEnrollment:

    marketplace_id: str
    # {'ref': '#/components/schemas/MarketplaceId', 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}
    seller_sku: str
    # {'ref': '#/components/schemas/SellerSKU', 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}
    status: Union[Literal["ENROLLED"], Literal["NOT_ENROLLED"]]
    # {'ref': '#/components/schemas/SmallAndLightEnrollmentStatus', 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}
    pass


@attrs.define
class SmallAndLightEnrollmentStatus:

    pass


@attrs.define
class SmallAndLightFeePreviewRequest:

    items: list[dict[str, Any]]
    # {'type': 'array', 'items': Reference(ref='#/components/schemas/Item'), 'generator': <__mp_main__.Generator object at 0x000001E78613B310>, 'maxItems': 25}

    marketplace_id: str
    # {'ref': '#/components/schemas/MarketplaceId', 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}
    pass


@attrs.define
class SmallAndLightFeePreviews:

    data: list[dict[str, Any]]
    # {'type': 'array', 'items': Reference(ref='#/components/schemas/FeePreview'), 'generator': <__mp_main__.Generator object at 0x000001E78613B310>}

    pass


class FbaSmallAndLightV1Client(BaseClient):
    def delete_small_and_light_enrollment_by_seller_sku(
        self,
        seller_sku: str,
        marketplace_ids: list[str],
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
            url, "DELETE", values, self._delete_small_and_light_enrollment_by_seller_sku_params
        )
        return response

    _delete_small_and_light_enrollment_by_seller_sku_params = (  # name, param in
        ("sellerSKU", "path"),
        ("marketplaceIds", "query"),
    )

    def get_small_and_light_eligibility_by_seller_sku(
        self,
        seller_sku: str,
        marketplace_ids: list[str],
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
            url, "GET", values, self._get_small_and_light_eligibility_by_seller_sku_params
        )
        return response

    _get_small_and_light_eligibility_by_seller_sku_params = (  # name, param in
        ("sellerSKU", "path"),
        ("marketplaceIds", "query"),
    )

    def get_small_and_light_enrollment_by_seller_sku(
        self,
        seller_sku: str,
        marketplace_ids: list[str],
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
            url, "GET", values, self._get_small_and_light_enrollment_by_seller_sku_params
        )
        return response

    _get_small_and_light_enrollment_by_seller_sku_params = (  # name, param in
        ("sellerSKU", "path"),
        ("marketplaceIds", "query"),
    )

    def get_small_and_light_fee_preview(
        self,
    ):
        """
        Returns the Small and Light fee estimates for the specified items. You must include a marketplaceId parameter to retrieve the proper fee estimates for items to be sold in that marketplace. The ordering of items in the response will mirror the order of the items in the request. Duplicate ASIN/price combinations are removed.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 3 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/fba/smallAndLight/v1/feePreviews"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._get_small_and_light_fee_preview_params)
        return response

    _get_small_and_light_fee_preview_params = ()  # name, param in

    def put_small_and_light_enrollment_by_seller_sku(
        self,
        seller_sku: str,
        marketplace_ids: list[str],
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
            url, "PUT", values, self._put_small_and_light_enrollment_by_seller_sku_params
        )
        return response

    _put_small_and_light_enrollment_by_seller_sku_params = (  # name, param in
        ("sellerSKU", "path"),
        ("marketplaceIds", "query"),
    )
