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


@attrs.define
class Address:

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

    address_type: "AddressTypeEnum" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class AddressTypeEnum:

    pass


@attrs.define
class Blob:

    pass


@attrs.define
class BuyerTaxInfo:

    company_legal_name: str = attrs.field(
        kw_only=True,
    )
    """
    The legal name of the company.
    """

    taxing_region: str = attrs.field(
        kw_only=True,
    )
    """
    The country or region imposing the tax.
    """

    tax_classifications: "TaxClassificationList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Error:

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

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class GetInvoiceStatusResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "ShipmentInvoiceStatusResponse" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class GetShipmentDetailsResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payload: "ShipmentDetail" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class MarketplaceTaxInfo:

    company_legal_name: str = attrs.field(
        kw_only=True,
    )
    """
    The legal name of the company.
    """

    taxing_region: str = attrs.field(
        kw_only=True,
    )
    """
    The country or region imposing the tax.
    """

    tax_classifications: "TaxClassificationList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class Money:

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

    pass


@attrs.define
class PaymentMethodDetailItemList:

    pass


@attrs.define
class SerialNumbersList:

    pass


@attrs.define
class ShipmentDetail:

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

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    The identifier for the marketplace where the order was placed.
    """

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

    warehouse_id: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon-defined identifier for the warehouse.
    """

    buyer_tax_info: "BuyerTaxInfo" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    marketplace_tax_info: "MarketplaceTaxInfo" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    payment_method_details: "PaymentMethodDetailItemList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipment_items: "ShipmentItems" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_address: "Address" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ShipmentInvoiceStatus:

    pass


@attrs.define
class ShipmentInvoiceStatusInfo:

    amazon_shipment_id: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon-defined shipment identifier.
    """

    invoice_status: "ShipmentInvoiceStatus" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ShipmentInvoiceStatusResponse:

    shipments: "ShipmentInvoiceStatusInfo" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ShipmentItem:

    asin: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    order_item_id: str = attrs.field(
        kw_only=True,
    )
    """
    The Amazon-defined identifier for the order item.
    """

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

    title: str = attrs.field(
        kw_only=True,
    )
    """
    The name of the item.
    """

    gift_wrap_price: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    item_price: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    promotion_discount: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    serial_numbers: "SerialNumbersList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_discount: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    shipping_price: "Money" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class ShipmentItems:

    pass


@attrs.define
class SubmitInvoiceRequest:

    content_md5value: str = attrs.field(
        kw_only=True,
    )
    """
    MD5 sum for validating the invoice data. For more information about calculating this value, see [Working with Content-MD5 Checksums](https://docs.developer.amazonservices.com/en_US/dev_guide/DG_MD5.html).
    """

    marketplace_id: str = attrs.field(
        kw_only=True,
    )
    """
    An Amazon marketplace identifier.
    """

    invoice_content: "Blob" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class SubmitInvoiceResponse:

    errors: "ErrorList" = attrs.field(
        kw_only=True,
    )
    """
    no description.
    """

    pass


@attrs.define
class TaxClassification:

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

    pass


@attrs.define
class TaxClassificationList:

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
        invoice_content: bytes,
        content_md5value: str,
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
            invoice_content: Shipment invoice document content.
            marketplace_id: An Amazon marketplace identifier.
            content_md5value: MD5 sum for validating the invoice data. For more information about calculating this value, see [Working with Content-MD5 Checksums](https://docs.developer.amazonservices.com/en_US/dev_guide/DG_MD5.html).
        """
        url = "/fba/outbound/brazil/v0/shipments/{shipmentId}/invoice"
        values = (
            shipment_id,
            invoice_content,
            marketplace_id,
            content_md5value,
        )
        response = self._parse_args_and_request(url, "POST", values, self._submit_invoice_params)
        return response

    _submit_invoice_params = (  # name, param in
        ("shipmentId", "path"),
        ("InvoiceContent", "body"),
        ("MarketplaceId", "body"),
        ("ContentMD5Value", "body"),
    )
