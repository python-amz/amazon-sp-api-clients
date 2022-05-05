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

    address_line1: str
    address_line2: str
    address_line3: str
    city: str
    country_code: str
    county: str
    district: str
    name: str
    phone: str
    postal_code: str
    state_or_region: str

    address_type: "AddressTypeEnum"
    pass


@attrs.define
class AddressTypeEnum:

    pass


@attrs.define
class Blob:

    pass


@attrs.define
class BuyerTaxInfo:

    company_legal_name: str
    taxing_region: str

    tax_classifications: "TaxClassificationList"
    pass


@attrs.define
class Error:

    code: str
    details: str
    message: str

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class GetInvoiceStatusResponse:

    errors: "ErrorList"
    payload: "ShipmentInvoiceStatusResponse"
    pass


@attrs.define
class GetShipmentDetailsResponse:

    errors: "ErrorList"
    payload: "ShipmentDetail"
    pass


@attrs.define
class MarketplaceTaxInfo:

    company_legal_name: str
    taxing_region: str

    tax_classifications: "TaxClassificationList"
    pass


@attrs.define
class Money:

    amount: str
    currency_code: str

    pass


@attrs.define
class PaymentMethodDetailItemList:

    pass


@attrs.define
class SerialNumbersList:

    pass


@attrs.define
class ShipmentDetail:

    amazon_order_id: str
    amazon_shipment_id: str
    buyer_county: str
    buyer_name: str
    marketplace_id: str
    purchase_date: str
    # {'schema_format': 'date-time'}
    seller_display_name: str
    seller_id: str
    warehouse_id: str

    buyer_tax_info: "BuyerTaxInfo"
    marketplace_tax_info: "MarketplaceTaxInfo"
    payment_method_details: "PaymentMethodDetailItemList"
    shipment_items: "ShipmentItems"
    shipping_address: "Address"
    pass


@attrs.define
class ShipmentInvoiceStatus:

    pass


@attrs.define
class ShipmentInvoiceStatusInfo:

    amazon_shipment_id: str

    invoice_status: "ShipmentInvoiceStatus"
    pass


@attrs.define
class ShipmentInvoiceStatusResponse:

    shipments: "ShipmentInvoiceStatusInfo"
    pass


@attrs.define
class ShipmentItem:

    asin: str
    order_item_id: str
    quantity_ordered: Union[float, int]
    seller_sku: str
    title: str

    gift_wrap_price: "Money"
    item_price: "Money"
    promotion_discount: "Money"
    serial_numbers: "SerialNumbersList"
    shipping_discount: "Money"
    shipping_price: "Money"
    pass


@attrs.define
class ShipmentItems:

    pass


@attrs.define
class SubmitInvoiceRequest:

    content_md5value: str
    marketplace_id: str

    invoice_content: "Blob"
    pass


@attrs.define
class SubmitInvoiceResponse:

    errors: "ErrorList"
    pass


@attrs.define
class TaxClassification:

    name: str
    value: str

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
