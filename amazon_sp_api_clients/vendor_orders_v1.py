from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List


class GetPurchaseOrdersResponse:
    """
    The response schema for the getPurchaseOrders operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: OrderList = OrderList(data["payload"])
        else:
            self.payload: OrderList = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetPurchaseOrderResponse:
    """
    The response schema for the getPurchaseOrder operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: Order = Order(data["payload"])
        else:
            self.payload: Order = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class OrderList:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "pagination" in data:
            self.pagination: Pagination = Pagination(data["pagination"])
        else:
            self.pagination: Pagination = None
        if "orders" in data:
            self.orders: _List[Order] = [Order(datum) for datum in data["orders"]]
        else:
            self.orders: _List[Order] = []


class Pagination:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "nextToken" in data:
            self.nextToken: str = str(data["nextToken"])
        else:
            self.nextToken: str = None


class Order:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = str(data["purchaseOrderNumber"])
        else:
            self.purchaseOrderNumber: str = None
        if "purchaseOrderState" in data:
            self.purchaseOrderState: str = str(data["purchaseOrderState"])
        else:
            self.purchaseOrderState: str = None
        if "orderDetails" in data:
            self.orderDetails: OrderDetails = OrderDetails(data["orderDetails"])
        else:
            self.orderDetails: OrderDetails = None


class OrderDetails:
    """
    Details of an order.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "purchaseOrderDate" in data:
            self.purchaseOrderDate: str = str(data["purchaseOrderDate"])
        else:
            self.purchaseOrderDate: str = None
        if "purchaseOrderChangedDate" in data:
            self.purchaseOrderChangedDate: str = str(data["purchaseOrderChangedDate"])
        else:
            self.purchaseOrderChangedDate: str = None
        if "purchaseOrderStateChangedDate" in data:
            self.purchaseOrderStateChangedDate: str = str(data["purchaseOrderStateChangedDate"])
        else:
            self.purchaseOrderStateChangedDate: str = None
        if "purchaseOrderType" in data:
            self.purchaseOrderType: str = str(data["purchaseOrderType"])
        else:
            self.purchaseOrderType: str = None
        if "importDetails" in data:
            self.importDetails: ImportDetails = ImportDetails(data["importDetails"])
        else:
            self.importDetails: ImportDetails = None
        if "dealCode" in data:
            self.dealCode: str = str(data["dealCode"])
        else:
            self.dealCode: str = None
        if "paymentMethod" in data:
            self.paymentMethod: str = str(data["paymentMethod"])
        else:
            self.paymentMethod: str = None
        if "buyingParty" in data:
            self.buyingParty: PartyIdentification = PartyIdentification(data["buyingParty"])
        else:
            self.buyingParty: PartyIdentification = None
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = PartyIdentification(data["sellingParty"])
        else:
            self.sellingParty: PartyIdentification = None
        if "shipToParty" in data:
            self.shipToParty: PartyIdentification = PartyIdentification(data["shipToParty"])
        else:
            self.shipToParty: PartyIdentification = None
        if "billToParty" in data:
            self.billToParty: PartyIdentification = PartyIdentification(data["billToParty"])
        else:
            self.billToParty: PartyIdentification = None
        if "shipWindow" in data:
            self.shipWindow: DateTimeInterval = DateTimeInterval(data["shipWindow"])
        else:
            self.shipWindow: DateTimeInterval = None
        if "deliveryWindow" in data:
            self.deliveryWindow: DateTimeInterval = DateTimeInterval(data["deliveryWindow"])
        else:
            self.deliveryWindow: DateTimeInterval = None
        if "items" in data:
            self.items: _List[OrderItem] = [OrderItem(datum) for datum in data["items"]]
        else:
            self.items: _List[OrderItem] = []


class ImportDetails:
    """
    Import details for an import order.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "methodOfPayment" in data:
            self.methodOfPayment: str = str(data["methodOfPayment"])
        else:
            self.methodOfPayment: str = None
        if "internationalCommercialTerms" in data:
            self.internationalCommercialTerms: str = str(data["internationalCommercialTerms"])
        else:
            self.internationalCommercialTerms: str = None
        if "portOfDelivery" in data:
            self.portOfDelivery: str = str(data["portOfDelivery"])
        else:
            self.portOfDelivery: str = None
        if "importContainers" in data:
            self.importContainers: str = str(data["importContainers"])
        else:
            self.importContainers: str = None
        if "shippingInstructions" in data:
            self.shippingInstructions: str = str(data["shippingInstructions"])
        else:
            self.shippingInstructions: str = None


class PartyIdentification:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "partyId" in data:
            self.partyId: str = str(data["partyId"])
        else:
            self.partyId: str = None
        if "address" in data:
            self.address: Address = Address(data["address"])
        else:
            self.address: Address = None
        if "taxInfo" in data:
            self.taxInfo: TaxRegistrationDetails = TaxRegistrationDetails(data["taxInfo"])
        else:
            self.taxInfo: TaxRegistrationDetails = None


class TaxRegistrationDetails:
    """
    Tax registration details of the entity.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "taxRegistrationType" in data:
            self.taxRegistrationType: str = str(data["taxRegistrationType"])
        else:
            self.taxRegistrationType: str = None
        if "taxRegistrationNumber" in data:
            self.taxRegistrationNumber: str = str(data["taxRegistrationNumber"])
        else:
            self.taxRegistrationNumber: str = None


class Address:
    """
    Address of the party.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "name" in data:
            self.name: str = str(data["name"])
        else:
            self.name: str = None
        if "addressLine1" in data:
            self.addressLine1: str = str(data["addressLine1"])
        else:
            self.addressLine1: str = None
        if "addressLine2" in data:
            self.addressLine2: str = str(data["addressLine2"])
        else:
            self.addressLine2: str = None
        if "addressLine3" in data:
            self.addressLine3: str = str(data["addressLine3"])
        else:
            self.addressLine3: str = None
        if "city" in data:
            self.city: str = str(data["city"])
        else:
            self.city: str = None
        if "county" in data:
            self.county: str = str(data["county"])
        else:
            self.county: str = None
        if "district" in data:
            self.district: str = str(data["district"])
        else:
            self.district: str = None
        if "stateOrRegion" in data:
            self.stateOrRegion: str = str(data["stateOrRegion"])
        else:
            self.stateOrRegion: str = None
        if "postalCode" in data:
            self.postalCode: str = str(data["postalCode"])
        else:
            self.postalCode: str = None
        if "countryCode" in data:
            self.countryCode: str = str(data["countryCode"])
        else:
            self.countryCode: str = None
        if "phone" in data:
            self.phone: str = str(data["phone"])
        else:
            self.phone: str = None


class OrderItem:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "itemSequenceNumber" in data:
            self.itemSequenceNumber: str = str(data["itemSequenceNumber"])
        else:
            self.itemSequenceNumber: str = None
        if "amazonProductIdentifier" in data:
            self.amazonProductIdentifier: str = str(data["amazonProductIdentifier"])
        else:
            self.amazonProductIdentifier: str = None
        if "vendorProductIdentifier" in data:
            self.vendorProductIdentifier: str = str(data["vendorProductIdentifier"])
        else:
            self.vendorProductIdentifier: str = None
        if "orderedQuantity" in data:
            self.orderedQuantity: ItemQuantity = ItemQuantity(data["orderedQuantity"])
        else:
            self.orderedQuantity: ItemQuantity = None
        if "isBackOrderAllowed" in data:
            self.isBackOrderAllowed: bool = convert_bool(data["isBackOrderAllowed"])
        else:
            self.isBackOrderAllowed: bool = None
        if "netCost" in data:
            self.netCost: Money = Money(data["netCost"])
        else:
            self.netCost: Money = None
        if "listPrice" in data:
            self.listPrice: Money = Money(data["listPrice"])
        else:
            self.listPrice: Money = None


class Money:
    """
    An amount of money, including units in the form of currency.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "currencyCode" in data:
            self.currencyCode: str = str(data["currencyCode"])
        else:
            self.currencyCode: str = None
        if "amount" in data:
            self.amount: Decimal = Decimal(data["amount"])
        else:
            self.amount: Decimal = None


class SubmitAcknowledgementResponse:
    """
    The response schema for the submitAcknowledgement operation
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: TransactionId = TransactionId(data["payload"])
        else:
            self.payload: TransactionId = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class TransactionId:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "transactionId" in data:
            self.transactionId: str = str(data["transactionId"])
        else:
            self.transactionId: str = None


class SubmitAcknowledgementRequest:
    """
    The request schema for the submitAcknowledgment operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "acknowledgements" in data:
            self.acknowledgements: _List[OrderAcknowledgement] = [
                OrderAcknowledgement(datum) for datum in data["acknowledgements"]
            ]
        else:
            self.acknowledgements: _List[OrderAcknowledgement] = []


class OrderAcknowledgement:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = str(data["purchaseOrderNumber"])
        else:
            self.purchaseOrderNumber: str = None
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = PartyIdentification(data["sellingParty"])
        else:
            self.sellingParty: PartyIdentification = None
        if "acknowledgementDate" in data:
            self.acknowledgementDate: str = str(data["acknowledgementDate"])
        else:
            self.acknowledgementDate: str = None
        if "items" in data:
            self.items: _List[OrderAcknowledgementItem] = [OrderAcknowledgementItem(datum) for datum in data["items"]]
        else:
            self.items: _List[OrderAcknowledgementItem] = []


class OrderAcknowledgementItem:
    """
    Details of the item being acknowledged.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "itemSequenceNumber" in data:
            self.itemSequenceNumber: str = str(data["itemSequenceNumber"])
        else:
            self.itemSequenceNumber: str = None
        if "amazonProductIdentifier" in data:
            self.amazonProductIdentifier: str = str(data["amazonProductIdentifier"])
        else:
            self.amazonProductIdentifier: str = None
        if "vendorProductIdentifier" in data:
            self.vendorProductIdentifier: str = str(data["vendorProductIdentifier"])
        else:
            self.vendorProductIdentifier: str = None
        if "orderedQuantity" in data:
            self.orderedQuantity: ItemQuantity = ItemQuantity(data["orderedQuantity"])
        else:
            self.orderedQuantity: ItemQuantity = None
        if "netCost" in data:
            self.netCost: Money = Money(data["netCost"])
        else:
            self.netCost: Money = None
        if "listPrice" in data:
            self.listPrice: Money = Money(data["listPrice"])
        else:
            self.listPrice: Money = None
        if "discountMultiplier" in data:
            self.discountMultiplier: str = str(data["discountMultiplier"])
        else:
            self.discountMultiplier: str = None
        if "itemAcknowledgements" in data:
            self.itemAcknowledgements: _List[OrderItemAcknowledgement] = [
                OrderItemAcknowledgement(datum) for datum in data["itemAcknowledgements"]
            ]
        else:
            self.itemAcknowledgements: _List[OrderItemAcknowledgement] = []


class OrderItemAcknowledgement:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "acknowledgementCode" in data:
            self.acknowledgementCode: str = str(data["acknowledgementCode"])
        else:
            self.acknowledgementCode: str = None
        if "acknowledgedQuantity" in data:
            self.acknowledgedQuantity: ItemQuantity = ItemQuantity(data["acknowledgedQuantity"])
        else:
            self.acknowledgedQuantity: ItemQuantity = None
        if "scheduledShipDate" in data:
            self.scheduledShipDate: str = str(data["scheduledShipDate"])
        else:
            self.scheduledShipDate: str = None
        if "scheduledDeliveryDate" in data:
            self.scheduledDeliveryDate: str = str(data["scheduledDeliveryDate"])
        else:
            self.scheduledDeliveryDate: str = None
        if "rejectionReason" in data:
            self.rejectionReason: str = str(data["rejectionReason"])
        else:
            self.rejectionReason: str = None


class ItemQuantity:
    """
    Details of quantity ordered.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "amount" in data:
            self.amount: int = int(data["amount"])
        else:
            self.amount: int = None
        if "unitOfMeasure" in data:
            self.unitOfMeasure: str = str(data["unitOfMeasure"])
        else:
            self.unitOfMeasure: str = None
        if "unitSize" in data:
            self.unitSize: int = int(data["unitSize"])
        else:
            self.unitSize: int = None


class GetPurchaseOrdersStatusResponse:
    """
    The response schema for the getPurchaseOrdersStatus operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: OrderListStatus = OrderListStatus(data["payload"])
        else:
            self.payload: OrderListStatus = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class OrderListStatus:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "pagination" in data:
            self.pagination: Pagination = Pagination(data["pagination"])
        else:
            self.pagination: Pagination = None
        if "ordersStatus" in data:
            self.ordersStatus: _List[OrderStatus] = [OrderStatus(datum) for datum in data["ordersStatus"]]
        else:
            self.ordersStatus: _List[OrderStatus] = []


class OrderStatus:
    """
    Current status of a purchase order.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = str(data["purchaseOrderNumber"])
        else:
            self.purchaseOrderNumber: str = None
        if "purchaseOrderStatus" in data:
            self.purchaseOrderStatus: str = str(data["purchaseOrderStatus"])
        else:
            self.purchaseOrderStatus: str = None
        if "purchaseOrderDate" in data:
            self.purchaseOrderDate: str = str(data["purchaseOrderDate"])
        else:
            self.purchaseOrderDate: str = None
        if "lastUpdatedDate" in data:
            self.lastUpdatedDate: str = str(data["lastUpdatedDate"])
        else:
            self.lastUpdatedDate: str = None
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = PartyIdentification(data["sellingParty"])
        else:
            self.sellingParty: PartyIdentification = None
        if "shipToParty" in data:
            self.shipToParty: PartyIdentification = PartyIdentification(data["shipToParty"])
        else:
            self.shipToParty: PartyIdentification = None
        if "itemStatus" in data:
            self.itemStatus: ItemStatus = ItemStatus(data["itemStatus"])
        else:
            self.itemStatus: ItemStatus = None


class OrderItemStatus:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "itemSequenceNumber" in data:
            self.itemSequenceNumber: str = str(data["itemSequenceNumber"])
        else:
            self.itemSequenceNumber: str = None
        if "buyerProductIdentifier" in data:
            self.buyerProductIdentifier: str = str(data["buyerProductIdentifier"])
        else:
            self.buyerProductIdentifier: str = None
        if "vendorProductIdentifier" in data:
            self.vendorProductIdentifier: str = str(data["vendorProductIdentifier"])
        else:
            self.vendorProductIdentifier: str = None
        if "netCost" in data:
            self.netCost: Money = Money(data["netCost"])
        else:
            self.netCost: Money = None
        if "listPrice" in data:
            self.listPrice: Money = Money(data["listPrice"])
        else:
            self.listPrice: Money = None
        if "orderedQuantity" in data:
            self.orderedQuantity: dict = dict(data["orderedQuantity"])
        else:
            self.orderedQuantity: dict = None
        if "acknowledgementStatus" in data:
            self.acknowledgementStatus: dict = dict(data["acknowledgementStatus"])
        else:
            self.acknowledgementStatus: dict = None


class OrderedQuantityDetails:
    """
    Details of item quantity ordered
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "updatedDate" in data:
            self.updatedDate: str = str(data["updatedDate"])
        else:
            self.updatedDate: str = None
        if "orderedQuantity" in data:
            self.orderedQuantity: ItemQuantity = ItemQuantity(data["orderedQuantity"])
        else:
            self.orderedQuantity: ItemQuantity = None
        if "cancelledQuantity" in data:
            self.cancelledQuantity: ItemQuantity = ItemQuantity(data["cancelledQuantity"])
        else:
            self.cancelledQuantity: ItemQuantity = None


class AcknowledgementStatusDetails:
    """
    Details of item quantity ordered
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "acknowledgementDate" in data:
            self.acknowledgementDate: str = str(data["acknowledgementDate"])
        else:
            self.acknowledgementDate: str = None
        if "acceptedQuantity" in data:
            self.acceptedQuantity: ItemQuantity = ItemQuantity(data["acceptedQuantity"])
        else:
            self.acceptedQuantity: ItemQuantity = None
        if "rejectedQuantity" in data:
            self.rejectedQuantity: ItemQuantity = ItemQuantity(data["rejectedQuantity"])
        else:
            self.rejectedQuantity: ItemQuantity = None


class Error:
    """
    Error response returned when the request is unsuccessful.
    """

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
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/vendor/orders/v1/purchaseOrders".format()
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
        response = self.request(url, method="GET", params=params)
        return {
            200: GetPurchaseOrdersResponse,
            400: GetPurchaseOrdersResponse,
            403: GetPurchaseOrdersResponse,
            404: GetPurchaseOrdersResponse,
            415: GetPurchaseOrdersResponse,
            429: GetPurchaseOrdersResponse,
            500: GetPurchaseOrdersResponse,
            503: GetPurchaseOrdersResponse,
        }[response.status_code](self._get_response_json(response))

    def getPurchaseOrder(
        self,
        purchaseOrderNumber: str,
    ):
        """
                Returns a purchase order based on the purchaseOrderNumber value that you specify.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/vendor/orders/v1/purchaseOrders/{purchaseOrderNumber}".format(
            purchaseOrderNumber=purchaseOrderNumber,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetPurchaseOrderResponse,
            400: GetPurchaseOrderResponse,
            401: GetPurchaseOrderResponse,
            403: GetPurchaseOrderResponse,
            404: GetPurchaseOrderResponse,
            415: GetPurchaseOrderResponse,
            429: GetPurchaseOrderResponse,
            500: GetPurchaseOrderResponse,
            503: GetPurchaseOrderResponse,
        }[response.status_code](self._get_response_json(response))

    def submitAcknowledgement(
        self,
        data: SubmitAcknowledgementRequest,
    ):
        """
                Submits acknowledgements for one or more purchase orders.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/vendor/orders/v1/acknowledgements".format()
        params = {}
        response = self.request(url, method="POST", data=params)
        return {
            202: SubmitAcknowledgementResponse,
            400: SubmitAcknowledgementResponse,
            403: SubmitAcknowledgementResponse,
            404: SubmitAcknowledgementResponse,
            413: SubmitAcknowledgementResponse,
            415: SubmitAcknowledgementResponse,
            429: SubmitAcknowledgementResponse,
            500: SubmitAcknowledgementResponse,
            503: SubmitAcknowledgementResponse,
        }[response.status_code](self._get_response_json(response))

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
        orderingVendorCode: str = None,
        shipToPartyId: str = None,
    ):
        """
                Returns purchase order statuses based on the filters that you specify. Date range to search must not be more than 7 days. You can return a list of purchase order statuses using the available filters, or a single purchase order status by providing the purchase order number.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/vendor/orders/v1/purchaseOrdersStatus".format()
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
        if orderingVendorCode is not None:
            params["orderingVendorCode"] = orderingVendorCode
        if shipToPartyId is not None:
            params["shipToPartyId"] = shipToPartyId
        response = self.request(url, method="GET", params=params)
        return {
            200: GetPurchaseOrdersStatusResponse,
            400: GetPurchaseOrdersStatusResponse,
            403: GetPurchaseOrdersStatusResponse,
            404: GetPurchaseOrdersStatusResponse,
            415: GetPurchaseOrdersStatusResponse,
            429: GetPurchaseOrdersStatusResponse,
            500: GetPurchaseOrdersStatusResponse,
            503: GetPurchaseOrdersStatusResponse,
        }[response.status_code](self._get_response_json(response))
