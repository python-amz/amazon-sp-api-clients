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

    address_line1: str = attrs.field()
    address_line2: str = attrs.field()
    address_line3: str = attrs.field()
    city: str = attrs.field()
    country_code: str = attrs.field()
    county: str = attrs.field()
    district: str = attrs.field()
    name: str = attrs.field()
    phone: str = attrs.field()
    postal_code: str = attrs.field()
    state_or_region: str = attrs.field()

    address_type: "AddressTypeEnum" = attrs.field()
    pass


@attrs.define
class AddressTypeEnum:

    pass


@attrs.define
class Blob:

    pass


@attrs.define
class BuyerTaxInfo:

    company_legal_name: str = attrs.field()
    taxing_region: str = attrs.field()

    tax_classifications: "TaxClassificationList" = attrs.field()
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
class GetInvoiceStatusResponse:

    errors: "ErrorList" = attrs.field()
    payload: "ShipmentInvoiceStatusResponse" = attrs.field()
    pass


@attrs.define
class GetShipmentDetailsResponse:

    errors: "ErrorList" = attrs.field()
    payload: "ShipmentDetail" = attrs.field()
    pass


@attrs.define
class MarketplaceTaxInfo:

    company_legal_name: str = attrs.field()
    taxing_region: str = attrs.field()

    tax_classifications: "TaxClassificationList" = attrs.field()
    pass


@attrs.define
class Money:

    amount: str = attrs.field()
    currency_code: str = attrs.field()

    pass


@attrs.define
class PaymentMethodDetailItemList:

    pass


@attrs.define
class SerialNumbersList:

    pass


@attrs.define
class ShipmentDetail:

    amazon_order_id: str = attrs.field()
    amazon_shipment_id: str = attrs.field()
    buyer_county: str = attrs.field()
    buyer_name: str = attrs.field()
    marketplace_id: str = attrs.field()
    purchase_date: str = attrs.field()
    # {'schema_format': 'date-time'}
    seller_display_name: str = attrs.field()
    seller_id: str = attrs.field()
    warehouse_id: str = attrs.field()

    buyer_tax_info: "BuyerTaxInfo" = attrs.field()
    marketplace_tax_info: "MarketplaceTaxInfo" = attrs.field()
    payment_method_details: "PaymentMethodDetailItemList" = attrs.field()
    shipment_items: "ShipmentItems" = attrs.field()
    shipping_address: "Address" = attrs.field()
    pass


@attrs.define
class ShipmentInvoiceStatus:

    pass


@attrs.define
class ShipmentInvoiceStatusInfo:

    amazon_shipment_id: str = attrs.field()

    invoice_status: "ShipmentInvoiceStatus" = attrs.field()
    pass


@attrs.define
class ShipmentInvoiceStatusResponse:

    shipments: "ShipmentInvoiceStatusInfo" = attrs.field()
    pass


@attrs.define
class ShipmentItem:

    asin: str = attrs.field()
    order_item_id: str = attrs.field()
    quantity_ordered: Union[float, int] = attrs.field()
    seller_sku: str = attrs.field()
    title: str = attrs.field()

    gift_wrap_price: "Money" = attrs.field()
    item_price: "Money" = attrs.field()
    promotion_discount: "Money" = attrs.field()
    serial_numbers: "SerialNumbersList" = attrs.field()
    shipping_discount: "Money" = attrs.field()
    shipping_price: "Money" = attrs.field()
    pass


@attrs.define
class ShipmentItems:

    pass


@attrs.define
class SubmitInvoiceRequest:

    content_md5value: str = attrs.field()
    marketplace_id: str = attrs.field()

    invoice_content: "Blob" = attrs.field()
    pass


@attrs.define
class SubmitInvoiceResponse:

    errors: "ErrorList" = attrs.field()
    pass


@attrs.define
class TaxClassification:

    name: str = attrs.field()
    value: str = attrs.field()

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
        invoice_content: str,
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
