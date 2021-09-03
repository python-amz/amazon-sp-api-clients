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


class ErrorList:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: _List[Error] = [Error(datum) for datum in data["errors"]]
        else:
            self.errors: _List[Error] = []


class SmallAndLightEnrollment:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "marketplaceId" in data:
            self.marketplaceId: MarketplaceId = MarketplaceId(data["marketplaceId"])
        else:
            self.marketplaceId: MarketplaceId = None
        if "sellerSKU" in data:
            self.sellerSKU: SellerSKU = SellerSKU(data["sellerSKU"])
        else:
            self.sellerSKU: SellerSKU = None
        if "status" in data:
            self.status: SmallAndLightEnrollmentStatus = SmallAndLightEnrollmentStatus(data["status"])
        else:
            self.status: SmallAndLightEnrollmentStatus = None


class SmallAndLightEligibility:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "marketplaceId" in data:
            self.marketplaceId: MarketplaceId = MarketplaceId(data["marketplaceId"])
        else:
            self.marketplaceId: MarketplaceId = None
        if "sellerSKU" in data:
            self.sellerSKU: SellerSKU = SellerSKU(data["sellerSKU"])
        else:
            self.sellerSKU: SellerSKU = None
        if "status" in data:
            self.status: SmallAndLightEligibilityStatus = SmallAndLightEligibilityStatus(data["status"])
        else:
            self.status: SmallAndLightEligibilityStatus = None


class SmallAndLightFeePreviewRequest:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "marketplaceId" in data:
            self.marketplaceId: MarketplaceId = MarketplaceId(data["marketplaceId"])
        else:
            self.marketplaceId: MarketplaceId = None
        if "items" in data:
            self.items: _List[Item] = [Item(datum) for datum in data["items"]]
        else:
            self.items: _List[Item] = []


class SmallAndLightFeePreviews:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "data" in data:
            self.data: _List[FeePreview] = [FeePreview(datum) for datum in data["data"]]
        else:
            self.data: _List[FeePreview] = []


class Item:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "asin" in data:
            self.asin: str = str(data["asin"])
        else:
            self.asin: str = None
        if "price" in data:
            self.price: MoneyType = MoneyType(data["price"])
        else:
            self.price: MoneyType = None


class FeePreview:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "asin" in data:
            self.asin: str = str(data["asin"])
        else:
            self.asin: str = None
        if "price" in data:
            self.price: MoneyType = MoneyType(data["price"])
        else:
            self.price: MoneyType = None
        if "feeBreakdown" in data:
            self.feeBreakdown: _List[FeeLineItem] = [FeeLineItem(datum) for datum in data["feeBreakdown"]]
        else:
            self.feeBreakdown: _List[FeeLineItem] = []
        if "totalFees" in data:
            self.totalFees: MoneyType = MoneyType(data["totalFees"])
        else:
            self.totalFees: MoneyType = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class FeeLineItem:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "feeType" in data:
            self.feeType: str = str(data["feeType"])
        else:
            self.feeType: str = None
        if "feeCharge" in data:
            self.feeCharge: MoneyType = MoneyType(data["feeCharge"])
        else:
            self.feeCharge: MoneyType = None


class MoneyType:
    def __init__(self, data):
        super().__init__()
        self.data = data
        if "currencyCode" in data:
            self.currencyCode: str = str(data["currencyCode"])
        else:
            self.currencyCode: str = None
        if "amount" in data:
            self.amount: float = float(data["amount"])
        else:
            self.amount: float = None


class MarketplaceId(str):
    pass


class SellerSKU(str):
    pass


class SmallAndLightEnrollmentStatus(str):
    pass


class SmallAndLightEligibilityStatus(str):
    pass


class FbaSmallAndLightV1Client(__BaseClient):
    def getSmallAndLightEnrollmentBySellerSKU(
        self,
        sellerSKU: str,
        marketplaceIds: _List[str],
    ):
        url = "/fba/smallAndLight/v1/enrollments/{sellerSKU}".format(
            sellerSKU=sellerSKU,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="GET", params=params)
        return {
            200: SmallAndLightEnrollment,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self.__get_response_json(response))

    def putSmallAndLightEnrollmentBySellerSKU(
        self,
        sellerSKU: str,
        marketplaceIds: _List[str],
    ):
        url = "/fba/smallAndLight/v1/enrollments/{sellerSKU}".format(
            sellerSKU=sellerSKU,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="PUT", data=data.data)
        return {
            200: SmallAndLightEnrollment,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self.__get_response_json(response))

    def deleteSmallAndLightEnrollmentBySellerSKU(
        self,
        sellerSKU: str,
        marketplaceIds: _List[str],
    ):
        url = "/fba/smallAndLight/v1/enrollments/{sellerSKU}".format(
            sellerSKU=sellerSKU,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="DELETE", data=data.data)
        return {
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self.__get_response_json(response))

    def getSmallAndLightEligibilityBySellerSKU(
        self,
        sellerSKU: str,
        marketplaceIds: _List[str],
    ):
        url = "/fba/smallAndLight/v1/eligibilities/{sellerSKU}".format(
            sellerSKU=sellerSKU,
        )
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(url, method="GET", params=params)
        return {
            200: SmallAndLightEligibility,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self.__get_response_json(response))

    def getSmallAndLightFeePreview(
        self,
        data: SmallAndLightFeePreviewRequest,
    ):
        url = "/fba/smallAndLight/v1/feePreviews".format()
        params = {}
        response = self.request(url, method="POST", data=data.data)
        return {
            200: SmallAndLightFeePreviews,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }[response.status_code](self.__get_response_json(response))
