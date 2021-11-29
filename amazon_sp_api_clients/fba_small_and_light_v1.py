from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


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


class SmallAndLightEnrollment(__BaseDictObject):
    """
    The Small and Light enrollment status of the item indicated by the specified seller SKU.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: MarketplaceId = self._get_value(MarketplaceId, "marketplaceId")
        else:
            self.marketplaceId: MarketplaceId = None
        if "sellerSKU" in data:
            self.sellerSKU: SellerSKU = self._get_value(SellerSKU, "sellerSKU")
        else:
            self.sellerSKU: SellerSKU = None
        if "status" in data:
            self.status: SmallAndLightEnrollmentStatus = self._get_value(SmallAndLightEnrollmentStatus, "status")
        else:
            self.status: SmallAndLightEnrollmentStatus = None


class SmallAndLightEligibility(__BaseDictObject):
    """
    The Small and Light eligibility status of the item indicated by the specified seller SKU.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: MarketplaceId = self._get_value(MarketplaceId, "marketplaceId")
        else:
            self.marketplaceId: MarketplaceId = None
        if "sellerSKU" in data:
            self.sellerSKU: SellerSKU = self._get_value(SellerSKU, "sellerSKU")
        else:
            self.sellerSKU: SellerSKU = None
        if "status" in data:
            self.status: SmallAndLightEligibilityStatus = self._get_value(SmallAndLightEligibilityStatus, "status")
        else:
            self.status: SmallAndLightEligibilityStatus = None


class SmallAndLightFeePreviewRequest(__BaseDictObject):
    """
    Request schema for submitting items for which to retrieve fee estimates.
    """

    def __init__(self, data):
        super().__init__(data)
        if "marketplaceId" in data:
            self.marketplaceId: MarketplaceId = self._get_value(MarketplaceId, "marketplaceId")
        else:
            self.marketplaceId: MarketplaceId = None
        if "items" in data:
            self.items: _List[Item] = [Item(datum) for datum in data["items"]]
        else:
            self.items: _List[Item] = []


class SmallAndLightFeePreviews(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "data" in data:
            self.data: _List[FeePreview] = [FeePreview(datum) for datum in data["data"]]
        else:
            self.data: _List[FeePreview] = []


class Item(__BaseDictObject):
    """
    An item to be sold.
    """

    def __init__(self, data):
        super().__init__(data)
        if "asin" in data:
            self.asin: str = self._get_value(str, "asin")
        else:
            self.asin: str = None
        if "price" in data:
            self.price: MoneyType = self._get_value(MoneyType, "price")
        else:
            self.price: MoneyType = None


class FeePreview(__BaseDictObject):
    """
    The fee estimate for a specific item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "asin" in data:
            self.asin: str = self._get_value(str, "asin")
        else:
            self.asin: str = None
        if "price" in data:
            self.price: MoneyType = self._get_value(MoneyType, "price")
        else:
            self.price: MoneyType = None
        if "feeBreakdown" in data:
            self.feeBreakdown: _List[FeeLineItem] = [FeeLineItem(datum) for datum in data["feeBreakdown"]]
        else:
            self.feeBreakdown: _List[FeeLineItem] = []
        if "totalFees" in data:
            self.totalFees: MoneyType = self._get_value(MoneyType, "totalFees")
        else:
            self.totalFees: MoneyType = None
        if "errors" in data:
            self.errors: _List[Error] = [Error(datum) for datum in data["errors"]]
        else:
            self.errors: _List[Error] = []


class FeeLineItem(__BaseDictObject):
    """
    Fee details for a specific fee.
    """

    def __init__(self, data):
        super().__init__(data)
        if "feeType" in data:
            self.feeType: str = self._get_value(str, "feeType")
        else:
            self.feeType: str = None
        if "feeCharge" in data:
            self.feeCharge: MoneyType = self._get_value(MoneyType, "feeCharge")
        else:
            self.feeCharge: MoneyType = None


class MoneyType(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "currencyCode" in data:
            self.currencyCode: str = self._get_value(str, "currencyCode")
        else:
            self.currencyCode: str = None
        if "amount" in data:
            self.amount: float = self._get_value(float, "amount")
        else:
            self.amount: float = None


class MarketplaceId(str):
    """
    A marketplace identifier.
    """


class SellerSKU(str):
    """
    Identifies an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.
    """


class SmallAndLightEnrollmentStatus(str):
    """
    The Small and Light enrollment status of the item.
    """


class SmallAndLightEligibilityStatus(str):
    """
    The Small and Light eligibility status of the item.
    """


class FbaSmallAndLightV1Client(__BaseClient):
    def getSmallAndLightEnrollmentBySellerSKU(
        self,
        sellerSKU: str,
        marketplaceIds: _List[str],
    ):
        """
                Returns the Small and Light enrollment status for the item indicated by the specified seller SKU in the specified marketplace.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/fba/smallAndLight/v1/enrollments/{sellerSKU}"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: SmallAndLightEnrollment,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def putSmallAndLightEnrollmentBySellerSKU(
        self,
        sellerSKU: str,
        marketplaceIds: _List[str],
    ):
        """
                Enrolls the item indicated by the specified seller SKU in the Small and Light program in the specified marketplace. If the item is not eligible, the ineligibility reasons are returned.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/fba/smallAndLight/v1/enrollments/{sellerSKU}"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="PUT",
            params=params,
        )
        response_type = {
            200: SmallAndLightEnrollment,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def deleteSmallAndLightEnrollmentBySellerSKU(
        self,
        sellerSKU: str,
        marketplaceIds: _List[str],
    ):
        """
                Removes the item indicated by the specified seller SKU from the Small and Light program in the specified marketplace. If the item is not eligible for disenrollment, the ineligibility reasons are returned.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 5 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/fba/smallAndLight/v1/enrollments/{sellerSKU}"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="DELETE",
            params=params,
        )
        response_type = {
            204: None,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getSmallAndLightEligibilityBySellerSKU(
        self,
        sellerSKU: str,
        marketplaceIds: _List[str],
    ):
        """
                Returns the Small and Light program eligibility status of the item indicated by the specified seller SKU in the specified marketplace. If the item is not eligible, the ineligibility reasons are returned.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/fba/smallAndLight/v1/eligibilities/{sellerSKU}"
        params = {}
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: SmallAndLightEligibility,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            413: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getSmallAndLightFeePreview(
        self,
        data: SmallAndLightFeePreviewRequest,
    ):
        """
                Returns the Small and Light fee estimates for the specified items. You must include a marketplaceId parameter to retrieve the proper fee estimates for items to be sold in that marketplace. The ordering of items in the response will mirror the order of the items in the request. Duplicate ASIN/price combinations are removed.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 3 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/fba/smallAndLight/v1/feePreviews"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: SmallAndLightFeePreviews,
            400: ErrorList,
            401: ErrorList,
            403: ErrorList,
            404: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
