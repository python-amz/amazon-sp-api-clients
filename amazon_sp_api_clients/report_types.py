"""
The groups and report names are defined.
The enums are generated automatically from GitHub markdown file, but they will not be covered in the future. The index
values can be guaranteed to be consistent, and can be saved in database.
"""

from dataclasses import dataclass
from enum import IntEnum, Enum


class ReportTypeGroup(IntEnum):
    inventory_reports = 1
    order_reports = 2
    order_tracking_reports = 3
    pending_order_reports = 4
    returns_reports = 5
    performance_reports = 6
    settlement_reports = 7
    fulfillment_by_amazon_fba_reports = 8
    tax_reports = 9
    browse_tree_report = 10
    easy_ship_reports = 11
    amazon_business_reports = 12
    amazon_pay_report = 13
    b2b_product_opportunities_reports = 14

    @property
    def reports(self):
        return (report for report in ReportType if report.group == self)


@dataclass
class __ReportTypeDefinition:
    group_index: int
    report_index: int
    upload_name: str

    @property
    def index(self):
        return self.group_index * 100 + self.report_index

    @property
    def group(self) -> ReportTypeGroup:
        return ReportTypeGroup(self.group_index)


class ReportType(__ReportTypeDefinition, Enum):
    inventory_report = 1, 1, "GET_FLAT_FILE_OPEN_LISTINGS_DATA"
    all_listings_report = 1, 2, "GET_MERCHANT_LISTINGS_ALL_DATA"
    active_listings_report = 1, 3, "GET_MERCHANT_LISTINGS_DATA"
    inactive_listings_report = 1, 4, "GET_MERCHANT_LISTINGS_INACTIVE_DATA"
    open_listings_report = 1, 5, "GET_MERCHANT_LISTINGS_DATA_BACK_COMPAT"
    open_listings_report_lite = 1, 6, "GET_MERCHANT_LISTINGS_DATA_LITE"
    open_listings_report_liter = 1, 7, "GET_MERCHANT_LISTINGS_DATA_LITER"
    canceled_listings_report = 1, 8, "GET_MERCHANT_CANCELLED_LISTINGS_DATA"
    listing_quality_and_suppressed_listing_report = 1, 9, "GET_MERCHANT_LISTINGS_DEFECT_DATA"
    global_expansion_opportunities_report = 1, 10, "GET_FLAT_FILE_GEO_OPPORTUNITIES"
    referral_fee_preview_report = 1, 11, "GET_REFERRAL_FEE_PREVIEW_REPORT"
    unshipped_orders_report = 2, 1, "GET_FLAT_FILE_ACTIONABLE_ORDER_DATA_SHIPPING"
    requested_or_scheduled_flat_file_order_report_shipping = 2, 2, "GET_FLAT_FILE_ORDER_REPORT_DATA_SHIPPING"
    flat_file_orders_by_last_update_report = 3, 1, "GET_FLAT_FILE_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL"
    flat_file_orders_by_order_date_report = 3, 2, "GET_FLAT_FILE_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL"
    flat_file_archived_orders_report = 3, 3, "GET_FLAT_FILE_ARCHIVED_ORDERS_DATA_BY_ORDER_DATE"
    xml_orders_by_last_update_report = 3, 4, "GET_XML_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL"
    xml_orders_by_order_date_report = 3, 5, "GET_XML_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL"
    flat_file_pending_orders_report = 4, 1, "GET_FLAT_FILE_PENDING_ORDERS_DATA"
    xml_pending_orders_report = 4, 2, "GET_PENDING_ORDERS_DATA"
    converged_flat_file_pending_orders_report = 4, 3, "GET_CONVERGED_FLAT_FILE_PENDING_ORDERS_DATA"
    xml_returns_report_by_return_date = 5, 1, "GET_XML_RETURNS_DATA_BY_RETURN_DATE"
    flat_file_returns_report_by_return_date = 5, 2, "GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE"
    xml_prime_returns_report_by_return_date = 5, 3, "GET_XML_MFN_PRIME_RETURNS_REPORT"
    csv_prime_returns_report_by_return_date = 5, 4, "GET_CSV_MFN_PRIME_RETURNS_REPORT"
    xml_return_attributes_report_by_return_date = 5, 5, "GET_XML_MFN_SKU_RETURN_ATTRIBUTES_REPORT"
    flat_file_return_attributes_report_by_return_date = 5, 6, "GET_FLAT_FILE_MFN_SKU_RETURN_ATTRIBUTES_REPORT"
    flat_file_feedback_report = 6, 1, "GET_SELLER_FEEDBACK_DATA"
    xml_customer_metrics_report = 6, 2, "GET_V1_SELLER_PERFORMANCE_REPORT"
    seller_performance_report = 6, 3, "GET_V2_SELLER_PERFORMANCE_REPORT"
    flat_file_settlement_report = 7, 1, "GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE"
    xml_settlement_report = 7, 2, "GET_V2_SETTLEMENT_REPORT_DATA_XML"
    flat_file_v2_settlement_report = 7, 3, "GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2"
    fba_amazon_fulfilled_shipments_report = 8, 1, "GET_AMAZON_FULFILLED_SHIPMENTS_DATA_GENERAL"
    fba_amazon_fulfilled_shipments_report_invoicing = 8, 2, "GET_AMAZON_FULFILLED_SHIPMENTS_DATA_INVOICING"
    fba_amazon_fulfilled_shipments_report_tax = 8, 3, "GET_AMAZON_FULFILLED_SHIPMENTS_DATA_TAX"
    flat_file_all_orders_report_by_last_update = 8, 4, "GET_FLAT_FILE_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL"
    flat_file_all_orders_report_by_order_date = 8, 5, "GET_FLAT_FILE_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL"
    xml_all_orders_report_by_last_update = 8, 6, "GET_XML_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL"
    xml_all_orders_report_by_order_date = 8, 7, "GET_XML_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL"
    fba_customer_shipment_sales_report = 8, 8, "GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_SALES_DATA"
    fba_promotions_report = 8, 9, "GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_PROMOTION_DATA"
    fba_customer_taxes = 8, 10, "GET_FBA_FULFILLMENT_CUSTOMER_TAXES_DATA"
    remote_fulfillment_eligibility = 8, 11, "GET_REMOTE_FULFILLMENT_ELIGIBILITY"
    sales_tax_report = 9, 1, "GET_FLAT_FILE_SALES_TAX_DATA"
    amazon_vat_calculation_report = 9, 2, "SC_VAT_TAX_REPORT"
    amazon_vat_transactions_report = 9, 3, "GET_VAT_TRANSACTION_DATA"
    on_demand_gst_merchant_tax_report_b2b = 9, 4, "GET_GST_MTR_B2B_CUSTOM"
    on_demand_gst_merchant_tax_report_b2c = 9, 5, "GET_GST_MTR_B2C_CUSTOM"
    browse_tree_report = 10, 1, "GET_XML_BROWSE_TREE_DATA"
    easyship_report = 11, 1, "GET_EASYSHIP_DOCUMENTS"
    easyship_picked_up_report = 11, 2, "GET_EASYSHIP_PICKEDUP"
    easyship_waiting_for_pick_up_report = 11, 3, "GET_EASYSHIP_WAITING_FOR_PICKUP"
    manage_quotes_report = 12, 1, "RFQD_BULK_DOWNLOAD"
    referral_fee_discounts_report = 12, 2, "FEE_DISCOUNTS_REPORT"
    amazonpay_sandbox_settlement_report = 13, 1, "GET_FLAT_FILE_OFFAMAZONPAYMENTS_SANDBOX_SETTLEMENT_DATA"
    b2b_product_opportunities_recommended_for_you_report = 14, 1, "GET_B2B_PRODUCT_OPPORTUNITIES_RECOMMENDED_FOR_YOU"
    b2b_product_opportunities_not_yet_on_amazon = 14, 2, "GET_B2B_PRODUCT_OPPORTUNITIES_NOT_YET_ON_AMAZON"
