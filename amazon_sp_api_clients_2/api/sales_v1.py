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
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class Decimal:
    """
    A decimal number with no loss of precision. Useful when precision loss is unnaceptable, as with currencies. Follows RFC7159 for number representation.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occured.
    """

    details: Optional[str] = attrs.field()
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition in a human-readable form.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetOrderMetricsResponse:
    """
    The response schema for the getOrderMetrics operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional[List["OrderMetricsInterval"]] = attrs.field()
    """
    A set of order metrics, each scoped to a particular time interval.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Money:
    """
    The currency type and the amount.
    """

    amount: "Decimal" = attrs.field()
    """
    A decimal number with no loss of precision. Useful when precision loss is unnaceptable, as with currencies. Follows RFC7159 for number representation.
    """

    currency_code: str = attrs.field()
    """
    Three-digit currency code. In ISO 4217 format.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class OrderMetricsInterval:
    """
    Contains order metrics.
    """

    average_unit_price: "Money" = attrs.field()
    """
    The currency type and the amount.
    """

    interval: str = attrs.field()
    """
    The interval of time based on requested granularity (ex. Hour, Day, etc.) If this is the first or the last interval from the list, it might contain incomplete data if the requested interval doesn't align with the requested granularity (ex. request interval 2018-09-01T02:00:00Z--2018-09-04T19:00:00Z and granularity day will result in Sept 1st UTC day and Sept 4th UTC days having partial data).
    """

    order_count: int = attrs.field()
    """
    The number of orders based on the specified filters.
    """

    order_item_count: int = attrs.field()
    """
    The number of order items based on the specified filters.
    """

    total_sales: "Money" = attrs.field()
    """
    The currency type and the amount.
    """

    unit_count: int = attrs.field()
    """
    The number of units in orders based on the specified filters.
    """


class SalesV1Client(BaseClient):
    def get_order_metrics(
        self,
        marketplace_ids: List[str],
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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_order_metrics_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

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

    _get_order_metrics_responses = {
        (200, "application/json"): GetOrderMetricsResponse,
        (400, "application/json"): GetOrderMetricsResponse,
        (403, "application/json"): GetOrderMetricsResponse,
        (404, "application/json"): GetOrderMetricsResponse,
        (413, "application/json"): GetOrderMetricsResponse,
        (415, "application/json"): GetOrderMetricsResponse,
        (429, "application/json"): GetOrderMetricsResponse,
        (500, "application/json"): GetOrderMetricsResponse,
        (503, "application/json"): GetOrderMetricsResponse,
    }
