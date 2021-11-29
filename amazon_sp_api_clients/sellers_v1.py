from .base import BaseClient as __BaseClient, convert_bool, BaseObject as __BaseObject
from typing import List as _List


class Error(__BaseObject):
    """
    Error response returned when the request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "code" in data:
            self.code: str = str(data["code"])
        else:
            self.code: str = None
        if "message" in data:
            self.message: str = str(data["message"])
        else:
            self.message: str = None
        if "details" in data:
            self.details: str = str(data["details"])
        else:
            self.details: str = None


class MarketplaceParticipation(__BaseObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "marketplace" in data:
            self.marketplace: Marketplace = Marketplace(data["marketplace"])
        else:
            self.marketplace: Marketplace = None
        if "participation" in data:
            self.participation: Participation = Participation(data["participation"])
        else:
            self.participation: Participation = None


class GetMarketplaceParticipationsResponse(__BaseObject):
    """
    The response schema for the getMarketplaceParticipations operation.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "payload" in data:
            self.payload: MarketplaceParticipationList = MarketplaceParticipationList(data["payload"])
        else:
            self.payload: MarketplaceParticipationList = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class Marketplace(__BaseObject):
    """
    Detailed information about an Amazon market where a seller can list items for sale and customers can view and purchase items.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "id" in data:
            self.id: str = str(data["id"])
        else:
            self.id: str = None
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None
        if "countryCode" in data:
            self.countryCode: str = str(data["countryCode"])
        else:
            self.countryCode: str = None
        if "defaultCurrencyCode" in data:
            self.defaultCurrencyCode: str = str(data["defaultCurrencyCode"])
        else:
            self.defaultCurrencyCode: str = None
        if "defaultLanguageCode" in data:
            self.defaultLanguageCode: str = str(data["defaultLanguageCode"])
        else:
            self.defaultLanguageCode: str = None
        if "domainName" in data:
            self.domainName: str = str(data["domainName"])
        else:
            self.domainName: str = None


class Participation(__BaseObject):
    """
    Detailed information that is specific to a seller in a Marketplace.
    """

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        if "isParticipating" in data:
            self.isParticipating: bool = convert_bool(data["isParticipating"])
        else:
            self.isParticipating: bool = None
        if "hasSuspendedListings" in data:
            self.hasSuspendedListings: bool = convert_bool(data["hasSuspendedListings"])
        else:
            self.hasSuspendedListings: bool = None


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class MarketplaceParticipationList(list, _List["MarketplaceParticipation"]):
    """
    List of marketplace participations.
    """

    def __init__(self, data):
        super().__init__([MarketplaceParticipation(datum) for datum in data])
        self.data = data


class SellersV1Client(__BaseClient):
    def getMarketplaceParticipations(
        self,
    ):
        """
                Returns a list of marketplaces that the seller submitting the request can sell in and information about the seller's participation in those marketplaces.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | .016 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/sellers/v1/marketplaceParticipations"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetMarketplaceParticipationsResponse,
            400: GetMarketplaceParticipationsResponse,
            403: GetMarketplaceParticipationsResponse,
            404: GetMarketplaceParticipationsResponse,
            413: GetMarketplaceParticipationsResponse,
            415: GetMarketplaceParticipationsResponse,
            429: GetMarketplaceParticipationsResponse,
            500: GetMarketplaceParticipationsResponse,
            503: GetMarketplaceParticipationsResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
