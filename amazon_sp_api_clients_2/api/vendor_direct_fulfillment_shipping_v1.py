"""
Selling Partner API for Direct Fulfillment Shipping
=============================================================================================

The Selling Partner API for Direct Fulfillment Shipping provides programmatic access to a direct fulfillment vendor's shipping data.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime
import cattrs


@attrs.define(kw_only=True, frozen=True, slots=True)
class Address:
    """
    Address of the party.
    """

    address_line1: str = attrs.field()
    """
    First line of the address.
    """

    address_line2: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional street address information, if required.
    """

    address_line3: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional street address information, if required.
    """

    city: Optional[str] = attrs.field(
        default=None,
    )
    """
    The city where the person, business or institution is located.
    """

    country_code: str = attrs.field()
    """
    The two digit country code in ISO 3166-1 alpha-2 format.
    """

    county: Optional[str] = attrs.field(
        default=None,
    )
    """
    The county where person, business or institution is located.
    """

    district: Optional[str] = attrs.field(
        default=None,
    )
    """
    The district where person, business or institution is located.
    """

    name: str = attrs.field()
    """
    The name of the person, business or institution at that address.
    """

    phone: Optional[str] = attrs.field(
        default=None,
    )
    """
    The phone number of the person, business or institution located at that address.
    """

    postal_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The postal code of that address. It contains a series of letters or digits or both, sometimes including spaces or punctuation.
    """

    state_or_region: Optional[str] = attrs.field(
        default=None,
    )
    """
    The state or region where person, business or institution is located.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Container:

    carrier: Optional[str] = attrs.field(
        default=None,
    )
    """
    Carrier required for EU VOC vendors only.
    """

    container_identifier: str = attrs.field()
    """
    The container identifier.
    """

    container_sequence_number: Optional[int] = attrs.field(
        default=None,
    )
    """
    An integer that must be submitted for multi-box shipments only, where one item may come in separate packages.
    """

    container_type: Union[Literal["carton"], Literal["pallet"]] = attrs.field()
    """
    The type of container.
    """

    dimensions: Optional["Dimensions"] = attrs.field(
        default=None,
    )
    """
    Physical dimensional measurements of a container.
    """

    manifest_date: Optional[str] = attrs.field(
        default=None,
    )
    """
    The date of the manifest.
    """

    manifest_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The manifest identifier.
    """

    packed_items: List["PackedItem"] = attrs.field()
    """
    A list of packed items.
    """

    scac_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    SCAC code required for NA VOC vendors only.
    """

    ship_method: Optional[str] = attrs.field(
        default=None,
    )
    """
    The shipment method.
    """

    tracking_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    The tracking number.
    """

    weight: Optional["Weight"] = attrs.field(
        default=None,
    )
    """
    The weight.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CustomerInvoice:

    content: str = attrs.field()
    """
    The Base64encoded customer invoice.
    """

    purchase_order_number: str = attrs.field()
    """
    The purchase order number for this order.

    Extra fields:
    {'pattern': '^[a-zA-Z0-9]+$'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CustomerInvoiceList:

    customer_invoices: Optional[List["CustomerInvoice"]] = attrs.field()

    pagination: Optional["Pagination"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Decimal:
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation.  <br>**Pattern** : `^-?(0|([1-9]\\d*))(\\.\\d+)?([eE][+-]?\\d+)?$`.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Dimensions:
    """
    Physical dimensional measurements of a container.
    """

    height: "Decimal" = attrs.field()
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation.  <br>**Pattern** : `^-?(0|([1-9]\\d*))(\\.\\d+)?([eE][+-]?\\d+)?$`.
    """

    length: "Decimal" = attrs.field()
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation.  <br>**Pattern** : `^-?(0|([1-9]\\d*))(\\.\\d+)?([eE][+-]?\\d+)?$`.
    """

    unit_of_measure: Union[Literal["IN"], Literal["CM"]] = attrs.field()
    """
    The unit of measure for dimensions.
    """

    width: "Decimal" = attrs.field()
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation.  <br>**Pattern** : `^-?(0|([1-9]\\d*))(\\.\\d+)?([eE][+-]?\\d+)?$`.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetCustomerInvoiceResponse:
    """
    The response schema for the getCustomerInvoice operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["CustomerInvoice"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetCustomerInvoicesResponse:
    """
    The response schema for the getCustomerInvoices operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["CustomerInvoiceList"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetPackingSlipListResponse:

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["PackingSlipList"] = attrs.field()
    """
    A list of packing slips.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetPackingSlipResponse:

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["PackingSlip"] = attrs.field()
    """
    Packing slip information.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetShippingLabelListResponse:
    """
    The response schema for the getShippingLabels operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["ShippingLabelList"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetShippingLabelResponse:
    """
    The response schema for the getShippingLabel operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["ShippingLabel"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Item:
    """
    Details of the item being shipped.
    """

    buyer_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    Buyer's Standard Identification Number (ASIN) of an item. Either buyerProductIdentifier or vendorProductIdentifier is required.
    """

    item_sequence_number: int = attrs.field()
    """
    Item Sequence Number for the item. This must be the same value as sent in order for a given item.
    """

    shipped_quantity: "ItemQuantity" = attrs.field()
    """
    Details of item quantity.
    """

    vendor_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    The vendor selected product identification of the item. Should be the same as was sent in the purchase order, like SKU Number.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ItemQuantity:
    """
    Details of item quantity.
    """

    amount: int = attrs.field()
    """
    Quantity of units shipped for a specific item at a shipment level. If the item is present only in certain packages or pallets within the shipment, please provide this at the appropriate package or pallet level.
    """

    unit_of_measure: str = attrs.field()
    """
    Unit of measure for the shipped quantity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelData:
    """
    Details of the shipment label.
    """

    content: str = attrs.field()
    """
    This field will contain the Base64encoded string of the shipment label content.
    """

    package_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    Identifier for the package. The first package will be 001, the second 002, and so on. This number is used as a reference to refer to this package from the pallet level.
    """

    ship_method: Optional[str] = attrs.field(
        default=None,
    )
    """
    Ship method to be used for shipping the order. Amazon defines Ship Method Codes indicating shipping carrier and shipment service level. Ship Method Codes are case and format sensitive. The same ship method code should returned on the shipment confirmation. Note that the Ship Method Codes are vendor specific and will be provided to each vendor during the implementation.
    """

    ship_method_name: Optional[str] = attrs.field(
        default=None,
    )
    """
    Shipping method name for internal reference.
    """

    tracking_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    Package tracking identifier from the shipping carrier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PackedItem:

    buyer_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    Buyer's Standard Identification Number (ASIN) of an item. Either buyerProductIdentifier or vendorProductIdentifier is required.
    """

    item_sequence_number: int = attrs.field()
    """
    Item Sequence Number for the item. This must be the same value as sent in the order for a given item.
    """

    packed_quantity: "ItemQuantity" = attrs.field()
    """
    Details of item quantity.
    """

    vendor_product_identifier: Optional[str] = attrs.field(
        default=None,
    )
    """
    The vendor selected product identification of the item. Should be the same as was sent in the Purchase Order, like SKU Number.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PackingSlip:
    """
    Packing slip information.
    """

    content: str = attrs.field()
    """
    A Base64encoded string of the packing slip PDF.
    """

    content_type: Optional[Union[Literal["application/pdf"]]] = attrs.field(
        default=None,
    )
    """
    The format of the file such as PDF, JPEG etc.
    """

    purchase_order_number: str = attrs.field()
    """
    Purchase order number of the shipment that the packing slip is for.

    Extra fields:
    {'pattern': '^[a-zA-Z0-9]+$'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PackingSlipList:
    """
    A list of packing slips.
    """

    packing_slips: Optional[List["PackingSlip"]] = attrs.field()

    pagination: Optional["Pagination"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Pagination:

    next_token: Optional[str] = attrs.field()
    """
    A generated string used to pass information to your next request. If NextToken is returned, pass the value of NextToken to the next request. If NextToken is not returned, there are no more order items to return.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartyIdentification:

    address: Optional["Address"] = attrs.field(
        default=None,
    )
    """
    Address of the party.
    """

    party_id: str = attrs.field()
    """
    Assigned Identification for the party.
    """

    tax_registration_details: Optional[List["TaxRegistrationDetails"]] = attrs.field(
        default=None,
    )
    """
    Tax registration details of the entity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentConfirmation:

    containers: Optional[List["Container"]] = attrs.field(
        default=None,
    )
    """
    Provide the details of the items in this shipment. If any of the item details field is common at a package or a pallet level, then provide them at the corresponding package.
    """

    items: List["Item"] = attrs.field()
    """
    Provide the details of the items in this shipment. If any of the item details field is common at a package or a pallet level, then provide them at the corresponding package.
    """

    purchase_order_number: str = attrs.field()
    """
    Purchase order number corresponding to the shipment.

    Extra fields:
    {'pattern': '^[a-zA-Z0-9]+$'}
    """

    selling_party: "PartyIdentification" = attrs.field()

    ship_from_party: "PartyIdentification" = attrs.field()

    shipment_details: "ShipmentDetails" = attrs.field()
    """
    Details about a shipment.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentDetails:
    """
    Details about a shipment.
    """

    estimated_delivery_date: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    Date on which the shipment is expected to reach the buyer's warehouse. It needs to be an estimate based on the average transit time between the ship-from location and the destination. The exact appointment time will be provided by buyer and is potentially not known when creating the shipment confirmation.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    is_priority_shipment: Optional[bool] = attrs.field(
        default=None,
    )
    """
    Provide the priority of the shipment.
    """

    shipment_status: Union[Literal["SHIPPED"], Literal["FLOOR_DENIAL"]] = attrs.field()
    """
    Indicate the shipment status.
    """

    shipped_date: datetime = attrs.field()
    """
    This field indicates the date of the departure of the shipment from vendor's location. Vendors are requested to send ASNs within 30 minutes of departure from their warehouse/distribution center or at least 6 hours prior to the appointment time at the Amazon destination warehouse, whichever is sooner. Shipped date mentioned in the Shipment Confirmation should not be in the future.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    vendor_order_number: Optional[str] = attrs.field(
        default=None,
    )
    """
    The vendor order number is a unique identifier generated by a vendor for their reference.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentStatusUpdate:

    purchase_order_number: str = attrs.field()
    """
    Purchase order number of the shipment for which to update the shipment status.

    Extra fields:
    {'pattern': '^[a-zA-Z0-9]+$'}
    """

    selling_party: "PartyIdentification" = attrs.field()

    ship_from_party: "PartyIdentification" = attrs.field()

    status_update_details: "StatusUpdateDetails" = attrs.field()
    """
    Details for the shipment status update given by the vendor for the specific package.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShippingLabel:

    label_data: List["LabelData"] = attrs.field()
    """
    Provides the details of the packages in this shipment.
    """

    label_format: Union[Literal["PNG"], Literal["ZPL"]] = attrs.field()
    """
    Format of the label.
    """

    purchase_order_number: str = attrs.field()
    """
    This field will contain the Purchase Order Number for this order.

    Extra fields:
    {'pattern': '^[a-zA-Z0-9]+$'}
    """

    selling_party: "PartyIdentification" = attrs.field()

    ship_from_party: "PartyIdentification" = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShippingLabelList:

    pagination: Optional["Pagination"] = attrs.field()

    shipping_labels: Optional[List["ShippingLabel"]] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShippingLabelRequest:

    containers: Optional[List["Container"]] = attrs.field(
        default=None,
    )
    """
    A list of the packages in this shipment.
    """

    purchase_order_number: str = attrs.field()
    """
    Purchase order number of the order for which to create a shipping label.

    Extra fields:
    {'pattern': '^[a-zA-Z0-9]+$'}
    """

    selling_party: "PartyIdentification" = attrs.field()

    ship_from_party: "PartyIdentification" = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class StatusUpdateDetails:
    """
    Details for the shipment status update given by the vendor for the specific package.
    """

    reason_code: str = attrs.field()
    """
    Provides a reason code for the status of the package that will provide additional information about the transportation status.
    """

    shipment_schedule: Optional["StatusUpdateDetailsShipmentSchedule"] = attrs.field(
        default=None,
    )

    status_code: str = attrs.field()
    """
    Indicates the shipment status code of the package that provides transportation information for Amazon tracking systems and ultimately for the final customer.
    """

    status_date_time: datetime = attrs.field()
    """
    The date and time when the shipment status was updated. This field is expected to be in ISO-8601 date/time format, with UTC time zone or UTC offset. For example, 2020-07-16T23:00:00Z or 2020-07-16T23:00:00+01:00.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    status_location_address: "Address" = attrs.field()
    """
    Address of the party.
    """

    tracking_number: str = attrs.field()
    """
    This is required to be provided for every package and should match with the trackingNumber sent for the shipment confirmation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class StatusUpdateDetailsShipmentSchedule:

    appt_window_end_date_time: Optional[datetime] = attrs.field()
    """
    This field indicates the date and time at the end of the appointment window scheduled to deliver the shipment. This field is expected to be in ISO-8601 date/time format, with UTC time zone or UTC offset. For example, 2020-07-16T23:00:00Z or 2020-07-16T23:00:00+01:00.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    appt_window_start_date_time: Optional[datetime] = attrs.field()
    """
    This field indicates the date and time at the start of the appointment window scheduled to deliver the shipment. This field is expected to be in ISO-8601 date/time format, with UTC time zone or UTC offset. For example, 2020-07-16T23:00:00Z or 2020-07-16T23:00:00+01:00.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    estimated_delivery_date_time: Optional[datetime] = attrs.field()
    """
    Date on which the shipment is expected to reach the customer delivery location. This field is expected to be in ISO-8601 date/time format, with UTC time zone or UTC offset. For example, 2020-07-16T23:00:00Z or 2020-07-16T23:00:00+01:00.

    Extra fields:
    {'schema_format': 'date-time'}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitShipmentConfirmationsRequest:

    shipment_confirmations: Optional[List["ShipmentConfirmation"]] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitShipmentConfirmationsResponse:
    """
    The response schema for the submitShipmentConfirmations operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["TransactionReference"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitShipmentStatusUpdatesRequest:

    shipment_status_updates: Optional[List["ShipmentStatusUpdate"]] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitShipmentStatusUpdatesResponse:
    """
    The response schema for the submitShipmentStatusUpdates operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["TransactionReference"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitShippingLabelsRequest:

    shipping_label_requests: Optional[List["ShippingLabelRequest"]] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitShippingLabelsResponse:
    """
    The response schema for the submitShippingLabelRequest operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["TransactionReference"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxRegistrationDetails:
    """
    Tax registration details of the entity.
    """

    tax_registration_address: Optional["Address"] = attrs.field(
        default=None,
    )
    """
    Address of the party.
    """

    tax_registration_messages: Optional[str] = attrs.field(
        default=None,
    )
    """
    Tax registration message that can be used for additional tax related details.
    """

    tax_registration_number: str = attrs.field()
    """
    Tax registration number for the party. For example, VAT ID.
    """

    tax_registration_type: Optional[Union[Literal["VAT"], Literal["GST"]]] = attrs.field(
        default=None,
    )
    """
    Tax registration type for the entity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransactionReference:

    transaction_id: Optional[str] = attrs.field()
    """
    GUID to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Weight:
    """
    The weight.
    """

    unit_of_measure: Union[Literal["KG"], Literal["LB"]] = attrs.field()
    """
    The unit of measurement.
    """

    value: "Decimal" = attrs.field()
    """
    A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation.  <br>**Pattern** : `^-?(0|([1-9]\\d*))(\\.\\d+)?([eE][+-]?\\d+)?$`.
    """


class VendorDirectFulfillmentShippingV1Client(BaseClient):
    def get_customer_invoice(
        self,
        purchase_order_number: str,
    ) -> Union[GetCustomerInvoiceResponse]:
        """
        Returns a customer invoice based on the purchaseOrderNumber that you specify.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            purchase_order_number: Purchase order number of the shipment for which to return the invoice.
        """
        url = "/vendor/directFulfillment/shipping/v1/customerInvoices/{purchaseOrderNumber}"
        values = (purchase_order_number,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_customer_invoice_params,
        )
        klass = self._get_customer_invoice_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = cattrs.structure(response.json(), klass)
        return obj

    _get_customer_invoice_params = (("purchaseOrderNumber", "path"),)  # name, param in

    _get_customer_invoice_responses = {
        200: GetCustomerInvoiceResponse,
        400: GetCustomerInvoiceResponse,
        401: GetCustomerInvoiceResponse,
        403: GetCustomerInvoiceResponse,
        404: GetCustomerInvoiceResponse,
        415: GetCustomerInvoiceResponse,
        429: GetCustomerInvoiceResponse,
        500: GetCustomerInvoiceResponse,
        503: GetCustomerInvoiceResponse,
    }

    def get_customer_invoices(
        self,
        created_after: datetime,
        created_before: datetime,
        ship_from_party_id: str = None,
        limit: int = None,
        sort_order: Union[Literal["ASC"], Literal["DESC"]] = None,
        next_token: str = None,
    ) -> Union[GetCustomerInvoiceResponse, GetCustomerInvoicesResponse]:
        """
        Returns a list of customer invoices created during a time frame that you specify. You define the  time frame using the createdAfter and createdBefore parameters. You must use both of these parameters. The date range to search must be no more than 7 days.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            ship_from_party_id: The vendor warehouseId for order fulfillment. If not specified, the result will contain orders for all warehouses.
            limit: The limit to the number of records returned
            created_after: Orders that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
            created_before: Orders that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
            sort_order: Sort ASC or DESC by order creation date.
            next_token: Used for pagination when there are more orders than the specified result size limit. The token value is returned in the previous API call.
        """
        url = "/vendor/directFulfillment/shipping/v1/customerInvoices"
        values = (
            ship_from_party_id,
            limit,
            created_after,
            created_before,
            sort_order,
            next_token,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_customer_invoices_params,
        )
        klass = self._get_customer_invoices_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = cattrs.structure(response.json(), klass)
        return obj

    _get_customer_invoices_params = (  # name, param in
        ("shipFromPartyId", "query"),
        ("limit", "query"),
        ("createdAfter", "query"),
        ("createdBefore", "query"),
        ("sortOrder", "query"),
        ("nextToken", "query"),
    )

    _get_customer_invoices_responses = {
        200: GetCustomerInvoicesResponse,
        400: GetCustomerInvoiceResponse,
        403: GetCustomerInvoiceResponse,
        404: GetCustomerInvoiceResponse,
        415: GetCustomerInvoiceResponse,
        429: GetCustomerInvoiceResponse,
        500: GetCustomerInvoiceResponse,
        503: GetCustomerInvoiceResponse,
    }

    def get_packing_slip(
        self,
        purchase_order_number: str,
    ) -> Union[GetPackingSlipResponse]:
        """
        Returns a packing slip based on the purchaseOrderNumber that you specify.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            purchase_order_number: The purchaseOrderNumber for the packing slip you want.
        """
        url = "/vendor/directFulfillment/shipping/v1/packingSlips/{purchaseOrderNumber}"
        values = (purchase_order_number,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_packing_slip_params,
        )
        klass = self._get_packing_slip_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = cattrs.structure(response.json(), klass)
        return obj

    _get_packing_slip_params = (("purchaseOrderNumber", "path"),)  # name, param in

    _get_packing_slip_responses = {
        200: GetPackingSlipResponse,
        400: GetPackingSlipResponse,
        401: GetPackingSlipResponse,
        403: GetPackingSlipResponse,
        404: GetPackingSlipResponse,
        415: GetPackingSlipResponse,
        429: GetPackingSlipResponse,
        500: GetPackingSlipResponse,
        503: GetPackingSlipResponse,
    }

    def get_packing_slips(
        self,
        created_after: datetime,
        created_before: datetime,
        ship_from_party_id: str = None,
        limit: int = None,
        sort_order: Union[Literal["ASC"], Literal["DESC"]] = None,
        next_token: str = None,
    ) -> Union[GetPackingSlipListResponse]:
        """
        Returns a list of packing slips for the purchase orders that match the criteria specified. Date range to search must not be more than 7 days.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            ship_from_party_id: The vendor warehouseId for order fulfillment. If not specified the result will contain orders for all warehouses.
            limit: The limit to the number of records returned
            created_after: Packing slips that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
            created_before: Packing slips that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
            sort_order: Sort ASC or DESC by packing slip creation date.
            next_token: Used for pagination when there are more packing slips than the specified result size limit. The token value is returned in the previous API call.
        """
        url = "/vendor/directFulfillment/shipping/v1/packingSlips"
        values = (
            ship_from_party_id,
            limit,
            created_after,
            created_before,
            sort_order,
            next_token,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_packing_slips_params,
        )
        klass = self._get_packing_slips_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = cattrs.structure(response.json(), klass)
        return obj

    _get_packing_slips_params = (  # name, param in
        ("shipFromPartyId", "query"),
        ("limit", "query"),
        ("createdAfter", "query"),
        ("createdBefore", "query"),
        ("sortOrder", "query"),
        ("nextToken", "query"),
    )

    _get_packing_slips_responses = {
        200: GetPackingSlipListResponse,
        400: GetPackingSlipListResponse,
        401: GetPackingSlipListResponse,
        403: GetPackingSlipListResponse,
        404: GetPackingSlipListResponse,
        415: GetPackingSlipListResponse,
        429: GetPackingSlipListResponse,
        500: GetPackingSlipListResponse,
        503: GetPackingSlipListResponse,
    }

    def get_shipping_label(
        self,
        purchase_order_number: str,
    ) -> Union[GetShippingLabelResponse]:
        """
        Returns a shipping label for the purchaseOrderNumber that you specify.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            purchase_order_number: The purchase order number for which you want to return the shipping label. It should be the same purchaseOrderNumber as received in the order.
        """
        url = "/vendor/directFulfillment/shipping/v1/shippingLabels/{purchaseOrderNumber}"
        values = (purchase_order_number,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_shipping_label_params,
        )
        klass = self._get_shipping_label_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = cattrs.structure(response.json(), klass)
        return obj

    _get_shipping_label_params = (("purchaseOrderNumber", "path"),)  # name, param in

    _get_shipping_label_responses = {
        200: GetShippingLabelResponse,
        400: GetShippingLabelResponse,
        401: GetShippingLabelResponse,
        403: GetShippingLabelResponse,
        404: GetShippingLabelResponse,
        415: GetShippingLabelResponse,
        429: GetShippingLabelResponse,
        500: GetShippingLabelResponse,
        503: GetShippingLabelResponse,
    }

    def get_shipping_labels(
        self,
        created_after: datetime,
        created_before: datetime,
        ship_from_party_id: str = None,
        limit: int = None,
        sort_order: Union[Literal["ASC"], Literal["DESC"]] = None,
        next_token: str = None,
    ) -> Union[GetShippingLabelListResponse]:
        """
        Returns a list of shipping labels created during the time frame that you specify. You define that time frame using the createdAfter and createdBefore parameters. You must use both of these parameters. The date range to search must not be more than 7 days.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            ship_from_party_id: The vendor warehouseId for order fulfillment. If not specified, the result will contain orders for all warehouses.
            limit: The limit to the number of records returned.
            created_after: Shipping labels that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
            created_before: Shipping labels that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
            sort_order: Sort ASC or DESC by order creation date.
            next_token: Used for pagination when there are more ship labels than the specified result size limit. The token value is returned in the previous API call.
        """
        url = "/vendor/directFulfillment/shipping/v1/shippingLabels"
        values = (
            ship_from_party_id,
            limit,
            created_after,
            created_before,
            sort_order,
            next_token,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_shipping_labels_params,
        )
        klass = self._get_shipping_labels_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = cattrs.structure(response.json(), klass)
        return obj

    _get_shipping_labels_params = (  # name, param in
        ("shipFromPartyId", "query"),
        ("limit", "query"),
        ("createdAfter", "query"),
        ("createdBefore", "query"),
        ("sortOrder", "query"),
        ("nextToken", "query"),
    )

    _get_shipping_labels_responses = {
        200: GetShippingLabelListResponse,
        400: GetShippingLabelListResponse,
        403: GetShippingLabelListResponse,
        404: GetShippingLabelListResponse,
        415: GetShippingLabelListResponse,
        429: GetShippingLabelListResponse,
        500: GetShippingLabelListResponse,
        503: GetShippingLabelListResponse,
    }

    def submit_shipment_confirmations(
        self,
        shipment_confirmations: List["ShipmentConfirmation"] = None,
    ) -> Union[SubmitShipmentConfirmationsResponse]:
        """
        Submits one or more shipment confirmations for vendor orders.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_confirmations: no description.
        """
        url = "/vendor/directFulfillment/shipping/v1/shipmentConfirmations"
        values = (shipment_confirmations,)
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._submit_shipment_confirmations_params,
        )
        klass = self._submit_shipment_confirmations_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = cattrs.structure(response.json(), klass)
        return obj

    _submit_shipment_confirmations_params = (("shipmentConfirmations", "body"),)  # name, param in

    _submit_shipment_confirmations_responses = {
        202: SubmitShipmentConfirmationsResponse,
        400: SubmitShipmentConfirmationsResponse,
        403: SubmitShipmentConfirmationsResponse,
        404: SubmitShipmentConfirmationsResponse,
        413: SubmitShipmentConfirmationsResponse,
        415: SubmitShipmentConfirmationsResponse,
        429: SubmitShipmentConfirmationsResponse,
        500: SubmitShipmentConfirmationsResponse,
        503: SubmitShipmentConfirmationsResponse,
    }

    def submit_shipment_status_updates(
        self,
        shipment_status_updates: List["ShipmentStatusUpdate"] = None,
    ) -> Union[SubmitShipmentStatusUpdatesResponse]:
        """
        This API call is only to be used by Vendor-Own-Carrier (VOC) vendors. Calling this API will submit a shipment status update for the package that a vendor has shipped. It will provide the Amazon customer visibility on their order, when the package is outside of Amazon Network visibility.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_status_updates: no description.
        """
        url = "/vendor/directFulfillment/shipping/v1/shipmentStatusUpdates"
        values = (shipment_status_updates,)
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._submit_shipment_status_updates_params,
        )
        klass = self._submit_shipment_status_updates_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = cattrs.structure(response.json(), klass)
        return obj

    _submit_shipment_status_updates_params = (("shipmentStatusUpdates", "body"),)  # name, param in

    _submit_shipment_status_updates_responses = {
        202: SubmitShipmentStatusUpdatesResponse,
        400: SubmitShipmentStatusUpdatesResponse,
        403: SubmitShipmentStatusUpdatesResponse,
        404: SubmitShipmentStatusUpdatesResponse,
        413: SubmitShipmentStatusUpdatesResponse,
        415: SubmitShipmentStatusUpdatesResponse,
        429: SubmitShipmentStatusUpdatesResponse,
        500: SubmitShipmentStatusUpdatesResponse,
        503: SubmitShipmentStatusUpdatesResponse,
    }

    def submit_shipping_label_request(
        self,
        shipping_label_requests: List["ShippingLabelRequest"] = None,
    ) -> Union[SubmitShippingLabelsResponse]:
        """
        Creates a shipping label for a purchase order and returns a transactionId for reference.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipping_label_requests: no description.
        """
        url = "/vendor/directFulfillment/shipping/v1/shippingLabels"
        values = (shipping_label_requests,)
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._submit_shipping_label_request_params,
        )
        klass = self._submit_shipping_label_request_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = cattrs.structure(response.json(), klass)
        return obj

    _submit_shipping_label_request_params = (("shippingLabelRequests", "body"),)  # name, param in

    _submit_shipping_label_request_responses = {
        202: SubmitShippingLabelsResponse,
        400: SubmitShippingLabelsResponse,
        403: SubmitShippingLabelsResponse,
        404: SubmitShippingLabelsResponse,
        413: SubmitShippingLabelsResponse,
        415: SubmitShippingLabelsResponse,
        429: SubmitShippingLabelsResponse,
        500: SubmitShippingLabelsResponse,
        503: SubmitShippingLabelsResponse,
    }
