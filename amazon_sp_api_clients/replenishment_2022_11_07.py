from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class GetSellingPartnerMetricsRequest(__BaseDictObject):
    """
    The request body for the `getSellingPartnerMetrics` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "aggregationFrequency" in data:
            self.aggregationFrequency: AggregationFrequency = self._get_value(
                AggregationFrequency, "aggregationFrequency"
            )
        else:
            self.aggregationFrequency: AggregationFrequency = None
        if "timeInterval" in data:
            self.timeInterval: TimeInterval = self._get_value(TimeInterval, "timeInterval")
        else:
            self.timeInterval: TimeInterval = None
        if "metrics" in data:
            self.metrics: _List[Metric] = [Metric(datum) for datum in data["metrics"]]
        else:
            self.metrics: _List[Metric] = []
        if "timePeriodType" in data:
            self.timePeriodType: TimePeriodType = self._get_value(TimePeriodType, "timePeriodType")
        else:
            self.timePeriodType: TimePeriodType = None
        if "marketplaceId" in data:
            self.marketplaceId: MarketplaceId = self._get_value(MarketplaceId, "marketplaceId")
        else:
            self.marketplaceId: MarketplaceId = None
        if "programTypes" in data:
            self.programTypes: ProgramTypes = self._get_value(ProgramTypes, "programTypes")
        else:
            self.programTypes: ProgramTypes = None


class ListOfferMetricsRequest(__BaseDictObject):
    """
    The request body for the `listOfferMetrics` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "pagination" in data:
            self.pagination: ListOfferMetricsRequestPagination = self._get_value(
                ListOfferMetricsRequestPagination, "pagination"
            )
        else:
            self.pagination: ListOfferMetricsRequestPagination = None
        if "sort" in data:
            self.sort: ListOfferMetricsRequestSort = self._get_value(ListOfferMetricsRequestSort, "sort")
        else:
            self.sort: ListOfferMetricsRequestSort = None
        if "filters" in data:
            self.filters: ListOfferMetricsRequestFilters = self._get_value(ListOfferMetricsRequestFilters, "filters")
        else:
            self.filters: ListOfferMetricsRequestFilters = None


class ListOffersRequest(__BaseDictObject):
    """
    The request body for the `listOffers` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "pagination" in data:
            self.pagination: ListOffersRequestPagination = self._get_value(ListOffersRequestPagination, "pagination")
        else:
            self.pagination: ListOffersRequestPagination = None
        if "filters" in data:
            self.filters: ListOffersRequestFilters = self._get_value(ListOffersRequestFilters, "filters")
        else:
            self.filters: ListOffersRequestFilters = None
        if "sort" in data:
            self.sort: ListOffersRequestSort = self._get_value(ListOffersRequestSort, "sort")
        else:
            self.sort: ListOffersRequestSort = None


class Preference(__BaseDictObject):
    """
    Offer preferences that you can include in the result filter criteria.
    """

    def __init__(self, data):
        super().__init__(data)
        if "autoEnrollment" in data:
            self.autoEnrollment: _List[AutoEnrollmentPreference] = [
                AutoEnrollmentPreference(datum) for datum in data["autoEnrollment"]
            ]
        else:
            self.autoEnrollment: _List[AutoEnrollmentPreference] = []


class Promotion(__BaseDictObject):
    """
    Offer promotions to include in the result filter criteria.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sellingPartnerFundedBaseDiscount" in data:
            self.sellingPartnerFundedBaseDiscount: DiscountFunding = self._get_value(
                DiscountFunding, "sellingPartnerFundedBaseDiscount"
            )
        else:
            self.sellingPartnerFundedBaseDiscount: DiscountFunding = None
        if "sellingPartnerFundedTieredDiscount" in data:
            self.sellingPartnerFundedTieredDiscount: DiscountFunding = self._get_value(
                DiscountFunding, "sellingPartnerFundedTieredDiscount"
            )
        else:
            self.sellingPartnerFundedTieredDiscount: DiscountFunding = None
        if "amazonFundedBaseDiscount" in data:
            self.amazonFundedBaseDiscount: DiscountFunding = self._get_value(
                DiscountFunding, "amazonFundedBaseDiscount"
            )
        else:
            self.amazonFundedBaseDiscount: DiscountFunding = None
        if "amazonFundedTieredDiscount" in data:
            self.amazonFundedTieredDiscount: DiscountFunding = self._get_value(
                DiscountFunding, "amazonFundedTieredDiscount"
            )
        else:
            self.amazonFundedTieredDiscount: DiscountFunding = None


class DiscountFunding(__BaseDictObject):
    """
    The discount funding on the offer.
    """

    def __init__(self, data):
        super().__init__(data)
        if "percentage" in data:
            self.percentage: _List[float] = [float(datum) for datum in data["percentage"]]
        else:
            self.percentage: _List[float] = []


class OfferProgramConfiguration(__BaseDictObject):
    """
    The offer program configuration contains a set of program properties for an offer.
    """

    def __init__(self, data):
        super().__init__(data)
        if "preferences" in data:
            self.preferences: OfferProgramConfigurationPreferences = self._get_value(
                OfferProgramConfigurationPreferences, "preferences"
            )
        else:
            self.preferences: OfferProgramConfigurationPreferences = None
        if "promotions" in data:
            self.promotions: OfferProgramConfigurationPromotions = self._get_value(
                OfferProgramConfigurationPromotions, "promotions"
            )
        else:
            self.promotions: OfferProgramConfigurationPromotions = None
        if "enrollmentMethod" in data:
            self.enrollmentMethod: EnrollmentMethod = self._get_value(EnrollmentMethod, "enrollmentMethod")
        else:
            self.enrollmentMethod: EnrollmentMethod = None


class OfferProgramConfigurationPreferences(__BaseDictObject):
    """
    An object which contains the preferences applied to the offer.
    """

    def __init__(self, data):
        super().__init__(data)
        if "autoEnrollment" in data:
            self.autoEnrollment: AutoEnrollmentPreference = self._get_value(AutoEnrollmentPreference, "autoEnrollment")
        else:
            self.autoEnrollment: AutoEnrollmentPreference = None


class OfferProgramConfigurationPromotions(__BaseDictObject):
    """
    An object which represents all promotions applied to an offer.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sellingPartnerFundedBaseDiscount" in data:
            self.sellingPartnerFundedBaseDiscount: OfferProgramConfigurationPromotionsDiscountFunding = self._get_value(
                OfferProgramConfigurationPromotionsDiscountFunding, "sellingPartnerFundedBaseDiscount"
            )
        else:
            self.sellingPartnerFundedBaseDiscount: OfferProgramConfigurationPromotionsDiscountFunding = None
        if "sellingPartnerFundedTieredDiscount" in data:
            self.sellingPartnerFundedTieredDiscount: OfferProgramConfigurationPromotionsDiscountFunding = (
                self._get_value(
                    OfferProgramConfigurationPromotionsDiscountFunding, "sellingPartnerFundedTieredDiscount"
                )
            )
        else:
            self.sellingPartnerFundedTieredDiscount: OfferProgramConfigurationPromotionsDiscountFunding = None
        if "amazonFundedBaseDiscount" in data:
            self.amazonFundedBaseDiscount: OfferProgramConfigurationPromotionsDiscountFunding = self._get_value(
                OfferProgramConfigurationPromotionsDiscountFunding, "amazonFundedBaseDiscount"
            )
        else:
            self.amazonFundedBaseDiscount: OfferProgramConfigurationPromotionsDiscountFunding = None
        if "amazonFundedTieredDiscount" in data:
            self.amazonFundedTieredDiscount: OfferProgramConfigurationPromotionsDiscountFunding = self._get_value(
                OfferProgramConfigurationPromotionsDiscountFunding, "amazonFundedTieredDiscount"
            )
        else:
            self.amazonFundedTieredDiscount: OfferProgramConfigurationPromotionsDiscountFunding = None


class OfferProgramConfigurationPromotionsDiscountFunding(__BaseDictObject):
    """
    A promotional percentage discount applied to the offer.
    """

    def __init__(self, data):
        super().__init__(data)
        if "percentage" in data:
            self.percentage: float = self._get_value(float, "percentage")
        else:
            self.percentage: float = None


class ListOfferMetricsRequestPagination(__BaseDictObject):
    """
    Use these parameters to paginate through the response.
    """

    def __init__(self, data):
        super().__init__(data)
        if "limit" in data:
            self.limit: int = self._get_value(int, "limit")
        else:
            self.limit: int = None
        if "offset" in data:
            self.offset: int = self._get_value(int, "offset")
        else:
            self.offset: int = None


class ListOfferMetricsRequestFilters(__BaseDictObject):
    """
    Use these parameters to filter results. Any result must match all provided parameters. For any parameter that is an array, the result must match at least one element in the provided array.
    """

    def __init__(self, data):
        super().__init__(data)
        if "aggregationFrequency" in data:
            self.aggregationFrequency: AggregationFrequency = self._get_value(
                AggregationFrequency, "aggregationFrequency"
            )
        else:
            self.aggregationFrequency: AggregationFrequency = None
        if "timeInterval" in data:
            self.timeInterval: TimeInterval = self._get_value(TimeInterval, "timeInterval")
        else:
            self.timeInterval: TimeInterval = None
        if "timePeriodType" in data:
            self.timePeriodType: TimePeriodType = self._get_value(TimePeriodType, "timePeriodType")
        else:
            self.timePeriodType: TimePeriodType = None
        if "marketplaceId" in data:
            self.marketplaceId: MarketplaceId = self._get_value(MarketplaceId, "marketplaceId")
        else:
            self.marketplaceId: MarketplaceId = None
        if "programTypes" in data:
            self.programTypes: ProgramTypes = self._get_value(ProgramTypes, "programTypes")
        else:
            self.programTypes: ProgramTypes = None
        if "asins" in data:
            self.asins: _List[str] = [str(datum) for datum in data["asins"]]
        else:
            self.asins: _List[str] = []


class ListOfferMetricsRequestSort(__BaseDictObject):
    """
    Use these parameters to sort the response.
    """

    def __init__(self, data):
        super().__init__(data)
        if "order" in data:
            self.order: SortOrder = self._get_value(SortOrder, "order")
        else:
            self.order: SortOrder = None
        if "key" in data:
            self.key: ListOfferMetricsSortKey = self._get_value(ListOfferMetricsSortKey, "key")
        else:
            self.key: ListOfferMetricsSortKey = None


class ListOffersRequestPagination(__BaseDictObject):
    """
    Use these parameters to paginate through the response.
    """

    def __init__(self, data):
        super().__init__(data)
        if "limit" in data:
            self.limit: int = self._get_value(int, "limit")
        else:
            self.limit: int = None
        if "offset" in data:
            self.offset: int = self._get_value(int, "offset")
        else:
            self.offset: int = None


class ListOffersRequestFilters(__BaseDictObject):
    """
    Use these parameters to filter results. Any result must match all of the provided parameters. For any parameter that is an array, the result must match at least one element in the provided array.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: MarketplaceId = self._get_value(MarketplaceId, "marketplaceId")
        else:
            self.marketplaceId: MarketplaceId = None
        if "skus" in data:
            self.skus: _List[str] = [str(datum) for datum in data["skus"]]
        else:
            self.skus: _List[str] = []
        if "asins" in data:
            self.asins: _List[str] = [str(datum) for datum in data["asins"]]
        else:
            self.asins: _List[str] = []
        if "eligibilities" in data:
            self.eligibilities: _List[EligibilityStatus] = [EligibilityStatus(datum) for datum in data["eligibilities"]]
        else:
            self.eligibilities: _List[EligibilityStatus] = []
        if "preferences" in data:
            self.preferences: Preference = self._get_value(Preference, "preferences")
        else:
            self.preferences: Preference = None
        if "promotions" in data:
            self.promotions: Promotion = self._get_value(Promotion, "promotions")
        else:
            self.promotions: Promotion = None
        if "programTypes" in data:
            self.programTypes: ProgramTypes = self._get_value(ProgramTypes, "programTypes")
        else:
            self.programTypes: ProgramTypes = None


class ListOffersRequestSort(__BaseDictObject):
    """
    Use these parameters to sort the response.
    """

    def __init__(self, data):
        super().__init__(data)
        if "order" in data:
            self.order: SortOrder = self._get_value(SortOrder, "order")
        else:
            self.order: SortOrder = None
        if "key" in data:
            self.key: ListOffersSortKey = self._get_value(ListOffersSortKey, "key")
        else:
            self.key: ListOffersSortKey = None


class TimeInterval(__BaseDictObject):
    """
       A date-time interval in ISO 8601 format which is used to compute metrics. Only the date is required, but you must pass the complete date and time value. For example, November 11, 2022 should be passed as "2022-11-07T00:00:00Z". Note that only data for the trailing 2 years is supported.
    **Note**: The `listOfferMetrics` operation only supports a time interval which covers a single unit of the aggregation frequency. For example, for a MONTH aggregation frequency, the duration of the interval between the startDate and endDate can not be more than 1 month.
    """

    def __init__(self, data):
        super().__init__(data)
        if "startDate" in data:
            self.startDate: str = self._get_value(str, "startDate")
        else:
            self.startDate: str = None
        if "endDate" in data:
            self.endDate: str = self._get_value(str, "endDate")
        else:
            self.endDate: str = None


class GetSellingPartnerMetricsResponse(__BaseDictObject):
    """
    The response schema for the `getSellingPartnerMetrics` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "metrics" in data:
            self.metrics: _List[GetSellingPartnerMetricsResponseMetric] = [
                GetSellingPartnerMetricsResponseMetric(datum) for datum in data["metrics"]
            ]
        else:
            self.metrics: _List[GetSellingPartnerMetricsResponseMetric] = []


class GetSellingPartnerMetricsResponseMetric(__BaseDictObject):
    """
    An object which contains metric data for a selling partner.
    """

    def __init__(self, data):
        super().__init__(data)
        if "notDeliveredDueToOOS" in data:
            self.notDeliveredDueToOOS: float = self._get_value(float, "notDeliveredDueToOOS")
        else:
            self.notDeliveredDueToOOS: float = None
        if "totalSubscriptionsRevenue" in data:
            self.totalSubscriptionsRevenue: float = self._get_value(float, "totalSubscriptionsRevenue")
        else:
            self.totalSubscriptionsRevenue: float = None
        if "shippedSubscriptionUnits" in data:
            self.shippedSubscriptionUnits: float = self._get_value(float, "shippedSubscriptionUnits")
        else:
            self.shippedSubscriptionUnits: float = None
        if "activeSubscriptions" in data:
            self.activeSubscriptions: float = self._get_value(float, "activeSubscriptions")
        else:
            self.activeSubscriptions: float = None
        if "subscriberAverageRevenue" in data:
            self.subscriberAverageRevenue: float = self._get_value(float, "subscriberAverageRevenue")
        else:
            self.subscriberAverageRevenue: float = None
        if "nonSubscriberAverageRevenue" in data:
            self.nonSubscriberAverageRevenue: float = self._get_value(float, "nonSubscriberAverageRevenue")
        else:
            self.nonSubscriberAverageRevenue: float = None
        if "timeInterval" in data:
            self.timeInterval: TimeInterval = self._get_value(TimeInterval, "timeInterval")
        else:
            self.timeInterval: TimeInterval = None
        if "currencyCode" in data:
            self.currencyCode: str = self._get_value(str, "currencyCode")
        else:
            self.currencyCode: str = None


class ListOfferMetricsResponse(__BaseDictObject):
    """
    The response schema for the `listOfferMetrics` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "offers" in data:
            self.offers: _List[ListOfferMetricsResponseOffer] = [
                ListOfferMetricsResponseOffer(datum) for datum in data["offers"]
            ]
        else:
            self.offers: _List[ListOfferMetricsResponseOffer] = []
        if "pagination" in data:
            self.pagination: PaginationResponse = self._get_value(PaginationResponse, "pagination")
        else:
            self.pagination: PaginationResponse = None


class ListOffersResponse(__BaseDictObject):
    """
    The response schema for the `listOffers` operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "offers" in data:
            self.offers: _List[ListOffersResponseOffer] = [ListOffersResponseOffer(datum) for datum in data["offers"]]
        else:
            self.offers: _List[ListOffersResponseOffer] = []
        if "pagination" in data:
            self.pagination: PaginationResponse = self._get_value(PaginationResponse, "pagination")
        else:
            self.pagination: PaginationResponse = None


class ListOffersResponseOffer(__BaseDictObject):
    """
    An object which contains details about an offer.
    """

    def __init__(self, data):
        super().__init__(data)
        if "sku" in data:
            self.sku: str = self._get_value(str, "sku")
        else:
            self.sku: str = None
        if "asin" in data:
            self.asin: str = self._get_value(str, "asin")
        else:
            self.asin: str = None
        if "marketplaceId" in data:
            self.marketplaceId: MarketplaceId = self._get_value(MarketplaceId, "marketplaceId")
        else:
            self.marketplaceId: MarketplaceId = None
        if "eligibility" in data:
            self.eligibility: EligibilityStatus = self._get_value(EligibilityStatus, "eligibility")
        else:
            self.eligibility: EligibilityStatus = None
        if "offerProgramConfiguration" in data:
            self.offerProgramConfiguration: OfferProgramConfiguration = self._get_value(
                OfferProgramConfiguration, "offerProgramConfiguration"
            )
        else:
            self.offerProgramConfiguration: OfferProgramConfiguration = None
        if "programType" in data:
            self.programType: ProgramType = self._get_value(ProgramType, "programType")
        else:
            self.programType: ProgramType = None
        if "vendorCodes" in data:
            self.vendorCodes: _List[str] = [str(datum) for datum in data["vendorCodes"]]
        else:
            self.vendorCodes: _List[str] = []


class PaginationResponse(__BaseDictObject):
    """
    Use these parameters to paginate through the response.
    """

    def __init__(self, data):
        super().__init__(data)
        if "totalResults" in data:
            self.totalResults: int = self._get_value(int, "totalResults")
        else:
            self.totalResults: int = None


class ListOfferMetricsResponseOffer(__BaseDictObject):
    """
    An object which contains offer metrics.
    """

    def __init__(self, data):
        super().__init__(data)
        if "asin" in data:
            self.asin: str = self._get_value(str, "asin")
        else:
            self.asin: str = None
        if "notDeliveredDueToOOS" in data:
            self.notDeliveredDueToOOS: float = self._get_value(float, "notDeliveredDueToOOS")
        else:
            self.notDeliveredDueToOOS: float = None
        if "totalSubscriptionsRevenue" in data:
            self.totalSubscriptionsRevenue: float = self._get_value(float, "totalSubscriptionsRevenue")
        else:
            self.totalSubscriptionsRevenue: float = None
        if "shippedSubscriptionUnits" in data:
            self.shippedSubscriptionUnits: float = self._get_value(float, "shippedSubscriptionUnits")
        else:
            self.shippedSubscriptionUnits: float = None
        if "activeSubscriptions" in data:
            self.activeSubscriptions: float = self._get_value(float, "activeSubscriptions")
        else:
            self.activeSubscriptions: float = None
        if "revenuePenetration" in data:
            self.revenuePenetration: float = self._get_value(float, "revenuePenetration")
        else:
            self.revenuePenetration: float = None
        if "next30DayTotalSubscriptionsRevenue" in data:
            self.next30DayTotalSubscriptionsRevenue: float = self._get_value(
                float, "next30DayTotalSubscriptionsRevenue"
            )
        else:
            self.next30DayTotalSubscriptionsRevenue: float = None
        if "next60DayTotalSubscriptionsRevenue" in data:
            self.next60DayTotalSubscriptionsRevenue: float = self._get_value(
                float, "next60DayTotalSubscriptionsRevenue"
            )
        else:
            self.next60DayTotalSubscriptionsRevenue: float = None
        if "next90DayTotalSubscriptionsRevenue" in data:
            self.next90DayTotalSubscriptionsRevenue: float = self._get_value(
                float, "next90DayTotalSubscriptionsRevenue"
            )
        else:
            self.next90DayTotalSubscriptionsRevenue: float = None
        if "next30DayShippedSubscriptionUnits" in data:
            self.next30DayShippedSubscriptionUnits: float = self._get_value(float, "next30DayShippedSubscriptionUnits")
        else:
            self.next30DayShippedSubscriptionUnits: float = None
        if "next60DayShippedSubscriptionUnits" in data:
            self.next60DayShippedSubscriptionUnits: float = self._get_value(float, "next60DayShippedSubscriptionUnits")
        else:
            self.next60DayShippedSubscriptionUnits: float = None
        if "next90DayShippedSubscriptionUnits" in data:
            self.next90DayShippedSubscriptionUnits: float = self._get_value(float, "next90DayShippedSubscriptionUnits")
        else:
            self.next90DayShippedSubscriptionUnits: float = None
        if "timeInterval" in data:
            self.timeInterval: TimeInterval = self._get_value(TimeInterval, "timeInterval")
        else:
            self.timeInterval: TimeInterval = None
        if "currencyCode" in data:
            self.currencyCode: str = self._get_value(str, "currencyCode")
        else:
            self.currencyCode: str = None


class ErrorList(__BaseDictObject):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        if "errors" in data:
            self.errors: _List[Error] = [Error(datum) for datum in data["errors"]]
        else:
            self.errors: _List[Error] = []


class Error(__BaseDictObject):
    """
    Error response returned when the request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        if "code" in data:
            self.code: str = self._get_value(str, "code")
        else:
            self.code: str = None
        if "message" in data:
            self.message: str = self._get_value(str, "message")
        else:
            self.message: str = None
        if "details" in data:
            self.details: str = self._get_value(str, "details")
        else:
            self.details: str = None


class ProgramTypes(list, _List["ProgramType"]):
    """
    A list of replenishment program types.
    """

    def __init__(self, data):
        super().__init__([ProgramType(datum) for datum in data])
        self.data = data


class EligibilityStatus(str):
    """
    The current eligibility status of an offer.
    """


class AutoEnrollmentPreference(str):
    """
    The auto-enrollment preference indicates whether the offer is opted-in to or opted-out of Amazon's auto-enrollment feature.
    """


class ProgramType(str):
    """
    The replenishment program type.
    """


class EnrollmentMethod(str):
    """
    The enrollment method used to enroll the offer into the program.
    """


class ListOfferMetricsSortKey(str):
    """
    The attribute to use to sort the results.
    """


class ListOffersSortKey(str):
    """
    The attribute to use to sort the results.
    """


class MarketplaceId(str):
    """
    The marketplace identifier. The supported marketplaces for both sellers and vendors are US, CA, ES, UK, FR, IT, IN, DE and JP. The supported marketplaces for vendors only are BR, AU, MX, AE and NL. Refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids) to find the identifier for the marketplace.
    """


class AggregationFrequency(str):
    """
    The time period used to group data in the response. Note that this is only valid for the performance time period type.
    """


class Metric(str):
    """
    The metric name and description.
    """


class SortOrder(str):
    """
    The sort order.
    """


class TimePeriodType(str):
    """
    The time period type that determines whether the metrics requested are backward-looking (performance) or forward-looking (forecast).
    """


class Replenishment20221107Client(__BaseClient):
    def getSellingPartnerMetrics(
        self,
        data: GetSellingPartnerMetricsRequest,
    ):
        """
                Returns aggregated replenishment program metrics for a selling partner.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/replenishment/2022-11-07/sellingPartners/metrics/search"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: GetSellingPartnerMetricsResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def listOfferMetrics(
        self,
        data: ListOfferMetricsRequest,
    ):
        """
                Returns aggregated replenishment program metrics for a selling partner's offers.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/replenishment/2022-11-07/offers/metrics/search"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: ListOfferMetricsResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def listOffers(
        self,
        data: ListOffersRequest,
    ):
        """
                Returns the details of a selling partner's replenishment program offers. Note that this operation only supports sellers at this time.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/replenishment/2022-11-07/offers/search"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: ListOffersResponse,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
