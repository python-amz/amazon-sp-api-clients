from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List


class GetOrdersResponse:
    """
    The response schema for the getOrders operation.
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


class GetOrderResponse:
    """
    The response schema for the getOrder operation.
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
        if "customerOrderNumber" in data:
            self.customerOrderNumber: str = str(data["customerOrderNumber"])
        else:
            self.customerOrderNumber: str = None
        if "orderDate" in data:
            self.orderDate: str = str(data["orderDate"])
        else:
            self.orderDate: str = None
        if "orderStatus" in data:
            self.orderStatus: str = str(data["orderStatus"])
        else:
            self.orderStatus: str = None
        if "shipmentDetails" in data:
            self.shipmentDetails: ShipmentDetails = ShipmentDetails(data["shipmentDetails"])
        else:
            self.shipmentDetails: ShipmentDetails = None
        if "taxTotal" in data:
            self.taxTotal: dict = dict(data["taxTotal"])
        else:
            self.taxTotal: dict = None
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = PartyIdentification(data["sellingParty"])
        else:
            self.sellingParty: PartyIdentification = None
        if "shipFromParty" in data:
            self.shipFromParty: PartyIdentification = PartyIdentification(data["shipFromParty"])
        else:
            self.shipFromParty: PartyIdentification = None
        if "shipToParty" in data:
            self.shipToParty: Address = Address(data["shipToParty"])
        else:
            self.shipToParty: Address = None
        if "billToParty" in data:
            self.billToParty: PartyIdentification = PartyIdentification(data["billToParty"])
        else:
            self.billToParty: PartyIdentification = None
        if "items" in data:
            self.items: _List[OrderItem] = [OrderItem(datum) for datum in data["items"]]
        else:
            self.items: _List[OrderItem] = []


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
        if "taxRegistrationAddress" in data:
            self.taxRegistrationAddress: Address = Address(data["taxRegistrationAddress"])
        else:
            self.taxRegistrationAddress: Address = None
        if "taxRegistrationMessages" in data:
            self.taxRegistrationMessages: str = str(data["taxRegistrationMessages"])
        else:
            self.taxRegistrationMessages: str = None


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
        if "attention" in data:
            self.attention: str = str(data["attention"])
        else:
            self.attention: str = None
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
        if "buyerProductIdentifier" in data:
            self.buyerProductIdentifier: str = str(data["buyerProductIdentifier"])
        else:
            self.buyerProductIdentifier: str = None
        if "vendorProductIdentifier" in data:
            self.vendorProductIdentifier: str = str(data["vendorProductIdentifier"])
        else:
            self.vendorProductIdentifier: str = None
        if "title" in data:
            self.title: str = str(data["title"])
        else:
            self.title: str = None
        if "orderedQuantity" in data:
            self.orderedQuantity: ItemQuantity = ItemQuantity(data["orderedQuantity"])
        else:
            self.orderedQuantity: ItemQuantity = None
        if "scheduledDeliveryShipment" in data:
            self.scheduledDeliveryShipment: ScheduledDeliveryShipment = ScheduledDeliveryShipment(
                data["scheduledDeliveryShipment"]
            )
        else:
            self.scheduledDeliveryShipment: ScheduledDeliveryShipment = None
        if "giftDetails" in data:
            self.giftDetails: GiftDetails = GiftDetails(data["giftDetails"])
        else:
            self.giftDetails: GiftDetails = None
        if "netPrice" in data:
            self.netPrice: Money = Money(data["netPrice"])
        else:
            self.netPrice: Money = None
        if "taxDetails" in data:
            self.taxDetails: dict = dict(data["taxDetails"])
        else:
            self.taxDetails: dict = None
        if "totalPrice" in data:
            self.totalPrice: Money = Money(data["totalPrice"])
        else:
            self.totalPrice: Money = None


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
    The response schema for the submitAcknowledgement operation.
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
    The request schema for the submitAcknowledgement operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "orderAcknowledgements" in data:
            self.orderAcknowledgements: _List[OrderAcknowledgementItem] = [
                OrderAcknowledgementItem(datum) for datum in data["orderAcknowledgements"]
            ]
        else:
            self.orderAcknowledgements: _List[OrderAcknowledgementItem] = []


class OrderAcknowledgementItem:
    """
    Details of an individual order being acknowledged.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = str(data["purchaseOrderNumber"])
        else:
            self.purchaseOrderNumber: str = None
        if "vendorOrderNumber" in data:
            self.vendorOrderNumber: str = str(data["vendorOrderNumber"])
        else:
            self.vendorOrderNumber: str = None
        if "acknowledgementDate" in data:
            self.acknowledgementDate: str = str(data["acknowledgementDate"])
        else:
            self.acknowledgementDate: str = None
        if "acknowledgementStatus" in data:
            self.acknowledgementStatus: AcknowledgementStatus = AcknowledgementStatus(data["acknowledgementStatus"])
        else:
            self.acknowledgementStatus: AcknowledgementStatus = None
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = PartyIdentification(data["sellingParty"])
        else:
            self.sellingParty: PartyIdentification = None
        if "shipFromParty" in data:
            self.shipFromParty: PartyIdentification = PartyIdentification(data["shipFromParty"])
        else:
            self.shipFromParty: PartyIdentification = None
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
        if "acknowledgedQuantity" in data:
            self.acknowledgedQuantity: ItemQuantity = ItemQuantity(data["acknowledgedQuantity"])
        else:
            self.acknowledgedQuantity: ItemQuantity = None


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


class TaxDetails:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "taxRate" in data:
            self.taxRate: Decimal = Decimal(data["taxRate"])
        else:
            self.taxRate: Decimal = None
        if "taxAmount" in data:
            self.taxAmount: Money = Money(data["taxAmount"])
        else:
            self.taxAmount: Money = None
        if "taxableAmount" in data:
            self.taxableAmount: Money = Money(data["taxableAmount"])
        else:
            self.taxableAmount: Money = None
        if "type" in data:
            self.type: str = str(data["type"])
        else:
            self.type: str = None


class AcknowledgementStatus:
    """
    Status of acknowledgement.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "code" in data:
            self.code: str = str(data["code"])
        else:
            self.code: str = None
        if "description" in data:
            self.description: str = str(data["description"])
        else:
            self.description: str = None


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


class ShipmentDetails:
    """
    Shipment details required for the shipment.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "isPriorityShipment" in data:
            self.isPriorityShipment: bool = convert_bool(data["isPriorityShipment"])
        else:
            self.isPriorityShipment: bool = None
        if "isScheduledDeliveryShipment" in data:
            self.isScheduledDeliveryShipment: bool = convert_bool(data["isScheduledDeliveryShipment"])
        else:
            self.isScheduledDeliveryShipment: bool = None
        if "isPslipRequired" in data:
            self.isPslipRequired: bool = convert_bool(data["isPslipRequired"])
        else:
            self.isPslipRequired: bool = None
        if "isGift" in data:
            self.isGift: bool = convert_bool(data["isGift"])
        else:
            self.isGift: bool = None
        if "shipMethod" in data:
            self.shipMethod: str = str(data["shipMethod"])
        else:
            self.shipMethod: str = None
        if "shipmentDates" in data:
            self.shipmentDates: ShipmentDates = ShipmentDates(data["shipmentDates"])
        else:
            self.shipmentDates: ShipmentDates = None
        if "messageToCustomer" in data:
            self.messageToCustomer: str = str(data["messageToCustomer"])
        else:
            self.messageToCustomer: str = None


class ShipmentDates:
    """
    Shipment dates.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "requiredShipDate" in data:
            self.requiredShipDate: str = str(data["requiredShipDate"])
        else:
            self.requiredShipDate: str = None
        if "promisedDeliveryDate" in data:
            self.promisedDeliveryDate: str = str(data["promisedDeliveryDate"])
        else:
            self.promisedDeliveryDate: str = None


class ScheduledDeliveryShipment:
    """
    Dates for the scheduled delivery shipments.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "scheduledDeliveryServiceType" in data:
            self.scheduledDeliveryServiceType: str = str(data["scheduledDeliveryServiceType"])
        else:
            self.scheduledDeliveryServiceType: str = None
        if "earliestNominatedDeliveryDate" in data:
            self.earliestNominatedDeliveryDate: str = str(data["earliestNominatedDeliveryDate"])
        else:
            self.earliestNominatedDeliveryDate: str = None
        if "latestNominatedDeliveryDate" in data:
            self.latestNominatedDeliveryDate: str = str(data["latestNominatedDeliveryDate"])
        else:
            self.latestNominatedDeliveryDate: str = None


class GiftDetails:
    """
    Gift details for the item.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "giftMessage" in data:
            self.giftMessage: str = str(data["giftMessage"])
        else:
            self.giftMessage: str = None
        if "giftWrapId" in data:
            self.giftWrapId: str = str(data["giftWrapId"])
        else:
            self.giftWrapId: str = None


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class TaxLineItem(list, _List["TaxDetails"]):
    """
    A list of tax line items.
    """

    def __init__(self, data):
        super().__init__([TaxDetails(datum) for datum in data])
        self.data = data


class Decimal(str):
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation.
    """


class VendorDirectFulfillmentOrdersV1Client(__BaseClient):
    def getOrders(
        self,
        createdAfter: str,
        createdBefore: str,
        shipFromPartyId: str = None,
        status: str = None,
        limit: int = None,
        sortOrder: str = None,
        nextToken: str = None,
        includeDetails: str = None,
    ):
        """
                Returns a list of purchase orders created during the time frame that you specify. You define the time frame using the createdAfter and createdBefore parameters. You must use both parameters. You can choose to get only the purchase order numbers by setting the includeDetails parameter to false. In that case, the operation returns a list of purchase order numbers. You can then call the getOrder operation to return the details of a specific order.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/vendor/directFulfillment/orders/v1/purchaseOrders".format()
        params = {}
        if shipFromPartyId is not None:
            params["shipFromPartyId"] = shipFromPartyId
        if status is not None:
            params["status"] = status
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
        response = self.request(url, method="GET", params=params)
        return {
            200: GetOrdersResponse,
            400: GetOrdersResponse,
            403: GetOrdersResponse,
            404: GetOrdersResponse,
            415: GetOrdersResponse,
            429: GetOrdersResponse,
            500: GetOrdersResponse,
            503: GetOrdersResponse,
        }[response.status_code](self._get_response_json(response))

    def getOrder(
        self,
        purchaseOrderNumber: str,
    ):
        """
                Returns purchase order information for the purchaseOrderNumber that you specify.
        **Usage Plans:**
        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = "/vendor/directFulfillment/orders/v1/purchaseOrders/{purchaseOrderNumber}".format(
            purchaseOrderNumber=purchaseOrderNumber,
        )
        params = {}
        response = self.request(url, method="GET", params=params)
        return {
            200: GetOrderResponse,
            400: GetOrderResponse,
            401: GetOrderResponse,
            403: GetOrderResponse,
            404: GetOrderResponse,
            415: GetOrderResponse,
            429: GetOrderResponse,
            500: GetOrderResponse,
            503: GetOrderResponse,
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
        url = "/vendor/directFulfillment/orders/v1/acknowledgements".format()
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
