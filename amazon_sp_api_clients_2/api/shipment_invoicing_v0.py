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
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class Address:
    """
    The shipping address details of the shipment.
    """

    address_line1: Optional[str] = attrs.field()
    """
    The street address.
    """

    address_line2: Optional[str] = attrs.field()
    """
    Additional street address information, if required.
    """

    address_line3: Optional[str] = attrs.field()
    """
    Additional street address information, if required.
    """

    address_type: Optional["AddressTypeEnum"] = attrs.field()
    """
    The shipping address type.
    """

    city: Optional[str] = attrs.field()
    """
    The city.
    """

    country_code: Optional[str] = attrs.field()
    """
    The country code.
    """

    county: Optional[str] = attrs.field()
    """
    The county.
    """

    district: Optional[str] = attrs.field()
    """
    The district.
    """

    name: Optional[str] = attrs.field()
    """
    The name.
    """

    phone: Optional[str] = attrs.field()
    """
    The phone number.
    """

    postal_code: Optional[str] = attrs.field()
    """
    The postal code.
    """

    state_or_region: Optional[str] = attrs.field()
    """
    The state or region.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class AddressTypeEnum:
    """
    The shipping address type.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Blob:
    """
    Shipment invoice document content.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class BuyerTaxInfo:
    """
    Tax information about the buyer.
    """

    company_legal_name: Optional[str] = attrs.field()
    """
    The legal name of the company.
    """

    tax_classifications: Optional[List["TaxClassification"]] = attrs.field()
    """
    The list of tax classifications.
    """

    taxing_region: Optional[str] = attrs.field()
    """
    The country or region imposing the tax.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    An error response returned when the request is unsuccessful.
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
class GetInvoiceStatusResponse:
    """
    The response schema for the getInvoiceStatus operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["ShipmentInvoiceStatusResponse"] = attrs.field()
    """
    The shipment invoice status response.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetShipmentDetailsResponse:
    """
    The response schema for the getShipmentDetails operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["ShipmentDetail"] = attrs.field()
    """
    The information required by a selling partner to issue a shipment invoice.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class MarketplaceTaxInfo:
    """
    Tax information about the marketplace.
    """

    company_legal_name: Optional[str] = attrs.field()
    """
    The legal name of the company.
    """

    tax_classifications: Optional[List["TaxClassification"]] = attrs.field()
    """
    The list of tax classifications.
    """

    taxing_region: Optional[str] = attrs.field()
    """
    The country or region imposing the tax.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Money:
    """
    The currency type and amount.
    """

    amount: Optional[str] = attrs.field()
    """
    The currency amount.
    """

    currency_code: Optional[str] = attrs.field()
    """
    Three-digit currency code in ISO 4217 format.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentDetail:
    """
    The information required by a selling partner to issue a shipment invoice.
    """

    amazon_order_id: Optional[str] = attrs.field()
    """
    The Amazon-defined identifier for the order.
    """

    amazon_shipment_id: Optional[str] = attrs.field()
    """
    The Amazon-defined identifier for the shipment.
    """

    buyer_county: Optional[str] = attrs.field()
    """
    The county of the buyer.
    """

    buyer_name: Optional[str] = attrs.field()
    """
    The name of the buyer.
    """

    buyer_tax_info: Optional["BuyerTaxInfo"] = attrs.field()
    """
    Tax information about the buyer.
    """

    marketplace_id: Optional[str] = attrs.field()
    """
    The identifier for the marketplace where the order was placed.
    """

    marketplace_tax_info: Optional["MarketplaceTaxInfo"] = attrs.field()
    """
    Tax information about the marketplace.
    """

    payment_method_details: Optional[List[str]] = attrs.field()
    """
    The list of payment method details.
    """

    purchase_date: Optional[datetime] = attrs.field()
    """
    The date and time when the order was created.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    seller_display_name: Optional[str] = attrs.field()
    """
    The seller’s friendly name registered in the marketplace.
    """

    seller_id: Optional[str] = attrs.field()
    """
    The seller identifier.
    """

    shipment_items: Optional[List["ShipmentItem"]] = attrs.field()
    """
    A list of shipment items.
    """

    shipping_address: Optional["Address"] = attrs.field()
    """
    The shipping address details of the shipment.
    """

    warehouse_id: Optional[str] = attrs.field()
    """
    The Amazon-defined identifier for the warehouse.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentInvoiceStatus:
    """
    The shipment invoice status.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentInvoiceStatusInfo:
    """
    The shipment invoice status information.
    """

    amazon_shipment_id: Optional[str] = attrs.field()
    """
    The Amazon-defined shipment identifier.
    """

    invoice_status: Optional["ShipmentInvoiceStatus"] = attrs.field()
    """
    The shipment invoice status.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentInvoiceStatusResponse:
    """
    The shipment invoice status response.
    """

    shipments: Optional["ShipmentInvoiceStatusInfo"] = attrs.field()
    """
    The shipment invoice status information.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentItem:
    """
    The shipment item information required by a seller to issue a shipment invoice.
    """

    asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    gift_wrap_price: Optional["Money"] = attrs.field()
    """
    The currency type and amount.
    """

    item_price: Optional["Money"] = attrs.field()
    """
    The currency type and amount.
    """

    order_item_id: Optional[str] = attrs.field()
    """
    The Amazon-defined identifier for the order item.
    """

    promotion_discount: Optional["Money"] = attrs.field()
    """
    The currency type and amount.
    """

    quantity_ordered: Optional[float] = attrs.field()
    """
    The number of items ordered.
    """

    seller_sku: Optional[str] = attrs.field()
    """
    The seller SKU of the item.
    """

    serial_numbers: Optional[List[str]] = attrs.field()
    """
    The list of serial numbers.
    """

    shipping_discount: Optional["Money"] = attrs.field()
    """
    The currency type and amount.
    """

    shipping_price: Optional["Money"] = attrs.field()
    """
    The currency type and amount.
    """

    title: Optional[str] = attrs.field()
    """
    The name of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitInvoiceRequest:
    """
    The request schema for the submitInvoice operation.
    """

    content_md5value: str = attrs.field()
    """
    MD5 sum for validating the invoice data. For more information about calculating this value, see [Working with Content-MD5 Checksums](https://docs.developer.amazonservices.com/en_US/dev_guide/DG_MD5.html).
    """

    invoice_content: "Blob" = attrs.field()
    """
    Shipment invoice document content.
    """

    marketplace_id: Optional[str] = attrs.field()
    """
    An Amazon marketplace identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitInvoiceResponse:
    """
    The response schema for the submitInvoice operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxClassification:
    """
    The tax classification for the entity.
    """

    name: Optional[str] = attrs.field()
    """
    The type of tax.
    """

    value: Optional[str] = attrs.field()
    """
    The entity's tax identifier.
    """


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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_invoice_status_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _get_invoice_status_params = (("shipmentId", "path"),)  # name, param in

    _get_invoice_status_responses = {
        (200, "application/json"): GetInvoiceStatusResponse,
        (400, "application/json"): GetInvoiceStatusResponse,
        (401, "application/json"): GetInvoiceStatusResponse,
        (403, "application/json"): GetInvoiceStatusResponse,
        (404, "application/json"): GetInvoiceStatusResponse,
        (415, "application/json"): GetInvoiceStatusResponse,
        (429, "application/json"): GetInvoiceStatusResponse,
        (500, "application/json"): GetInvoiceStatusResponse,
        (503, "application/json"): GetInvoiceStatusResponse,
    }

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
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_shipment_details_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _get_shipment_details_params = (("shipmentId", "path"),)  # name, param in

    _get_shipment_details_responses = {
        (200, "application/json"): GetShipmentDetailsResponse,
        (400, "application/json"): GetShipmentDetailsResponse,
        (401, "application/json"): GetShipmentDetailsResponse,
        (403, "application/json"): GetShipmentDetailsResponse,
        (404, "application/json"): GetShipmentDetailsResponse,
        (415, "application/json"): GetShipmentDetailsResponse,
        (429, "application/json"): GetShipmentDetailsResponse,
        (500, "application/json"): GetShipmentDetailsResponse,
        (503, "application/json"): GetShipmentDetailsResponse,
    }

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
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._submit_invoice_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        obj = klass(**response.json())
        return obj

    _submit_invoice_params = (  # name, param in
        ("shipmentId", "path"),
        ("ContentMD5Value", "body"),
        ("InvoiceContent", "body"),
        ("MarketplaceId", "body"),
    )

    _submit_invoice_responses = {
        (200, "application/json"): SubmitInvoiceResponse,
        (400, "application/json"): SubmitInvoiceResponse,
        (401, "application/json"): SubmitInvoiceResponse,
        (403, "application/json"): SubmitInvoiceResponse,
        (404, "application/json"): SubmitInvoiceResponse,
        (415, "application/json"): SubmitInvoiceResponse,
        (429, "application/json"): SubmitInvoiceResponse,
        (500, "application/json"): SubmitInvoiceResponse,
        (503, "application/json"): SubmitInvoiceResponse,
    }
