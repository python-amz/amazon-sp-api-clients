from .base import BaseClient as __BaseClient
from typing import List as _List


class Error:
    def __init__(self, data):
        super().__init__()
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


class MarketplaceParticipation:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "marketplace" in data:
            self.marketplace: Marketplace = Marketplace(data["marketplace"])
        else:
            self.marketplace: Marketplace = None
        if "participation" in data:
            self.participation: Participation = Participation(data["participation"])
        else:
            self.participation: Participation = None


class GetMarketplaceParticipationsResponse:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: MarketplaceParticipationList = MarketplaceParticipationList(data["payload"])
        else:
            self.payload: MarketplaceParticipationList = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class Marketplace:
    def __init__(self, data):
        super().__init__()
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


class Participation:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "isParticipating" in data:
            self.isParticipating: bool = bool(data["isParticipating"])
        else:
            self.isParticipating: bool = None
        if "hasSuspendedListings" in data:
            self.hasSuspendedListings: bool = bool(data["hasSuspendedListings"])
        else:
            self.hasSuspendedListings: bool = None


class ErrorList(list, _List["Error"]):
    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class MarketplaceParticipationList(list, _List["MarketplaceParticipation"]):
    def __init__(self, data):
        super().__init__([MarketplaceParticipation(datum) for datum in data])
        self.data = data


class SellersV1Client(__BaseClient):
    def getMarketplaceParticipations(
        self,
    ):
        url = "/sellers/v1/marketplaceParticipations".format()
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetMarketplaceParticipationsResponse,
            400: GetMarketplaceParticipationsResponse,
            403: GetMarketplaceParticipationsResponse,
            404: GetMarketplaceParticipationsResponse,
            413: GetMarketplaceParticipationsResponse,
            415: GetMarketplaceParticipationsResponse,
            429: GetMarketplaceParticipationsResponse,
            500: GetMarketplaceParticipationsResponse,
            503: GetMarketplaceParticipationsResponse,
        }[response.status_code](response.json())
