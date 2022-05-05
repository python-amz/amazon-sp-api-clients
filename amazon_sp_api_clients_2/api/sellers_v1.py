"""
Selling Partner API for Sellers
=============================================================================================

The Selling Partner API for Sellers lets you retrieve information on behalf of sellers about their seller account, such as the marketplaces they participate in. Along with listing the marketplaces that a seller can sell in, the API also provides additional information about the marketplace such as the default language and the default currency. The API also provides seller-specific information such as whether the seller has suspended listings in that marketplace.
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
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB310>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB310>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB310>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class GetMarketplaceParticipationsResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB310>}
    payload: list[dict[str, Any]]
    # {'ref': '#/components/schemas/MarketplaceParticipationList', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB310>}
    pass


@attrs.define
class Marketplace:

    country_code: str
    # {'pattern': '^([A-Z]{2})$', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB310>, 'type': 'string'}
    default_currency_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB310>, 'type': 'string'}
    default_language_code: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB310>, 'type': 'string'}
    domain_name: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB310>, 'type': 'string'}
    id: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB310>, 'type': 'string'}
    name: str
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB310>, 'type': 'string'}

    pass


@attrs.define
class MarketplaceParticipation:

    marketplace: dict[str, Any]
    # {'ref': '#/components/schemas/Marketplace', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB310>}
    participation: dict[str, Any]
    # {'ref': '#/components/schemas/Participation', 'generator': <__mp_main__.Generator object at 0x0000019E57FCB310>}
    pass


@attrs.define
class MarketplaceParticipationList:

    pass


@attrs.define
class Participation:

    has_suspended_listings: bool
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB310>, 'type': 'boolean'}
    is_participating: bool
    # {'generator': <__mp_main__.Generator object at 0x0000019E57FCB310>, 'type': 'boolean'}

    pass


class SellersV1Client(BaseClient):
    def get_marketplace_participations(
        self,
    ):
        """
        Returns a list of marketplaces that the seller submitting the request can sell in and information about the seller's participation in those marketplaces.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | .016 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/sellers/v1/marketplaceParticipations"
        values = ()
        response = self._parse_args_and_request(url, "GET", values, self._get_marketplace_participations_params)
        return response

    _get_marketplace_participations_params = ()  # name, param in
