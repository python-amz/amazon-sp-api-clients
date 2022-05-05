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

    pass


@attrs.define
class Carton:

    carton_identifiers: list["ContainerIdentification"]
    carton_sequence_number: str
    items: list["ContainerItem"]
    tracking_number: str

    dimensions: "Dimensions"
    weight: "Weight"
    pass


@attrs.define
class CartonReferenceDetails:

    carton_count: int
    carton_reference_numbers: list[str]

    pass


@attrs.define
class ContainerIdentification:

    container_identification_number: str
    container_identification_type: Union[
        Literal["SSCC"], Literal["AMZNCC"], Literal["GTIN"], Literal["BPS"], Literal["CID"]
    ]

    pass


@attrs.define
class ContainerItem:

    item_reference: str

    item_details: "ItemDetails"
    shipped_quantity: "ItemQuantity"
    pass


@attrs.define
class Decimal:

    pass


@attrs.define
class Dimensions:

    unit_of_measure: Union[Literal["In"], Literal["Ft"], Literal["Meter"], Literal["Yard"]]

    height: "Decimal"
    length: "Decimal"
    width: "Decimal"
    pass


@attrs.define
class Duration:

    duration_unit: Union[Literal["Days"], Literal["Months"]]
    duration_value: int

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
class Expiry:

    expiry_date: str
    # {'schema_format': 'date-time'}
    manufacturer_date: str
    # {'schema_format': 'date-time'}

    expiry_after_duration: "Duration"
    pass


@attrs.define
class ImportDetails:

    estimated_ship_by_date: str
    # {'schema_format': 'date-time'}
    import_containers: str
    # {'maxLength': 64}
    method_of_payment: Union[
        Literal["PaidByBuyer"],
        Literal["CollectOnDelivery"],
        Literal["DefinedByBuyerAndSeller"],
        Literal["FOBPortOfCall"],
        Literal["PrepaidBySeller"],
        Literal["PaidBySeller"],
    ]
    seal_number: str

    billable_weight: "Weight"
    route: "Route"
    pass


@attrs.define
class Item:

    amazon_product_identifier: str
    item_sequence_number: str
    vendor_product_identifier: str

    item_details: "ItemDetails"
    shipped_quantity: "ItemQuantity"
    pass


@attrs.define
class ItemDetails:

    handling_code: Union[Literal["Oversized"], Literal["Fragile"], Literal["Food"], Literal["HandleWithCare"]]
    lot_number: str
    purchase_order_number: str

    expiry: "Expiry"
    maximum_retail_price: "Money"
    pass


@attrs.define
class ItemQuantity:

    amount: int
    unit_of_measure: Union[Literal["Cases"], Literal["Eaches"]]
    unit_size: int

    pass


@attrs.define
class Location:

    country_code: str
    location_code: str
    type: str

    pass


@attrs.define
class Money:

    currency_code: str

    amount: "Decimal"
    pass


@attrs.define
class Pallet:

    block: int
    items: list["ContainerItem"]
    pallet_identifiers: list["ContainerIdentification"]
    tier: int

    carton_reference_details: "CartonReferenceDetails"
    dimensions: "Dimensions"
    weight: "Weight"
    pass


@attrs.define
class PartyIdentification:

    party_id: str
    tax_registration_details: list["TaxRegistrationDetails"]

    address: "Address"
    pass


@attrs.define
class Route:

    stops: list["Stop"]

    pass


@attrs.define
class ShipmentConfirmation:

    amazon_reference_number: str
    cartons: list["Carton"]
    estimated_delivery_date: str
    # {'schema_format': 'date-time'}
    pallets: list["Pallet"]
    shipment_confirmation_date: str
    # {'schema_format': 'date-time'}
    shipment_confirmation_type: Union[Literal["Original"], Literal["Replace"]]
    shipment_identifier: str
    shipment_structure: Union[
        Literal["PalletizedAssortmentCase"],
        Literal["LooseAssortmentCase"],
        Literal["PalletOfItems"],
        Literal["PalletizedStandardCase"],
        Literal["LooseStandardCase"],
        Literal["MasterPallet"],
        Literal["MasterCase"],
    ]
    shipment_type: Union[Literal["TruckLoad"], Literal["LessThanTruckLoad"], Literal["SmallParcel"]]
    shipped_date: str
    # {'schema_format': 'date-time'}
    shipped_items: list["Item"]

    import_details: "ImportDetails"
    selling_party: "PartyIdentification"
    ship_from_party: "PartyIdentification"
    ship_to_party: "PartyIdentification"
    shipment_measurements: "ShipmentMeasurements"
    transportation_details: "TransportationDetails"
    pass


@attrs.define
class ShipmentMeasurements:

    carton_count: int
    pallet_count: int

    gross_shipment_weight: "Weight"
    shipment_volume: "Volume"
    pass


@attrs.define
class Stop:

    arrival_time: str
    # {'schema_format': 'date-time'}
    departure_time: str
    # {'schema_format': 'date-time'}
    function_code: Union[Literal["PortOfDischarge"], Literal["FreightPayableAt"], Literal["PortOfLoading"]]

    location_identification: "Location"
    pass


@attrs.define
class SubmitShipmentConfirmationsRequest:

    shipment_confirmations: list["ShipmentConfirmation"]

    pass


@attrs.define
class SubmitShipmentConfirmationsResponse:

    errors: "ErrorList"
    payload: "TransactionReference"
    pass


@attrs.define
class TaxRegistrationDetails:

    tax_registration_number: str
    tax_registration_type: Union[Literal["VAT"], Literal["GST"]]

    pass


@attrs.define
class TransactionReference:

    transaction_id: str

    pass


@attrs.define
class TransportationDetails:

    bill_of_lading_number: str
    carrier_scac: str
    carrier_shipment_reference_number: str
    transportation_mode: Union[Literal["Road"], Literal["Air"], Literal["Ocean"]]

    pass


@attrs.define
class Volume:

    unit_of_measure: Union[Literal["CuFt"], Literal["CuIn"], Literal["CuM"], Literal["CuY"]]

    value: "Decimal"
    pass


@attrs.define
class Weight:

    unit_of_measure: Union[Literal["G"], Literal["Kg"], Literal["Oz"], Literal["Lb"]]

    value: "Decimal"
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
