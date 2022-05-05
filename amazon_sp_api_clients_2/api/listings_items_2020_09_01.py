"""
Selling Partner API for Listings Items
=============================================================================================

The Selling Partner API for Listings Items (Listings Items API) provides programmatic access to selling partner listings on Amazon. Use this API in collaboration with the Selling Partner API for Product Type Definitions, which you use to retrieve the information about Amazon product types needed to use the Listings Items API.

For more information, see the [Listing Items API Use Case Guide](doc:listings-items-api-v2020-09-01-use-case-guide).
API Version: 2020-09-01
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    errors: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/Error'), 'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'array'}

    pass


@attrs.define
class Issue:

    attribute_name: str
    # {'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'string'}
    code: str
    # {'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'string'}
    severity: Union[Literal["ERROR"], Literal["WARNING"], Literal["INFO"]]
    # {'enum': ['ERROR', 'WARNING', 'INFO'], 'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'string'}

    pass


@attrs.define
class ListingsItemPatchRequest:

    patches: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/PatchOperation'), 'minItems': 1, 'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'array'}
    product_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'string'}

    pass


@attrs.define
class ListingsItemPutRequest:

    attributes: dict[str, Any]
    # {'properties': {}, 'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'object'}
    product_type: str
    # {'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'string'}
    requirements: Union[Literal["LISTING"], Literal["LISTING_PRODUCT_ONLY"], Literal["LISTING_OFFER_ONLY"]]
    # {'enum': ['LISTING', 'LISTING_PRODUCT_ONLY', 'LISTING_OFFER_ONLY'], 'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'string'}

    pass


@attrs.define
class ListingsItemSubmissionResponse:

    issues: list[dict[str, Any]]
    # {'items': Reference(ref='#/components/schemas/Issue'), 'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'array'}
    sku: str
    # {'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'string'}
    status: Union[Literal["ACCEPTED"], Literal["INVALID"]]
    # {'enum': ['ACCEPTED', 'INVALID'], 'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'string'}
    submission_id: str
    # {'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'string'}

    pass


@attrs.define
class PatchOperation:

    op: Union[Literal["add"], Literal["replace"], Literal["delete"]]
    # {'enum': ['add', 'replace', 'delete'], 'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'string'}
    path: str
    # {'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'string'}
    value: list[dict[str, Any]]
    # {'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='object', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties={}, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'generator': <__mp_main__.Generator object at 0x0000023E8F207700>, 'type': 'array'}

    pass


class ListingsItems20200901Client(BaseClient):
    def delete_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        issue_locale: str = None,
    ):
        """
        Delete a listings item for a selling partner.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            seller_id: A selling partner identifier, such as a merchant account or vendor code.
            sku: A selling partner provided identifier for an Amazon listing.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers for the request.
            issue_locale: A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
        """
        url = "/listings/2020-09-01/items/{sellerId}/{sku}"
        values = (
            seller_id,
            sku,
            marketplace_ids,
            issue_locale,
        )
        response = self._parse_args_and_request(url, "DELETE", values, self._delete_listings_item_params)
        return response

    _delete_listings_item_params = (  # name, param in
        ("sellerId", "path"),
        ("sku", "path"),
        ("marketplaceIds", "query"),
        ("issueLocale", "query"),
    )

    def patch_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        product_type: str,
        patches: list[dict[str, Any]],
        issue_locale: str = None,
    ):
        """
        Partially update (patch) a listings item for a selling partner. Only top-level listings item attributes can be patched. Patching nested attributes is not supported.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            seller_id: A selling partner identifier, such as a merchant account or vendor code.
            sku: A selling partner provided identifier for an Amazon listing.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers for the request.
            issue_locale: A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
            product_type: The Amazon product type of the listings item.
            patches: One or more JSON Patch operations to perform on the listings item.
        """
        url = "/listings/2020-09-01/items/{sellerId}/{sku}"
        values = (
            seller_id,
            sku,
            marketplace_ids,
            issue_locale,
            product_type,
            patches,
        )
        response = self._parse_args_and_request(url, "PATCH", values, self._patch_listings_item_params)
        return response

    _patch_listings_item_params = (  # name, param in
        ("sellerId", "path"),
        ("sku", "path"),
        ("marketplaceIds", "query"),
        ("issueLocale", "query"),
        ("productType", "body"),
        ("patches", "body"),
    )

    def put_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        product_type: str,
        attributes: dict[str, Any],
        issue_locale: str = None,
        requirements: Union[Literal["LISTING"], Literal["LISTING_PRODUCT_ONLY"], Literal["LISTING_OFFER_ONLY"]] = None,
    ):
        """
        Creates a new or fully-updates an existing listings item for a selling partner.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            seller_id: A selling partner identifier, such as a merchant account or vendor code.
            sku: A selling partner provided identifier for an Amazon listing.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers for the request.
            issue_locale: A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
            product_type: The Amazon product type of the listings item.
            requirements: The name of the requirements set for the provided data.
            attributes: JSON object containing structured listings item attribute data keyed by attribute name.
        """
        url = "/listings/2020-09-01/items/{sellerId}/{sku}"
        values = (
            seller_id,
            sku,
            marketplace_ids,
            issue_locale,
            product_type,
            requirements,
            attributes,
        )
        response = self._parse_args_and_request(url, "PUT", values, self._put_listings_item_params)
        return response

    _put_listings_item_params = (  # name, param in
        ("sellerId", "path"),
        ("sku", "path"),
        ("marketplaceIds", "query"),
        ("issueLocale", "query"),
        ("productType", "body"),
        ("requirements", "body"),
        ("attributes", "body"),
    )
