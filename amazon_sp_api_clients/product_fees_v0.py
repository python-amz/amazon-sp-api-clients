from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class GetMyFeesEstimateRequest(__BaseDictObject):
    """
    Request schema.
    """

    def __init__(self, data):
        super().__init__(data)
        if "FeesEstimateRequest" in data:
            self.FeesEstimateRequest: FeesEstimateRequest = self._get_value(FeesEstimateRequest, "FeesEstimateRequest")
        else:
            self.FeesEstimateRequest: FeesEstimateRequest = None


class FeesEstimateRequest(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "MarketplaceId" in data:
            self.MarketplaceId: str = self._get_value(str, "MarketplaceId")
        else:
            self.MarketplaceId: str = None
        if "IsAmazonFulfilled" in data:
            self.IsAmazonFulfilled: bool = self._get_value(convert_bool, "IsAmazonFulfilled")
        else:
            self.IsAmazonFulfilled: bool = None
        if "PriceToEstimateFees" in data:
            self.PriceToEstimateFees: PriceToEstimateFees = self._get_value(PriceToEstimateFees, "PriceToEstimateFees")
        else:
            self.PriceToEstimateFees: PriceToEstimateFees = None
        if "Identifier" in data:
            self.Identifier: str = self._get_value(str, "Identifier")
        else:
            self.Identifier: str = None
        if "OptionalFulfillmentProgram" in data:
            self.OptionalFulfillmentProgram: OptionalFulfillmentProgram = self._get_value(
                OptionalFulfillmentProgram, "OptionalFulfillmentProgram"
            )
        else:
            self.OptionalFulfillmentProgram: OptionalFulfillmentProgram = None


class GetMyFeesEstimateResponse(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: GetMyFeesEstimateResult = self._get_value(GetMyFeesEstimateResult, "payload")
        else:
            self.payload: GetMyFeesEstimateResult = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetMyFeesEstimateResult(__BaseDictObject):
    """
    Response schema.
    """

    def __init__(self, data):
        super().__init__(data)
        if "FeesEstimateResult" in data:
            self.FeesEstimateResult: FeesEstimateResult = self._get_value(FeesEstimateResult, "FeesEstimateResult")
        else:
            self.FeesEstimateResult: FeesEstimateResult = None


class Points(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "PointsNumber" in data:
            self.PointsNumber: int = self._get_value(int, "PointsNumber")
        else:
            self.PointsNumber: int = None
        if "PointsMonetaryValue" in data:
            self.PointsMonetaryValue: MoneyType = self._get_value(MoneyType, "PointsMonetaryValue")
        else:
            self.PointsMonetaryValue: MoneyType = None


class Error(__BaseDictObject):
    """ """

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


class FeesEstimateResult(__BaseDictObject):
    """
    An item identifier and the estimated fees for the item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Status" in data:
            self.Status: str = self._get_value(str, "Status")
        else:
            self.Status: str = None
        if "FeesEstimateIdentifier" in data:
            self.FeesEstimateIdentifier: FeesEstimateIdentifier = self._get_value(
                FeesEstimateIdentifier, "FeesEstimateIdentifier"
            )
        else:
            self.FeesEstimateIdentifier: FeesEstimateIdentifier = None
        if "FeesEstimate" in data:
            self.FeesEstimate: FeesEstimate = self._get_value(FeesEstimate, "FeesEstimate")
        else:
            self.FeesEstimate: FeesEstimate = None
        if "Error" in data:
            self.Error: FeesEstimateError = self._get_value(FeesEstimateError, "Error")
        else:
            self.Error: FeesEstimateError = None


class FeesEstimateIdentifier(__BaseDictObject):
    """
    An item identifier, marketplace, time of request, and other details that identify an estimate.
    """

    def __init__(self, data):
        super().__init__(data)
        if "MarketplaceId" in data:
            self.MarketplaceId: str = self._get_value(str, "MarketplaceId")
        else:
            self.MarketplaceId: str = None
        if "SellerId" in data:
            self.SellerId: str = self._get_value(str, "SellerId")
        else:
            self.SellerId: str = None
        if "IdType" in data:
            self.IdType: str = self._get_value(str, "IdType")
        else:
            self.IdType: str = None
        if "IdValue" in data:
            self.IdValue: str = self._get_value(str, "IdValue")
        else:
            self.IdValue: str = None
        if "IsAmazonFulfilled" in data:
            self.IsAmazonFulfilled: bool = self._get_value(convert_bool, "IsAmazonFulfilled")
        else:
            self.IsAmazonFulfilled: bool = None
        if "PriceToEstimateFees" in data:
            self.PriceToEstimateFees: PriceToEstimateFees = self._get_value(PriceToEstimateFees, "PriceToEstimateFees")
        else:
            self.PriceToEstimateFees: PriceToEstimateFees = None
        if "SellerInputIdentifier" in data:
            self.SellerInputIdentifier: str = self._get_value(str, "SellerInputIdentifier")
        else:
            self.SellerInputIdentifier: str = None
        if "OptionalFulfillmentProgram" in data:
            self.OptionalFulfillmentProgram: OptionalFulfillmentProgram = self._get_value(
                OptionalFulfillmentProgram, "OptionalFulfillmentProgram"
            )
        else:
            self.OptionalFulfillmentProgram: OptionalFulfillmentProgram = None


class PriceToEstimateFees(__BaseDictObject):
    """
    Price information for an item, used to estimate fees.
    """

    def __init__(self, data):
        super().__init__(data)
        if "ListingPrice" in data:
            self.ListingPrice: MoneyType = self._get_value(MoneyType, "ListingPrice")
        else:
            self.ListingPrice: MoneyType = None
        if "Shipping" in data:
            self.Shipping: MoneyType = self._get_value(MoneyType, "Shipping")
        else:
            self.Shipping: MoneyType = None
        if "Points" in data:
            self.Points: Points = self._get_value(Points, "Points")
        else:
            self.Points: Points = None


class FeesEstimate(__BaseDictObject):
    """
    The total estimated fees for an item and a list of details.
    """

    def __init__(self, data):
        super().__init__(data)
        if "TimeOfFeesEstimation" in data:
            self.TimeOfFeesEstimation: str = self._get_value(str, "TimeOfFeesEstimation")
        else:
            self.TimeOfFeesEstimation: str = None
        if "TotalFeesEstimate" in data:
            self.TotalFeesEstimate: MoneyType = self._get_value(MoneyType, "TotalFeesEstimate")
        else:
            self.TotalFeesEstimate: MoneyType = None
        if "FeeDetailList" in data:
            self.FeeDetailList: FeeDetailList = self._get_value(FeeDetailList, "FeeDetailList")
        else:
            self.FeeDetailList: FeeDetailList = None


class FeesEstimateError(__BaseDictObject):
    """
    An unexpected error occurred during this operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "Type" in data:
            self.Type: str = self._get_value(str, "Type")
        else:
            self.Type: str = None
        if "Code" in data:
            self.Code: str = self._get_value(str, "Code")
        else:
            self.Code: str = None
        if "Message" in data:
            self.Message: str = self._get_value(str, "Message")
        else:
            self.Message: str = None
        if "Detail" in data:
            self.Detail: FeesEstimateErrorDetail = self._get_value(FeesEstimateErrorDetail, "Detail")
        else:
            self.Detail: FeesEstimateErrorDetail = None


class FeeDetail(__BaseDictObject):
    """
    The type of fee, fee amount, and other details.
    """

    def __init__(self, data):
        super().__init__(data)
        if "FeeType" in data:
            self.FeeType: str = self._get_value(str, "FeeType")
        else:
            self.FeeType: str = None
        if "FeeAmount" in data:
            self.FeeAmount: MoneyType = self._get_value(MoneyType, "FeeAmount")
        else:
            self.FeeAmount: MoneyType = None
        if "FeePromotion" in data:
            self.FeePromotion: MoneyType = self._get_value(MoneyType, "FeePromotion")
        else:
            self.FeePromotion: MoneyType = None
        if "TaxAmount" in data:
            self.TaxAmount: MoneyType = self._get_value(MoneyType, "TaxAmount")
        else:
            self.TaxAmount: MoneyType = None
        if "FinalFee" in data:
            self.FinalFee: MoneyType = self._get_value(MoneyType, "FinalFee")
        else:
            self.FinalFee: MoneyType = None
        if "IncludedFeeDetailList" in data:
            self.IncludedFeeDetailList: IncludedFeeDetailList = self._get_value(
                IncludedFeeDetailList, "IncludedFeeDetailList"
            )
        else:
            self.IncludedFeeDetailList: IncludedFeeDetailList = None


class IncludedFeeDetail(__BaseDictObject):
    """
    The type of fee, fee amount, and other details.
    """

    def __init__(self, data):
        super().__init__(data)
        if "FeeType" in data:
            self.FeeType: str = self._get_value(str, "FeeType")
        else:
            self.FeeType: str = None
        if "FeeAmount" in data:
            self.FeeAmount: MoneyType = self._get_value(MoneyType, "FeeAmount")
        else:
            self.FeeAmount: MoneyType = None
        if "FeePromotion" in data:
            self.FeePromotion: MoneyType = self._get_value(MoneyType, "FeePromotion")
        else:
            self.FeePromotion: MoneyType = None
        if "TaxAmount" in data:
            self.TaxAmount: MoneyType = self._get_value(MoneyType, "TaxAmount")
        else:
            self.TaxAmount: MoneyType = None
        if "FinalFee" in data:
            self.FinalFee: MoneyType = self._get_value(MoneyType, "FinalFee")
        else:
            self.FinalFee: MoneyType = None


class MoneyType(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "CurrencyCode" in data:
            self.CurrencyCode: str = self._get_value(str, "CurrencyCode")
        else:
            self.CurrencyCode: str = None
        if "Amount" in data:
            self.Amount: float = self._get_value(float, "Amount")
        else:
            self.Amount: float = None


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class FeeDetailList(list, _List["FeeDetail"]):
    """
    A list of other fees that contribute to a given fee.
    """

    def __init__(self, data):
        super().__init__([FeeDetail(datum) for datum in data])
        self.data = data


class FeesEstimateErrorDetail(list, _List["dict"]):
    """
    Additional information that can help the caller understand or fix the issue.
    """

    def __init__(self, data):
        super().__init__([dict(datum) for datum in data])
        self.data = data


class IncludedFeeDetailList(list, _List["IncludedFeeDetail"]):
    """
    A list of other fees that contribute to a given fee.
    """

    def __init__(self, data):
        super().__init__([IncludedFeeDetail(datum) for datum in data])
        self.data = data


class OptionalFulfillmentProgram(str):
    """
    An optional enrollment program to return the estimated fees when the offer is fulfilled by Amazon (IsAmazonFulfilled is set to true).
    """


class ProductFeesV0Client(__BaseClient):
    def getMyFeesEstimateForSKU(
        self,
        data: GetMyFeesEstimateRequest,
        SellerSKU: str,
    ):
        """
                Returns the estimated fees for the item indicated by the specified seller SKU in the marketplace specified in the request body.
        You can call getMyFeesEstimateForSKU for an item on behalf of a selling partner before the selling partner sets the item's price. They can then take estimated fees into account. With each fees estimate request, you must include an original identifier. This identifier is included in the fees estimate so you can correlate a fees estimate with the original request.
        **Note:** This value is only an estimate, actual costs may vary. Search "fees" in [Seller Central](https://sellercentral.amazon.com/) and consult the store-specific fee schedule for the most up-to-date information.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 20 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/products/fees/v0/listings/{SellerSKU}/feesEstimate"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: GetMyFeesEstimateResponse,
            400: GetMyFeesEstimateResponse,
            401: GetMyFeesEstimateResponse,
            403: GetMyFeesEstimateResponse,
            404: GetMyFeesEstimateResponse,
            429: GetMyFeesEstimateResponse,
            500: GetMyFeesEstimateResponse,
            503: GetMyFeesEstimateResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getMyFeesEstimateForASIN(
        self,
        data: GetMyFeesEstimateRequest,
        Asin: str,
    ):
        """
                Returns the estimated fees for the item indicated by the specified Asin in the marketplace specified in the request body.
        You can call getMyFeesEstimateForASIN for an item on behalf of a selling partner before the selling partner sets the item's price. They can then take estimated fees into account. With each product fees request, you must include an original identifier. This identifier is included in the fees estimate so you can correlate a fees estimate with the original request.
        **Note:** This value is only an estimate, actual costs may vary. Search "fees" in [Seller Central](https://sellercentral.amazon.com/) and consult the store-specific fee schedule for the most up-to-date information.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 20 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/products/fees/v0/items/{Asin}/feesEstimate"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            200: GetMyFeesEstimateResponse,
            400: GetMyFeesEstimateResponse,
            401: GetMyFeesEstimateResponse,
            403: GetMyFeesEstimateResponse,
            404: GetMyFeesEstimateResponse,
            429: GetMyFeesEstimateResponse,
            500: GetMyFeesEstimateResponse,
            503: GetMyFeesEstimateResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
