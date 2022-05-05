"""
Selling Partner API for Fulfillment Inbound
=============================================================================================
The Selling Partner API for Fulfillment Inbound lets you create applications that create and update inbound shipments of inventory to Amazon's fulfillment network.
Contact Amazon: Selling Partner API Developer Support https://sellercentral.amazon.com/gp/mws/contactus.html
License for the OpenAPI file: Apache License 2.0 http://www.apache.org/licenses/LICENSE-2.0
API Version: v0
"""
from ..utils.base_client import BaseClient
from typing import Any, List, Dict, Union, Literal


class FulfillmentInboundV0Client(BaseClient):
    def get_inbound_guidance(
        self,
        Marketplace_id: str,
        Seller_skulist: list[str] = None,
        ASINList: list[str] = None,
    ):
        """
        Returns information that lets a seller know if Amazon recommends sending an item to a given marketplace. In some cases, Amazon provides guidance for why a given SellerSKU or ASIN is not recommended for shipment to Amazon's fulfillment network. Sellers may still ship items that are not recommended, at their discretion.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            Marketplace_id: A marketplace identifier. Specifies the marketplace where the product would be stored.
            Seller_skulist: A list of SellerSKU values. Used to identify items for which you want inbound guidance for shipment to Amazon's fulfillment network. Note: SellerSKU is qualified by the SellerId, which is included with every Selling Partner API operation that you submit. If you specify a SellerSKU that identifies a variation parent ASIN, this operation returns an error. A variation parent ASIN represents a generic product that cannot be sold. Variation child ASINs represent products that have specific characteristics (such as size and color) and can be sold.
            ASINList: A list of ASIN values. Used to identify items for which you want inbound guidance for shipment to Amazon's fulfillment network. Note: If you specify a ASIN that identifies a variation parent ASIN, this operation returns an error. A variation parent ASIN represents a generic product that cannot be sold. Variation child ASINs represent products that have specific characteristics (such as size and color) and can be sold.
        """
        path_parameters = {}

        url = "/fba/inbound/v0/itemsGuidance".format(**path_parameters)

        query_parameters = {}

        query_parameters["MarketplaceId"] = Marketplace_id

        if Seller_skulist is not None:
            query_parameters["SellerSKUList"] = Seller_skulist

        if ASINList is not None:
            query_parameters["ASINList"] = ASINList

    def create_inbound_shipment_plan(
        self,
    ):
        """
        Returns one or more inbound shipment plans, which provide the information you need to create one or more inbound shipments for a set of items that you specify. Multiple inbound shipment plans might be required so that items can be optimally placed in Amazon's fulfillment network¡ªfor example, positioning inventory closer to the customer. Alternatively, two inbound shipment plans might be created with the same Amazon fulfillment center destination if the two shipment plans require different processing¡ªfor example, items that require labels must be shipped separately from stickerless, commingled inventory.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        """
        path_parameters = {}

        url = "/fba/inbound/v0/plans".format(**path_parameters)

        query_parameters = {}

    def create_inbound_shipment(
        self,
        shipment_id: str,
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
        """
        path_parameters = {}

        path_parameters["shipmentId"] = shipment_id

        url = "/fba/inbound/v0/shipments/{shipmentId}".format(**path_parameters)

        query_parameters = {}

    def update_inbound_shipment(
        self,
        shipment_id: str,
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
        """
        path_parameters = {}

        path_parameters["shipmentId"] = shipment_id

        url = "/fba/inbound/v0/shipments/{shipmentId}".format(**path_parameters)

        query_parameters = {}

    def get_preorder_info(
        self,
        shipment_id: str,
        Marketplace_id: str,
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
            Marketplace_id: A marketplace identifier. Specifies the marketplace the shipment is tied to.
        """
        path_parameters = {}

        path_parameters["shipmentId"] = shipment_id

        url = "/fba/inbound/v0/shipments/{shipmentId}/preorder".format(**path_parameters)

        query_parameters = {}

        query_parameters["MarketplaceId"] = Marketplace_id

    def confirm_preorder(
        self,
        shipment_id: str,
        Need_by_date: str,
        Marketplace_id: str,
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
            Need_by_date: Date that the shipment must arrive at the Amazon fulfillment center to avoid delivery promise breaks for pre-ordered items. Must be in YYYY-MM-DD format. The response to the getPreorderInfo operation returns this value.
            Marketplace_id: A marketplace identifier. Specifies the marketplace the shipment is tied to.
        """
        path_parameters = {}

        path_parameters["shipmentId"] = shipment_id

        url = "/fba/inbound/v0/shipments/{shipmentId}/preorder/confirm".format(**path_parameters)

        query_parameters = {}

        query_parameters["NeedByDate"] = Need_by_date

        query_parameters["MarketplaceId"] = Marketplace_id

    def get_prep_instructions(
        self,
        Ship_to_country_code: str,
        Seller_skulist: list[str] = None,
        ASINList: list[str] = None,
    ):
        """
        Returns labeling requirements and item preparation instructions to help prepare items for shipment to Amazon's fulfillment network.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            Ship_to_country_code: The country code of the country to which the items will be shipped. Note that labeling requirements and item preparation instructions can vary by country.
            Seller_skulist: A list of SellerSKU values. Used to identify items for which you want labeling requirements and item preparation instructions for shipment to Amazon's fulfillment network. The SellerSKU is qualified by the Seller ID, which is included with every call to the Seller Partner API.

        Note: Include seller SKUs that you have used to list items on Amazon's retail website. If you include a seller SKU that you have never used to list an item on Amazon's retail website, the seller SKU is returned in the InvalidSKUList property in the response.
            ASINList: A list of ASIN values. Used to identify items for which you want item preparation instructions to help with item sourcing decisions.

        Note: ASINs must be included in the product catalog for at least one of the marketplaces that the seller  participates in. Any ASIN that is not included in the product catalog for at least one of the marketplaces that the seller participates in is returned in the InvalidASINList property in the response. You can find out which marketplaces a seller participates in by calling the getMarketplaceParticipations operation in the Selling Partner API for Sellers.
        """
        path_parameters = {}

        url = "/fba/inbound/v0/prepInstructions".format(**path_parameters)

        query_parameters = {}

        query_parameters["ShipToCountryCode"] = Ship_to_country_code

        if Seller_skulist is not None:
            query_parameters["SellerSKUList"] = Seller_skulist

        if ASINList is not None:
            query_parameters["ASINList"] = ASINList

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
        path_parameters = {}

        path_parameters["shipmentId"] = shipment_id

        url = "/fba/inbound/v0/shipments/{shipmentId}/transport".format(**path_parameters)

        query_parameters = {}

    def put_transport_details(
        self,
        shipment_id: str,
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
        """
        path_parameters = {}

        path_parameters["shipmentId"] = shipment_id

        url = "/fba/inbound/v0/shipments/{shipmentId}/transport".format(**path_parameters)

        query_parameters = {}

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
        path_parameters = {}

        path_parameters["shipmentId"] = shipment_id

        url = "/fba/inbound/v0/shipments/{shipmentId}/transport/void".format(**path_parameters)

        query_parameters = {}

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
        path_parameters = {}

        path_parameters["shipmentId"] = shipment_id

        url = "/fba/inbound/v0/shipments/{shipmentId}/transport/estimate".format(**path_parameters)

        query_parameters = {}

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
        path_parameters = {}

        path_parameters["shipmentId"] = shipment_id

        url = "/fba/inbound/v0/shipments/{shipmentId}/transport/confirm".format(**path_parameters)

        query_parameters = {}

    def get_labels(
        self,
        shipment_id: str,
        Page_type: str,
        Label_type: str,
        Number_of_packages: int = None,
        Package_labels_to_print: list[str] = None,
        Number_of_pallets: int = None,
        Page_size: int = None,
        Page_start_index: int = None,
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
            Page_type: The page type to use to print the labels. Submitting a PageType value that is not supported in your marketplace returns an error.
            Label_type: The type of labels requested.
            Number_of_packages: The number of packages in the shipment.
            Package_labels_to_print: A list of identifiers that specify packages for which you want package labels printed.

        Must match CartonId values previously passed using the FBA Inbound Shipment Carton Information Feed. If not, the operation returns the IncorrectPackageIdentifier error code.
            Number_of_pallets: The number of pallets in the shipment. This returns four identical labels for each pallet.
            Page_size: The page size for paginating through the total packages' labels. This is a required parameter for Non-Partnered LTL Shipments. Max value:1000.
            Page_start_index: The page start index for paginating through the total packages' labels. This is a required parameter for Non-Partnered LTL Shipments.
        """
        path_parameters = {}

        path_parameters["shipmentId"] = shipment_id

        url = "/fba/inbound/v0/shipments/{shipmentId}/labels".format(**path_parameters)

        query_parameters = {}

        query_parameters["PageType"] = Page_type

        query_parameters["LabelType"] = Label_type

        if Number_of_packages is not None:
            query_parameters["NumberOfPackages"] = Number_of_packages

        if Package_labels_to_print is not None:
            query_parameters["PackageLabelsToPrint"] = Package_labels_to_print

        if Number_of_pallets is not None:
            query_parameters["NumberOfPallets"] = Number_of_pallets

        if Page_size is not None:
            query_parameters["PageSize"] = Page_size

        if Page_start_index is not None:
            query_parameters["PageStartIndex"] = Page_start_index

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
        path_parameters = {}

        path_parameters["shipmentId"] = shipment_id

        url = "/fba/inbound/v0/shipments/{shipmentId}/billOfLading".format(**path_parameters)

        query_parameters = {}

    def get_shipments(
        self,
        Shipment_status_list: list[
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
        Shipment_id_list: list[str] = None,
        Last_updated_after: str = None,
        Last_updated_before: str = None,
        Query_type: str,
        Next_token: str = None,
        Marketplace_id: str,
    ):
        """
        Returns a list of inbound shipments based on criteria that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            Shipment_status_list: A list of ShipmentStatus values. Used to select shipments with a current status that matches the status values that you specify.
            Shipment_id_list: A list of shipment IDs used to select the shipments that you want. If both ShipmentStatusList and ShipmentIdList are specified, only shipments that match both parameters are returned.
            Last_updated_after: A date used for selecting inbound shipments that were last updated after (or at) a specified time. The selection includes updates made by Amazon and by the seller.
            Last_updated_before: A date used for selecting inbound shipments that were last updated before (or at) a specified time. The selection includes updates made by Amazon and by the seller.
            Query_type: Indicates whether shipments are returned using shipment information (by providing the ShipmentStatusList or ShipmentIdList parameters), using a date range (by providing the LastUpdatedAfter and LastUpdatedBefore parameters), or by using NextToken to continue returning items specified in a previous request.
            Next_token: A string token returned in the response to your previous request.
            Marketplace_id: A marketplace identifier. Specifies the marketplace where the product would be stored.
        """
        path_parameters = {}

        url = "/fba/inbound/v0/shipments".format(**path_parameters)

        query_parameters = {}

        if Shipment_status_list is not None:
            query_parameters["ShipmentStatusList"] = Shipment_status_list

        if Shipment_id_list is not None:
            query_parameters["ShipmentIdList"] = Shipment_id_list

        if Last_updated_after is not None:
            query_parameters["LastUpdatedAfter"] = Last_updated_after

        if Last_updated_before is not None:
            query_parameters["LastUpdatedBefore"] = Last_updated_before

        query_parameters["QueryType"] = Query_type

        if Next_token is not None:
            query_parameters["NextToken"] = Next_token

        query_parameters["MarketplaceId"] = Marketplace_id

    def get_shipment_items_by_shipment_id(
        self,
        shipment_id: str,
        Marketplace_id: str,
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
            Marketplace_id: A marketplace identifier. Specifies the marketplace where the product would be stored.
        """
        path_parameters = {}

        path_parameters["shipmentId"] = shipment_id

        url = "/fba/inbound/v0/shipments/{shipmentId}/items".format(**path_parameters)

        query_parameters = {}

        query_parameters["MarketplaceId"] = Marketplace_id

    def get_shipment_items(
        self,
        Last_updated_after: str = None,
        Last_updated_before: str = None,
        Query_type: str,
        Next_token: str = None,
        Marketplace_id: str,
    ):
        """
        Returns a list of items in a specified inbound shipment, or a list of items that were updated within a specified time frame.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 30 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            Last_updated_after: A date used for selecting inbound shipment items that were last updated after (or at) a specified time. The selection includes updates made by Amazon and by the seller.
            Last_updated_before: A date used for selecting inbound shipment items that were last updated before (or at) a specified time. The selection includes updates made by Amazon and by the seller.
            Query_type: Indicates whether items are returned using a date range (by providing the LastUpdatedAfter and LastUpdatedBefore parameters), or using NextToken, which continues returning items specified in a previous request.
            Next_token: A string token returned in the response to your previous request.
            Marketplace_id: A marketplace identifier. Specifies the marketplace where the product would be stored.
        """
        path_parameters = {}

        url = "/fba/inbound/v0/shipmentItems".format(**path_parameters)

        query_parameters = {}

        if Last_updated_after is not None:
            query_parameters["LastUpdatedAfter"] = Last_updated_after

        if Last_updated_before is not None:
            query_parameters["LastUpdatedBefore"] = Last_updated_before

        query_parameters["QueryType"] = Query_type

        if Next_token is not None:
            query_parameters["NextToken"] = Next_token

        query_parameters["MarketplaceId"] = Marketplace_id
