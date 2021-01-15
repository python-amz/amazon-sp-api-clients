from .base import BaseClient as __BaseClient
from typing import List as _List


class GetMyFeesEstimateRequest:
    def __init__(self, data):
        super().__init__()
        if "FeesEstimateRequest" in data:
            self.FeesEstimateRequest: FeesEstimateRequest = FeesEstimateRequest(data["FeesEstimateRequest"])
        else:
            self.FeesEstimateRequest: FeesEstimateRequest = None


class FeesEstimateRequest:
    def __init__(self, data):
        super().__init__()
        if "MarketplaceId" in data:
            self.MarketplaceId: str = str(data["MarketplaceId"])
        else:
            self.MarketplaceId: str = None
        if "IsAmazonFulfilled" in data:
            self.IsAmazonFulfilled: bool = bool(data["IsAmazonFulfilled"])
        else:
            self.IsAmazonFulfilled: bool = None
        if "PriceToEstimateFees" in data:
            self.PriceToEstimateFees: PriceToEstimateFees = PriceToEstimateFees(data["PriceToEstimateFees"])
        else:
            self.PriceToEstimateFees: PriceToEstimateFees = None
        if "Identifier" in data:
            self.Identifier: str = str(data["Identifier"])
        else:
            self.Identifier: str = None


class GetMyFeesEstimateResponse:
    def __init__(self, data):
        super().__init__()
        if "payload" in data:
            self.payload: GetMyFeesEstimateResult = GetMyFeesEstimateResult(data["payload"])
        else:
            self.payload: GetMyFeesEstimateResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetMyFeesEstimateResult:
    def __init__(self, data):
        super().__init__()
        if "FeesEstimateResult" in data:
            self.FeesEstimateResult: FeesEstimateResult = FeesEstimateResult(data["FeesEstimateResult"])
        else:
            self.FeesEstimateResult: FeesEstimateResult = None


class Points:
    def __init__(self, data):
        super().__init__()
        if "PointsNumber" in data:
            self.PointsNumber: int = int(data["PointsNumber"])
        else:
            self.PointsNumber: int = None
        if "PointsMonetaryValue" in data:
            self.PointsMonetaryValue: MoneyType = MoneyType(data["PointsMonetaryValue"])
        else:
            self.PointsMonetaryValue: MoneyType = None


class Error:
    def __init__(self, data):
        super().__init__()
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


class FeesEstimateResult:
    def __init__(self, data):
        super().__init__()
        if "Status" in data:
            self.Status: str = str(data["Status"])
        else:
            self.Status: str = None
        if "FeesEstimateIdentifier" in data:
            self.FeesEstimateIdentifier: FeesEstimateIdentifier = FeesEstimateIdentifier(data["FeesEstimateIdentifier"])
        else:
            self.FeesEstimateIdentifier: FeesEstimateIdentifier = None
        if "FeesEstimate" in data:
            self.FeesEstimate: FeesEstimate = FeesEstimate(data["FeesEstimate"])
        else:
            self.FeesEstimate: FeesEstimate = None
        if "Error" in data:
            self.Error: FeesEstimateError = FeesEstimateError(data["Error"])
        else:
            self.Error: FeesEstimateError = None


class FeesEstimateIdentifier:
    def __init__(self, data):
        super().__init__()
        if "MarketplaceId" in data:
            self.MarketplaceId: str = str(data["MarketplaceId"])
        else:
            self.MarketplaceId: str = None
        if "SellerId" in data:
            self.SellerId: str = str(data["SellerId"])
        else:
            self.SellerId: str = None
        if "IdType" in data:
            self.IdType: str = str(data["IdType"])
        else:
            self.IdType: str = None
        if "IdValue" in data:
            self.IdValue: str = str(data["IdValue"])
        else:
            self.IdValue: str = None
        if "IsAmazonFulfilled" in data:
            self.IsAmazonFulfilled: bool = bool(data["IsAmazonFulfilled"])
        else:
            self.IsAmazonFulfilled: bool = None
        if "PriceToEstimateFees" in data:
            self.PriceToEstimateFees: PriceToEstimateFees = PriceToEstimateFees(data["PriceToEstimateFees"])
        else:
            self.PriceToEstimateFees: PriceToEstimateFees = None
        if "SellerInputIdentifier" in data:
            self.SellerInputIdentifier: str = str(data["SellerInputIdentifier"])
        else:
            self.SellerInputIdentifier: str = None


class PriceToEstimateFees:
    def __init__(self, data):
        super().__init__()
        if "ListingPrice" in data:
            self.ListingPrice: MoneyType = MoneyType(data["ListingPrice"])
        else:
            self.ListingPrice: MoneyType = None
        if "Shipping" in data:
            self.Shipping: MoneyType = MoneyType(data["Shipping"])
        else:
            self.Shipping: MoneyType = None
        if "Points" in data:
            self.Points: Points = Points(data["Points"])
        else:
            self.Points: Points = None


class FeesEstimate:
    def __init__(self, data):
        super().__init__()
        if "TimeOfFeesEstimation" in data:
            self.TimeOfFeesEstimation: str = str(data["TimeOfFeesEstimation"])
        else:
            self.TimeOfFeesEstimation: str = None
        if "TotalFeesEstimate" in data:
            self.TotalFeesEstimate: MoneyType = MoneyType(data["TotalFeesEstimate"])
        else:
            self.TotalFeesEstimate: MoneyType = None
        if "FeeDetailList" in data:
            self.FeeDetailList: FeeDetailList = FeeDetailList(data["FeeDetailList"])
        else:
            self.FeeDetailList: FeeDetailList = None


class FeesEstimateError:
    def __init__(self, data):
        super().__init__()
        if "Type" in data:
            self.Type: str = str(data["Type"])
        else:
            self.Type: str = None
        if "Code" in data:
            self.Code: str = str(data["Code"])
        else:
            self.Code: str = None
        if "Message" in data:
            self.Message: str = str(data["Message"])
        else:
            self.Message: str = None
        if "Detail" in data:
            self.Detail: FeesEstimateErrorDetail = FeesEstimateErrorDetail(data["Detail"])
        else:
            self.Detail: FeesEstimateErrorDetail = None


class FeeDetail:
    def __init__(self, data):
        super().__init__()
        if "FeeType" in data:
            self.FeeType: str = str(data["FeeType"])
        else:
            self.FeeType: str = None
        if "FeeAmount" in data:
            self.FeeAmount: MoneyType = MoneyType(data["FeeAmount"])
        else:
            self.FeeAmount: MoneyType = None
        if "FeePromotion" in data:
            self.FeePromotion: MoneyType = MoneyType(data["FeePromotion"])
        else:
            self.FeePromotion: MoneyType = None
        if "TaxAmount" in data:
            self.TaxAmount: MoneyType = MoneyType(data["TaxAmount"])
        else:
            self.TaxAmount: MoneyType = None
        if "FinalFee" in data:
            self.FinalFee: MoneyType = MoneyType(data["FinalFee"])
        else:
            self.FinalFee: MoneyType = None
        if "IncludedFeeDetailList" in data:
            self.IncludedFeeDetailList: IncludedFeeDetailList = IncludedFeeDetailList(data["IncludedFeeDetailList"])
        else:
            self.IncludedFeeDetailList: IncludedFeeDetailList = None


class IncludedFeeDetail:
    def __init__(self, data):
        super().__init__()
        if "FeeType" in data:
            self.FeeType: str = str(data["FeeType"])
        else:
            self.FeeType: str = None
        if "FeeAmount" in data:
            self.FeeAmount: MoneyType = MoneyType(data["FeeAmount"])
        else:
            self.FeeAmount: MoneyType = None
        if "FeePromotion" in data:
            self.FeePromotion: MoneyType = MoneyType(data["FeePromotion"])
        else:
            self.FeePromotion: MoneyType = None
        if "TaxAmount" in data:
            self.TaxAmount: MoneyType = MoneyType(data["TaxAmount"])
        else:
            self.TaxAmount: MoneyType = None
        if "FinalFee" in data:
            self.FinalFee: MoneyType = MoneyType(data["FinalFee"])
        else:
            self.FinalFee: MoneyType = None


class MoneyType:
    def __init__(self, data):
        super().__init__()
        if "CurrencyCode" in data:
            self.CurrencyCode: str = str(data["CurrencyCode"])
        else:
            self.CurrencyCode: str = None
        if "Amount" in data:
            self.Amount: float = float(data["Amount"])
        else:
            self.Amount: float = None


class ErrorList(list, _List["Error"]):
    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])


class FeeDetailList(list, _List["FeeDetail"]):
    def __init__(self, data):
        super().__init__([FeeDetail(datum) for datum in data])


class FeesEstimateErrorDetail(list, _List["dict"]):
    def __init__(self, data):
        super().__init__([dict(datum) for datum in data])


class IncludedFeeDetailList(list, _List["IncludedFeeDetail"]):
    def __init__(self, data):
        super().__init__([IncludedFeeDetail(datum) for datum in data])


class ProductFeesClient(__BaseClient):
    def getMyFeesEstimateForSKU(
        self,
        SellerSKU: str,
    ):
        url = "/products/fees/v0/listings/{SellerSKU}/feesEstimate".format(
            SellerSKU=SellerSKU,
        )
        data = {}
        response = self.request(url, method="POST", data=data)
        return {
            200: GetMyFeesEstimateResponse,
            400: GetMyFeesEstimateResponse,
            401: GetMyFeesEstimateResponse,
            403: GetMyFeesEstimateResponse,
            404: GetMyFeesEstimateResponse,
            429: GetMyFeesEstimateResponse,
            500: GetMyFeesEstimateResponse,
            503: GetMyFeesEstimateResponse,
        }[response.status_code](response.json())

    def getMyFeesEstimateForASIN(
        self,
        Asin: str,
    ):
        url = "/products/fees/v0/items/{Asin}/feesEstimate".format(
            Asin=Asin,
        )
        data = {}
        response = self.request(url, method="POST", data=data)
        return {
            200: GetMyFeesEstimateResponse,
            400: GetMyFeesEstimateResponse,
            401: GetMyFeesEstimateResponse,
            403: GetMyFeesEstimateResponse,
            404: GetMyFeesEstimateResponse,
            429: GetMyFeesEstimateResponse,
            500: GetMyFeesEstimateResponse,
            503: GetMyFeesEstimateResponse,
        }[response.status_code](response.json())
