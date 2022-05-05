"""
Selling Partner API for Sales
=============================================================================================

The Selling Partner API for Sales provides APIs related to sales performance.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class Decimal:

    pass


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x000002166D12B310>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x000002166D12B310>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x000002166D12B310>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class GetOrderMetricsResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002166D12B310>, 'ref': '#/components/schemas/ErrorList'}
    payload: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x000002166D12B310>, 'ref': '#/components/schemas/OrderMetricsList'}
    pass


@attrs.define
class Money:

    currency_code: str
    # {'generator': <__mp_main__.Generator object at 0x000002166D12B310>, 'type': 'string'}

    amount: str
    # {'generator': <__mp_main__.Generator object at 0x000002166D12B310>, 'ref': '#/components/schemas/Decimal'}
    pass


@attrs.define
class OrderMetricsInterval:

    interval: str
    # {'generator': <__mp_main__.Generator object at 0x000002166D12B310>, 'type': 'string'}
    order_count: int
    # {'generator': <__mp_main__.Generator object at 0x000002166D12B310>, 'type': 'integer'}
    order_item_count: int
    # {'generator': <__mp_main__.Generator object at 0x000002166D12B310>, 'type': 'integer'}
    unit_count: int
    # {'generator': <__mp_main__.Generator object at 0x000002166D12B310>, 'type': 'integer'}

    average_unit_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002166D12B310>, 'ref': '#/components/schemas/Money'}
    total_sales: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x000002166D12B310>, 'ref': '#/components/schemas/Money'}
    pass


@attrs.define
class OrderMetricsList:

    pass


class SalesV1Client(BaseClient):
    def get_order_metrics(
        self,
        marketplace_ids: list[str],
        interval: str,
        granularity: Union[
            Literal["Hour"], Literal["Day"], Literal["Week"], Literal["Month"], Literal["Year"], Literal["Total"]
        ],
        granularity_time_zone: str = None,
        buyer_type: Union[Literal["B2B"], Literal["B2C"], Literal["All"]] = None,
        fulfillment_network: str = None,
        first_day_of_week: Union[Literal["Monday"], Literal["Sunday"]] = None,
        asin: str = None,
        sku: str = None,
    ):
        """
        Returns aggregated order metrics for given interval, broken down by granularity, for given buyer type.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | .5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_ids: A list of marketplace identifiers. Example: ATVPDKIKX0DER indicates the US marketplace.
            interval: A time interval used for selecting order metrics. This takes the form of two dates separated by two hyphens (first date is inclusive; second date is exclusive). Dates are in ISO8601 format and must represent absolute time (either Z notation or offset notation). Example: 2018-09-01T00:00:00-07:00--2018-09-04T00:00:00-07:00 requests order metrics for Sept 1st, 2nd and 3rd in the -07:00 zone.
            granularity_time_zone: An IANA-compatible time zone for determining the day boundary. Required when specifying a granularity value greater than Hour. The granularityTimeZone value must align with the offset of the specified interval value. For example, if the interval value uses Z notation, then granularityTimeZone must be UTC. If the interval value uses an offset, then granularityTimeZone must be an IANA-compatible time zone that matches the offset. Example: US/Pacific to compute day boundaries, accounting for daylight time savings, for US/Pacific zone.
            granularity: The granularity of the grouping of order metrics, based on a unit of time. Specifying granularity=Hour results in a successful request only if the interval specified is less than or equal to 30 days from now. For all other granularities, the interval specified must be less or equal to 2 years from now. Specifying granularity=Total results in order metrics that are aggregated over the entire interval that you specify. If the interval start and end date don’t align with the specified granularity, the head and tail end of the response interval will contain partial data. Example: Day to get a daily breakdown of the request interval, where the day boundary is defined by the granularityTimeZone.
            buyer_type: Filters the results by the buyer type that you specify, B2B (business to business) or B2C (business to customer). Example: B2B, if you want the response to include order metrics for only B2B buyers.
            fulfillment_network: Filters the results by the fulfillment network that you specify, MFN (merchant fulfillment network) or AFN (Amazon fulfillment network). Do not include this filter if you want the response to include order metrics for all fulfillment networks. Example: AFN, if you want the response to include order metrics for only Amazon fulfillment network.
            first_day_of_week: Specifies the day that the week starts on when granularity=Week, either Monday or Sunday. Default: Monday. Example: Sunday, if you want the week to start on a Sunday.
            asin: Filters the results by the ASIN that you specify. Specifying both ASIN and SKU returns an error. Do not include this filter if you want the response to include order metrics for all ASINs. Example: B0792R1RSN, if you want the response to include order metrics for only ASIN B0792R1RSN.
            sku: Filters the results by the SKU that you specify. Specifying both ASIN and SKU returns an error. Do not include this filter if you want the response to include order metrics for all SKUs. Example: TestSKU, if you want the response to include order metrics for only SKU TestSKU.
        """
        url = "/sales/v1/orderMetrics"
        values = (
            marketplace_ids,
            interval,
            granularity_time_zone,
            granularity,
            buyer_type,
            fulfillment_network,
            first_day_of_week,
            asin,
            sku,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_order_metrics_params)
        return response

    _get_order_metrics_params = (  # name, param in
        ("marketplaceIds", "query"),
        ("interval", "query"),
        ("granularityTimeZone", "query"),
        ("granularity", "query"),
        ("buyerType", "query"),
        ("fulfillmentNetwork", "query"),
        ("firstDayOfWeek", "query"),
        ("asin", "query"),
        ("sku", "query"),
    )
