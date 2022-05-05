"""
Selling Partner API for Retail Procurement Shipments
=============================================================================================

The Selling Partner API for Retail Procurement Shipments provides programmatic access to retail shipping data for vendors.
API Version: v1
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


@attrs.define
class Address:

    address_line1: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    address_line2: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    address_line3: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    city: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    country_code: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    county: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    district: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    name: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    phone: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    postal_code: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    state_or_region: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}

    pass


@attrs.define
class Carton:

    carton_identifiers: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'items': Reference(ref='#/components/schemas/ContainerIdentification'), 'type': 'array'}
    carton_sequence_number: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'items': Reference(ref='#/components/schemas/ContainerItem'), 'type': 'array'}
    tracking_number: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}

    dimensions: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/Dimensions'}
    weight: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/Weight'}
    pass


@attrs.define
class CartonReferenceDetails:

    carton_count: int
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'integer'}
    carton_reference_numbers: list[str]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'items': Schema(title=None, multipleOf=None, maximum=None, exclusiveMaximum=None, minimum=None, exclusiveMinimum=None, maxLength=None, minLength=None, pattern=None, maxItems=None, minItems=None, uniqueItems=None, maxProperties=None, minProperties=None, required=None, enum=None, type='string', allOf=None, oneOf=None, anyOf=None, schema_not=None, items=None, properties=None, additionalProperties=None, description=None, schema_format=None, default=None, nullable=None, discriminator=None, readOnly=None, writeOnly=None, xml=None, externalDocs=None, example=None, deprecated=None), 'type': 'array'}

    pass


@attrs.define
class ContainerIdentification:

    container_identification_number: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    container_identification_type: Union[
        Literal["SSCC"], Literal["AMZNCC"], Literal["GTIN"], Literal["BPS"], Literal["CID"]
    ]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'enum': ['SSCC', 'AMZNCC', 'GTIN', 'BPS', 'CID']}

    pass


@attrs.define
class ContainerItem:

    item_reference: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}

    item_details: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/ItemDetails'}
    shipped_quantity: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/ItemQuantity'}
    pass


@attrs.define
class Decimal:

    pass


@attrs.define
class Dimensions:

    unit_of_measure: Union[Literal["In"], Literal["Ft"], Literal["Meter"], Literal["Yard"]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'enum': ['In', 'Ft', 'Meter', 'Yard']}

    height: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/Decimal'}
    length: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/Decimal'}
    width: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/Decimal'}
    pass


@attrs.define
class Duration:

    duration_unit: Union[Literal["Days"], Literal["Months"]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'enum': ['Days', 'Months']}
    duration_value: int
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'integer'}

    pass


@attrs.define
class Error:

    code: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    details: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    message: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}

    pass


@attrs.define
class ErrorList:

    pass


@attrs.define
class Expiry:

    expiry_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'schema_format': 'date-time'}
    manufacturer_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'schema_format': 'date-time'}

    expiry_after_duration: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/Duration'}
    pass


@attrs.define
class ImportDetails:

    estimated_ship_by_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'schema_format': 'date-time'}
    import_containers: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'maxLength': 64, 'type': 'string'}
    method_of_payment: Union[
        Literal["PaidByBuyer"],
        Literal["CollectOnDelivery"],
        Literal["DefinedByBuyerAndSeller"],
        Literal["FOBPortOfCall"],
        Literal["PrepaidBySeller"],
        Literal["PaidBySeller"],
    ]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'enum': ['PaidByBuyer', 'CollectOnDelivery', 'DefinedByBuyerAndSeller', 'FOBPortOfCall', 'PrepaidBySeller', 'PaidBySeller']}
    seal_number: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}

    billable_weight: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/Weight'}
    route: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/Route'}
    pass


@attrs.define
class Item:

    amazon_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    item_sequence_number: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    vendor_product_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}

    item_details: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/ItemDetails'}
    shipped_quantity: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/ItemQuantity'}
    pass


@attrs.define
class ItemDetails:

    handling_code: Union[Literal["Oversized"], Literal["Fragile"], Literal["Food"], Literal["HandleWithCare"]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'enum': ['Oversized', 'Fragile', 'Food', 'HandleWithCare']}
    lot_number: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    purchase_order_number: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}

    expiry: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/Expiry'}
    maximum_retail_price: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/Money'}
    pass


@attrs.define
class ItemQuantity:

    amount: int
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'integer'}
    unit_of_measure: Union[Literal["Cases"], Literal["Eaches"]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'enum': ['Cases', 'Eaches']}
    unit_size: int
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'integer'}

    pass


@attrs.define
class Location:

    country_code: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    location_code: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    type: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}

    pass


@attrs.define
class Money:

    currency_code: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}

    amount: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/Decimal'}
    pass


@attrs.define
class Pallet:

    block: int
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'integer'}
    items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'items': Reference(ref='#/components/schemas/ContainerItem'), 'type': 'array'}
    pallet_identifiers: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'items': Reference(ref='#/components/schemas/ContainerIdentification'), 'type': 'array'}
    tier: int
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'integer'}

    carton_reference_details: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/CartonReferenceDetails'}
    dimensions: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/Dimensions'}
    weight: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/Weight'}
    pass


@attrs.define
class PartyIdentification:

    party_id: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    tax_registration_details: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'items': Reference(ref='#/components/schemas/TaxRegistrationDetails'), 'type': 'array'}

    address: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/Address'}
    pass


@attrs.define
class Route:

    stops: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'items': Reference(ref='#/components/schemas/Stop'), 'type': 'array'}

    pass


@attrs.define
class ShipmentConfirmation:

    amazon_reference_number: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    cartons: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'items': Reference(ref='#/components/schemas/Carton'), 'type': 'array'}
    estimated_delivery_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'schema_format': 'date-time'}
    pallets: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'items': Reference(ref='#/components/schemas/Pallet'), 'type': 'array'}
    shipment_confirmation_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'schema_format': 'date-time'}
    shipment_confirmation_type: Union[Literal["Original"], Literal["Replace"]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'enum': ['Original', 'Replace']}
    shipment_identifier: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    shipment_structure: Union[
        Literal["PalletizedAssortmentCase"],
        Literal["LooseAssortmentCase"],
        Literal["PalletOfItems"],
        Literal["PalletizedStandardCase"],
        Literal["LooseStandardCase"],
        Literal["MasterPallet"],
        Literal["MasterCase"],
    ]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'enum': ['PalletizedAssortmentCase', 'LooseAssortmentCase', 'PalletOfItems', 'PalletizedStandardCase', 'LooseStandardCase', 'MasterPallet', 'MasterCase']}
    shipment_type: Union[Literal["TruckLoad"], Literal["LessThanTruckLoad"], Literal["SmallParcel"]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'enum': ['TruckLoad', 'LessThanTruckLoad', 'SmallParcel']}
    shipped_date: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'schema_format': 'date-time'}
    shipped_items: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'items': Reference(ref='#/components/schemas/Item'), 'type': 'array'}

    import_details: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/ImportDetails'}
    selling_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/PartyIdentification'}
    ship_from_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/PartyIdentification'}
    ship_to_party: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/PartyIdentification'}
    shipment_measurements: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/ShipmentMeasurements'}
    transportation_details: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/TransportationDetails'}
    pass


@attrs.define
class ShipmentMeasurements:

    carton_count: int
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'integer'}
    pallet_count: int
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'integer'}

    gross_shipment_weight: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/Weight'}
    shipment_volume: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/Volume'}
    pass


@attrs.define
class Stop:

    arrival_time: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'schema_format': 'date-time'}
    departure_time: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'schema_format': 'date-time'}
    function_code: Union[Literal["PortOfDischarge"], Literal["FreightPayableAt"], Literal["PortOfLoading"]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'enum': ['PortOfDischarge', 'FreightPayableAt', 'PortOfLoading']}

    location_identification: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/Location'}
    pass


@attrs.define
class SubmitShipmentConfirmationsRequest:

    shipment_confirmations: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'items': Reference(ref='#/components/schemas/ShipmentConfirmation'), 'type': 'array'}

    pass


@attrs.define
class SubmitShipmentConfirmationsResponse:

    errors: list[dict[str, Any]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/ErrorList'}
    payload: dict[str, Any]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/TransactionReference'}
    pass


@attrs.define
class TaxRegistrationDetails:

    tax_registration_number: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    tax_registration_type: Union[Literal["VAT"], Literal["GST"]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'enum': ['VAT', 'GST']}

    pass


@attrs.define
class TransactionReference:

    transaction_id: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}

    pass


@attrs.define
class TransportationDetails:

    bill_of_lading_number: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    carrier_scac: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    carrier_shipment_reference_number: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string'}
    transportation_mode: Union[Literal["Road"], Literal["Air"], Literal["Ocean"]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'enum': ['Road', 'Air', 'Ocean']}

    pass


@attrs.define
class Volume:

    unit_of_measure: Union[Literal["CuFt"], Literal["CuIn"], Literal["CuM"], Literal["CuY"]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'enum': ['CuFt', 'CuIn', 'CuM', 'CuY']}

    value: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/Decimal'}
    pass


@attrs.define
class Weight:

    unit_of_measure: Union[Literal["G"], Literal["Kg"], Literal["Oz"], Literal["Lb"]]
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'type': 'string', 'enum': ['G', 'Kg', 'Oz', 'Lb']}

    value: str
    # {'generator': <__mp_main__.Generator object at 0x00000163FB62B310>, 'ref': '#/components/schemas/Decimal'}
    pass


class VendorShipmentsV1Client(BaseClient):
    def submit_shipment_confirmations(
        self,
    ):
        """
        Submits one or more shipment confirmations for vendor orders.

        **Usage Plans:**

        | Plan type | Rate (requests per second) | Burst |
        | ---- | ---- | ---- |
        |Default| 10 | 10 |
        |Selling partner specific| Variable | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/vendor/shipping/v1/shipmentConfirmations"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._submit_shipment_confirmations_params)
        return response

    _submit_shipment_confirmations_params = ()  # name, param in
