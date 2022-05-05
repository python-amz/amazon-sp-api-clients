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
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    address_line2: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    address_line3: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    city: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    country_code: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    county: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    district: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    name: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    phone: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    postal_code: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    state_or_region: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}

    address_type: Union[Literal["Residential"], Literal["Commercial"]]
    # {'ref': '#/components/schemas/AddressTypeEnum', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
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
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    taxing_region: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}

    tax_classifications: list[dict[str, Any]]
    # {'ref': '#/components/schemas/TaxClassificationList', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    pass


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class GetInvoiceStatusResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/ShipmentInvoiceStatusResponse', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    pass


@attrs.define
class GetShipmentDetailsResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    payload: dict[str, Any]
    # {'ref': '#/components/schemas/ShipmentDetail', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    pass


@attrs.define
class MarketplaceTaxInfo:

    company_legal_name: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    taxing_region: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}

    tax_classifications: list[dict[str, Any]]
    # {'ref': '#/components/schemas/TaxClassificationList', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    pass


@attrs.define
class Money:

    amount: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    currency_code: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}

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
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    amazon_shipment_id: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    buyer_county: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    buyer_name: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    purchase_date: str
    # {'schema_format': 'date-time', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    seller_display_name: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    seller_id: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    warehouse_id: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}

    buyer_tax_info: dict[str, Any]
    # {'ref': '#/components/schemas/BuyerTaxInfo', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    marketplace_tax_info: dict[str, Any]
    # {'ref': '#/components/schemas/MarketplaceTaxInfo', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    payment_method_details: list[str]
    # {'ref': '#/components/schemas/PaymentMethodDetailItemList', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    shipment_items: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ShipmentItems', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    shipping_address: dict[str, Any]
    # {'ref': '#/components/schemas/Address', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    pass


@attrs.define
class ShipmentInvoiceStatus:

    pass


@attrs.define
class ShipmentInvoiceStatusInfo:

    amazon_shipment_id: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}

    invoice_status: Union[Literal["Processing"], Literal["Accepted"], Literal["Errored"], Literal["NotFound"]]
    # {'ref': '#/components/schemas/ShipmentInvoiceStatus', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    pass


@attrs.define
class ShipmentInvoiceStatusResponse:

    shipments: dict[str, Any]
    # {'ref': '#/components/schemas/ShipmentInvoiceStatusInfo', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    pass


@attrs.define
class ShipmentItem:

    asin: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    order_item_id: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    quantity_ordered: Union[float, int]
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'number'}
    seller_sku: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    title: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}

    gift_wrap_price: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    item_price: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    promotion_discount: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    serial_numbers: list[str]
    # {'ref': '#/components/schemas/SerialNumbersList', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    shipping_discount: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    shipping_price: dict[str, Any]
    # {'ref': '#/components/schemas/Money', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    pass


@attrs.define
class ShipmentItems:

    pass


@attrs.define
class SubmitInvoiceRequest:

    content_md5value: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    marketplace_id: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}

    invoice_content: str
    # {'ref': '#/components/schemas/Blob', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    pass


@attrs.define
class SubmitInvoiceResponse:

    errors: list[dict[str, Any]]
    # {'ref': '#/components/schemas/ErrorList', 'generator': <__mp_main__.Generator object at 0x000001FB33337160>}
    pass


@attrs.define
class TaxClassification:

    name: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}
    value: str
    # {'generator': <__mp_main__.Generator object at 0x000001FB33337160>, 'type': 'string'}

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
