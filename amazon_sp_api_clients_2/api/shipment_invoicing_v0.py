"""
Selling Partner API for Shipment Invoicing
=============================================================================================

The Selling Partner API for Shipment Invoicing helps you programmatically retrieve shipment invoice information in the Brazil marketplace for a selling partner’s Fulfillment by Amazon (FBA) orders.
API Version: v0
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal
from datetime import date, datetime


@attrs.define
class Address:
    """
    The shipping address details of the shipment.
    """

    address_line1: str = attrs.field(
        kw_only=True,
    )
    """
    The street address.
    """

    address_line2: str = attrs.field(
        kw_only=True,
    )
    """
    Additional street address information, if required.
    """

    address_line3: str = attrs.field(
        kw_only=True,
    )
    """
    Additional street address information, if required.
    """

    address_type: "AddressTypeEnum" = attrs.field(
        kw_only=True,
    )

    city: str = attrs.field(
        kw_only=True,
    )
    """
    The city.
    """

    country_code: str = attrs.field(
        kw_only=True,
    )
    """
    The country code.
    """

    county: str = attrs.field(
        kw_only=True,
    )
    """
    The county.
    """

    district: str = attrs.field(
        kw_only=True,
    )
    """
    The district.
    """

    name: str = attrs.field(
        kw_only=True,
    )
    """
    The name.
    """

    phone: str = attrs.field(
        kw_only=True,
    )
    """
    The phone number.
    """

    postal_code: str = attrs.field(
        kw_only=True,
    )
    """
    The postal code.
    """

    state_or_region: str = attrs.field(
        kw_only=True,
    )
    """
    The state or region.
    """


@attrs.define
class AddressTypeEnum:
    """
    The shipping address type.
    """

    pass


@attrs.define
class Blob:
    """
    Shipment invoice document content.
    """

    pass


@attrs.define
class BuyerTaxInfo:
    """
    Tax information about the buyer.
    """

    company_legal_name: str = attrs.field(
        kw_only=True,
    )
    """
    The legal name of the company.
    """

    tax_classifications: "TaxClassificationList" = attrs.field(
        kw_only=True,
    )

    taxing_region: str = attrs.field(
        kw_only=True,
    )
    """
    The country or region imposing the tax.
    """


@attrs.define
class Error:
    """
    An error response returned when the request is unsuccessful.
    """

    code: str = attrs.field(
        kw_only=True,
    )
    """
    An error code that identifies the type of error that occurred.
    """

    details: str = attrs.field(
        kw_only=True,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field(
        kw_only=True,
    )
    """
    A message that describes the error condition.
    """


@attrs.define
class ErrorList:
    """
    A list of error responses returned when a request is unsuccessful.
    """

    pass


@attrs.define
class GetInvoiceStatusResponse:
    """
    The response schema for the getInvoiceStatus operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "ShipmentInvoiceStatusResponse" = attrs.field(
        kw_only=True,
    )


@attrs.define
class GetShipmentDetailsResponse:
    """
    The response schema for the getShipmentDetails operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )

    payload: "ShipmentDetail" = attrs.field(
        kw_only=True,
    )


@attrs.define
class MarketplaceTaxInfo:
    """
    Tax information about the marketplace.
    """

    company_legal_name: str = attrs.field(
        kw_only=True,
    )
    """
    The legal name of the company.
    """

    tax_classifications: "TaxClassificationList" = attrs.field(
        kw_only=True,
    )

    taxing_region: str = attrs.field(
        kw_only=True,
    )
    """
    The country or region imposing the tax.
    """


@attrs.define
class Money:
    """
    The currency type and amount.
    """

    amount: str = attrs.field(
        kw_only=True,
    )
    """
    The currency amount.
    """

    currency_code: str = attrs.field(
        kw_only=True,
    )
    """
    Three-digit currency code in ISO 4217 format.
    """


@attrs.define
class PaymentMethodDetailItemList:
    """
    The list of payment method details.
    """

    pass


@attrs.define
class SerialNumbersList:
    """
    The list of serial numbers.
    """

    pass


@attrs.define
class ShipmentDetail:
    """
    The information required by a selling partner to issue a shipment invoice.
    """

    amazon_order_id: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon-defined identifier for the order.
    """

    amazon_shipment_id: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon-defined identifier for the shipment.
    """

    buyer_county: str = attrs.field(
        kw_only=True,
    )
    """
    The county of the buyer.
    """

    buyer_name: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the buyer.
    """

    buyer_tax_info: "BuyerTaxInfo" = attrs.field(
        kw_only=True,
    )

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the marketplace where the order was placed.
    """

    marketplace_tax_info: "MarketplaceTaxInfo" = attrs.field(
        kw_only=True,
    )

    payment_method_details: "PaymentMethodDetailItemList" = attrs.field(
        kw_only=True,
    )

    purchase_date: datetime = attrs.field(
        kw_only=True,
    )
    """
    The date and time when the order was created.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    seller_display_name: str = attrs.field(
        kw_only=True,
    )
    """
    The seller’s friendly name registered in the marketplace.
    """

    seller_id: str = attrs.field(
        kw_only=True,
    )
    """
    The seller identifier.
    """

    shipment_items: "ShipmentItems" = attrs.field(
        kw_only=True,
    )

    shipping_address: "Address" = attrs.field(
        kw_only=True,
    )

    warehouse_id: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon-defined identifier for the warehouse.
    """


@attrs.define
class ShipmentInvoiceStatus:
    """
    The shipment invoice status.
    """

    pass


@attrs.define
class ShipmentInvoiceStatusInfo:
    """
    The shipment invoice status information.
    """

    amazon_shipment_id: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon-defined shipment identifier.
    """

    invoice_status: "ShipmentInvoiceStatus" = attrs.field(
        kw_only=True,
    )


@attrs.define
class ShipmentInvoiceStatusResponse:
    """
    The shipment invoice status response.
    """

    shipments: "ShipmentInvoiceStatusInfo" = attrs.field(
        kw_only=True,
    )


@attrs.define
class ShipmentItem:
    """
    The shipment item information required by a seller to issue a shipment invoice.
    """

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    gift_wrap_price: "Money" = attrs.field(
        kw_only=True,
    )

    item_price: "Money" = attrs.field(
        kw_only=True,
    )

    order_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon-defined identifier for the order item.
    """

    promotion_discount: "Money" = attrs.field(
        kw_only=True,
    )

    quantity_ordered: float = attrs.field(
        kw_only=True,
    )
    """
    The number of items ordered.
    """

    seller_sku: str = attrs.field(
        kw_only=True,
    )
    """
    The seller SKU of the item.
    """

    serial_numbers: "SerialNumbersList" = attrs.field(
        kw_only=True,
    )

    shipping_discount: "Money" = attrs.field(
        kw_only=True,
    )

    shipping_price: "Money" = attrs.field(
        kw_only=True,
    )

    title: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the item.
    """


@attrs.define
class ShipmentItems:
    """
    A list of shipment items.
    """

    pass


@attrs.define
class SubmitInvoiceRequest:
    """
    The request schema for the submitInvoice operation.
    """

    content_md5value: str = attrs.field(
        kw_only=True,
    )
    """
    MD5 sum for validating the invoice data. For more information about calculating this value, see [Working with Content-MD5 Checksums](https://docs.developer.amazonservices.com/en_US/dev_guide/DG_MD5.html).
    """

    invoice_content: "Blob" = attrs.field(
        kw_only=True,
    )

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    An Amazon marketplace identifier.
    """


@attrs.define
class SubmitInvoiceResponse:
    """
    The response schema for the submitInvoice operation.
    """

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )


@attrs.define
class TaxClassification:
    """
    The tax classification for the entity.
    """

    name: str = attrs.field(
        kw_only=True,
    )
    """
    The type of tax.
    """

    value: str = attrs.field(
        kw_only=True,
    )
    """
    The entity's tax identifier.
    """


@attrs.define
class TaxClassificationList:
    """
    The list of tax classifications.
    """

    pass


class ShipmentInvoicingV0Client(BaseClient):
    def get_invoice_status(
        self,
        shipment_id: str,
    ):
        """
        Returns the invoice status for the shipment you specify.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 1.133 | 25 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: The shipment identifier for the shipment.
        """
        url = "/fba/outbound/brazil/v0/shipments/{shipmentId}/invoice/status"
        values = (shipment_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_invoice_status_params)
        return response

    _get_invoice_status_params = (("shipmentId", "path"),)  # name, param in

    def get_shipment_details(
        self,
        shipment_id: str,
    ):
        """
        Returns the shipment details required to issue an invoice for the specified shipment.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 1.133 | 25 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: The identifier for the shipment. Get this value from the FBAOutboundShipmentStatus notification. For information about subscribing to notifications, see the [Notifications API Use Case Guide](doc:notifications-api-v1-use-case-guide).
        """
        url = "/fba/outbound/brazil/v0/shipments/{shipmentId}"
        values = (shipment_id,)
        response = self._parse_args_and_request(url, "GET", values, self._get_shipment_details_params)
        return response

    _get_shipment_details_params = (("shipmentId", "path"),)  # name, param in

    def submit_invoice(
        self,
        shipment_id: str,
        content_md5value: str,
        invoice_content: bytes,
        marketplace_id: str = None,
    ):
        """
        Submits a shipment invoice document for a given shipment.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 1.133 | 25 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: The identifier for the shipment.
            content_md5value: MD5 sum for validating the invoice data. For more information about calculating this value, see [Working with Content-MD5 Checksums](https://docs.developer.amazonservices.com/en_US/dev_guide/DG_MD5.html).
            invoice_content: Shipment invoice document content.
            marketplace_id: An Amazon marketplace identifier.
        """
        url = "/fba/outbound/brazil/v0/shipments/{shipmentId}/invoice"
        values = (
            shipment_id,
            content_md5value,
            invoice_content,
            marketplace_id,
        )
        response = self._parse_args_and_request(url, "POST", values, self._submit_invoice_params)
        return response

    _submit_invoice_params = (  # name, param in
        ("shipmentId", "path"),
        ("ContentMD5Value", "body"),
        ("InvoiceContent", "body"),
        ("MarketplaceId", "body"),
    )
