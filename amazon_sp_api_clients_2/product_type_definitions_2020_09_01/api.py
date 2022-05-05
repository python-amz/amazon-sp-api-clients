"""
Selling Partner API for Product Type Definitions
=============================================================================================
The Selling Partner API for Product Type Definitions provides programmatic access to attribute and data requirements for product types in the Amazon catalog. Use this API to return the JSON Schema for a product type that you can then use with other Selling Partner APIs, such as the Selling Partner API for Listings Items, the Selling Partner API for Catalog Items, and the Selling Partner API for Feeds (for JSON-based listing feeds).

For more information, see the [Product Type Definitions API Use Case Guide](doc:product-type-api-use-case-guide).
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: 2020-09-01
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class ProductTypeDefinitions20200901Client(BaseClient):
    def search_definitions_product_types(
        self,
        keywords: list[str] = None,
        marketplace_ids: list[str],
    ):
        """
        Search for and return a list of Amazon product types that have definitions available.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            keywords: A comma-delimited list of keywords to search product types by.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers for the request.
        """
        path_parameters = {}

        url = "/definitions/2020-09-01/productTypes".format(**path_parameters)

        query_parameters = {}

        if keywords is not None:
            query_parameters["keywords"] = keywords

        query_parameters["marketplaceIds"] = marketplace_ids

    def get_definitions_product_type(
        self,
        product_type: str,
        seller_id: str = None,
        marketplace_ids: list[str],
        product_type_version: str = None,
        requirements: str = None,
        requirements_enforced: str = None,
        locale: str = None,
    ):
        """
        Retrieve an Amazon product type definition.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 5 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            product_type: The Amazon product type name.
            seller_id: A selling partner identifier. When provided, seller-specific requirements and values are populated within the product type definition schema, such as brand names associated with the selling partner.
            marketplace_ids: A comma-delimited list of Amazon marketplace identifiers for the request.
        Note: This parameter is limited to one marketplaceId at this time.
            product_type_version: The version of the Amazon product type to retrieve. Defaults to "LATEST",. Prerelease versions of product type definitions may be retrieved with "RELEASE_CANDIDATE". If no prerelease version is currently available, the "LATEST" live version will be provided.
            requirements: The name of the requirements set to retrieve requirements for.
            requirements_enforced: Identifies if the required attributes for a requirements set are enforced by the product type definition schema. Non-enforced requirements enable structural validation of individual attributes without all the required attributes being present (such as for partial updates).
            locale: Locale for retrieving display labels and other presentation details. Defaults to the default language of the first marketplace in the request.
        """
        path_parameters = {}

        path_parameters["productType"] = product_type

        url = "/definitions/2020-09-01/productTypes/{productType}".format(**path_parameters)

        query_parameters = {}

        if seller_id is not None:
            query_parameters["sellerId"] = seller_id

        query_parameters["marketplaceIds"] = marketplace_ids

        if product_type_version is not None:
            query_parameters["productTypeVersion"] = product_type_version

        if requirements is not None:
            query_parameters["requirements"] = requirements

        if requirements_enforced is not None:
            query_parameters["requirementsEnforced"] = requirements_enforced

        if locale is not None:
            query_parameters["locale"] = locale