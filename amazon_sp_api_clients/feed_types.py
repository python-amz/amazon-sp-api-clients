"""
The groups and feed names are defined.
The enums are generated automatically from documentation html, but they will not be covered in the future.
The index values can be guaranteed to be consistent, and can be saved in database.
"""

from dataclasses import dataclass
from enum import IntEnum, Enum


class FeedTypeGroup(IntEnum):
    listings = 1
    order = 2
    fulfillment_by_amazon = 3
    business = 4
    easy_ship = 5

    @property
    def feeds(self):
        return (report for report in FeedType if report.group == self)


@dataclass
class __FeedTypeDefinition:
    group_index: int
    feed_index: int
    upload_name: str

    @property
    def index(self):
        return self.group_index * 100 + self.feed_index

    @property
    def group(self) -> FeedTypeGroup:
        return FeedTypeGroup(self.group_index)


class FeedType(__FeedTypeDefinition, Enum):
    json_listings_feed = 1, 1, 'JSON_LISTINGS_FEED'
    post_product_data = 1, 2, 'POST_PRODUCT_DATA'
    post_inventory_availability_data = 1, 3, 'POST_INVENTORY_AVAILABILITY_DATA'
    post_product_overrides_data = 1, 4, 'POST_PRODUCT_OVERRIDES_DATA'
    post_product_pricing_data = 1, 5, 'POST_PRODUCT_PRICING_DATA'
    post_product_image_data = 1, 6, 'POST_PRODUCT_IMAGE_DATA'
    post_product_relationship_data = 1, 7, 'POST_PRODUCT_RELATIONSHIP_DATA'
    post_flat_file_invloader_data = 1, 8, 'POST_FLAT_FILE_INVLOADER_DATA'
    post_flat_file_listings_data = 1, 9, 'POST_FLAT_FILE_LISTINGS_DATA'
    post_flat_file_bookloader_data = 1, 10, 'POST_FLAT_FILE_BOOKLOADER_DATA'
    post_flat_file_convergence_listings_data = 1, 11, 'POST_FLAT_FILE_CONVERGENCE_LISTINGS_DATA'
    # This feed is probably misspelled, its original intention is to upload a video, comment it out for now.
    # post_flat_file_listings_data = 1, 12, 'POST_FLAT_FILE_LISTINGS_DATA'
    post_flat_file_priceandquantityonly_update_data = 1, 13, 'POST_FLAT_FILE_PRICEANDQUANTITYONLY_UPDATE_DATA'
    post_uiee_bookloader_data = 1, 14, 'POST_UIEE_BOOKLOADER_DATA'
    post_std_aces_data = 1, 15, 'POST_STD_ACES_DATA'
    post_order_acknowledgement_data = 2, 1, 'POST_ORDER_ACKNOWLEDGEMENT_DATA'
    post_payment_adjustment_data = 2, 2, 'POST_PAYMENT_ADJUSTMENT_DATA'
    post_order_fulfillment_data = 2, 3, 'POST_ORDER_FULFILLMENT_DATA'
    post_invoice_confirmation_data = 2, 4, 'POST_INVOICE_CONFIRMATION_DATA'
    post_expected_ship_date_sod = 2, 5, 'POST_EXPECTED_SHIP_DATE_SOD'
    post_flat_file_order_acknowledgement_data = 2, 6, 'POST_FLAT_FILE_ORDER_ACKNOWLEDGEMENT_DATA'
    post_flat_file_payment_adjustment_data = 2, 7, 'POST_FLAT_FILE_PAYMENT_ADJUSTMENT_DATA'
    post_flat_file_fulfillment_data = 2, 8, 'POST_FLAT_FILE_FULFILLMENT_DATA'
    post_expected_ship_date_sod_flat_file = 2, 9, 'POST_EXPECTED_SHIP_DATE_SOD_FLAT_FILE'
    post_fulfillment_order_request_data = 3, 1, 'POST_FULFILLMENT_ORDER_REQUEST_DATA'
    post_fulfillment_order_cancellation_request_data = 3, 2, 'POST_FULFILLMENT_ORDER_CANCELLATION_REQUEST_DATA'
    post_fba_inbound_carton_contents = 3, 3, 'POST_FBA_INBOUND_CARTON_CONTENTS'
    post_flat_file_fulfillment_order_request_data = 3, 4, 'POST_FLAT_FILE_FULFILLMENT_ORDER_REQUEST_DATA'
    post_flat_file_fulfillment_order_cancellation_request_data = 3, 5, 'POST_FLAT_FILE_FULFILLMENT_ORDER_CANCELLATION_REQUEST_DATA'
    post_flat_file_fba_create_inbound_plan = 3, 6, 'POST_FLAT_FILE_FBA_CREATE_INBOUND_PLAN'
    post_flat_file_fba_update_inbound_plan = 3, 7, 'POST_FLAT_FILE_FBA_UPDATE_INBOUND_PLAN'
    post_flat_file_fba_create_removal = 3, 8, 'POST_FLAT_FILE_FBA_CREATE_REMOVAL'
    rfq_upload_feed = 4, 1, 'RFQ_UPLOAD_FEED'
    post_easyship_documents = 5, 1, 'POST_EASYSHIP_DOCUMENTS'
