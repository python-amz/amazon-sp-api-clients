from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class GetPurchaseOrdersResponse(__BaseDictObject):
    """
    The response schema for the getPurchaseOrders operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: OrderList = self._get_value(OrderList, "payload")
        else:
            self.payload: OrderList = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class GetPurchaseOrderResponse(__BaseDictObject):
    """
    The response schema for the getPurchaseOrder operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: Order = self._get_value(Order, "payload")
        else:
            self.payload: Order = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class OrderList(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "pagination" in data:
            self.pagination: Pagination = self._get_value(Pagination, "pagination")
        else:
            self.pagination: Pagination = None
        if "orders" in data:
            self.orders: _List[Order] = [Order(datum) for datum in data["orders"]]
        else:
            self.orders: _List[Order] = []


class Pagination(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "nextToken" in data:
            self.nextToken: str = self._get_value(str, "nextToken")
        else:
            self.nextToken: str = None


class Order(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = self._get_value(str, "purchaseOrderNumber")
        else:
            self.purchaseOrderNumber: str = None
        if "purchaseOrderState" in data:
            self.purchaseOrderState: str = self._get_value(str, "purchaseOrderState")
        else:
            self.purchaseOrderState: str = None
        if "orderDetails" in data:
            self.orderDetails: OrderDetails = self._get_value(OrderDetails, "orderDetails")
        else:
            self.orderDetails: OrderDetails = None


class OrderDetails(__BaseDictObject):
    """
    Details of an order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "purchaseOrderDate" in data:
            self.purchaseOrderDate: str = self._get_value(str, "purchaseOrderDate")
        else:
            self.purchaseOrderDate: str = None
        if "purchaseOrderChangedDate" in data:
            self.purchaseOrderChangedDate: str = self._get_value(str, "purchaseOrderChangedDate")
        else:
            self.purchaseOrderChangedDate: str = None
        if "purchaseOrderStateChangedDate" in data:
            self.purchaseOrderStateChangedDate: str = self._get_value(str, "purchaseOrderStateChangedDate")
        else:
            self.purchaseOrderStateChangedDate: str = None
        if "purchaseOrderType" in data:
            self.purchaseOrderType: str = self._get_value(str, "purchaseOrderType")
        else:
            self.purchaseOrderType: str = None
        if "importDetails" in data:
            self.importDetails: ImportDetails = self._get_value(ImportDetails, "importDetails")
        else:
            self.importDetails: ImportDetails = None
        if "dealCode" in data:
            self.dealCode: str = self._get_value(str, "dealCode")
        else:
            self.dealCode: str = None
        if "paymentMethod" in data:
            self.paymentMethod: str = self._get_value(str, "paymentMethod")
        else:
            self.paymentMethod: str = None
        if "buyingParty" in data:
            self.buyingParty: PartyIdentification = self._get_value(PartyIdentification, "buyingParty")
        else:
            self.buyingParty: PartyIdentification = None
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = self._get_value(PartyIdentification, "sellingParty")
        else:
            self.sellingParty: PartyIdentification = None
        if "shipToParty" in data:
            self.shipToParty: PartyIdentification = self._get_value(PartyIdentification, "shipToParty")
        else:
            self.shipToParty: PartyIdentification = None
        if "billToParty" in data:
            self.billToParty: PartyIdentification = self._get_value(PartyIdentification, "billToParty")
        else:
            self.billToParty: PartyIdentification = None
        if "shipWindow" in data:
            self.shipWindow: DateTimeInterval = self._get_value(DateTimeInterval, "shipWindow")
        else:
            self.shipWindow: DateTimeInterval = None
        if "deliveryWindow" in data:
            self.deliveryWindow: DateTimeInterval = self._get_value(DateTimeInterval, "deliveryWindow")
        else:
            self.deliveryWindow: DateTimeInterval = None
        if "items" in data:
            self.items: _List[OrderItem] = [OrderItem(datum) for datum in data["items"]]
        else:
            self.items: _List[OrderItem] = []


class ImportDetails(__BaseDictObject):
    """
    Import details for an import order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "methodOfPayment" in data:
            self.methodOfPayment: str = self._get_value(str, "methodOfPayment")
        else:
            self.methodOfPayment: str = None
        if "internationalCommercialTerms" in data:
            self.internationalCommercialTerms: str = self._get_value(str, "internationalCommercialTerms")
        else:
            self.internationalCommercialTerms: str = None
        if "portOfDelivery" in data:
            self.portOfDelivery: str = self._get_value(str, "portOfDelivery")
        else:
            self.portOfDelivery: str = None
        if "importContainers" in data:
            self.importContainers: str = self._get_value(str, "importContainers")
        else:
            self.importContainers: str = None
        if "shippingInstructions" in data:
            self.shippingInstructions: str = self._get_value(str, "shippingInstructions")
        else:
            self.shippingInstructions: str = None


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
        if "taxInfo" in data:
            self.taxInfo: TaxRegistrationDetails = self._get_value(TaxRegistrationDetails, "taxInfo")
        else:
            self.taxInfo: TaxRegistrationDetails = None


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


class OrderItem(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "itemSequenceNumber" in data:
            self.itemSequenceNumber: str = self._get_value(str, "itemSequenceNumber")
        else:
            self.itemSequenceNumber: str = None
        if "amazonProductIdentifier" in data:
            self.amazonProductIdentifier: str = self._get_value(str, "amazonProductIdentifier")
        else:
            self.amazonProductIdentifier: str = None
        if "vendorProductIdentifier" in data:
            self.vendorProductIdentifier: str = self._get_value(str, "vendorProductIdentifier")
        else:
            self.vendorProductIdentifier: str = None
        if "orderedQuantity" in data:
            self.orderedQuantity: ItemQuantity = self._get_value(ItemQuantity, "orderedQuantity")
        else:
            self.orderedQuantity: ItemQuantity = None
        if "isBackOrderAllowed" in data:
            self.isBackOrderAllowed: bool = self._get_value(convert_bool, "isBackOrderAllowed")
        else:
            self.isBackOrderAllowed: bool = None
        if "netCost" in data:
            self.netCost: Money = self._get_value(Money, "netCost")
        else:
            self.netCost: Money = None
        if "listPrice" in data:
            self.listPrice: Money = self._get_value(Money, "listPrice")
        else:
            self.listPrice: Money = None


class Money(__BaseDictObject):
    """
    An amount of money, including units in the form of currency.
    """

    def __init__(self, data):
        super().__init__(data)
        if "currencyCode" in data:
            self.currencyCode: str = self._get_value(str, "currencyCode")
        else:
            self.currencyCode: str = None
        if "amount" in data:
            self.amount: Decimal = self._get_value(Decimal, "amount")
        else:
            self.amount: Decimal = None


class SubmitAcknowledgementResponse(__BaseDictObject):
    """
    The response schema for the submitAcknowledgement operation
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: TransactionId = self._get_value(TransactionId, "payload")
        else:
            self.payload: TransactionId = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class TransactionId(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "transactionId" in data:
            self.transactionId: str = self._get_value(str, "transactionId")
        else:
            self.transactionId: str = None


class SubmitAcknowledgementRequest(__BaseDictObject):
    """
    The request schema for the submitAcknowledgment operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "acknowledgements" in data:
            self.acknowledgements: _List[OrderAcknowledgement] = [
                OrderAcknowledgement(datum) for datum in data["acknowledgements"]
            ]
        else:
            self.acknowledgements: _List[OrderAcknowledgement] = []


class OrderAcknowledgement(__BaseDictObject):
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
        if "acknowledgementDate" in data:
            self.acknowledgementDate: str = self._get_value(str, "acknowledgementDate")
        else:
            self.acknowledgementDate: str = None
        if "items" in data:
            self.items: _List[OrderAcknowledgementItem] = [OrderAcknowledgementItem(datum) for datum in data["items"]]
        else:
            self.items: _List[OrderAcknowledgementItem] = []


class OrderAcknowledgementItem(__BaseDictObject):
    """
    Details of the item being acknowledged.
    """

    def __init__(self, data):
        super().__init__(data)
        if "itemSequenceNumber" in data:
            self.itemSequenceNumber: str = self._get_value(str, "itemSequenceNumber")
        else:
            self.itemSequenceNumber: str = None
        if "amazonProductIdentifier" in data:
            self.amazonProductIdentifier: str = self._get_value(str, "amazonProductIdentifier")
        else:
            self.amazonProductIdentifier: str = None
        if "vendorProductIdentifier" in data:
            self.vendorProductIdentifier: str = self._get_value(str, "vendorProductIdentifier")
        else:
            self.vendorProductIdentifier: str = None
        if "orderedQuantity" in data:
            self.orderedQuantity: ItemQuantity = self._get_value(ItemQuantity, "orderedQuantity")
        else:
            self.orderedQuantity: ItemQuantity = None
        if "netCost" in data:
            self.netCost: Money = self._get_value(Money, "netCost")
        else:
            self.netCost: Money = None
        if "listPrice" in data:
            self.listPrice: Money = self._get_value(Money, "listPrice")
        else:
            self.listPrice: Money = None
        if "discountMultiplier" in data:
            self.discountMultiplier: str = self._get_value(str, "discountMultiplier")
        else:
            self.discountMultiplier: str = None
        if "itemAcknowledgements" in data:
            self.itemAcknowledgements: _List[OrderItemAcknowledgement] = [
                OrderItemAcknowledgement(datum) for datum in data["itemAcknowledgements"]
            ]
        else:
            self.itemAcknowledgements: _List[OrderItemAcknowledgement] = []


class OrderItemAcknowledgement(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "acknowledgementCode" in data:
            self.acknowledgementCode: str = self._get_value(str, "acknowledgementCode")
        else:
            self.acknowledgementCode: str = None
        if "acknowledgedQuantity" in data:
            self.acknowledgedQuantity: ItemQuantity = self._get_value(ItemQuantity, "acknowledgedQuantity")
        else:
            self.acknowledgedQuantity: ItemQuantity = None
        if "scheduledShipDate" in data:
            self.scheduledShipDate: str = self._get_value(str, "scheduledShipDate")
        else:
            self.scheduledShipDate: str = None
        if "scheduledDeliveryDate" in data:
            self.scheduledDeliveryDate: str = self._get_value(str, "scheduledDeliveryDate")
        else:
            self.scheduledDeliveryDate: str = None
        if "rejectionReason" in data:
            self.rejectionReason: str = self._get_value(str, "rejectionReason")
        else:
            self.rejectionReason: str = None


class ItemQuantity(__BaseDictObject):
    """
    Details of quantity ordered.
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
        if "unitSize" in data:
            self.unitSize: int = self._get_value(int, "unitSize")
        else:
            self.unitSize: int = None


class GetPurchaseOrdersStatusResponse(__BaseDictObject):
    """
    The response schema for the getPurchaseOrdersStatus operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "payload" in data:
            self.payload: OrderListStatus = self._get_value(OrderListStatus, "payload")
        else:
            self.payload: OrderListStatus = None
        if "errors" in data:
            self.errors: ErrorList = self._get_value(ErrorList, "errors")
        else:
            self.errors: ErrorList = None


class OrderListStatus(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "pagination" in data:
            self.pagination: Pagination = self._get_value(Pagination, "pagination")
        else:
            self.pagination: Pagination = None
        if "ordersStatus" in data:
            self.ordersStatus: _List[OrderStatus] = [OrderStatus(datum) for datum in data["ordersStatus"]]
        else:
            self.ordersStatus: _List[OrderStatus] = []


class OrderStatus(__BaseDictObject):
    """
    Current status of a purchase order.
    """

    def __init__(self, data):
        super().__init__(data)
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = self._get_value(str, "purchaseOrderNumber")
        else:
            self.purchaseOrderNumber: str = None
        if "purchaseOrderStatus" in data:
            self.purchaseOrderStatus: str = self._get_value(str, "purchaseOrderStatus")
        else:
            self.purchaseOrderStatus: str = None
        if "purchaseOrderDate" in data:
            self.purchaseOrderDate: str = self._get_value(str, "purchaseOrderDate")
        else:
            self.purchaseOrderDate: str = None
        if "lastUpdatedDate" in data:
            self.lastUpdatedDate: str = self._get_value(str, "lastUpdatedDate")
        else:
            self.lastUpdatedDate: str = None
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = self._get_value(PartyIdentification, "sellingParty")
        else:
            self.sellingParty: PartyIdentification = None
        if "shipToParty" in data:
            self.shipToParty: PartyIdentification = self._get_value(PartyIdentification, "shipToParty")
        else:
            self.shipToParty: PartyIdentification = None
        if "itemStatus" in data:
            self.itemStatus: ItemStatus = self._get_value(ItemStatus, "itemStatus")
        else:
            self.itemStatus: ItemStatus = None


class OrderItemStatus(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "itemSequenceNumber" in data:
            self.itemSequenceNumber: str = self._get_value(str, "itemSequenceNumber")
        else:
            self.itemSequenceNumber: str = None
        if "buyerProductIdentifier" in data:
            self.buyerProductIdentifier: str = self._get_value(str, "buyerProductIdentifier")
        else:
            self.buyerProductIdentifier: str = None
        if "vendorProductIdentifier" in data:
            self.vendorProductIdentifier: str = self._get_value(str, "vendorProductIdentifier")
        else:
            self.vendorProductIdentifier: str = None
        if "netCost" in data:
            self.netCost: Money = self._get_value(Money, "netCost")
        else:
            self.netCost: Money = None
        if "listPrice" in data:
            self.listPrice: Money = self._get_value(Money, "listPrice")
        else:
            self.listPrice: Money = None
        if "orderedQuantity" in data:
            self.orderedQuantity: dict = self._get_value(dict, "orderedQuantity")
        else:
            self.orderedQuantity: dict = None
        if "acknowledgementStatus" in data:
            self.acknowledgementStatus: dict = self._get_value(dict, "acknowledgementStatus")
        else:
            self.acknowledgementStatus: dict = None
        if "receivingStatus" in data:
            self.receivingStatus: dict = self._get_value(dict, "receivingStatus")
        else:
            self.receivingStatus: dict = None


class OrderedQuantityDetails(__BaseDictObject):
    """
    Details of item quantity ordered
    """

    def __init__(self, data):
        super().__init__(data)
        if "updatedDate" in data:
            self.updatedDate: str = self._get_value(str, "updatedDate")
        else:
            self.updatedDate: str = None
        if "orderedQuantity" in data:
            self.orderedQuantity: ItemQuantity = self._get_value(ItemQuantity, "orderedQuantity")
        else:
            self.orderedQuantity: ItemQuantity = None
        if "cancelledQuantity" in data:
            self.cancelledQuantity: ItemQuantity = self._get_value(ItemQuantity, "cancelledQuantity")
        else:
            self.cancelledQuantity: ItemQuantity = None


class AcknowledgementStatusDetails(__BaseDictObject):
    """
    Details of item quantity ordered
    """

    def __init__(self, data):
        super().__init__(data)
        if "acknowledgementDate" in data:
            self.acknowledgementDate: str = self._get_value(str, "acknowledgementDate")
        else:
            self.acknowledgementDate: str = None
        if "acceptedQuantity" in data:
            self.acceptedQuantity: ItemQuantity = self._get_value(ItemQuantity, "acceptedQuantity")
        else:
            self.acceptedQuantity: ItemQuantity = None
        if "rejectedQuantity" in data:
            self.rejectedQuantity: ItemQuantity = self._get_value(ItemQuantity, "rejectedQuantity")
        else:
            self.rejectedQuantity: ItemQuantity = None


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


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class ItemStatus(list, _List["OrderItemStatus"]):
    """
    Detailed description of items order status.
    """

    def __init__(self, data):
        super().__init__([OrderItemStatus(datum) for datum in data])
        self.data = data


class DateTimeInterval(str):
    """
    Defines a date time interval according to ISO8601. Interval is separated by double hyphen (--).
    """


class Decimal(str):
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\d*))(\.\d+)?([eE][+-]?\d+)?$`.
    """


class VendorOrdersV1Client(__BaseClient):
    def getPurchaseOrders(
        self,
        limit: int = None,
        createdAfter: str = None,
        createdBefore: str = None,
        sortOrder: str = None,
        nextToken: str = None,
        includeDetails: str = None,
        changedAfter: str = None,
        changedBefore: str = None,
        poItemState: str = None,
        isPOChanged: str = None,
        purchaseOrderState: str = None,
        orderingVendorCode: str = None,
    ):
        """
                Returns a list of purchase orders created or changed during the time frame that you specify. You define the time frame using the createdAfter, createdBefore, changedAfter and changedBefore parameters. The date range to search must not be more than 7 days. You can choose to get only the purchase order numbers by setting includeDetails to false. You can then use the getPurchaseOrder operation to receive details for a specific purchase order.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/vendor/orders/v1/purchaseOrders"
        params = {}
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
        if includeDetails is not None:
            params["includeDetails"] = includeDetails
        if changedAfter is not None:
            params["changedAfter"] = changedAfter
        if changedBefore is not None:
            params["changedBefore"] = changedBefore
        if poItemState is not None:
            params["poItemState"] = poItemState
        if isPOChanged is not None:
            params["isPOChanged"] = isPOChanged
        if purchaseOrderState is not None:
            params["purchaseOrderState"] = purchaseOrderState
        if orderingVendorCode is not None:
            params["orderingVendorCode"] = orderingVendorCode
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetPurchaseOrdersResponse,
            400: GetPurchaseOrdersResponse,
            403: GetPurchaseOrdersResponse,
            404: GetPurchaseOrdersResponse,
            415: GetPurchaseOrdersResponse,
            429: GetPurchaseOrdersResponse,
            500: GetPurchaseOrdersResponse,
            503: GetPurchaseOrdersResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getPurchaseOrder(
        self,
        purchaseOrderNumber: str,
    ):
        """
                Returns a purchase order based on the purchaseOrderNumber value that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/vendor/orders/v1/purchaseOrders/{purchaseOrderNumber}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetPurchaseOrderResponse,
            400: GetPurchaseOrderResponse,
            401: GetPurchaseOrderResponse,
            403: GetPurchaseOrderResponse,
            404: GetPurchaseOrderResponse,
            415: GetPurchaseOrderResponse,
            429: GetPurchaseOrderResponse,
            500: GetPurchaseOrderResponse,
            503: GetPurchaseOrderResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def submitAcknowledgement(
        self,
        data: SubmitAcknowledgementRequest,
    ):
        """
                Submits acknowledgements for one or more purchase orders.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/vendor/orders/v1/acknowledgements"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        response_type = {
            202: SubmitAcknowledgementResponse,
            400: SubmitAcknowledgementResponse,
            403: SubmitAcknowledgementResponse,
            404: SubmitAcknowledgementResponse,
            413: SubmitAcknowledgementResponse,
            415: SubmitAcknowledgementResponse,
            429: SubmitAcknowledgementResponse,
            500: SubmitAcknowledgementResponse,
            503: SubmitAcknowledgementResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

    def getPurchaseOrdersStatus(
        self,
        limit: int = None,
        sortOrder: str = None,
        nextToken: str = None,
        createdAfter: str = None,
        createdBefore: str = None,
        updatedAfter: str = None,
        updatedBefore: str = None,
        purchaseOrderNumber: str = None,
        purchaseOrderStatus: str = None,
        itemConfirmationStatus: str = None,
        itemReceiveStatus: str = None,
        orderingVendorCode: str = None,
        shipToPartyId: str = None,
    ):
        """
                Returns purchase order statuses based on the filters that you specify. Date range to search must not be more than 7 days. You can return a list of purchase order statuses using the available filters, or a single purchase order status by providing the purchase order number.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        url = f"/vendor/orders/v1/purchaseOrdersStatus"
        params = {}
        if limit is not None:
            params["limit"] = limit
        if sortOrder is not None:
            params["sortOrder"] = sortOrder
        if nextToken is not None:
            params["nextToken"] = nextToken
        if createdAfter is not None:
            params["createdAfter"] = createdAfter
        if createdBefore is not None:
            params["createdBefore"] = createdBefore
        if updatedAfter is not None:
            params["updatedAfter"] = updatedAfter
        if updatedBefore is not None:
            params["updatedBefore"] = updatedBefore
        if purchaseOrderNumber is not None:
            params["purchaseOrderNumber"] = purchaseOrderNumber
        if purchaseOrderStatus is not None:
            params["purchaseOrderStatus"] = purchaseOrderStatus
        if itemConfirmationStatus is not None:
            params["itemConfirmationStatus"] = itemConfirmationStatus
        if itemReceiveStatus is not None:
            params["itemReceiveStatus"] = itemReceiveStatus
        if orderingVendorCode is not None:
            params["orderingVendorCode"] = orderingVendorCode
        if shipToPartyId is not None:
            params["shipToPartyId"] = shipToPartyId
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetPurchaseOrdersStatusResponse,
            400: GetPurchaseOrdersStatusResponse,
            403: GetPurchaseOrdersStatusResponse,
            404: GetPurchaseOrdersStatusResponse,
            415: GetPurchaseOrdersStatusResponse,
            429: GetPurchaseOrdersStatusResponse,
            500: GetPurchaseOrdersStatusResponse,
            503: GetPurchaseOrdersStatusResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))
