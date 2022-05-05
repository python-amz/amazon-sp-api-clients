"""
Selling Partner API for Retail Procurement Orders
=============================================================================================

The Selling Partner API for Retail Procurement Orders provides programmatic access to vendor orders data.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
from typing import Any, Union, Literal

import attrs

from ..utils.base_client import BaseClient


@attrs.define
class AcknowledgementStatusDetails:
    acknowledgement_date: str = attrs.field()
    # {'schema_format': 'date-time'}

    accepted_quantity: "ItemQuantity" = attrs.field()
    rejected_quantity: "ItemQuantity" = attrs.field()
    pass


@attrs.define
class Address:
    address_line1: str = attrs.field()
    address_line2: str = attrs.field()
    address_line3: str = attrs.field()
    city: str = attrs.field()
    country_code: str = attrs.field()
    # {'maxLength': 2}
    county: str = attrs.field()
    district: str = attrs.field()
    name: str = attrs.field()
    phone: str = attrs.field()
    postal_code: str = attrs.field()
    state_or_region: str = attrs.field()

    pass


@attrs.define
class DateTimeInterval:
    pass


@attrs.define
class Decimal:
    pass


@attrs.define
class Error:
    code: str = attrs.field()
    details: str = attrs.field()
    message: str = attrs.field()

    pass


@attrs.define
class ErrorList:
    pass


@attrs.define
class GetPurchaseOrderResponse:
    errors: "ErrorList" = attrs.field()
    payload: "Order" = attrs.field()
    pass


@attrs.define
class GetPurchaseOrdersResponse:
    errors: "ErrorList" = attrs.field()
    payload: "OrderList" = attrs.field()
    pass


@attrs.define
class GetPurchaseOrdersStatusResponse:
    errors: "ErrorList" = attrs.field()
    payload: "OrderListStatus" = attrs.field()
    pass


@attrs.define
class ImportDetails:
    import_containers: str = attrs.field()
    # {'maxLength': 64}
    international_commercial_terms: Union[
        Literal["ExWorks"],
        Literal["FreeCarrier"],
        Literal["FreeOnBoard"],
        Literal["FreeAlongSideShip"],
        Literal["CarriagePaidTo"],
        Literal["CostAndFreight"],
        Literal["CarriageAndInsurancePaidTo"],
        Literal["CostInsuranceAndFreight"],
        Literal["DeliveredAtTerminal"],
        Literal["DeliveredAtPlace"],
        Literal["DeliverDutyPaid"],
    ] = attrs.field()
    method_of_payment: Union[
        Literal["PaidByBuyer"],
        Literal["CollectOnDelivery"],
        Literal["DefinedByBuyerAndSeller"],
        Literal["FOBPortOfCall"],
        Literal["PrepaidBySeller"],
        Literal["PaidBySeller"],
    ] = attrs.field()
    port_of_delivery: str = attrs.field()
    # {'maxLength': 64}
    shipping_instructions: str = attrs.field()

    pass


@attrs.define
class ItemQuantity:
    amount: int = attrs.field()
    unit_of_measure: Union[Literal["Cases"], Literal["Eaches"]] = attrs.field()
    unit_size: int = attrs.field()

    pass


@attrs.define
class ItemStatus:
    pass


@attrs.define
class Money:
    currency_code: str = attrs.field()
    # {'maxLength': 3}

    amount: "Decimal" = attrs.field()
    pass


@attrs.define
class Order:
    purchase_order_number: str = attrs.field()
    purchase_order_state: Union[Literal["New"], Literal["Acknowledged"], Literal["Closed"]] = attrs.field()

    order_details: "OrderDetails" = attrs.field()
    pass


@attrs.define
class OrderAcknowledgement:
    acknowledgement_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    items: list["OrderAcknowledgementItem"] = attrs.field()
    purchase_order_number: str = attrs.field()

    selling_party: "PartyIdentification" = attrs.field()
    pass


@attrs.define
class OrderAcknowledgementItem:
    amazon_product_identifier: str = attrs.field()
    discount_multiplier: str = attrs.field()
    item_acknowledgements: list["OrderItemAcknowledgement"] = attrs.field()
    item_sequence_number: str = attrs.field()
    vendor_product_identifier: str = attrs.field()

    list_price: "Money" = attrs.field()
    net_cost: "Money" = attrs.field()
    ordered_quantity: "ItemQuantity" = attrs.field()
    pass


@attrs.define
class OrderDetails:
    deal_code: str = attrs.field()
    items: list["OrderItem"] = attrs.field()
    payment_method: Union[
        Literal["Invoice"], Literal["Consignment"], Literal["CreditCard"], Literal["Prepaid"]
    ] = attrs.field()
    purchase_order_changed_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    purchase_order_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    purchase_order_state_changed_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    purchase_order_type: Union[
        Literal["RegularOrder"], Literal["ConsignedOrder"], Literal["NewProductIntroduction"], Literal["RushOrder"]
    ] = attrs.field()

    bill_to_party: "PartyIdentification" = attrs.field()
    buying_party: "PartyIdentification" = attrs.field()
    delivery_window: "DateTimeInterval" = attrs.field()
    import_details: "ImportDetails" = attrs.field()
    selling_party: "PartyIdentification" = attrs.field()
    ship_to_party: "PartyIdentification" = attrs.field()
    ship_window: "DateTimeInterval" = attrs.field()
    pass


@attrs.define
class OrderItem:
    amazon_product_identifier: str = attrs.field()
    is_back_order_allowed: bool = attrs.field()
    item_sequence_number: str = attrs.field()
    vendor_product_identifier: str = attrs.field()

    list_price: "Money" = attrs.field()
    net_cost: "Money" = attrs.field()
    ordered_quantity: "ItemQuantity" = attrs.field()
    pass


@attrs.define
class OrderItemAcknowledgement:
    acknowledgement_code: Union[Literal["Accepted"], Literal["Backordered"], Literal["Rejected"]] = attrs.field()
    rejection_reason: Union[
        Literal["TemporarilyUnavailable"], Literal["InvalidProductIdentifier"], Literal["ObsoleteProduct"]
    ] = attrs.field()
    scheduled_delivery_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    scheduled_ship_date: str = attrs.field()
    # {'schema_format': 'date-time'}

    acknowledged_quantity: "ItemQuantity" = attrs.field()
    pass


@attrs.define
class OrderItemStatus:
    acknowledgement_status: dict[str, Any] = attrs.field()
    # {'properties': {'confirmationStatus': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=['ACCEPTED', 'PARTIALLY_ACCEPTED', 'REJECTED', 'UNCONFIRMED'], type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description='Confirmation status of line item.', schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'acceptedQuantity': Reference(ref='#/components/schemas/ItemQuantity'), 'rejectedQuantity': Reference(ref='#/components/schemas/ItemQuantity'), 'acknowledgementStatusDetails': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='array', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=Reference(ref='#/components/schemas/AcknowledgementStatusDetails'), properties=None, additionalProperties=None, description='Details of item quantity confirmed.', schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}}
    buyer_product_identifier: str = attrs.field()
    item_sequence_number: str = attrs.field()
    ordered_quantity: dict[str, Any] = attrs.field()
    # {'properties': {'orderedQuantity': Reference(ref='#/components/schemas/ItemQuantity'), 'orderedQuantityDetails': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='array', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=Reference(ref='#/components/schemas/OrderedQuantityDetails'), properties=None, additionalProperties=None, description='Details of item quantity ordered.', schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}}
    receiving_status: dict[str, Any] = attrs.field()
    # {'properties': {'receiveStatus': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=['NOT_RECEIVED', 'PARTIALLY_RECEIVED', 'RECEIVED'], type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description='Receive status of the line item.', schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'receivedQuantity': Reference(ref='#/components/schemas/ItemQuantity'), 'lastReceiveDate': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description="The date when the most recent item was received at the buyer's warehouse. Must be in ISO-8601 date/time format.", schema_format='date-time', default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None)}}
    vendor_product_identifier: str = attrs.field()

    list_price: "Money" = attrs.field()
    net_cost: "Money" = attrs.field()
    pass


@attrs.define
class OrderList:
    orders: list["Order"] = attrs.field()

    pagination: "Pagination" = attrs.field()
    pass


@attrs.define
class OrderListStatus:
    orders_status: list["OrderStatus"] = attrs.field()

    pagination: "Pagination" = attrs.field()
    pass


@attrs.define
class OrderStatus:
    last_updated_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    purchase_order_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    purchase_order_number: str = attrs.field()
    purchase_order_status: Union[Literal["OPEN"], Literal["CLOSED"]] = attrs.field()

    item_status: "ItemStatus" = attrs.field()
    selling_party: "PartyIdentification" = attrs.field()
    ship_to_party: "PartyIdentification" = attrs.field()
    pass


@attrs.define
class OrderedQuantityDetails:
    updated_date: str = attrs.field()
    # {'schema_format': 'date-time'}

    cancelled_quantity: "ItemQuantity" = attrs.field()
    ordered_quantity: "ItemQuantity" = attrs.field()
    pass


@attrs.define
class Pagination:
    next_token: str = attrs.field()

    pass


@attrs.define
class PartyIdentification:
    party_id: str = attrs.field()

    address: "Address" = attrs.field()
    tax_info: "TaxRegistrationDetails" = attrs.field()
    pass


@attrs.define
class SubmitAcknowledgementRequest:
    acknowledgements: list["OrderAcknowledgement"] = attrs.field()

    pass


@attrs.define
class SubmitAcknowledgementResponse:
    errors: "ErrorList" = attrs.field()
    payload: "TransactionId" = attrs.field()
    pass


@attrs.define
class TaxRegistrationDetails:
    tax_registration_number: str = attrs.field()
    tax_registration_type: Union[Literal["VAT"], Literal["GST"]] = attrs.field()

    pass


@attrs.define
class TransactionId:
    transaction_id: str = attrs.field()

    pass


class VendorOrdersV1Client(BaseClient):
    def get_purchase_order(
            self,
            purchase_order_number: str,
    ):
        """
        Returns a purchase order based on the purchaseOrderNumber value that you specify.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            purchase_order_number: The purchase order identifier for the order that you want. Formatting Notes: 8-character alpha-numeric code.
        """
        url = "/vendor/orders/v1/purchaseOrders/{purchaseOrderNumber}"
        values = (purchase_order_number,)
        response = self._parse_args_and_request(url, "GET", values, self._get_purchase_order_params)
        return response

    _get_purchase_order_params = (("purchaseOrderNumber", "path"),)  # name, param in

    def get_purchase_orders(
            self,
            limit: int = None,
            created_after: str = None,
            created_before: str = None,
            sort_order: Union[Literal["ASC"], Literal["DESC"]] = None,
            next_token: str = None,
            include_details: str = None,
            changed_after: str = None,
            changed_before: str = None,
            po_item_state: Union[Literal["Cancelled"]] = None,
            is_pochanged: str = None,
            purchase_order_state: Union[Literal["New"], Literal["Acknowledged"], Literal["Closed"]] = None,
            ordering_vendor_code: str = None,
    ):
        """
        Returns a list of purchase orders created or changed during the time frame that you specify. You define the time frame using the createdAfter, createdBefore, changedAfter and changedBefore parameters. The date range to search must not be more than 7 days. You can choose to get only the purchase order numbers by setting includeDetails to false. You can then use the getPurchaseOrder operation to receive details for a specific purchase order.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            limit: The limit to the number of records returned. Default value is 100 records.
            created_after: Purchase orders that became available after this time will be included in the result. Must be in ISO-8601 date/time format.
            created_before: Purchase orders that became available before this time will be included in the result. Must be in ISO-8601 date/time format.
            sort_order: Sort in ascending or descending order by purchase order creation date.
            next_token: Used for pagination when there is more purchase orders than the specified result size limit. The token value is returned in the previous API call
            include_details: When true, returns purchase orders with complete details. Otherwise, only purchase order numbers are returned. Default value is true.
            changed_after: Purchase orders that changed after this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            changed_before: Purchase orders that changed before this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            po_item_state: Current state of the purchase order item. If this value is Cancelled, this API will return purchase orders which have one or more items cancelled by Amazon with updated item quantity as zero.
            is_pochanged: When true, returns purchase orders which were modified after the order was placed. Vendors are required to pull the changed purchase order and fulfill the updated purchase order and not the original one. Default value is false.
            purchase_order_state: Filters purchase orders based on the purchase order state.
            ordering_vendor_code: Filters purchase orders based on the specified ordering vendor code. This value should be same as 'sellingParty.partyId' in the purchase order. If not included in the filter, all purchase orders for all of the vendor codes that exist in the vendor group used to authorize the API client application are returned.
        """
        url = "/vendor/orders/v1/purchaseOrders"
        values = (
            limit,
            created_after,
            created_before,
            sort_order,
            next_token,
            include_details,
            changed_after,
            changed_before,
            po_item_state,
            is_pochanged,
            purchase_order_state,
            ordering_vendor_code,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_purchase_orders_params)
        return response

    _get_purchase_orders_params = (  # name, param in
        ("limit", "query"),
        ("createdAfter", "query"),
        ("createdBefore", "query"),
        ("sortOrder", "query"),
        ("nextToken", "query"),
        ("includeDetails", "query"),
        ("changedAfter", "query"),
        ("changedBefore", "query"),
        ("poItemState", "query"),
        ("isPOChanged", "query"),
        ("purchaseOrderState", "query"),
        ("orderingVendorCode", "query"),
    )

    def get_purchase_orders_status(
            self,
            limit: int = None,
            sort_order: Union[Literal["ASC"], Literal["DESC"]] = None,
            next_token: str = None,
            created_after: str = None,
            created_before: str = None,
            updated_after: str = None,
            updated_before: str = None,
            purchase_order_number: str = None,
            purchase_order_status: Union[Literal["OPEN"], Literal["CLOSED"]] = None,
            item_confirmation_status: Union[
                Literal["ACCEPTED"], Literal["PARTIALLY_ACCEPTED"], Literal["REJECTED"], Literal["UNCONFIRMED"]
            ] = None,
            item_receive_status: Union[
                Literal["NOT_RECEIVED"], Literal["PARTIALLY_RECEIVED"], Literal["RECEIVED"]] = None,
            ordering_vendor_code: str = None,
            ship_to_party_id: str = None,
    ):
        """
        Returns purchase order statuses based on the filters that you specify. Date range to search must not be more than 7 days. You can return a list of purchase order statuses using the available filters, or a single purchase order status by providing the purchase order number.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            limit: The limit to the number of records returned. Default value is 100 records.
            sort_order: Sort in ascending or descending order by purchase order creation date.
            next_token: Used for pagination when there are more purchase orders than the specified result size limit.
            created_after: Purchase orders that became available after this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            created_before: Purchase orders that became available before this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            updated_after: Purchase orders for which the last purchase order update happened after this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            updated_before: Purchase orders for which the last purchase order update happened before this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            purchase_order_number: Provides purchase order status for the specified purchase order number.
            purchase_order_status: Filters purchase orders based on the specified purchase order status. If not included in filter, this will return purchase orders for all statuses.
            item_confirmation_status: Filters purchase orders based on their item confirmation status. If the item confirmation status is not included in the filter, purchase orders for all confirmation statuses are included.
            item_receive_status: Filters purchase orders based on the purchase order's item receive status. If the item receive status is not included in the filter, purchase orders for all receive statuses are included.
            ordering_vendor_code: Filters purchase orders based on the specified ordering vendor code. This value should be same as 'sellingParty.partyId' in the purchase order. If not included in filter, all purchase orders for all the vendor codes that exist in the vendor group used to authorize API client application are returned.
            ship_to_party_id: Filters purchase orders for a specific buyer's Fulfillment Center/warehouse by providing ship to location id here. This value should be same as 'shipToParty.partyId' in the purchase order. If not included in filter, this will return purchase orders for all the buyer's warehouses used for vendor group purchase orders.
        """
        url = "/vendor/orders/v1/purchaseOrdersStatus"
        values = (
            limit,
            sort_order,
            next_token,
            created_after,
            created_before,
            updated_after,
            updated_before,
            purchase_order_number,
            purchase_order_status,
            item_confirmation_status,
            item_receive_status,
            ordering_vendor_code,
            ship_to_party_id,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_purchase_orders_status_params)
        return response

    _get_purchase_orders_status_params = (  # name, param in
        ("limit", "query"),
        ("sortOrder", "query"),
        ("nextToken", "query"),
        ("createdAfter", "query"),
        ("createdBefore", "query"),
        ("updatedAfter", "query"),
        ("updatedBefore", "query"),
        ("purchaseOrderNumber", "query"),
        ("purchaseOrderStatus", "query"),
        ("itemConfirmationStatus", "query"),
        ("itemReceiveStatus", "query"),
        ("orderingVendorCode", "query"),
        ("shipToPartyId", "query"),
    )

    def submit_acknowledgement(
            self,
    ):
        """
        Submits acknowledgements for one or more purchase orders.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/vendor/orders/v1/acknowledgements"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._submit_acknowledgement_params)
        return response

    _submit_acknowledgement_params = ()  # name, param in
