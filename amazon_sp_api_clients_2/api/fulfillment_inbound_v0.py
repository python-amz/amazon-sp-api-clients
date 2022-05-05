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
from typing import Any, List, Dict, Union, Literal


@attrs.define
class Error:
    pass


@attrs.define
class ErrorList:
    pass


@attrs.define
class ASINInboundGuidance:
    pass


@attrs.define
class ASINInboundGuidanceList:
    pass


@attrs.define
class ASINPrepInstructions:
    pass


@attrs.define
class ASINPrepInstructionsList:
    pass


@attrs.define
class Address:
    pass


@attrs.define
class AmazonPrepFeesDetails:
    pass


@attrs.define
class AmazonPrepFeesDetailsList:
    pass


@attrs.define
class Amount:
    pass


@attrs.define
class BarcodeInstruction:
    pass


@attrs.define
class BigDecimalType:
    pass


@attrs.define
class BoxContentsFeeDetails:
    pass


@attrs.define
class BoxContentsSource:
    pass


@attrs.define
class Condition:
    pass


@attrs.define
class ConfirmPreorderResult:
    pass


@attrs.define
class ConfirmPreorderResponse:
    pass


@attrs.define
class CommonTransportResult:
    pass


@attrs.define
class ConfirmTransportResponse:
    pass


@attrs.define
class Contact:
    pass


@attrs.define
class CreateInboundShipmentPlanRequest:
    pass


@attrs.define
class CreateInboundShipmentPlanResult:
    pass


@attrs.define
class CreateInboundShipmentPlanResponse:
    pass


@attrs.define
class InboundShipmentRequest:
    pass


@attrs.define
class InboundShipmentResult:
    pass


@attrs.define
class InboundShipmentResponse:
    pass


@attrs.define
class CurrencyCode:
    pass


@attrs.define
class DateStringType:
    pass


@attrs.define
class Dimensions:
    pass


@attrs.define
class ErrorReason:
    pass


@attrs.define
class EstimateTransportResponse:
    pass


@attrs.define
class GetBillOfLadingResponse:
    pass


@attrs.define
class GetInboundGuidanceResult:
    pass


@attrs.define
class GetInboundGuidanceResponse:
    pass


@attrs.define
class LabelDownloadURL:
    pass


@attrs.define
class BillOfLadingDownloadURL:
    pass


@attrs.define
class GetLabelsResponse:
    pass


@attrs.define
class GetPreorderInfoResult:
    pass


@attrs.define
class GetPreorderInfoResponse:
    pass


@attrs.define
class GetPrepInstructionsResult:
    pass


@attrs.define
class GetPrepInstructionsResponse:
    pass


@attrs.define
class GetTransportDetailsResult:
    pass


@attrs.define
class GetTransportDetailsResponse:
    pass


@attrs.define
class GuidanceReason:
    pass


@attrs.define
class GuidanceReasonList:
    pass


@attrs.define
class InboundGuidance:
    pass


@attrs.define
class InboundShipmentHeader:
    pass


@attrs.define
class InboundShipmentInfo:
    pass


@attrs.define
class InboundShipmentItem:
    pass


@attrs.define
class InboundShipmentItemList:
    pass


@attrs.define
class InboundShipmentList:
    pass


@attrs.define
class InboundShipmentPlan:
    pass


@attrs.define
class InboundShipmentPlanItem:
    pass


@attrs.define
class InboundShipmentPlanItemList:
    pass


@attrs.define
class InboundShipmentPlanList:
    pass


@attrs.define
class InboundShipmentPlanRequestItem:
    pass


@attrs.define
class InboundShipmentPlanRequestItemList:
    pass


@attrs.define
class IntendedBoxContentsSource:
    pass


@attrs.define
class InvalidASIN:
    pass


@attrs.define
class InvalidASINList:
    pass


@attrs.define
class InvalidSKU:
    pass


@attrs.define
class InvalidSKUList:
    pass


@attrs.define
class LabelPrepPreference:
    pass


@attrs.define
class LabelPrepType:
    pass


@attrs.define
class GetShipmentItemsResult:
    pass


@attrs.define
class GetShipmentItemsResponse:
    pass


@attrs.define
class GetShipmentsResult:
    pass


@attrs.define
class GetShipmentsResponse:
    pass


@attrs.define
class NonPartneredLtlDataInput:
    pass


@attrs.define
class NonPartneredLtlDataOutput:
    pass


@attrs.define
class NonPartneredSmallParcelDataInput:
    pass


@attrs.define
class NonPartneredSmallParcelDataOutput:
    pass


@attrs.define
class NonPartneredSmallParcelPackageInput:
    pass


@attrs.define
class NonPartneredSmallParcelPackageInputList:
    pass


@attrs.define
class NonPartneredSmallParcelPackageOutput:
    pass


@attrs.define
class NonPartneredSmallParcelPackageOutputList:
    pass


@attrs.define
class PackageStatus:
    pass


@attrs.define
class Pallet:
    pass


@attrs.define
class PalletList:
    pass


@attrs.define
class PartneredEstimate:
    pass


@attrs.define
class PartneredLtlDataInput:
    pass


@attrs.define
class PartneredLtlDataOutput:
    pass


@attrs.define
class PartneredSmallParcelDataInput:
    pass


@attrs.define
class PartneredSmallParcelDataOutput:
    pass


@attrs.define
class PartneredSmallParcelPackageInput:
    pass


@attrs.define
class PartneredSmallParcelPackageInputList:
    pass


@attrs.define
class PartneredSmallParcelPackageOutput:
    pass


@attrs.define
class PartneredSmallParcelPackageOutputList:
    pass


@attrs.define
class PrepDetails:
    pass


@attrs.define
class PrepDetailsList:
    pass


@attrs.define
class PrepGuidance:
    pass


@attrs.define
class PrepInstruction:
    pass


@attrs.define
class PrepInstructionList:
    pass


@attrs.define
class PrepOwner:
    pass


@attrs.define
class ProNumber:
    pass


@attrs.define
class PutTransportDetailsRequest:
    pass


@attrs.define
class PutTransportDetailsResponse:
    pass


@attrs.define
class Quantity:
    pass


@attrs.define
class SKUInboundGuidance:
    pass


@attrs.define
class SKUInboundGuidanceList:
    pass


@attrs.define
class SKUPrepInstructions:
    pass


@attrs.define
class SKUPrepInstructionsList:
    pass


@attrs.define
class SellerFreightClass:
    pass


@attrs.define
class ShipmentStatus:
    pass


@attrs.define
class ShipmentType:
    pass


@attrs.define
class TimeStampStringType:
    pass


@attrs.define
class TrackingId:
    pass


@attrs.define
class TransportContent:
    pass


@attrs.define
class TransportDetailInput:
    pass


@attrs.define
class TransportDetailOutput:
    pass


@attrs.define
class TransportHeader:
    pass


@attrs.define
class TransportResult:
    pass


@attrs.define
class TransportStatus:
    pass


@attrs.define
class UnitOfMeasurement:
    pass


@attrs.define
class UnitOfWeight:
    pass


@attrs.define
class UnsignedIntType:
    pass


@attrs.define
class VoidTransportResponse:
    pass


@attrs.define
class Weight:
    pass


class FulfillmentInboundV0Client(BaseClient):
    def confirm_preorder(
        self,
        shipment_id: str,
        need_by_date: str,
        marketplace_id: str,
    ):
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
        response = self._parse_args_and_request(url, "PUT", values, self._confirm_preorder_params)
        return response

    _confirm_preorder_params = (  # name, param in
        ("shipmentId", "path"),
        ("NeedByDate", "query"),
        ("MarketplaceId", "query"),
    )

    def confirm_transport(
        self,
        shipment_id: str,
    ):
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
        response = self._parse_args_and_request(url, "POST", values, self._confirm_transport_params)
        return response

    _confirm_transport_params = (("shipmentId", "path"),)  # name, param in

    def create_inbound_shipment(
        self,
        shipment_id: str,
        inbound_shipment_header: dict[str, Any],
        inbound_shipment_items: list[dict[str, Any]],
        marketplace_id: str,
    ):
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
        response = self._parse_args_and_request(url, "POST", values, self._create_inbound_shipment_params)
        return response

    _create_inbound_shipment_params = (  # name, param in
        ("shipmentId", "path"),
        ("InboundShipmentHeader", "body"),
        ("InboundShipmentItems", "body"),
        ("MarketplaceId", "body"),
    )

    def create_inbound_shipment_plan(
        self,
    ):
        """
        Returns one or more inbound shipment plans, which provide the information you need to create one or more inbound shipments for a set of items that you specify. Multiple inbound shipment plans might be required so that items can be optimally placed in Amazon's fulfillment network��for example, positioning inventory closer to the customer. Alternatively, two inbound shipment plans might be created with the same Amazon fulfillment center destination if the two shipment plans require different processing��for example, items that require labels must be shipped separately from stickerless, commingled inventory.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        url = "/fba/inbound/v0/plans"
        values = ()
        response = self._parse_args_and_request(url, "POST", values, self._create_inbound_shipment_plan_params)
        return response

    _create_inbound_shipment_plan_params = ()  # name, param in

    def estimate_transport(
        self,
        shipment_id: str,
    ):
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
        response = self._parse_args_and_request(url, "POST", values, self._estimate_transport_params)
        return response

    _estimate_transport_params = (("shipmentId", "path"),)  # name, param in

    def get_bill_of_lading(
        self,
        shipment_id: str,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_bill_of_lading_params)
        return response

    _get_bill_of_lading_params = (("shipmentId", "path"),)  # name, param in

    def get_inbound_guidance(
        self,
        marketplace_id: str,
        seller_skulist: list[str] = None,
        asinlist: list[str] = None,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_inbound_guidance_params)
        return response

    _get_inbound_guidance_params = (  # name, param in
        ("MarketplaceId", "query"),
        ("SellerSKUList", "query"),
        ("ASINList", "query"),
    )

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
        package_labels_to_print: list[str] = None,
        number_of_pallets: int = None,
        page_size: int = None,
        page_start_index: int = None,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_labels_params)
        return response

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

    def get_preorder_info(
        self,
        shipment_id: str,
        marketplace_id: str,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_preorder_info_params)
        return response

    _get_preorder_info_params = (  # name, param in
        ("shipmentId", "path"),
        ("MarketplaceId", "query"),
    )

    def get_prep_instructions(
        self,
        ship_to_country_code: str,
        seller_skulist: list[str] = None,
        asinlist: list[str] = None,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_prep_instructions_params)
        return response

    _get_prep_instructions_params = (  # name, param in
        ("ShipToCountryCode", "query"),
        ("SellerSKUList", "query"),
        ("ASINList", "query"),
    )

    def get_shipment_items(
        self,
        query_type: Union[Literal["DATE_RANGE"], Literal["NEXT_TOKEN"]],
        marketplace_id: str,
        last_updated_after: str = None,
        last_updated_before: str = None,
        next_token: str = None,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_shipment_items_params)
        return response

    _get_shipment_items_params = (  # name, param in
        ("LastUpdatedAfter", "query"),
        ("LastUpdatedBefore", "query"),
        ("QueryType", "query"),
        ("NextToken", "query"),
        ("MarketplaceId", "query"),
    )

    def get_shipment_items_by_shipment_id(
        self,
        shipment_id: str,
        marketplace_id: str,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_shipment_items_by_shipment_id_params)
        return response

    _get_shipment_items_by_shipment_id_params = (  # name, param in
        ("shipmentId", "path"),
        ("MarketplaceId", "query"),
    )

    def get_shipments(
        self,
        query_type: Union[Literal["SHIPMENT"], Literal["DATE_RANGE"], Literal["NEXT_TOKEN"]],
        marketplace_id: str,
        shipment_status_list: list[
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
        shipment_id_list: list[str] = None,
        last_updated_after: str = None,
        last_updated_before: str = None,
        next_token: str = None,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_shipments_params)
        return response

    _get_shipments_params = (  # name, param in
        ("ShipmentStatusList", "query"),
        ("ShipmentIdList", "query"),
        ("LastUpdatedAfter", "query"),
        ("LastUpdatedBefore", "query"),
        ("QueryType", "query"),
        ("NextToken", "query"),
        ("MarketplaceId", "query"),
    )

    def get_transport_details(
        self,
        shipment_id: str,
    ):
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
        response = self._parse_args_and_request(url, "GET", values, self._get_transport_details_params)
        return response

    _get_transport_details_params = (("shipmentId", "path"),)  # name, param in

    def put_transport_details(
        self,
        shipment_id: str,
        is_partnered: bool,
        shipment_type: Union[Literal["SP"], Literal["LTL"]],
        transport_details: dict[str, Any],
    ):
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
        response = self._parse_args_and_request(url, "PUT", values, self._put_transport_details_params)
        return response

    _put_transport_details_params = (  # name, param in
        ("shipmentId", "path"),
        ("IsPartnered", "body"),
        ("ShipmentType", "body"),
        ("TransportDetails", "body"),
    )

    def update_inbound_shipment(
        self,
        shipment_id: str,
        inbound_shipment_header: dict[str, Any],
        inbound_shipment_items: list[dict[str, Any]],
        marketplace_id: str,
    ):
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
        response = self._parse_args_and_request(url, "PUT", values, self._update_inbound_shipment_params)
        return response

    _update_inbound_shipment_params = (  # name, param in
        ("shipmentId", "path"),
        ("InboundShipmentHeader", "body"),
        ("InboundShipmentItems", "body"),
        ("MarketplaceId", "body"),
    )

    def void_transport(
        self,
        shipment_id: str,
    ):
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
        response = self._parse_args_and_request(url, "POST", values, self._void_transport_params)
        return response

    _void_transport_params = (("shipmentId", "path"),)  # name, param in
