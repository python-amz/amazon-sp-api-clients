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

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _address_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Address(**data)

    address_line1: Optional[str] = attrs.field(
        default=None,
    )
    """
    The street address.
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

    address_type: Optional["AddressTypeEnum"] = attrs.field(
        default=None,
    )
    """
    The shipping address type.
    """

    city: Optional[str] = attrs.field(
        default=None,
    )
    """
    The city.
    """

    country_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The country code.
    """

    county: Optional[str] = attrs.field(
        default=None,
    )
    """
    The county.
    """

    district: Optional[str] = attrs.field(
        default=None,
    )
    """
    The district.
    """

    name: Optional[str] = attrs.field(
        default=None,
    )
    """
    The name.
    """

    phone: Optional[str] = attrs.field(
        default=None,
    )
    """
    The phone number.
    """

    postal_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    The postal code.
    """

    state_or_region: Optional[str] = attrs.field(
        default=None,
    )
    """
    The state or region.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class AddressTypeEnum:
    """
    The shipping address type.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _address_type_enum_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return AddressTypeEnum(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Blob:
    """
    Shipment invoice document content.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _blob_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Blob(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class BuyerTaxInfo:
    """
    Tax information about the buyer.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _buyer_tax_info_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return BuyerTaxInfo(**data)

    company_legal_name: Optional[str] = attrs.field(
        default=None,
    )
    """
    The legal name of the company.
    """

    tax_classifications: Optional[List["TaxClassification"]] = attrs.field(
        default=None,
    )
    """
    The list of tax classifications.
    """

    taxing_region: Optional[str] = attrs.field(
        default=None,
    )
    """
    The country or region imposing the tax.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    An error response returned when the request is unsuccessful.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _error_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Error(**data)

    code: str = attrs.field(
        default=None,
    )
    """
    An error code that identifies the type of error that occurred.
    """

    details: Optional[str] = attrs.field(
        default=None,
    )
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field(
        default=None,
    )
    """
    A message that describes the error condition.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetInvoiceStatusResponse:
    """
    The response schema for the getInvoiceStatus operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_invoice_status_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return GetInvoiceStatusResponse(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["ShipmentInvoiceStatusResponse"] = attrs.field(
        default=None,
    )
    """
    The shipment invoice status response.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetShipmentDetailsResponse:
    """
    The response schema for the getShipmentDetails operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _get_shipment_details_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return GetShipmentDetailsResponse(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["ShipmentDetail"] = attrs.field(
        default=None,
    )
    """
    The information required by a selling partner to issue a shipment invoice.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class MarketplaceTaxInfo:
    """
    Tax information about the marketplace.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _marketplace_tax_info_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return MarketplaceTaxInfo(**data)

    company_legal_name: Optional[str] = attrs.field(
        default=None,
    )
    """
    The legal name of the company.
    """

    tax_classifications: Optional[List["TaxClassification"]] = attrs.field(
        default=None,
    )
    """
    The list of tax classifications.
    """

    taxing_region: Optional[str] = attrs.field(
        default=None,
    )
    """
    The country or region imposing the tax.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Money:
    """
    The currency type and amount.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _money_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return Money(**data)

    amount: Optional[str] = attrs.field(
        default=None,
    )
    """
    The currency amount.
    """

    currency_code: Optional[str] = attrs.field(
        default=None,
    )
    """
    Three-digit currency code in ISO 4217 format.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentDetail:
    """
    The information required by a selling partner to issue a shipment invoice.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _shipment_detail_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ShipmentDetail(**data)

    amazon_order_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The Amazon-defined identifier for the order.
    """

    amazon_shipment_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The Amazon-defined identifier for the shipment.
    """

    buyer_county: Optional[str] = attrs.field(
        default=None,
    )
    """
    The county of the buyer.
    """

    buyer_name: Optional[str] = attrs.field(
        default=None,
    )
    """
    The name of the buyer.
    """

    buyer_tax_info: Optional["BuyerTaxInfo"] = attrs.field(
        default=None,
    )
    """
    Tax information about the buyer.
    """

    marketplace_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The identifier for the marketplace where the order was placed.
    """

    marketplace_tax_info: Optional["MarketplaceTaxInfo"] = attrs.field(
        default=None,
    )
    """
    Tax information about the marketplace.
    """

    payment_method_details: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    The list of payment method details.
    """

    purchase_date: Optional[datetime] = attrs.field(
        default=None,
    )
    """
    The date and time when the order was created.

    Extra fields:
    {'schema_format': 'date-time'}
    """

    seller_display_name: Optional[str] = attrs.field(
        default=None,
    )
    """
    The seller’s friendly name registered in the marketplace.
    """

    seller_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The seller identifier.
    """

    shipment_items: Optional[List["ShipmentItem"]] = attrs.field(
        default=None,
    )
    """
    A list of shipment items.
    """

    shipping_address: Optional["Address"] = attrs.field(
        default=None,
    )
    """
    The shipping address details of the shipment.
    """

    warehouse_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The Amazon-defined identifier for the warehouse.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentInvoiceStatus:
    """
    The shipment invoice status.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _shipment_invoice_status_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ShipmentInvoiceStatus(**data)

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentInvoiceStatusInfo:
    """
    The shipment invoice status information.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _shipment_invoice_status_info_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ShipmentInvoiceStatusInfo(**data)

    amazon_shipment_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The Amazon-defined shipment identifier.
    """

    invoice_status: Optional["ShipmentInvoiceStatus"] = attrs.field(
        default=None,
    )
    """
    The shipment invoice status.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentInvoiceStatusResponse:
    """
    The shipment invoice status response.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _shipment_invoice_status_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ShipmentInvoiceStatusResponse(**data)

    shipments: Optional["ShipmentInvoiceStatusInfo"] = attrs.field(
        default=None,
    )
    """
    The shipment invoice status information.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentItem:
    """
    The shipment item information required by a seller to issue a shipment invoice.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _shipment_item_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return ShipmentItem(**data)

    asin: Optional[str] = attrs.field(
        default=None,
    )
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    gift_wrap_price: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The currency type and amount.
    """

    item_price: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The currency type and amount.
    """

    order_item_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    The Amazon-defined identifier for the order item.
    """

    promotion_discount: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The currency type and amount.
    """

    quantity_ordered: Optional[float] = attrs.field(
        default=None,
    )
    """
    The number of items ordered.
    """

    seller_sku: Optional[str] = attrs.field(
        default=None,
    )
    """
    The seller SKU of the item.
    """

    serial_numbers: Optional[List[str]] = attrs.field(
        default=None,
    )
    """
    The list of serial numbers.
    """

    shipping_discount: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The currency type and amount.
    """

    shipping_price: Optional["Money"] = attrs.field(
        default=None,
    )
    """
    The currency type and amount.
    """

    title: Optional[str] = attrs.field(
        default=None,
    )
    """
    The name of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitInvoiceRequest:
    """
    The request schema for the submitInvoice operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _submit_invoice_request_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return SubmitInvoiceRequest(**data)

    content_md5value: str = attrs.field(
        default=None,
    )
    """
    MD5 sum for validating the invoice data. For more information about calculating this value, see [Working with Content-MD5 Checksums](https://docs.developer.amazonservices.com/en_US/dev_guide/DG_MD5.html).
    """

    invoice_content: "Blob" = attrs.field(
        default=None,
    )
    """
    Shipment invoice document content.
    """

    marketplace_id: Optional[str] = attrs.field(
        default=None,
    )
    """
    An Amazon marketplace identifier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SubmitInvoiceResponse:
    """
    The response schema for the submitInvoice operation.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _submit_invoice_response_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return SubmitInvoiceResponse(**data)

    errors: Optional[List["Error"]] = attrs.field(
        default=None,
    )
    """
    A list of error responses returned when a request is unsuccessful.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TaxClassification:
    """
    The tax classification for the entity.
    """

    @classmethod
    def from_json(cls, data: dict):
        name_convert = _tax_classification_name_convert
        data = {name_convert[k]: v for k, v in data.items()}
        return TaxClassification(**data)

    name: Optional[str] = attrs.field(
        default=None,
    )
    """
    The type of tax.
    """

    value: Optional[str] = attrs.field(
        default=None,
    )
    """
    The entity's tax identifier.
    """


_address_name_convert = {
    "AddressLine1": "address_line1",
    "AddressLine2": "address_line2",
    "AddressLine3": "address_line3",
    "AddressType": "address_type",
    "City": "city",
    "CountryCode": "country_code",
    "County": "county",
    "District": "district",
    "Name": "name",
    "Phone": "phone",
    "PostalCode": "postal_code",
    "StateOrRegion": "state_or_region",
}

_address_type_enum_name_convert = {}

_blob_name_convert = {}

_buyer_tax_info_name_convert = {
    "CompanyLegalName": "company_legal_name",
    "TaxClassifications": "tax_classifications",
    "TaxingRegion": "taxing_region",
}

_error_name_convert = {
    "code": "code",
    "details": "details",
    "message": "message",
}

_get_invoice_status_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_get_shipment_details_response_name_convert = {
    "errors": "errors",
    "payload": "payload",
}

_marketplace_tax_info_name_convert = {
    "CompanyLegalName": "company_legal_name",
    "TaxClassifications": "tax_classifications",
    "TaxingRegion": "taxing_region",
}

_money_name_convert = {
    "Amount": "amount",
    "CurrencyCode": "currency_code",
}

_shipment_detail_name_convert = {
    "AmazonOrderId": "amazon_order_id",
    "AmazonShipmentId": "amazon_shipment_id",
    "BuyerCounty": "buyer_county",
    "BuyerName": "buyer_name",
    "BuyerTaxInfo": "buyer_tax_info",
    "MarketplaceId": "marketplace_id",
    "MarketplaceTaxInfo": "marketplace_tax_info",
    "PaymentMethodDetails": "payment_method_details",
    "PurchaseDate": "purchase_date",
    "SellerDisplayName": "seller_display_name",
    "SellerId": "seller_id",
    "ShipmentItems": "shipment_items",
    "ShippingAddress": "shipping_address",
    "WarehouseId": "warehouse_id",
}

_shipment_invoice_status_name_convert = {}

_shipment_invoice_status_info_name_convert = {
    "AmazonShipmentId": "amazon_shipment_id",
    "InvoiceStatus": "invoice_status",
}

_shipment_invoice_status_response_name_convert = {
    "Shipments": "shipments",
}

_shipment_item_name_convert = {
    "ASIN": "asin",
    "GiftWrapPrice": "gift_wrap_price",
    "ItemPrice": "item_price",
    "OrderItemId": "order_item_id",
    "PromotionDiscount": "promotion_discount",
    "QuantityOrdered": "quantity_ordered",
    "SellerSKU": "seller_sku",
    "SerialNumbers": "serial_numbers",
    "ShippingDiscount": "shipping_discount",
    "ShippingPrice": "shipping_price",
    "Title": "title",
}

_submit_invoice_request_name_convert = {
    "ContentMD5Value": "content_md5value",
    "InvoiceContent": "invoice_content",
    "MarketplaceId": "marketplace_id",
}

_submit_invoice_response_name_convert = {
    "errors": "errors",
}

_tax_classification_name_convert = {
    "Name": "name",
    "Value": "value",
}


class ShipmentInvoicingV0Client(BaseClient):
    def get_invoice_status(
        self,
        shipment_id: str,
    ) -> Union[GetInvoiceStatusResponse]:
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
            self._get_invoice_status_responses,
        )
        return response

    _get_invoice_status_params = (("shipmentId", "path"),)  # name, param in

    _get_invoice_status_responses = {
        200: GetInvoiceStatusResponse,
        400: GetInvoiceStatusResponse,
        401: GetInvoiceStatusResponse,
        403: GetInvoiceStatusResponse,
        404: GetInvoiceStatusResponse,
        415: GetInvoiceStatusResponse,
        429: GetInvoiceStatusResponse,
        500: GetInvoiceStatusResponse,
        503: GetInvoiceStatusResponse,
    }

    def get_shipment_details(
        self,
        shipment_id: str,
    ) -> Union[GetShipmentDetailsResponse]:
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
            self._get_shipment_details_responses,
        )
        return response

    _get_shipment_details_params = (("shipmentId", "path"),)  # name, param in

    _get_shipment_details_responses = {
        200: GetShipmentDetailsResponse,
        400: GetShipmentDetailsResponse,
        401: GetShipmentDetailsResponse,
        403: GetShipmentDetailsResponse,
        404: GetShipmentDetailsResponse,
        415: GetShipmentDetailsResponse,
        429: GetShipmentDetailsResponse,
        500: GetShipmentDetailsResponse,
        503: GetShipmentDetailsResponse,
    }

    def submit_invoice(
        self,
        shipment_id: str,
        content_md5value: str,
        invoice_content: bytes,
        marketplace_id: str = None,
    ) -> Union[SubmitInvoiceResponse]:
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
            self._submit_invoice_responses,
        )
        return response

    _submit_invoice_params = (  # name, param in
        ("shipmentId", "path"),
        ("ContentMD5Value", "body"),
        ("InvoiceContent", "body"),
        ("MarketplaceId", "body"),
    )

    _submit_invoice_responses = {
        200: SubmitInvoiceResponse,
        400: SubmitInvoiceResponse,
        401: SubmitInvoiceResponse,
        403: SubmitInvoiceResponse,
        404: SubmitInvoiceResponse,
        415: SubmitInvoiceResponse,
        429: SubmitInvoiceResponse,
        500: SubmitInvoiceResponse,
        503: SubmitInvoiceResponse,
    }
