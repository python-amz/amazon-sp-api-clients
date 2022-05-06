"""
Selling Partner API for Direct Fulfillment Shipping
=============================================================================================

The Selling Partner API for Direct Fulfillment Shipping provides programmatic access to a direct fulfillment vendor's shipping data.
API Version: 2021-12-28
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class Address:
    """
    Address of the party.
    """

    address_line1: str = attrs.field()
    """
    First line of the address.
    """

    address_line2: Optional[str] = attrs.field()
    """
    Additional street address information, if required.
    """

    address_line3: Optional[str] = attrs.field()
    """
    Additional street address information, if required.
    """

    city: Optional[str] = attrs.field()
    """
    The city where the person, business or institution is located.
    """

    country_code: str = attrs.field()
    """
    The two digit country code in ISO 3166-1 alpha-2 format.
    """

    county: Optional[str] = attrs.field()
    """
    The county where person, business or institution is located.
    """

    district: Optional[str] = attrs.field()
    """
    The district where person, business or institution is located.
    """

    name: str = attrs.field()
    """
    The name of the person, business or institution at that address.
    """

    phone: Optional[str] = attrs.field()
    """
    The phone number of the person, business or institution located at that address.
    """

    postal_code: Optional[str] = attrs.field()
    """
    The postal code of that address. It contains a series of letters or digits or both, sometimes including spaces or punctuation.
    """

    state_or_region: Optional[str] = attrs.field()
    """
    The state or region where person, business or institution is located.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Container:

    carrier: Optional[str] = attrs.field()
    """
    Carrier required for EU VOC vendors only.
    """

    container_identifier: str = attrs.field()
    """
    The container identifier.
    """

    container_sequence_number: Optional[int] = attrs.field()
    """
    An integer that must be submitted for multi-box shipments only, where one item may come in separate packages.
    """

    container_type: Union[Literal["Carton"], Literal["Pallet"]] = attrs.field()
    """
    The type of container.
    """

    dimensions: Optional["Dimensions"] = attrs.field()

    manifest_date: Optional[str] = attrs.field()
    """
    The date of the manifest.
    """

    manifest_id: Optional[str] = attrs.field()
    """
    The manifest identifier.
    """

    packed_items: List["PackedItem"] = attrs.field()
    """
    A list of packed items.
    """

    scac_code: Optional[str] = attrs.field()
    """
    SCAC code required for NA VOC vendors only.
    """

    ship_method: Optional[str] = attrs.field()
    """
    The shipment method.
    """

    tracking_number: Optional[str] = attrs.field()
    """
    The tracking number.
    """

    weight: Optional["Weight"] = attrs.field()


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

    length: "Decimal" = attrs.field()

    unit_of_measure: Union[Literal["IN"], Literal["CM"]] = attrs.field()
    """
    The unit of measure for dimensions.
    """

    width: "Decimal" = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field()
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    errors: List["Error"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetCustomerInvoiceResponse:
    """
    The response schema for the getCustomerInvoice operation.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["CustomerInvoice"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetCustomerInvoicesResponse:
    """
    The response schema for the getCustomerInvoices operation.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["CustomerInvoiceList"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetShippingLabelListResponse:
    """
    The response schema for the getShippingLabels operation.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["ShippingLabelList"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetShippingLabelResponse:
    """
    The response schema for the getShippingLabel operation.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["ShippingLabel"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Item:
    """
    Details of the item being shipped.
    """

    buyer_product_identifier: Optional[str] = attrs.field()
    """
    Buyer's Standard Identification Number (ASIN) of an item. Either buyerProductIdentifier or vendorProductIdentifier is required.
    """

    item_sequence_number: int = attrs.field()
    """
    Item Sequence Number for the item. This must be the same value as sent in order for a given item.
    """

    shipped_quantity: "ItemQuantity" = attrs.field()

    vendor_product_identifier: Optional[str] = attrs.field()
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

    package_identifier: Optional[str] = attrs.field()
    """
    Identifier for the package. The first package will be 001, the second 002, and so on. This number is used as a reference to refer to this package from the pallet level.
    """

    ship_method: Optional[str] = attrs.field()
    """
    Ship method to be used for shipping the order. Amazon defines Ship Method Codes indicating shipping carrier and shipment service level. Ship Method Codes are case and format sensitive. The same ship method code should returned on the shipment confirmation. Note that the Ship Method Codes are vendor specific and will be provided to each vendor during the implementation.
    """

    ship_method_name: Optional[str] = attrs.field()
    """
    Shipping method name for internal reference.
    """

    tracking_number: Optional[str] = attrs.field()
    """
    Package tracking identifier from the shipping carrier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PackedItem:

    buyer_product_identifier: Optional[str] = attrs.field()
    """
    Buyer's Standard Identification Number (ASIN) of an item. Either buyerProductIdentifier or vendorProductIdentifier is required.
    """

    item_sequence_number: int = attrs.field()
    """
    Item Sequence Number for the item. This must be the same value as sent in the order for a given item.
    """

    packed_quantity: "ItemQuantity" = attrs.field()

    vendor_product_identifier: Optional[str] = attrs.field()
    """
    The vendor selected product identification of the item. Should be the same as was sent in the Purchase Order, like SKU Number.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Pagination:

    next_token: Optional[str] = attrs.field()
    """
    A generated string used to pass information to your next request. If NextToken is returned, pass the value of NextToken to the next request. If NextToken is not returned, there are no more order items to return.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartyIdentification:

    address: Optional["Address"] = attrs.field()

    party_id: str = attrs.field()
    """
    Assigned Identification for the party.
    """

    tax_registration_details: Optional[List["TaxRegistrationDetails"]] = attrs.field()
    """
    Tax registration details of the entity.
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

    containers: Optional[List["Container"]] = attrs.field()
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
class SubmitShippingLabelsRequest:

    shipping_label_requests: Optional[List["ShippingLabelRequest"]] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitShippingLabelsResponse:
    """
    The response schema for the submitShippingLabelRequest operation.
    """

    errors: Optional["ErrorList"] = attrs.field()

    payload: Optional["TransactionReference"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxRegistrationDetails:
    """
    Tax registration details of the entity.
    """

    tax_registration_address: Optional["Address"] = attrs.field()

    tax_registration_messages: Optional[str] = attrs.field()
    """
    Tax registration message that can be used for additional tax related details.
    """

    tax_registration_number: str = attrs.field()
    """
    Tax registration number for the party. For example, VAT ID.
    """

    tax_registration_type: Optional[Union[Literal["VAT"], Literal["GST"]]] = attrs.field()
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


class VendorDirectFulfillmentShipping20211228Client(BaseClient):
    def get_shipping_label(
        self,
        purchase_order_number: str,
    ):
        """
        Returns a shipping label for the purchaseOrderNumber that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            purchase_order_number: The purchase order number for which you want to return the shipping label. It should be the same purchaseOrderNumber as received in the order.
        """
        url = "/vendor/directFulfillment/shipping/2021-12-28/shippingLabels/{purchaseOrderNumber}"
        values = (purchase_order_number,)
        response = self._parse_args_and_request(url, "GET", values, self._get_shipping_label_params)
        return response

    _get_shipping_label_params = (("purchaseOrderNumber", "path"),)  # name, param in

    def get_shipping_labels(
        self,
        created_after: datetime,
        created_before: datetime,
        ship_from_party_id: str = None,
        limit: int = None,
        sort_order: Union[Literal["ASC"], Literal["DESC"]] = None,
        next_token: str = None,
    ):
        """
        Returns a list of shipping labels created during the time frame that you specify. You define that time frame using the createdAfter and createdBefore parameters. You must use both of these parameters. The date range to search must not be more than 7 days.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            ship_from_party_id: The vendor warehouseId for order fulfillment. If not specified, the result will contain orders for all warehouses.
            limit: The limit to the number of records returned.
            created_after: Shipping labels that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
            created_before: Shipping labels that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
            sort_order: Sort ASC or DESC by order creation date.
            next_token: Used for pagination when there are more ship labels than the specified result size limit. The token value is returned in the previous API call.
        """
        url = "/vendor/directFulfillment/shipping/2021-12-28/shippingLabels"
        values = (
            ship_from_party_id,
            limit,
            created_after,
            created_before,
            sort_order,
            next_token,
        )
        response = self._parse_args_and_request(url, "GET", values, self._get_shipping_labels_params)
        return response

    _get_shipping_labels_params = (  # name, param in
        ("shipFromPartyId", "query"),
        ("limit", "query"),
        ("createdAfter", "query"),
        ("createdBefore", "query"),
        ("sortOrder", "query"),
        ("nextToken", "query"),
    )

    def submit_shipping_label_request(
        self,
        shipping_label_requests: List["ShippingLabelRequest"] = None,
    ):
        """
        Creates a shipping label for a purchase order and returns a transactionId for reference.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            shipping_label_requests: no description.
        """
        url = "/vendor/directFulfillment/shipping/2021-12-28/shippingLabels"
        values = (shipping_label_requests,)
        response = self._parse_args_and_request(url, "POST", values, self._submit_shipping_label_request_params)
        return response

    _submit_shipping_label_request_params = (("shippingLabelRequests", "body"),)  # name, param in
