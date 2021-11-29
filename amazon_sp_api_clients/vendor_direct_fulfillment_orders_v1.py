from .base import BaseClient as __BaseClient, convert_bool, BaseDictObject as __BaseDictObject
from typing import List as _List


class GetOrdersResponse(__BaseDictObject):
    """
    The response schema for the getOrders operation.
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


class GetOrderResponse(__BaseDictObject):
    """
    The response schema for the getOrder operation.
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
        if "customerOrderNumber" in data:
            self.customerOrderNumber: str = self._get_value(str, "customerOrderNumber")
        else:
            self.customerOrderNumber: str = None
        if "orderDate" in data:
            self.orderDate: str = self._get_value(str, "orderDate")
        else:
            self.orderDate: str = None
        if "orderStatus" in data:
            self.orderStatus: str = self._get_value(str, "orderStatus")
        else:
            self.orderStatus: str = None
        if "shipmentDetails" in data:
            self.shipmentDetails: ShipmentDetails = self._get_value(ShipmentDetails, "shipmentDetails")
        else:
            self.shipmentDetails: ShipmentDetails = None
        if "taxTotal" in data:
            self.taxTotal: dict = self._get_value(dict, "taxTotal")
        else:
            self.taxTotal: dict = None
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = self._get_value(PartyIdentification, "sellingParty")
        else:
            self.sellingParty: PartyIdentification = None
        if "shipFromParty" in data:
            self.shipFromParty: PartyIdentification = self._get_value(PartyIdentification, "shipFromParty")
        else:
            self.shipFromParty: PartyIdentification = None
        if "shipToParty" in data:
            self.shipToParty: Address = self._get_value(Address, "shipToParty")
        else:
            self.shipToParty: Address = None
        if "billToParty" in data:
            self.billToParty: PartyIdentification = self._get_value(PartyIdentification, "billToParty")
        else:
            self.billToParty: PartyIdentification = None
        if "items" in data:
            self.items: _List[OrderItem] = [OrderItem(datum) for datum in data["items"]]
        else:
            self.items: _List[OrderItem] = []


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
        if "attention" in data:
            self.attention: str = self._get_value(str, "attention")
        else:
            self.attention: str = None
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
        if "buyerProductIdentifier" in data:
            self.buyerProductIdentifier: str = self._get_value(str, "buyerProductIdentifier")
        else:
            self.buyerProductIdentifier: str = None
        if "vendorProductIdentifier" in data:
            self.vendorProductIdentifier: str = self._get_value(str, "vendorProductIdentifier")
        else:
            self.vendorProductIdentifier: str = None
        if "title" in data:
            self.title: str = self._get_value(str, "title")
        else:
            self.title: str = None
        if "orderedQuantity" in data:
            self.orderedQuantity: ItemQuantity = self._get_value(ItemQuantity, "orderedQuantity")
        else:
            self.orderedQuantity: ItemQuantity = None
        if "scheduledDeliveryShipment" in data:
            self.scheduledDeliveryShipment: ScheduledDeliveryShipment = self._get_value(
                ScheduledDeliveryShipment, "scheduledDeliveryShipment"
            )
        else:
            self.scheduledDeliveryShipment: ScheduledDeliveryShipment = None
        if "giftDetails" in data:
            self.giftDetails: GiftDetails = self._get_value(GiftDetails, "giftDetails")
        else:
            self.giftDetails: GiftDetails = None
        if "netPrice" in data:
            self.netPrice: Money = self._get_value(Money, "netPrice")
        else:
            self.netPrice: Money = None
        if "taxDetails" in data:
            self.taxDetails: dict = self._get_value(dict, "taxDetails")
        else:
            self.taxDetails: dict = None
        if "totalPrice" in data:
            self.totalPrice: Money = self._get_value(Money, "totalPrice")
        else:
            self.totalPrice: Money = None


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
    The response schema for the submitAcknowledgement operation.
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
    The request schema for the submitAcknowledgement operation.
    """

    def __init__(self, data):
        super().__init__(data)
        if "orderAcknowledgements" in data:
            self.orderAcknowledgements: _List[OrderAcknowledgementItem] = [
                OrderAcknowledgementItem(datum) for datum in data["orderAcknowledgements"]
            ]
        else:
            self.orderAcknowledgements: _List[OrderAcknowledgementItem] = []


class OrderAcknowledgementItem(__BaseDictObject):
    """
    Details of an individual order being acknowledged.
    """

    def __init__(self, data):
        super().__init__(data)
        if "purchaseOrderNumber" in data:
            self.purchaseOrderNumber: str = self._get_value(str, "purchaseOrderNumber")
        else:
            self.purchaseOrderNumber: str = None
        if "vendorOrderNumber" in data:
            self.vendorOrderNumber: str = self._get_value(str, "vendorOrderNumber")
        else:
            self.vendorOrderNumber: str = None
        if "acknowledgementDate" in data:
            self.acknowledgementDate: str = self._get_value(str, "acknowledgementDate")
        else:
            self.acknowledgementDate: str = None
        if "acknowledgementStatus" in data:
            self.acknowledgementStatus: AcknowledgementStatus = self._get_value(
                AcknowledgementStatus, "acknowledgementStatus"
            )
        else:
            self.acknowledgementStatus: AcknowledgementStatus = None
        if "sellingParty" in data:
            self.sellingParty: PartyIdentification = self._get_value(PartyIdentification, "sellingParty")
        else:
            self.sellingParty: PartyIdentification = None
        if "shipFromParty" in data:
            self.shipFromParty: PartyIdentification = self._get_value(PartyIdentification, "shipFromParty")
        else:
            self.shipFromParty: PartyIdentification = None
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
        if "acknowledgedQuantity" in data:
            self.acknowledgedQuantity: ItemQuantity = self._get_value(ItemQuantity, "acknowledgedQuantity")
        else:
            self.acknowledgedQuantity: ItemQuantity = None


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


class TaxDetails(__BaseDictObject):
    """ """

    def __init__(self, data):
        super().__init__(data)
        if "taxRate" in data:
            self.taxRate: Decimal = self._get_value(Decimal, "taxRate")
        else:
            self.taxRate: Decimal = None
        if "taxAmount" in data:
            self.taxAmount: Money = self._get_value(Money, "taxAmount")
        else:
            self.taxAmount: Money = None
        if "taxableAmount" in data:
            self.taxableAmount: Money = self._get_value(Money, "taxableAmount")
        else:
            self.taxableAmount: Money = None
        if "type" in data:
            self.type: str = self._get_value(str, "type")
        else:
            self.type: str = None


class AcknowledgementStatus(__BaseDictObject):
    """
    Status of acknowledgement.
    """

    def __init__(self, data):
        super().__init__(data)
        if "code" in data:
            self.code: str = self._get_value(str, "code")
        else:
            self.code: str = None
        if "description" in data:
            self.description: str = self._get_value(str, "description")
        else:
            self.description: str = None


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


class ShipmentDetails(__BaseDictObject):
    """
    Shipment details required for the shipment.
    """

    def __init__(self, data):
        super().__init__(data)
        if "isPriorityShipment" in data:
            self.isPriorityShipment: bool = self._get_value(convert_bool, "isPriorityShipment")
        else:
            self.isPriorityShipment: bool = None
        if "isScheduledDeliveryShipment" in data:
            self.isScheduledDeliveryShipment: bool = self._get_value(convert_bool, "isScheduledDeliveryShipment")
        else:
            self.isScheduledDeliveryShipment: bool = None
        if "isPslipRequired" in data:
            self.isPslipRequired: bool = self._get_value(convert_bool, "isPslipRequired")
        else:
            self.isPslipRequired: bool = None
        if "isGift" in data:
            self.isGift: bool = self._get_value(convert_bool, "isGift")
        else:
            self.isGift: bool = None
        if "shipMethod" in data:
            self.shipMethod: str = self._get_value(str, "shipMethod")
        else:
            self.shipMethod: str = None
        if "shipmentDates" in data:
            self.shipmentDates: ShipmentDates = self._get_value(ShipmentDates, "shipmentDates")
        else:
            self.shipmentDates: ShipmentDates = None
        if "messageToCustomer" in data:
            self.messageToCustomer: str = self._get_value(str, "messageToCustomer")
        else:
            self.messageToCustomer: str = None


class ShipmentDates(__BaseDictObject):
    """
    Shipment dates.
    """

    def __init__(self, data):
        super().__init__(data)
        if "requiredShipDate" in data:
            self.requiredShipDate: str = self._get_value(str, "requiredShipDate")
        else:
            self.requiredShipDate: str = None
        if "promisedDeliveryDate" in data:
            self.promisedDeliveryDate: str = self._get_value(str, "promisedDeliveryDate")
        else:
            self.promisedDeliveryDate: str = None


class ScheduledDeliveryShipment(__BaseDictObject):
    """
    Dates for the scheduled delivery shipments.
    """

    def __init__(self, data):
        super().__init__(data)
        if "scheduledDeliveryServiceType" in data:
            self.scheduledDeliveryServiceType: str = self._get_value(str, "scheduledDeliveryServiceType")
        else:
            self.scheduledDeliveryServiceType: str = None
        if "earliestNominatedDeliveryDate" in data:
            self.earliestNominatedDeliveryDate: str = self._get_value(str, "earliestNominatedDeliveryDate")
        else:
            self.earliestNominatedDeliveryDate: str = None
        if "latestNominatedDeliveryDate" in data:
            self.latestNominatedDeliveryDate: str = self._get_value(str, "latestNominatedDeliveryDate")
        else:
            self.latestNominatedDeliveryDate: str = None


class GiftDetails(__BaseDictObject):
    """
    Gift details for the item.
    """

    def __init__(self, data):
        super().__init__(data)
        if "giftMessage" in data:
            self.giftMessage: str = self._get_value(str, "giftMessage")
        else:
            self.giftMessage: str = None
        if "giftWrapId" in data:
            self.giftWrapId: str = self._get_value(str, "giftWrapId")
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
        url = f"/vendor/directFulfillment/orders/v1/purchaseOrders"
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
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetOrdersResponse,
            400: GetOrdersResponse,
            403: GetOrdersResponse,
            404: GetOrdersResponse,
            415: GetOrdersResponse,
            429: GetOrdersResponse,
            500: GetOrdersResponse,
            503: GetOrdersResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

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
        url = f"/vendor/directFulfillment/orders/v1/purchaseOrders/{purchaseOrderNumber}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        response_type = {
            200: GetOrderResponse,
            400: GetOrderResponse,
            401: GetOrderResponse,
            403: GetOrderResponse,
            404: GetOrderResponse,
            415: GetOrderResponse,
            429: GetOrderResponse,
            500: GetOrderResponse,
            503: GetOrderResponse,
        }.get(response.status_code, None)
        return None if response_type is None else response_type(self._get_response_json(response))

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
        url = f"/vendor/directFulfillment/orders/v1/acknowledgements"
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
