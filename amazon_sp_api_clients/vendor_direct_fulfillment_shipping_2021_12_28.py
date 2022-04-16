from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class SubmitShippingLabelsRequest(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "shippingLabelRequests" in data:
            self.shippingLabelRequests: _List[ShippingLabelRequest] = [
                ShippingLabelRequest(datum) for datum in data["shippingLabelRequests"]
            ]
        else:
            self.shippingLabelRequests: _List[ShippingLabelRequest] = []


class ShippingLabelRequest(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = self._get_value(str, "purchaseOrderNumber")
        else:
            self.purchaseOrderNumber: str = None
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = self._get_value(PartyIdentification, "sellingParty")
        else:
            self.sellingParty: PartyIdentification = None
        if "shipFromParty" in data:
            self.shipFromParty: PartyIdentification = self._get_value(PartyIdentification, "shipFromParty")
        else:
            self.shipFromParty: PartyIdentification = None
        if "containers" in data:
            self.containers: _List[Container] = [Container(datum) for datum in data["containers"]]
        else:
            self.containers: _List[Container] = []


class Item(__BaseDictObject):
    """
    Details of the item being shipped.
    """

    def __init__(self, data):
        super().__init__(data)
        if "itemSequenceNumber" in data:
            self.itemSequenceNumber: int = self._get_value(int, "itemSequenceNumber")
        else:
            self.itemSequenceNumber: int = None
        if "buyerProductIdentifier" in data:
            self.buyerProductIdentifier: str = self._get_value(str, "buyerProductIdentifier")
        else:
            self.buyerProductIdentifier: str = None
        if "vendorProductIdentifier" in data:
            self.vendorProductIdentifier: str = self._get_value(str, "vendorProductIdentifier")
        else:
            self.vendorProductIdentifier: str = None
        if "shippedQuantity" in data:
            self.shippedQuantity: ItemQuantity = self._get_value(ItemQuantity, "shippedQuantity")
        else:
            self.shippedQuantity: ItemQuantity = None


class PackedItem(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "itemSequenceNumber" in data:
            self.itemSequenceNumber: int = self._get_value(int, "itemSequenceNumber")
        else:
            self.itemSequenceNumber: int = None
        if "buyerProductIdentifier" in data:
            self.buyerProductIdentifier: str = self._get_value(str, "buyerProductIdentifier")
        else:
            self.buyerProductIdentifier: str = None
        if "vendorProductIdentifier" in data:
            self.vendorProductIdentifier: str = self._get_value(str, "vendorProductIdentifier")
        else:
            self.vendorProductIdentifier: str = None
        if "packedQuantity" in data:
            self.packedQuantity: ItemQuantity = self._get_value(ItemQuantity, "packedQuantity")
        else:
            self.packedQuantity: ItemQuantity = None


class PartyIdentification(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "partyId" in data:
            self.partyId: str = self._get_value(str, "partyId")
        else:
            self.partyId: str = None
        if "address" in data:
            self.address: Address = self._get_value(Address, "address")
        else:
            self.address: Address = None
        if "taxRegistrationDetails" in data:
            self.taxRegistrationDetails: _List[TaxRegistrationDetails] = [
                TaxRegistrationDetails(datum) for datum in data["taxRegistrationDetails"]
            ]
        else:
            self.taxRegistrationDetails: _List[TaxRegistrationDetails] = []


class TaxRegistrationDetails(__BaseDictObject):
    """
    Tax registration details of the entity.
    """

    def __init__(self, data):
        super().__init__(data)
        if "taxRegistrationType" in data:
            self.taxRegistrationType: str = self._get_value(str, "taxRegistrationType")
        else:
            self.taxRegistrationType: str = None
        if "taxRegistrationNumber" in data:
            self.taxRegistrationNumber: str = self._get_value(str, "taxRegistrationNumber")
        else:
            self.taxRegistrationNumber: str = None
        if "taxRegistrationAddress" in data:
            self.taxRegistrationAddress: Address = self._get_value(Address, "taxRegistrationAddress")
        else:
            self.taxRegistrationAddress: Address = None
        if "taxRegistrationMessages" in data:
            self.taxRegistrationMessages: str = self._get_value(str, "taxRegistrationMessages")
        else:
            self.taxRegistrationMessages: str = None


class Address(__BaseDictObject):
    """
    Address of the party.
    """

    def __init__(self, data):
        super().__init__(data)
        if "name" in data:
            self.name: str = self._get_value(str, "name")
        else:
            self.name: str = None
        if "addressLine1" in data:
            self.addressLine1: str = self._get_value(str, "addressLine1")
        else:
            self.addressLine1: str = None
        if "addressLine2" in data:
            self.addressLine2: str = self._get_value(str, "addressLine2")
        else:
            self.addressLine2: str = None
        if "addressLine3" in data:
            self.addressLine3: str = self._get_value(str, "addressLine3")
        else:
            self.addressLine3: str = None
        if "city" in data:
            self.city: str = self._get_value(str, "city")
        else:
            self.city: str = None
        if "county" in data:
            self.county: str = self._get_value(str, "county")
        else:
            self.county: str = None
        if "district" in data:
            self.district: str = self._get_value(str, "district")
        else:
            self.district: str = None
        if "stateOrRegion" in data:
            self.stateOrRegion: str = self._get_value(str, "stateOrRegion")
        else:
            self.stateOrRegion: str = None
        if "postalCode" in data:
            self.postalCode: str = self._get_value(str, "postalCode")
        else:
            self.postalCode: str = None
        if "countryCode" in data:
            self.countryCode: str = self._get_value(str, "countryCode")
        else:
            self.countryCode: str = None
        if "phone" in data:
            self.phone: str = self._get_value(str, "phone")
        else:
            self.phone: str = None


class Dimensions(__BaseDictObject):
    """
    Physical dimensional measurements of a container.
    """

    def __init__(self, data):
        super().__init__(data)
        if "length" in data:
            self.length: Decimal = self._get_value(Decimal, "length")
        else:
            self.length: Decimal = None
        if "width" in data:
            self.width: Decimal = self._get_value(Decimal, "width")
        else:
            self.width: Decimal = None
        if "height" in data:
            self.height: Decimal = self._get_value(Decimal, "height")
        else:
            self.height: Decimal = None
        if "unitOfMeasure" in data:
            self.unitOfMeasure: str = self._get_value(str, "unitOfMeasure")
        else:
            self.unitOfMeasure: str = None


class Weight(__BaseDictObject):
    """
    The weight.
    """

    def __init__(self, data):
        super().__init__(data)
        if "unitOfMeasure" in data:
            self.unitOfMeasure: str = self._get_value(str, "unitOfMeasure")
        else:
            self.unitOfMeasure: str = None
        if "value" in data:
            self.value: Decimal = self._get_value(Decimal, "value")
        else:
            self.value: Decimal = None


class ItemQuantity(__BaseDictObject):
    """
    Details of item quantity.
    """

    def __init__(self, data):
        super().__init__(data)
        if "amount" in data:
            self.amount: int = self._get_value(int, "amount")
        else:
            self.amount: int = None
        if "unitOfMeasure" in data:
            self.unitOfMeasure: str = self._get_value(str, "unitOfMeasure")
        else:
            self.unitOfMeasure: str = None


class GetShippingLabelListResponse(__BaseDictObject):
    """
    The response schema for the getShippingLabels operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: ShippingLabelList = self._get_value(ShippingLabelList, "payload")
        else:
            self.payload: ShippingLabelList = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetShippingLabelResponse(__BaseDictObject):
    """
    The response schema for the getShippingLabel operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: ShippingLabel = self._get_value(ShippingLabel, "payload")
        else:
            self.payload: ShippingLabel = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class ShippingLabelList(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "pagination" in data:
            self.pagination: Pagination = self._get_value(Pagination, "pagination")
        else:
            self.pagination: Pagination = None
        if "shippingLabels" in data:
            self.shippingLabels: _List[ShippingLabel] = [ShippingLabel(datum) for datum in data["shippingLabels"]]
        else:
            self.shippingLabels: _List[ShippingLabel] = []


class LabelData(__BaseDictObject):
    """
    Details of the shipment label.
    """

    def __init__(self, data):
        super().__init__(data)
        if "packageIdentifier" in data:
            self.packageIdentifier: str = self._get_value(str, "packageIdentifier")
        else:
            self.packageIdentifier: str = None
        if "trackingNumber" in data:
            self.trackingNumber: str = self._get_value(str, "trackingNumber")
        else:
            self.trackingNumber: str = None
        if "shipMethod" in data:
            self.shipMethod: str = self._get_value(str, "shipMethod")
        else:
            self.shipMethod: str = None
        if "shipMethodName" in data:
            self.shipMethodName: str = self._get_value(str, "shipMethodName")
        else:
            self.shipMethodName: str = None
        if "content" in data:
            self.content: str = self._get_value(str, "content")
        else:
            self.content: str = None


class ShippingLabel(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = self._get_value(str, "purchaseOrderNumber")
        else:
            self.purchaseOrderNumber: str = None
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = self._get_value(PartyIdentification, "sellingParty")
        else:
            self.sellingParty: PartyIdentification = None
        if "shipFromParty" in data:
            self.shipFromParty: PartyIdentification = self._get_value(PartyIdentification, "shipFromParty")
        else:
            self.shipFromParty: PartyIdentification = None
        if "labelFormat" in data:
            self.labelFormat: str = self._get_value(str, "labelFormat")
        else:
            self.labelFormat: str = None
        if "labelData" in data:
            self.labelData: _List[LabelData] = [LabelData(datum) for datum in data["labelData"]]
        else:
            self.labelData: _List[LabelData] = []


class SubmitShippingLabelsResponse(__BaseDictObject):
    """
    The response schema for the submitShippingLabelRequest operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: TransactionReference = self._get_value(TransactionReference, "payload")
        else:
            self.payload: TransactionReference = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetCustomerInvoicesResponse(__BaseDictObject):
    """
    The response schema for the getCustomerInvoices operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: CustomerInvoiceList = self._get_value(CustomerInvoiceList, "payload")
        else:
            self.payload: CustomerInvoiceList = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetCustomerInvoiceResponse(__BaseDictObject):
    """
    The response schema for the getCustomerInvoice operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: CustomerInvoice = self._get_value(CustomerInvoice, "payload")
        else:
            self.payload: CustomerInvoice = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class CustomerInvoiceList(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "pagination" in data:
            self.pagination: Pagination = self._get_value(Pagination, "pagination")
        else:
            self.pagination: Pagination = None
        if "customerInvoices" in data:
            self.customerInvoices: _List[CustomerInvoice] = [
                CustomerInvoice(datum) for datum in data["customerInvoices"]
            ]
        else:
            self.customerInvoices: _List[CustomerInvoice] = []


class Pagination(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "nextToken" in data:
            self.nextToken: str = self._get_value(str, "nextToken")
        else:
            self.nextToken: str = None


class CustomerInvoice(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = self._get_value(str, "purchaseOrderNumber")
        else:
            self.purchaseOrderNumber: str = None
        if "content" in data:
            self.content: str = self._get_value(str, "content")
        else:
            self.content: str = None


class TransactionReference(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "transactionId" in data:
            self.transactionId: str = self._get_value(str, "transactionId")
        else:
            self.transactionId: str = None


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


class Container(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "containerType" in data:
            self.containerType: str = self._get_value(str, "containerType")
        else:
            self.containerType: str = None
        if "containerIdentifier" in data:
            self.containerIdentifier: str = self._get_value(str, "containerIdentifier")
        else:
            self.containerIdentifier: str = None
        if "trackingNumber" in data:
            self.trackingNumber: str = self._get_value(str, "trackingNumber")
        else:
            self.trackingNumber: str = None
        if "manifestId" in data:
            self.manifestId: str = self._get_value(str, "manifestId")
        else:
            self.manifestId: str = None
        if "manifestDate" in data:
            self.manifestDate: str = self._get_value(str, "manifestDate")
        else:
            self.manifestDate: str = None
        if "shipMethod" in data:
            self.shipMethod: str = self._get_value(str, "shipMethod")
        else:
            self.shipMethod: str = None
        if "scacCode" in data:
            self.scacCode: str = self._get_value(str, "scacCode")
        else:
            self.scacCode: str = None
        if "carrier" in data:
            self.carrier: str = self._get_value(str, "carrier")
        else:
            self.carrier: str = None
        if "containerSequenceNumber" in data:
            self.containerSequenceNumber: int = self._get_value(int, "containerSequenceNumber")
        else:
            self.containerSequenceNumber: int = None
        if "dimensions" in data:
            self.dimensions: Dimensions = self._get_value(Dimensions, "dimensions")
        else:
            self.dimensions: Dimensions = None
        if "weight" in data:
            self.weight: Weight = self._get_value(Weight, "weight")
        else:
            self.weight: Weight = None
        if "packedItems" in data:
            self.packedItems: _List[PackedItem] = [PackedItem(datum) for datum in data["packedItems"]]
        else:
            self.packedItems: _List[PackedItem] = []


class Decimal(str):
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation.  <br>**Pattern** : `^-?(0|([1-9]\\d*))(\\.\\d+)?([eE][+-]?\\d+)?$`.
    """


class VendorDirectFulfillmentShipping20211228Client(__BaseClient):
    def getShippingLabels(
        self,
        createdAfter: str,
        createdBefore: str,
        shipFromPartyId: str = None,
        limit: int = None,
        sortOrder: str = None,
        nextToken: str = None,
    ):
        """
                Returns a list of shipping labels created during the time frame that you specify. You define that time frame using the createdAfter and createdBefore parameters. You must use both of these parameters. The date range to search must not be more than 7 days.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/vendor/directFulfillment/shipping/2021-12-28/shippingLabels"
        params = {}
        if shipFromPartyId is not None:
            params["shipFromPartyId"] = shipFromPartyId
        if limit is not None:
            params["limit"] = limit
        if createdAfter is not None:
            params["createdAfter"] = createdAfter
        if createdBefore is not None:
            params["createdBefore"] = createdBefore
        if sortOrder is not None:
            params["sortOrder"] = sortOrder
        if nextToken is not None:
            params["nextToken"] = nextToken
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: ShippingLabelList,
            400: ErrorList,
            403: ErrorList,
            404: ErrorList,
            415: ErrorList,
            429: ErrorList,
            500: ErrorList,
            503: ErrorList,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def submitShippingLabelRequest(
        self,
        data: SubmitShippingLabelsRequest,
    ):
        """
                Creates a shipping label for a purchase order and returns a transactionId for reference.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/vendor/directFulfillment/shipping/2021-12-28/shippingLabels"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            202: TransactionReference,
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

    def getShippingLabel(
        self,
        purchaseOrderNumber: str,
    ):
        """
                Returns a shipping label for the purchaseOrderNumber that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/vendor/directFulfillment/shipping/2021-12-28/shippingLabels/{purchaseOrderNumber}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: ShippingLabel,
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
