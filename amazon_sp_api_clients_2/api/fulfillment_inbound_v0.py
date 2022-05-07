"""
Selling Partner API for Fulfillment Inbound
=============================================================================================

The Selling Partner API for Fulfillment Inbound lets you create applications that create and update inbound shipments of inventory to Amazon's fulfillment network.
API Version: v0
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
"""
import attrs
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal, Optional
from datetime import date, datetime


@attrs.define(kw_only=True, frozen=True, slots=True)
class ASINInboundGuidance:
    """
    Reasons why a given ASIN is not recommended for shipment to Amazon's fulfillment network.
    """

    asin: str = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    guidance_reason_list: Optional[List["GuidanceReason"]] = attrs.field()
    """
    A list of inbound guidance reason information.
    """

    inbound_guidance: "InboundGuidance" = attrs.field()
    """
    Specific inbound guidance for an item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ASINPrepInstructions:
    """
    Item preparation instructions to help with item sourcing decisions.
    """

    asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    barcode_instruction: Optional["BarcodeInstruction"] = attrs.field()
    """
    Labeling requirements for the item. For more information about FBA labeling requirements, see the Seller Central Help for your marketplace.
    """

    prep_guidance: Optional["PrepGuidance"] = attrs.field()
    """
    Item preparation instructions.
    """

    prep_instruction_list: Optional[List["PrepInstruction"]] = attrs.field()
    """
    A list of preparation instructions to help with item sourcing decisions.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Address:

    address_line1: str = attrs.field()
    """
    The street address information.

    Extra fields:
    {'maxLength': 180}
    """

    address_line2: Optional[str] = attrs.field()
    """
    Additional street address information, if required.

    Extra fields:
    {'maxLength': 60}
    """

    city: str = attrs.field()
    """
    The city.

    Extra fields:
    {'maxLength': 30}
    """

    country_code: str = attrs.field()
    """
    The country code in two-character ISO 3166-1 alpha-2 format.
    """

    district_or_county: Optional[str] = attrs.field()
    """
    The district or county.

    Extra fields:
    {'maxLength': 25}
    """

    name: str = attrs.field()
    """
    Name of the individual or business.

    Extra fields:
    {'maxLength': 50}
    """

    postal_code: str = attrs.field()
    """
    The postal code.
        If postal codes are used in your marketplace, we recommended that you include one with your request. This helps Amazon select the most appropriate Amazon fulfillment center for the inbound shipment plan.

    Extra fields:
    {'maxLength': 30}
    """

    state_or_province_code: str = attrs.field()
    """
    The state or province code.
        If state or province codes are used in your marketplace, it is recommended that you include one with your request. This helps Amazon to select the most appropriate Amazon fulfillment center for your inbound shipment plan.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class AmazonPrepFeesDetails:
    """
    The fees for Amazon to prep goods for shipment.
    """

    fee_per_unit: Optional["Amount"] = attrs.field()
    """
    The monetary value.
    """

    prep_instruction: Optional["PrepInstruction"] = attrs.field()
    """
    Preparation instructions for shipping an item to Amazon's fulfillment network. For more information about preparing items for shipment to Amazon's fulfillment network, see the Seller Central Help for your marketplace.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Amount:
    """
    The monetary value.
    """

    currency_code: "CurrencyCode" = attrs.field()
    """
    The currency code.
    """

    value: "BigDecimalType" = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class BarcodeInstruction:
    """
    Labeling requirements for the item. For more information about FBA labeling requirements, see the Seller Central Help for your marketplace.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class BigDecimalType:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class BillOfLadingDownloadURL:

    download_url: Optional[str] = attrs.field()
    """
    URL to download the bill of lading for the package. Note: The URL will only be valid for 15 seconds
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class BoxContentsFeeDetails:
    """
    The manual processing fee per unit and total fee for a shipment.
    """

    fee_per_unit: Optional["Amount"] = attrs.field()
    """
    The monetary value.
    """

    total_fee: Optional["Amount"] = attrs.field()
    """
    The monetary value.
    """

    total_units: Optional["Quantity"] = attrs.field()
    """
    The item quantity.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class BoxContentsSource:
    """
    Where the seller provided box contents information for a shipment.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class CommonTransportResult:

    transport_result: Optional["TransportResult"] = attrs.field()
    """
    The workflow status for a shipment with an Amazon-partnered carrier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class Condition:
    """
    The condition of the item.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ConfirmPreorderResponse:
    """
    The response schema for the confirmPreorder operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["ConfirmPreorderResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ConfirmPreorderResult:

    confirmed_fulfillable_date: Optional["DateStringType"] = attrs.field()

    confirmed_need_by_date: Optional["DateStringType"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class ConfirmTransportResponse:
    """
    The response schema for the confirmTransport operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["CommonTransportResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Contact:
    """
    Contact information for the person in the seller's organization who is responsible for a Less Than Truckload/Full Truckload (LTL/FTL) shipment.
    """

    email: str = attrs.field()
    """
    The email address of the contact person.

    Extra fields:
    {'maxLength': 50}
    """

    fax: Optional[str] = attrs.field()
    """
    The fax number of the contact person.

    Extra fields:
    {'maxLength': 20}
    """

    name: str = attrs.field()
    """
    The name of the contact person.

    Extra fields:
    {'maxLength': 50}
    """

    phone: str = attrs.field()
    """
    The phone number of the contact person.

    Extra fields:
    {'maxLength': 20}
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateInboundShipmentPlanRequest:
    """
    The request schema for the createInboundShipmentPlan operation.
    """

    inbound_shipment_plan_request_items: List["InboundShipmentPlanRequestItem"] = attrs.field()

    label_prep_preference: "LabelPrepPreference" = attrs.field()
    """
    The preference for label preparation for an inbound shipment.
    """

    ship_from_address: "Address" = attrs.field()

    ship_to_country_code: Optional[str] = attrs.field()
    """
    The two-character country code for the country where the inbound shipment is to be sent.
        Note: Not required. Specifying both ShipToCountryCode and ShipToCountrySubdivisionCode returns an error.
        Values:
        ShipToCountryCode values for North America:
        * CA – Canada
        * MX - Mexico
        * US - United States
        ShipToCountryCode values for MCI sellers in Europe:
        * DE – Germany
        * ES – Spain
        * FR – France
        * GB – United Kingdom
        * IT – Italy
        Default: The country code for the seller's home marketplace.
    """

    ship_to_country_subdivision_code: Optional[str] = attrs.field()
    """
    The two-character country code, followed by a dash and then up to three characters that represent the subdivision of the country where the inbound shipment is to be sent. For example, "IN-MH". In full ISO 3166-2 format.
        Note: Not required. Specifying both ShipToCountryCode and ShipToCountrySubdivisionCode returns an error.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateInboundShipmentPlanResponse:
    """
    The response schema for the createInboundShipmentPlan operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["CreateInboundShipmentPlanResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class CreateInboundShipmentPlanResult:

    inbound_shipment_plans: Optional[List["InboundShipmentPlan"]] = attrs.field()
    """
    A list of inbound shipment plan information
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class CurrencyCode:
    """
    The currency code.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class DateStringType:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Dimensions:
    """
    The dimension values and unit of measurement.
    """

    height: "BigDecimalType" = attrs.field()

    length: "BigDecimalType" = attrs.field()

    unit: "UnitOfMeasurement" = attrs.field()
    """
    Indicates the unit of measurement.
    """

    width: "BigDecimalType" = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    code: str = attrs.field()
    """
    An error code that identifies the type of error that occured.
    """

    details: Optional[str] = attrs.field()
    """
    Additional details that can help the caller understand or fix the issue.
    """

    message: str = attrs.field()
    """
    A message that describes the error condition in a human-readable form.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class ErrorReason:
    """
    The reason that the ASIN is invalid.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class EstimateTransportResponse:
    """
    The response schema for the estimateTransport operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["CommonTransportResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetBillOfLadingResponse:
    """
    The response schema for the getBillOfLading operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["BillOfLadingDownloadURL"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetInboundGuidanceResponse:
    """
    The response schema for the getInboundGuidance operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["GetInboundGuidanceResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetInboundGuidanceResult:

    asininbound_guidance_list: Optional[List["ASINInboundGuidance"]] = attrs.field()
    """
    A list of ASINs and their associated inbound guidance.
    """

    invalid_asinlist: Optional[List["InvalidASIN"]] = attrs.field()
    """
    A list of invalid ASIN values and the reasons they are invalid.
    """

    invalid_skulist: Optional[List["InvalidSKU"]] = attrs.field()
    """
    A list of invalid SKU values and the reason they are invalid.
    """

    skuinbound_guidance_list: Optional[List["SKUInboundGuidance"]] = attrs.field()
    """
    A list of SKU inbound guidance information.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetLabelsResponse:
    """
    The response schema for the getLabels operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["LabelDownloadURL"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetPreorderInfoResponse:
    """
    The response schema for the getPreorderInfo operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["GetPreorderInfoResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetPreorderInfoResult:

    confirmed_fulfillable_date: Optional["DateStringType"] = attrs.field()

    need_by_date: Optional["DateStringType"] = attrs.field()

    shipment_confirmed_for_preorder: Optional[bool] = attrs.field()
    """
    Indicates whether this shipment has been confirmed for pre-order.
    """

    shipment_contains_preorderable_items: Optional[bool] = attrs.field()
    """
    Indicates whether the shipment contains items that have been enabled for pre-order. For more information about enabling items for pre-order, see the Seller Central Help.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetPrepInstructionsResponse:
    """
    The response schema for the getPrepInstructions operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["GetPrepInstructionsResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetPrepInstructionsResult:

    asinprep_instructions_list: Optional[List["ASINPrepInstructions"]] = attrs.field()
    """
    A list of item preparation instructions.
    """

    invalid_asinlist: Optional[List["InvalidASIN"]] = attrs.field()
    """
    A list of invalid ASIN values and the reasons they are invalid.
    """

    invalid_skulist: Optional[List["InvalidSKU"]] = attrs.field()
    """
    A list of invalid SKU values and the reason they are invalid.
    """

    skuprep_instructions_list: Optional[List["SKUPrepInstructions"]] = attrs.field()
    """
    A list of SKU labeling requirements and item preparation instructions.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetShipmentItemsResponse:
    """
    The response schema for the getShipmentItems operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["GetShipmentItemsResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetShipmentItemsResult:

    item_data: Optional[List["InboundShipmentItem"]] = attrs.field()
    """
    A list of inbound shipment item information.
    """

    next_token: Optional[str] = attrs.field()
    """
    When present and not empty, pass this string token in the next request to return the next response page.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetShipmentsResponse:
    """
    The response schema for the getShipments operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["GetShipmentsResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetShipmentsResult:

    next_token: Optional[str] = attrs.field()
    """
    When present and not empty, pass this string token in the next request to return the next response page.
    """

    shipment_data: Optional[List["InboundShipmentInfo"]] = attrs.field()
    """
    A list of inbound shipment information.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetTransportDetailsResponse:
    """
    The response schema for the getTransportDetails operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["GetTransportDetailsResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class GetTransportDetailsResult:

    transport_content: Optional["TransportContent"] = attrs.field()
    """
    Inbound shipment information, including carrier details, shipment status, and the workflow status for a request for shipment with an Amazon-partnered carrier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class GuidanceReason:
    """
    A reason for the current inbound guidance for an item.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class InboundGuidance:
    """
    Specific inbound guidance for an item.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class InboundShipmentHeader:
    """
    Inbound shipment information used to create and update inbound shipments.
    """

    are_cases_required: Optional[bool] = attrs.field()
    """
    Indicates whether or not an inbound shipment contains case-packed boxes. Note: A shipment must contain either all case-packed boxes or all individually packed boxes.
        Possible values:
        true - All boxes in the shipment must be case packed.
        false - All boxes in the shipment must be individually packed.
        Note: If AreCasesRequired = true for an inbound shipment, then the value of QuantityInCase must be greater than zero for every item in the shipment. Otherwise the service returns an error.
    """

    destination_fulfillment_center_id: str = attrs.field()
    """
    The identifier for the fulfillment center to which the shipment will be shipped. Get this value from the InboundShipmentPlan object in the response returned by the createInboundShipmentPlan operation.
    """

    intended_box_contents_source: Optional["IntendedBoxContentsSource"] = attrs.field()
    """
    How the seller intends to provide box contents information for a shipment.
    """

    label_prep_preference: "LabelPrepPreference" = attrs.field()
    """
    The preference for label preparation for an inbound shipment.
    """

    ship_from_address: "Address" = attrs.field()

    shipment_name: str = attrs.field()
    """
    The name for the shipment. Use a naming convention that helps distinguish between shipments over time, such as the date the shipment was created.
    """

    shipment_status: "ShipmentStatus" = attrs.field()
    """
    Indicates the status of the inbound shipment. When used with the createInboundShipment operation, WORKING is the only valid value. When used with the updateInboundShipment operation, possible values are WORKING, SHIPPED or CANCELLED.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class InboundShipmentInfo:
    """
    Information about the seller's inbound shipments. Returned by the listInboundShipments operation.
    """

    are_cases_required: bool = attrs.field()
    """
    Indicates whether or not an inbound shipment contains case-packed boxes. When AreCasesRequired = true for an inbound shipment, all items in the inbound shipment must be case packed.
    """

    box_contents_source: Optional["BoxContentsSource"] = attrs.field()
    """
    Where the seller provided box contents information for a shipment.
    """

    confirmed_need_by_date: Optional["DateStringType"] = attrs.field()

    destination_fulfillment_center_id: Optional[str] = attrs.field()
    """
    An Amazon fulfillment center identifier created by Amazon.
    """

    estimated_box_contents_fee: Optional["BoxContentsFeeDetails"] = attrs.field()
    """
    The manual processing fee per unit and total fee for a shipment.
    """

    label_prep_type: Optional["LabelPrepType"] = attrs.field()
    """
    The type of label preparation that is required for the inbound shipment.
    """

    ship_from_address: "Address" = attrs.field()

    shipment_id: Optional[str] = attrs.field()
    """
    The shipment identifier submitted in the request.
    """

    shipment_name: Optional[str] = attrs.field()
    """
    The name for the inbound shipment.
    """

    shipment_status: Optional["ShipmentStatus"] = attrs.field()
    """
    Indicates the status of the inbound shipment. When used with the createInboundShipment operation, WORKING is the only valid value. When used with the updateInboundShipment operation, possible values are WORKING, SHIPPED or CANCELLED.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class InboundShipmentItem:
    """
    Item information for an inbound shipment. Submitted with a call to the createInboundShipment or updateInboundShipment operation.
    """

    fulfillment_network_sku: Optional[str] = attrs.field()
    """
    Amazon's fulfillment network SKU of the item.
    """

    prep_details_list: Optional[List["PrepDetails"]] = attrs.field()
    """
    A list of preparation instructions and who is responsible for that preparation.
    """

    quantity_in_case: Optional["Quantity"] = attrs.field()
    """
    The item quantity.
    """

    quantity_received: Optional["Quantity"] = attrs.field()
    """
    The item quantity.
    """

    quantity_shipped: "Quantity" = attrs.field()
    """
    The item quantity.
    """

    release_date: Optional["DateStringType"] = attrs.field()

    seller_sku: str = attrs.field()
    """
    The seller SKU of the item.
    """

    shipment_id: Optional[str] = attrs.field()
    """
    A shipment identifier originally returned by the createInboundShipmentPlan operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class InboundShipmentPlan:
    """
    Inbound shipment information used to create an inbound shipment. Returned by the createInboundShipmentPlan operation.
    """

    destination_fulfillment_center_id: str = attrs.field()
    """
    An Amazon fulfillment center identifier created by Amazon.
    """

    estimated_box_contents_fee: Optional["BoxContentsFeeDetails"] = attrs.field()
    """
    The manual processing fee per unit and total fee for a shipment.
    """

    items: List["InboundShipmentPlanItem"] = attrs.field()
    """
    A list of inbound shipment plan item information.
    """

    label_prep_type: "LabelPrepType" = attrs.field()
    """
    The type of label preparation that is required for the inbound shipment.
    """

    ship_to_address: "Address" = attrs.field()

    shipment_id: str = attrs.field()
    """
    A shipment identifier originally returned by the createInboundShipmentPlan operation.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class InboundShipmentPlanItem:
    """
    Item information used to create an inbound shipment. Returned by the createInboundShipmentPlan operation.
    """

    fulfillment_network_sku: str = attrs.field()
    """
    Amazon's fulfillment network SKU of the item.
    """

    prep_details_list: Optional[List["PrepDetails"]] = attrs.field()
    """
    A list of preparation instructions and who is responsible for that preparation.
    """

    quantity: "Quantity" = attrs.field()
    """
    The item quantity.
    """

    seller_sku: str = attrs.field()
    """
    The seller SKU of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class InboundShipmentPlanRequestItem:
    """
    Item information for creating an inbound shipment plan. Submitted with a call to the createInboundShipmentPlan operation.
    """

    asin: str = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    condition: "Condition" = attrs.field()
    """
    The condition of the item.
    """

    prep_details_list: Optional[List["PrepDetails"]] = attrs.field()
    """
    A list of preparation instructions and who is responsible for that preparation.
    """

    quantity: "Quantity" = attrs.field()
    """
    The item quantity.
    """

    quantity_in_case: Optional["Quantity"] = attrs.field()
    """
    The item quantity.
    """

    seller_sku: str = attrs.field()
    """
    The seller SKU of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class InboundShipmentRequest:
    """
    The request schema for an inbound shipment.
    """

    inbound_shipment_header: "InboundShipmentHeader" = attrs.field()
    """
    Inbound shipment information used to create and update inbound shipments.
    """

    inbound_shipment_items: List["InboundShipmentItem"] = attrs.field()
    """
    A list of inbound shipment item information.
    """

    marketplace_id: str = attrs.field()
    """
    A marketplace identifier. Specifies the marketplace where the product would be stored.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class InboundShipmentResponse:
    """
    The response schema for this operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["InboundShipmentResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class InboundShipmentResult:

    shipment_id: str = attrs.field()
    """
    The shipment identifier submitted in the request.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class IntendedBoxContentsSource:
    """
    How the seller intends to provide box contents information for a shipment.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class InvalidASIN:

    asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    error_reason: Optional["ErrorReason"] = attrs.field()
    """
    The reason that the ASIN is invalid.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class InvalidSKU:

    error_reason: Optional["ErrorReason"] = attrs.field()
    """
    The reason that the ASIN is invalid.
    """

    seller_sku: Optional[str] = attrs.field()
    """
    The seller SKU of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelDownloadURL:

    download_url: Optional[str] = attrs.field()
    """
    URL to download the label for the package. Note: The URL will only be valid for 15 seconds
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelPrepPreference:
    """
    The preference for label preparation for an inbound shipment.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class LabelPrepType:
    """
    The type of label preparation that is required for the inbound shipment.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class NonPartneredLtlDataInput:
    """
    Information that you provide to Amazon about a Less Than Truckload/Full Truckload (LTL/FTL) shipment by a carrier that has not partnered with Amazon.
    """

    carrier_name: str = attrs.field()
    """
    The carrier that you are using for the inbound shipment.
    """

    pro_number: "ProNumber" = attrs.field()
    """
    The PRO number ("progressive number" or "progressive ID") assigned to the shipment by the carrier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class NonPartneredLtlDataOutput:
    """
    Information returned by Amazon about a Less Than Truckload/Full Truckload (LTL/FTL) shipment shipped by a carrier that has not partnered with Amazon.
    """

    carrier_name: str = attrs.field()
    """
    The carrier that you are using for the inbound shipment.
    """

    pro_number: "ProNumber" = attrs.field()
    """
    The PRO number ("progressive number" or "progressive ID") assigned to the shipment by the carrier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class NonPartneredSmallParcelDataInput:
    """
    Information that you provide to Amazon about a Small Parcel shipment shipped by a carrier that has not partnered with Amazon.
    """

    carrier_name: str = attrs.field()
    """
    The carrier that you are using for the inbound shipment.
    """

    package_list: List["NonPartneredSmallParcelPackageInput"] = attrs.field()
    """
    A list of package tracking information.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class NonPartneredSmallParcelDataOutput:
    """
    Information returned by Amazon about a Small Parcel shipment by a carrier that has not partnered with Amazon.
    """

    package_list: List["NonPartneredSmallParcelPackageOutput"] = attrs.field()
    """
    A list of packages, including carrier, tracking number, and status information for each package.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class NonPartneredSmallParcelPackageInput:
    """
    The tracking number of the package, provided by the carrier.
    """

    tracking_id: "TrackingId" = attrs.field()
    """
    The tracking number of the package, provided by the carrier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class NonPartneredSmallParcelPackageOutput:
    """
    Carrier, tracking number, and status information for the package.
    """

    carrier_name: str = attrs.field()
    """
    The carrier that you are using for the inbound shipment.
    """

    package_status: "PackageStatus" = attrs.field()
    """
    The shipment status of the package.
    """

    tracking_id: "TrackingId" = attrs.field()
    """
    The tracking number of the package, provided by the carrier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PackageStatus:
    """
    The shipment status of the package.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class Pallet:
    """
    Pallet information.
    """

    dimensions: "Dimensions" = attrs.field()
    """
    The dimension values and unit of measurement.
    """

    is_stacked: bool = attrs.field()
    """
    Indicates whether pallets will be stacked when carrier arrives for pick-up.
    """

    weight: Optional["Weight"] = attrs.field()
    """
    The weight of the package.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartneredEstimate:
    """
    The estimated shipping cost for a shipment using an Amazon-partnered carrier.
    """

    amount: "Amount" = attrs.field()
    """
    The monetary value.
    """

    confirm_deadline: Optional["TimeStampStringType"] = attrs.field()

    void_deadline: Optional["TimeStampStringType"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartneredLtlDataInput:
    """
    Information that is required by an Amazon-partnered carrier to ship a Less Than Truckload/Full Truckload (LTL/FTL) inbound shipment.
    """

    box_count: Optional["UnsignedIntType"] = attrs.field()

    contact: Optional["Contact"] = attrs.field()
    """
    Contact information for the person in the seller's organization who is responsible for a Less Than Truckload/Full Truckload (LTL/FTL) shipment.
    """

    freight_ready_date: Optional["DateStringType"] = attrs.field()

    pallet_list: Optional[List["Pallet"]] = attrs.field()
    """
    A list of pallet information.
    """

    seller_declared_value: Optional["Amount"] = attrs.field()
    """
    The monetary value.
    """

    seller_freight_class: Optional["SellerFreightClass"] = attrs.field()
    """
    The freight class of the shipment. For information about determining the freight class, contact the carrier.
    """

    total_weight: Optional["Weight"] = attrs.field()
    """
    The weight of the package.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartneredLtlDataOutput:
    """
    Information returned by Amazon about a Less Than Truckload/Full Truckload (LTL/FTL) shipment by an Amazon-partnered carrier.
    """

    amazon_calculated_value: Optional["Amount"] = attrs.field()
    """
    The monetary value.
    """

    amazon_reference_id: str = attrs.field()
    """
    A unique identifier created by Amazon that identifies this Amazon-partnered, Less Than Truckload/Full Truckload (LTL/FTL) shipment.
    """

    box_count: "UnsignedIntType" = attrs.field()

    carrier_name: str = attrs.field()
    """
    The carrier for the inbound shipment.
    """

    contact: "Contact" = attrs.field()
    """
    Contact information for the person in the seller's organization who is responsible for a Less Than Truckload/Full Truckload (LTL/FTL) shipment.
    """

    freight_ready_date: "DateStringType" = attrs.field()

    is_bill_of_lading_available: bool = attrs.field()
    """
    Indicates whether the bill of lading for the shipment is available.
    """

    pallet_list: List["Pallet"] = attrs.field()
    """
    A list of pallet information.
    """

    partnered_estimate: Optional["PartneredEstimate"] = attrs.field()
    """
    The estimated shipping cost for a shipment using an Amazon-partnered carrier.
    """

    preview_delivery_date: "DateStringType" = attrs.field()

    preview_freight_class: "SellerFreightClass" = attrs.field()
    """
    The freight class of the shipment. For information about determining the freight class, contact the carrier.
    """

    preview_pickup_date: "DateStringType" = attrs.field()

    seller_declared_value: Optional["Amount"] = attrs.field()
    """
    The monetary value.
    """

    seller_freight_class: Optional["SellerFreightClass"] = attrs.field()
    """
    The freight class of the shipment. For information about determining the freight class, contact the carrier.
    """

    total_weight: "Weight" = attrs.field()
    """
    The weight of the package.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartneredSmallParcelDataInput:
    """
    Information that is required by an Amazon-partnered carrier to ship a Small Parcel inbound shipment.
    """

    carrier_name: Optional[str] = attrs.field()
    """
    The Amazon-partnered carrier to use for the inbound shipment.
    """

    package_list: Optional[List["PartneredSmallParcelPackageInput"]] = attrs.field()
    """
    A list of dimensions and weight information for packages.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartneredSmallParcelDataOutput:
    """
    Information returned by Amazon about a Small Parcel shipment by an Amazon-partnered carrier.
    """

    package_list: List["PartneredSmallParcelPackageOutput"] = attrs.field()
    """
    A list of packages, including shipping information from the Amazon-partnered carrier.
    """

    partnered_estimate: Optional["PartneredEstimate"] = attrs.field()
    """
    The estimated shipping cost for a shipment using an Amazon-partnered carrier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartneredSmallParcelPackageInput:
    """
    Dimension and weight information for the package.
    """

    dimensions: "Dimensions" = attrs.field()
    """
    The dimension values and unit of measurement.
    """

    weight: "Weight" = attrs.field()
    """
    The weight of the package.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PartneredSmallParcelPackageOutput:
    """
    Dimension, weight, and shipping information for the package.
    """

    carrier_name: str = attrs.field()
    """
    The carrier specified with a previous call to putTransportDetails.
    """

    dimensions: "Dimensions" = attrs.field()
    """
    The dimension values and unit of measurement.
    """

    package_status: "PackageStatus" = attrs.field()
    """
    The shipment status of the package.
    """

    tracking_id: "TrackingId" = attrs.field()
    """
    The tracking number of the package, provided by the carrier.
    """

    weight: "Weight" = attrs.field()
    """
    The weight of the package.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PrepDetails:
    """
    Preparation instructions and who is responsible for the preparation.
    """

    prep_instruction: "PrepInstruction" = attrs.field()
    """
    Preparation instructions for shipping an item to Amazon's fulfillment network. For more information about preparing items for shipment to Amazon's fulfillment network, see the Seller Central Help for your marketplace.
    """

    prep_owner: "PrepOwner" = attrs.field()
    """
    Indicates who will prepare the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PrepGuidance:
    """
    Item preparation instructions.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PrepInstruction:
    """
    Preparation instructions for shipping an item to Amazon's fulfillment network. For more information about preparing items for shipment to Amazon's fulfillment network, see the Seller Central Help for your marketplace.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PrepOwner:
    """
    Indicates who will prepare the item.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ProNumber:
    """
    The PRO number ("progressive number" or "progressive ID") assigned to the shipment by the carrier.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class PutTransportDetailsRequest:
    """
    The request schema for a putTransportDetails operation.
    """

    is_partnered: bool = attrs.field()
    """
    Indicates whether a putTransportDetails request is for an Amazon-partnered carrier.
    """

    shipment_type: "ShipmentType" = attrs.field()
    """
    Specifies the carrier shipment type in a putTransportDetails request.
    """

    transport_details: "TransportDetailInput" = attrs.field()
    """
    Information required to create an Amazon-partnered carrier shipping estimate, or to alert the Amazon fulfillment center to the arrival of an inbound shipment by a non-Amazon-partnered carrier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class PutTransportDetailsResponse:
    """
    Workflow status for a shipment with an Amazon-partnered carrier.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["CommonTransportResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Quantity:
    """
    The item quantity.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class SKUInboundGuidance:
    """
    Reasons why a given seller SKU is not recommended for shipment to Amazon's fulfillment network.
    """

    asin: str = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    guidance_reason_list: Optional[List["GuidanceReason"]] = attrs.field()
    """
    A list of inbound guidance reason information.
    """

    inbound_guidance: "InboundGuidance" = attrs.field()
    """
    Specific inbound guidance for an item.
    """

    seller_sku: str = attrs.field()
    """
    The seller SKU of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SKUPrepInstructions:
    """
    Labeling requirements and item preparation instructions to help you prepare items for shipment to Amazon's fulfillment network.
    """

    asin: Optional[str] = attrs.field()
    """
    The Amazon Standard Identification Number (ASIN) of the item.
    """

    amazon_prep_fees_details_list: Optional[List["AmazonPrepFeesDetails"]] = attrs.field()
    """
    A list of preparation instructions and fees for Amazon to prep goods for shipment.
    """

    barcode_instruction: Optional["BarcodeInstruction"] = attrs.field()
    """
    Labeling requirements for the item. For more information about FBA labeling requirements, see the Seller Central Help for your marketplace.
    """

    prep_guidance: Optional["PrepGuidance"] = attrs.field()
    """
    Item preparation instructions.
    """

    prep_instruction_list: Optional[List["PrepInstruction"]] = attrs.field()
    """
    A list of preparation instructions to help with item sourcing decisions.
    """

    seller_sku: Optional[str] = attrs.field()
    """
    The seller SKU of the item.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class SellerFreightClass:
    """
    The freight class of the shipment. For information about determining the freight class, contact the carrier.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentStatus:
    """
    Indicates the status of the inbound shipment. When used with the createInboundShipment operation, WORKING is the only valid value. When used with the updateInboundShipment operation, possible values are WORKING, SHIPPED or CANCELLED.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class ShipmentType:
    """
    Specifies the carrier shipment type in a putTransportDetails request.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class TimeStampStringType:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class TrackingId:
    """
    The tracking number of the package, provided by the carrier.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransportContent:
    """
    Inbound shipment information, including carrier details, shipment status, and the workflow status for a request for shipment with an Amazon-partnered carrier.
    """

    transport_details: "TransportDetailOutput" = attrs.field()
    """
    Inbound shipment information, including carrier details and shipment status.
    """

    transport_header: "TransportHeader" = attrs.field()
    """
    The shipping identifier, information about whether the shipment is by an Amazon-partnered carrier, and information about whether the shipment is Small Parcel or Less Than Truckload/Full Truckload (LTL/FTL).
    """

    transport_result: "TransportResult" = attrs.field()
    """
    The workflow status for a shipment with an Amazon-partnered carrier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransportDetailInput:
    """
    Information required to create an Amazon-partnered carrier shipping estimate, or to alert the Amazon fulfillment center to the arrival of an inbound shipment by a non-Amazon-partnered carrier.
    """

    non_partnered_ltl_data: Optional["NonPartneredLtlDataInput"] = attrs.field()
    """
    Information that you provide to Amazon about a Less Than Truckload/Full Truckload (LTL/FTL) shipment by a carrier that has not partnered with Amazon.
    """

    non_partnered_small_parcel_data: Optional["NonPartneredSmallParcelDataInput"] = attrs.field()
    """
    Information that you provide to Amazon about a Small Parcel shipment shipped by a carrier that has not partnered with Amazon.
    """

    partnered_ltl_data: Optional["PartneredLtlDataInput"] = attrs.field()
    """
    Information that is required by an Amazon-partnered carrier to ship a Less Than Truckload/Full Truckload (LTL/FTL) inbound shipment.
    """

    partnered_small_parcel_data: Optional["PartneredSmallParcelDataInput"] = attrs.field()
    """
    Information that is required by an Amazon-partnered carrier to ship a Small Parcel inbound shipment.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransportDetailOutput:
    """
    Inbound shipment information, including carrier details and shipment status.
    """

    non_partnered_ltl_data: Optional["NonPartneredLtlDataOutput"] = attrs.field()
    """
    Information returned by Amazon about a Less Than Truckload/Full Truckload (LTL/FTL) shipment shipped by a carrier that has not partnered with Amazon.
    """

    non_partnered_small_parcel_data: Optional["NonPartneredSmallParcelDataOutput"] = attrs.field()
    """
    Information returned by Amazon about a Small Parcel shipment by a carrier that has not partnered with Amazon.
    """

    partnered_ltl_data: Optional["PartneredLtlDataOutput"] = attrs.field()
    """
    Information returned by Amazon about a Less Than Truckload/Full Truckload (LTL/FTL) shipment by an Amazon-partnered carrier.
    """

    partnered_small_parcel_data: Optional["PartneredSmallParcelDataOutput"] = attrs.field()
    """
    Information returned by Amazon about a Small Parcel shipment by an Amazon-partnered carrier.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransportHeader:
    """
    The shipping identifier, information about whether the shipment is by an Amazon-partnered carrier, and information about whether the shipment is Small Parcel or Less Than Truckload/Full Truckload (LTL/FTL).
    """

    is_partnered: bool = attrs.field()
    """
    Indicates whether a putTransportDetails request is for a partnered carrier.
        Possible values:
        * true – Request is for an Amazon-partnered carrier.
        * false – Request is for a non-Amazon-partnered carrier.
    """

    seller_id: str = attrs.field()
    """
    The Amazon seller identifier.
    """

    shipment_id: str = attrs.field()
    """
    A shipment identifier originally returned by the createInboundShipmentPlan operation.
    """

    shipment_type: "ShipmentType" = attrs.field()
    """
    Specifies the carrier shipment type in a putTransportDetails request.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransportResult:
    """
    The workflow status for a shipment with an Amazon-partnered carrier.
    """

    error_code: Optional[str] = attrs.field()
    """
    An error code that identifies the type of error that occured.
    """

    error_description: Optional[str] = attrs.field()
    """
    A message that describes the error condition.
    """

    transport_status: "TransportStatus" = attrs.field()
    """
    Indicates the status of the Amazon-partnered carrier shipment.
    """


@attrs.define(kw_only=True, frozen=True, slots=True)
class TransportStatus:
    """
    Indicates the status of the Amazon-partnered carrier shipment.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class UnitOfMeasurement:
    """
    Indicates the unit of measurement.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class UnitOfWeight:
    """
    Indicates the unit of weight.
    """

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class UnsignedIntType:

    pass


@attrs.define(kw_only=True, frozen=True, slots=True)
class VoidTransportResponse:
    """
    The response schema for the voidTransport operation.
    """

    errors: Optional[List["Error"]] = attrs.field()
    """
    A list of error responses returned when a request is unsuccessful.
    """

    payload: Optional["CommonTransportResult"] = attrs.field()


@attrs.define(kw_only=True, frozen=True, slots=True)
class Weight:
    """
    The weight of the package.
    """

    unit: "UnitOfWeight" = attrs.field()
    """
    Indicates the unit of weight.
    """

    value: "BigDecimalType" = attrs.field()


class FulfillmentInboundV0Client(BaseClient):
    def confirm_preorder(
        self,
        shipment_id: str,
        need_by_date: date,
        marketplace_id: str,
    ) -> Union[ConfirmPreorderResponse]:
        """
        Returns information needed to confirm a shipment for pre-order. Call this operation after calling the getPreorderInfo operation to get the NeedByDate value and other pre-order information about the shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
            need_by_date: Date that the shipment must arrive at the Amazon fulfillment center to avoid delivery promise breaks for pre-ordered items. Must be in YYYY-MM-DD format. The response to the getPreorderInfo operation returns this value.
            marketplace_id: A marketplace identifier. Specifies the marketplace the shipment is tied to.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/preorder/confirm"
        values = (
            shipment_id,
            need_by_date,
            marketplace_id,
        )
        response = self._parse_args_and_request(
            url,
            "PUT",
            values,
            self._confirm_preorder_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _confirm_preorder_params = (  # name, param in
        ("shipmentId", "path"),
        ("NeedByDate", "query"),
        ("MarketplaceId", "query"),
    )

    _confirm_preorder_responses = {
        (200, "application/json"): ConfirmPreorderResponse,
        (400, "application/json"): ConfirmPreorderResponse,
        (401, "application/json"): ConfirmPreorderResponse,
        (403, "application/json"): ConfirmPreorderResponse,
        (404, "application/json"): ConfirmPreorderResponse,
        (429, "application/json"): ConfirmPreorderResponse,
        (500, "application/json"): ConfirmPreorderResponse,
        (503, "application/json"): ConfirmPreorderResponse,
    }

    def confirm_transport(
        self,
        shipment_id: str,
    ) -> Union[ConfirmTransportResponse]:
        """
        Confirms that the seller accepts the Amazon-partnered shipping estimate, agrees to allow Amazon to charge their account for the shipping cost, and requests that the Amazon-partnered carrier ship the inbound shipment.

        Prior to calling the confirmTransport operation, you should call the getTransportDetails operation to get the Amazon-partnered shipping estimate.

        Important: After confirming the transportation request, if the seller decides that they do not want the Amazon-partnered carrier to ship the inbound shipment, you can call the voidTransport operation to cancel the transportation request. Note that for a Small Parcel shipment, the seller has 24 hours after confirming a transportation request to void the transportation request. For a Less Than Truckload/Full Truckload (LTL/FTL) shipment, the seller has one hour after confirming a transportation request to void it. After the grace period has expired the seller's account will be charged for the shipping cost.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport/confirm"
        values = (shipment_id,)
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._confirm_transport_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _confirm_transport_params = (("shipmentId", "path"),)  # name, param in

    _confirm_transport_responses = {
        (200, "application/json"): ConfirmTransportResponse,
        (400, "application/json"): ConfirmTransportResponse,
        (401, "application/json"): ConfirmTransportResponse,
        (403, "application/json"): ConfirmTransportResponse,
        (404, "application/json"): ConfirmTransportResponse,
        (429, "application/json"): ConfirmTransportResponse,
        (500, "application/json"): ConfirmTransportResponse,
        (503, "application/json"): ConfirmTransportResponse,
    }

    def create_inbound_shipment(
        self,
        shipment_id: str,
        inbound_shipment_header: Dict[str, Any],
        inbound_shipment_items: List["InboundShipmentItem"],
        marketplace_id: str,
    ) -> Union[InboundShipmentResponse]:
        """
        Returns a new inbound shipment based on the specified shipmentId that was returned by the createInboundShipmentPlan operation.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
            inbound_shipment_header: Inbound shipment information used to create and update inbound shipments.
            inbound_shipment_items: A list of inbound shipment item information.
            marketplace_id: A marketplace identifier. Specifies the marketplace where the product would be stored.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}"
        values = (
            shipment_id,
            inbound_shipment_header,
            inbound_shipment_items,
            marketplace_id,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_inbound_shipment_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _create_inbound_shipment_params = (  # name, param in
        ("shipmentId", "path"),
        ("InboundShipmentHeader", "body"),
        ("InboundShipmentItems", "body"),
        ("MarketplaceId", "body"),
    )

    _create_inbound_shipment_responses = {
        (200, "application/json"): InboundShipmentResponse,
        (400, "application/json"): InboundShipmentResponse,
        (401, "application/json"): InboundShipmentResponse,
        (403, "application/json"): InboundShipmentResponse,
        (404, "application/json"): InboundShipmentResponse,
        (429, "application/json"): InboundShipmentResponse,
        (500, "application/json"): InboundShipmentResponse,
        (503, "application/json"): InboundShipmentResponse,
    }

    def create_inbound_shipment_plan(
        self,
        inbound_shipment_plan_request_items: List["InboundShipmentPlanRequestItem"],
        label_prep_preference: Union[
            Literal["SELLER_LABEL"], Literal["AMAZON_LABEL_ONLY"], Literal["AMAZON_LABEL_PREFERRED"]
        ],
        ship_from_address: Dict[str, Any],
        ship_to_country_code: str = None,
        ship_to_country_subdivision_code: str = None,
    ) -> Union[CreateInboundShipmentPlanResponse]:
        """
        Returns one or more inbound shipment plans, which provide the information you need to create one or more inbound shipments for a set of items that you specify. Multiple inbound shipment plans might be required so that items can be optimally placed in Amazon's fulfillment network—for example, positioning inventory closer to the customer. Alternatively, two inbound shipment plans might be created with the same Amazon fulfillment center destination if the two shipment plans require different processing—for example, items that require labels must be shipped separately from stickerless, commingled inventory.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            inbound_shipment_plan_request_items: no description.
            label_prep_preference: The preference for label preparation for an inbound shipment.
            ship_from_address: no description.
            ship_to_country_code: The two-character country code for the country where the inbound shipment is to be sent.
                Note: Not required. Specifying both ShipToCountryCode and ShipToCountrySubdivisionCode returns an error.
                Values:
                ShipToCountryCode values for North America:
                * CA – Canada
                * MX - Mexico
                * US - United States
                ShipToCountryCode values for MCI sellers in Europe:
                * DE – Germany
                * ES – Spain
                * FR – France
                * GB – United Kingdom
                * IT – Italy
                Default: The country code for the seller's home marketplace.
            ship_to_country_subdivision_code: The two-character country code, followed by a dash and then up to three characters that represent the subdivision of the country where the inbound shipment is to be sent. For example, "IN-MH". In full ISO 3166-2 format.
                Note: Not required. Specifying both ShipToCountryCode and ShipToCountrySubdivisionCode returns an error.
        """
        url = "/fba/inbound/v0/plans"
        values = (
            inbound_shipment_plan_request_items,
            label_prep_preference,
            ship_from_address,
            ship_to_country_code,
            ship_to_country_subdivision_code,
        )
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._create_inbound_shipment_plan_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _create_inbound_shipment_plan_params = (  # name, param in
        ("InboundShipmentPlanRequestItems", "body"),
        ("LabelPrepPreference", "body"),
        ("ShipFromAddress", "body"),
        ("ShipToCountryCode", "body"),
        ("ShipToCountrySubdivisionCode", "body"),
    )

    _create_inbound_shipment_plan_responses = {
        (200, "application/json"): CreateInboundShipmentPlanResponse,
        (400, "application/json"): CreateInboundShipmentPlanResponse,
        (401, "application/json"): CreateInboundShipmentPlanResponse,
        (403, "application/json"): CreateInboundShipmentPlanResponse,
        (404, "application/json"): CreateInboundShipmentPlanResponse,
        (429, "application/json"): CreateInboundShipmentPlanResponse,
        (500, "application/json"): CreateInboundShipmentPlanResponse,
        (503, "application/json"): CreateInboundShipmentPlanResponse,
    }

    def estimate_transport(
        self,
        shipment_id: str,
    ) -> Union[EstimateTransportResponse]:
        """
        Initiates the process of estimating the shipping cost for an inbound shipment by an Amazon-partnered carrier.

        Prior to calling the estimateTransport operation, you must call the putTransportDetails operation to provide Amazon with the transportation information for the inbound shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport/estimate"
        values = (shipment_id,)
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._estimate_transport_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _estimate_transport_params = (("shipmentId", "path"),)  # name, param in

    _estimate_transport_responses = {
        (200, "application/json"): EstimateTransportResponse,
        (400, "application/json"): EstimateTransportResponse,
        (401, "application/json"): EstimateTransportResponse,
        (403, "application/json"): EstimateTransportResponse,
        (404, "application/json"): EstimateTransportResponse,
        (429, "application/json"): EstimateTransportResponse,
        (500, "application/json"): EstimateTransportResponse,
        (503, "application/json"): EstimateTransportResponse,
    }

    def get_bill_of_lading(
        self,
        shipment_id: str,
    ) -> Union[GetBillOfLadingResponse]:
        """
        Returns a bill of lading for a Less Than Truckload/Full Truckload (LTL/FTL) shipment. The getBillOfLading operation returns PDF document data for printing a bill of lading for an Amazon-partnered Less Than Truckload/Full Truckload (LTL/FTL) inbound shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/billOfLading"
        values = (shipment_id,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_bill_of_lading_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_bill_of_lading_params = (("shipmentId", "path"),)  # name, param in

    _get_bill_of_lading_responses = {
        (200, "application/json"): GetBillOfLadingResponse,
        (400, "application/json"): GetBillOfLadingResponse,
        (401, "application/json"): GetBillOfLadingResponse,
        (403, "application/json"): GetBillOfLadingResponse,
        (404, "application/json"): GetBillOfLadingResponse,
        (429, "application/json"): GetBillOfLadingResponse,
        (500, "application/json"): GetBillOfLadingResponse,
        (503, "application/json"): GetBillOfLadingResponse,
    }

    def get_inbound_guidance(
        self,
        marketplace_id: str,
        seller_skulist: List[str] = None,
        asinlist: List[str] = None,
    ) -> Union[GetInboundGuidanceResponse]:
        """
        Returns information that lets a seller know if Amazon recommends sending an item to a given marketplace. In some cases, Amazon provides guidance for why a given SellerSKU or ASIN is not recommended for shipment to Amazon's fulfillment network. Sellers may still ship items that are not recommended, at their discretion.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            marketplace_id: A marketplace identifier. Specifies the marketplace where the product would be stored.
            seller_skulist: A list of SellerSKU values. Used to identify items for which you want inbound guidance for shipment to Amazon's fulfillment network. Note: SellerSKU is qualified by the SellerId, which is included with every Selling Partner API operation that you submit. If you specify a SellerSKU that identifies a variation parent ASIN, this operation returns an error. A variation parent ASIN represents a generic product that cannot be sold. Variation child ASINs represent products that have specific characteristics (such as size and color) and can be sold.
            asinlist: A list of ASIN values. Used to identify items for which you want inbound guidance for shipment to Amazon's fulfillment network. Note: If you specify a ASIN that identifies a variation parent ASIN, this operation returns an error. A variation parent ASIN represents a generic product that cannot be sold. Variation child ASINs represent products that have specific characteristics (such as size and color) and can be sold.
        """
        url = "/fba/inbound/v0/itemsGuidance"
        values = (
            marketplace_id,
            seller_skulist,
            asinlist,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_inbound_guidance_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_inbound_guidance_params = (  # name, param in
        ("MarketplaceId", "query"),
        ("SellerSKUList", "query"),
        ("ASINList", "query"),
    )

    _get_inbound_guidance_responses = {
        (200, "application/json"): GetInboundGuidanceResponse,
        (400, "application/json"): GetInboundGuidanceResponse,
        (401, "application/json"): GetInboundGuidanceResponse,
        (403, "application/json"): GetInboundGuidanceResponse,
        (404, "application/json"): GetInboundGuidanceResponse,
        (429, "application/json"): GetInboundGuidanceResponse,
        (500, "application/json"): GetInboundGuidanceResponse,
        (503, "application/json"): GetInboundGuidanceResponse,
    }

    def get_labels(
        self,
        shipment_id: str,
        page_type: Union[
            Literal["PackageLabel_Letter_2"],
            Literal["PackageLabel_Letter_4"],
            Literal["PackageLabel_Letter_6"],
            Literal["PackageLabel_Letter_6_CarrierLeft"],
            Literal["PackageLabel_A4_2"],
            Literal["PackageLabel_A4_4"],
            Literal["PackageLabel_Plain_Paper"],
            Literal["PackageLabel_Plain_Paper_CarrierBottom"],
            Literal["PackageLabel_Thermal"],
            Literal["PackageLabel_Thermal_Unified"],
            Literal["PackageLabel_Thermal_NonPCP"],
            Literal["PackageLabel_Thermal_No_Carrier_Rotation"],
        ],
        label_type: Union[Literal["BARCODE_2D"], Literal["UNIQUE"], Literal["PALLET"]],
        number_of_packages: int = None,
        package_labels_to_print: List[str] = None,
        number_of_pallets: int = None,
        page_size: int = None,
        page_start_index: int = None,
    ) -> Union[GetLabelsResponse]:
        """
        Returns package/pallet labels for faster and more accurate shipment processing at the Amazon fulfillment center.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
            page_type: The page type to use to print the labels. Submitting a PageType value that is not supported in your marketplace returns an error.
            label_type: The type of labels requested.
            number_of_packages: The number of packages in the shipment.
            package_labels_to_print: A list of identifiers that specify packages for which you want package labels printed.
                Must match CartonId values previously passed using the FBA Inbound Shipment Carton Information Feed. If not, the operation returns the IncorrectPackageIdentifier error code.
            number_of_pallets: The number of pallets in the shipment. This returns four identical labels for each pallet.
            page_size: The page size for paginating through the total packages' labels. This is a required parameter for Non-Partnered LTL Shipments. Max value:1000.
            page_start_index: The page start index for paginating through the total packages' labels. This is a required parameter for Non-Partnered LTL Shipments.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/labels"
        values = (
            shipment_id,
            page_type,
            label_type,
            number_of_packages,
            package_labels_to_print,
            number_of_pallets,
            page_size,
            page_start_index,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_labels_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_labels_params = (  # name, param in
        ("shipmentId", "path"),
        ("PageType", "query"),
        ("LabelType", "query"),
        ("NumberOfPackages", "query"),
        ("PackageLabelsToPrint", "query"),
        ("NumberOfPallets", "query"),
        ("PageSize", "query"),
        ("PageStartIndex", "query"),
    )

    _get_labels_responses = {
        (200, "application/json"): GetLabelsResponse,
        (400, "application/json"): GetLabelsResponse,
        (401, "application/json"): GetLabelsResponse,
        (403, "application/json"): GetLabelsResponse,
        (404, "application/json"): GetLabelsResponse,
        (429, "application/json"): GetLabelsResponse,
        (500, "application/json"): GetLabelsResponse,
        (503, "application/json"): GetLabelsResponse,
    }

    def get_preorder_info(
        self,
        shipment_id: str,
        marketplace_id: str,
    ) -> Union[GetPreorderInfoResponse]:
        """
        Returns pre-order information, including dates, that a seller needs before confirming a shipment for pre-order.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
            marketplace_id: A marketplace identifier. Specifies the marketplace the shipment is tied to.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/preorder"
        values = (
            shipment_id,
            marketplace_id,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_preorder_info_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_preorder_info_params = (  # name, param in
        ("shipmentId", "path"),
        ("MarketplaceId", "query"),
    )

    _get_preorder_info_responses = {
        (200, "application/json"): GetPreorderInfoResponse,
        (400, "application/json"): GetPreorderInfoResponse,
        (401, "application/json"): GetPreorderInfoResponse,
        (403, "application/json"): GetPreorderInfoResponse,
        (404, "application/json"): GetPreorderInfoResponse,
        (429, "application/json"): GetPreorderInfoResponse,
        (500, "application/json"): GetPreorderInfoResponse,
        (503, "application/json"): GetPreorderInfoResponse,
    }

    def get_prep_instructions(
        self,
        ship_to_country_code: str,
        seller_skulist: List[str] = None,
        asinlist: List[str] = None,
    ) -> Union[GetPrepInstructionsResponse]:
        """
        Returns labeling requirements and item preparation instructions to help prepare items for shipment to Amazon's fulfillment network.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            ship_to_country_code: The country code of the country to which the items will be shipped. Note that labeling requirements and item preparation instructions can vary by country.
            seller_skulist: A list of SellerSKU values. Used to identify items for which you want labeling requirements and item preparation instructions for shipment to Amazon's fulfillment network. The SellerSKU is qualified by the Seller ID, which is included with every call to the Seller Partner API.
                Note: Include seller SKUs that you have used to list items on Amazon's retail website. If you include a seller SKU that you have never used to list an item on Amazon's retail website, the seller SKU is returned in the InvalidSKUList property in the response.
            asinlist: A list of ASIN values. Used to identify items for which you want item preparation instructions to help with item sourcing decisions.
                Note: ASINs must be included in the product catalog for at least one of the marketplaces that the seller  participates in. Any ASIN that is not included in the product catalog for at least one of the marketplaces that the seller participates in is returned in the InvalidASINList property in the response. You can find out which marketplaces a seller participates in by calling the getMarketplaceParticipations operation in the Selling Partner API for Sellers.
        """
        url = "/fba/inbound/v0/prepInstructions"
        values = (
            ship_to_country_code,
            seller_skulist,
            asinlist,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_prep_instructions_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_prep_instructions_params = (  # name, param in
        ("ShipToCountryCode", "query"),
        ("SellerSKUList", "query"),
        ("ASINList", "query"),
    )

    _get_prep_instructions_responses = {
        (200, "application/json"): GetPrepInstructionsResponse,
        (400, "application/json"): GetPrepInstructionsResponse,
        (401, "application/json"): GetPrepInstructionsResponse,
        (403, "application/json"): GetPrepInstructionsResponse,
        (404, "application/json"): GetPrepInstructionsResponse,
        (429, "application/json"): GetPrepInstructionsResponse,
        (500, "application/json"): GetPrepInstructionsResponse,
        (503, "application/json"): GetPrepInstructionsResponse,
    }

    def get_shipment_items(
        self,
        query_type: Union[Literal["DATE_RANGE"], Literal["NEXT_TOKEN"]],
        marketplace_id: str,
        last_updated_after: datetime = None,
        last_updated_before: datetime = None,
        next_token: str = None,
    ) -> Union[GetShipmentItemsResponse]:
        """
        Returns a list of items in a specified inbound shipment, or a list of items that were updated within a specified time frame.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            last_updated_after: A date used for selecting inbound shipment items that were last updated after (or at) a specified time. The selection includes updates made by Amazon and by the seller.
            last_updated_before: A date used for selecting inbound shipment items that were last updated before (or at) a specified time. The selection includes updates made by Amazon and by the seller.
            query_type: Indicates whether items are returned using a date range (by providing the LastUpdatedAfter and LastUpdatedBefore parameters), or using NextToken, which continues returning items specified in a previous request.
            next_token: A string token returned in the response to your previous request.
            marketplace_id: A marketplace identifier. Specifies the marketplace where the product would be stored.
        """
        url = "/fba/inbound/v0/shipmentItems"
        values = (
            last_updated_after,
            last_updated_before,
            query_type,
            next_token,
            marketplace_id,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_shipment_items_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_shipment_items_params = (  # name, param in
        ("LastUpdatedAfter", "query"),
        ("LastUpdatedBefore", "query"),
        ("QueryType", "query"),
        ("NextToken", "query"),
        ("MarketplaceId", "query"),
    )

    _get_shipment_items_responses = {
        (200, "application/json"): GetShipmentItemsResponse,
        (400, "application/json"): GetShipmentItemsResponse,
        (401, "application/json"): GetShipmentItemsResponse,
        (403, "application/json"): GetShipmentItemsResponse,
        (404, "application/json"): GetShipmentItemsResponse,
        (429, "application/json"): GetShipmentItemsResponse,
        (500, "application/json"): GetShipmentItemsResponse,
        (503, "application/json"): GetShipmentItemsResponse,
    }

    def get_shipment_items_by_shipment_id(
        self,
        shipment_id: str,
        marketplace_id: str,
    ) -> Union[GetShipmentItemsResponse]:
        """
        Returns a list of items in a specified inbound shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier used for selecting items in a specific inbound shipment.
            marketplace_id: A marketplace identifier. Specifies the marketplace where the product would be stored.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/items"
        values = (
            shipment_id,
            marketplace_id,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_shipment_items_by_shipment_id_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_shipment_items_by_shipment_id_params = (  # name, param in
        ("shipmentId", "path"),
        ("MarketplaceId", "query"),
    )

    _get_shipment_items_by_shipment_id_responses = {
        (200, "application/json"): GetShipmentItemsResponse,
        (400, "application/json"): GetShipmentItemsResponse,
        (401, "application/json"): GetShipmentItemsResponse,
        (403, "application/json"): GetShipmentItemsResponse,
        (404, "application/json"): GetShipmentItemsResponse,
        (429, "application/json"): GetShipmentItemsResponse,
        (500, "application/json"): GetShipmentItemsResponse,
        (503, "application/json"): GetShipmentItemsResponse,
    }

    def get_shipments(
        self,
        query_type: Union[Literal["SHIPMENT"], Literal["DATE_RANGE"], Literal["NEXT_TOKEN"]],
        marketplace_id: str,
        shipment_status_list: List[
            Union[
                Literal["WORKING"],
                Literal["SHIPPED"],
                Literal["RECEIVING"],
                Literal["CANCELLED"],
                Literal["DELETED"],
                Literal["CLOSED"],
                Literal["ERROR"],
                Literal["IN_TRANSIT"],
                Literal["DELIVERED"],
                Literal["CHECKED_IN"],
            ]
        ] = None,
        shipment_id_list: List[str] = None,
        last_updated_after: datetime = None,
        last_updated_before: datetime = None,
        next_token: str = None,
    ) -> Union[GetShipmentsResponse]:
        """
        Returns a list of inbound shipments based on criteria that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_status_list: A list of ShipmentStatus values. Used to select shipments with a current status that matches the status values that you specify.
            shipment_id_list: A list of shipment IDs used to select the shipments that you want. If both ShipmentStatusList and ShipmentIdList are specified, only shipments that match both parameters are returned.
            last_updated_after: A date used for selecting inbound shipments that were last updated after (or at) a specified time. The selection includes updates made by Amazon and by the seller.
            last_updated_before: A date used for selecting inbound shipments that were last updated before (or at) a specified time. The selection includes updates made by Amazon and by the seller.
            query_type: Indicates whether shipments are returned using shipment information (by providing the ShipmentStatusList or ShipmentIdList parameters), using a date range (by providing the LastUpdatedAfter and LastUpdatedBefore parameters), or by using NextToken to continue returning items specified in a previous request.
            next_token: A string token returned in the response to your previous request.
            marketplace_id: A marketplace identifier. Specifies the marketplace where the product would be stored.
        """
        url = "/fba/inbound/v0/shipments"
        values = (
            shipment_status_list,
            shipment_id_list,
            last_updated_after,
            last_updated_before,
            query_type,
            next_token,
            marketplace_id,
        )
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_shipments_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_shipments_params = (  # name, param in
        ("ShipmentStatusList", "query"),
        ("ShipmentIdList", "query"),
        ("LastUpdatedAfter", "query"),
        ("LastUpdatedBefore", "query"),
        ("QueryType", "query"),
        ("NextToken", "query"),
        ("MarketplaceId", "query"),
    )

    _get_shipments_responses = {
        (200, "application/json"): GetShipmentsResponse,
        (400, "application/json"): GetShipmentsResponse,
        (401, "application/json"): GetShipmentsResponse,
        (403, "application/json"): GetShipmentsResponse,
        (404, "application/json"): GetShipmentsResponse,
        (429, "application/json"): GetShipmentsResponse,
        (500, "application/json"): GetShipmentsResponse,
        (503, "application/json"): GetShipmentsResponse,
    }

    def get_transport_details(
        self,
        shipment_id: str,
    ) -> Union[GetTransportDetailsResponse]:
        """
        Returns current transportation information about an inbound shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport"
        values = (shipment_id,)
        response = self._parse_args_and_request(
            url,
            "GET",
            values,
            self._get_transport_details_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _get_transport_details_params = (("shipmentId", "path"),)  # name, param in

    _get_transport_details_responses = {
        (200, "application/json"): GetTransportDetailsResponse,
        (400, "application/json"): GetTransportDetailsResponse,
        (401, "application/json"): GetTransportDetailsResponse,
        (403, "application/json"): GetTransportDetailsResponse,
        (404, "application/json"): GetTransportDetailsResponse,
        (429, "application/json"): GetTransportDetailsResponse,
        (500, "application/json"): GetTransportDetailsResponse,
        (503, "application/json"): GetTransportDetailsResponse,
    }

    def put_transport_details(
        self,
        shipment_id: str,
        is_partnered: bool,
        shipment_type: Union[Literal["SP"], Literal["LTL"]],
        transport_details: Dict[str, Any],
    ) -> Union[PutTransportDetailsResponse]:
        """
        Sends transportation information to Amazon about an inbound shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
            is_partnered: Indicates whether a putTransportDetails request is for an Amazon-partnered carrier.
            shipment_type: Specifies the carrier shipment type in a putTransportDetails request.
            transport_details: Information required to create an Amazon-partnered carrier shipping estimate, or to alert the Amazon fulfillment center to the arrival of an inbound shipment by a non-Amazon-partnered carrier.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport"
        values = (
            shipment_id,
            is_partnered,
            shipment_type,
            transport_details,
        )
        response = self._parse_args_and_request(
            url,
            "PUT",
            values,
            self._put_transport_details_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _put_transport_details_params = (  # name, param in
        ("shipmentId", "path"),
        ("IsPartnered", "body"),
        ("ShipmentType", "body"),
        ("TransportDetails", "body"),
    )

    _put_transport_details_responses = {
        (200, "application/json"): PutTransportDetailsResponse,
        (400, "application/json"): PutTransportDetailsResponse,
        (401, "application/json"): PutTransportDetailsResponse,
        (403, "application/json"): PutTransportDetailsResponse,
        (404, "application/json"): PutTransportDetailsResponse,
        (429, "application/json"): PutTransportDetailsResponse,
        (500, "application/json"): PutTransportDetailsResponse,
        (503, "application/json"): PutTransportDetailsResponse,
    }

    def update_inbound_shipment(
        self,
        shipment_id: str,
        inbound_shipment_header: Dict[str, Any],
        inbound_shipment_items: List["InboundShipmentItem"],
        marketplace_id: str,
    ) -> Union[InboundShipmentResponse]:
        """
        Updates or removes items from the inbound shipment identified by the specified shipment identifier. Adding new items is not supported.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
            inbound_shipment_header: Inbound shipment information used to create and update inbound shipments.
            inbound_shipment_items: A list of inbound shipment item information.
            marketplace_id: A marketplace identifier. Specifies the marketplace where the product would be stored.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}"
        values = (
            shipment_id,
            inbound_shipment_header,
            inbound_shipment_items,
            marketplace_id,
        )
        response = self._parse_args_and_request(
            url,
            "PUT",
            values,
            self._update_inbound_shipment_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _update_inbound_shipment_params = (  # name, param in
        ("shipmentId", "path"),
        ("InboundShipmentHeader", "body"),
        ("InboundShipmentItems", "body"),
        ("MarketplaceId", "body"),
    )

    _update_inbound_shipment_responses = {
        (200, "application/json"): InboundShipmentResponse,
        (400, "application/json"): InboundShipmentResponse,
        (401, "application/json"): InboundShipmentResponse,
        (403, "application/json"): InboundShipmentResponse,
        (404, "application/json"): InboundShipmentResponse,
        (429, "application/json"): InboundShipmentResponse,
        (500, "application/json"): InboundShipmentResponse,
        (503, "application/json"): InboundShipmentResponse,
    }

    def void_transport(
        self,
        shipment_id: str,
    ) -> Union[VoidTransportResponse]:
        """
        Cancels a previously-confirmed request to ship an inbound shipment using an Amazon-partnered carrier.

        To be successful, you must call this operation before the VoidDeadline date that is returned by the getTransportDetails operation.

        Important: The VoidDeadline date is 24 hours after you confirm a Small Parcel shipment transportation request or one hour after you confirm a Less Than Truckload/Full Truckload (LTL/FTL) shipment transportation request. After the void deadline passes, your account will be charged for the shipping cost.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipment_id: A shipment identifier originally returned by the createInboundShipmentPlan operation.
        """
        url = "/fba/inbound/v0/shipments/{shipmentId}/transport/void"
        values = (shipment_id,)
        response = self._parse_args_and_request(
            url,
            "POST",
            values,
            self._void_transport_params,
        )
        klass = self._update_verification_status_responses.get(response.status_code)
        # noinspection PyArgumentList
        obj = klass(**response.json())
        return obj

    _void_transport_params = (("shipmentId", "path"),)  # name, param in

    _void_transport_responses = {
        (200, "application/json"): VoidTransportResponse,
        (400, "application/json"): VoidTransportResponse,
        (401, "application/json"): VoidTransportResponse,
        (403, "application/json"): VoidTransportResponse,
        (404, "application/json"): VoidTransportResponse,
        (429, "application/json"): VoidTransportResponse,
        (500, "application/json"): VoidTransportResponse,
        (503, "application/json"): VoidTransportResponse,
    }
