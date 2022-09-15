from enum import IntEnum, Enum
from dataclasses import dataclass


class ReportTypeGroup(IntEnum):
    brand_analytics_reports = 1
    vendor_retail_analytics_reports = 2
    seller_retail_analytics_reports = 3
    inventory_reports = 4
    order_reports = 5
    order_tracking_reports = 6
    pending_order_reports = 7
    returns_reports = 8
    performance_reports = 9
    settlement_reports = 10
    fulfillment_by_amazon_fba_reports = 11
    tax_reports = 12
    invoice_data_reports = 13
    browse_tree_report = 14
    easy_ship_reports = 15
    amazon_business_reports = 16
    b2b_product_opportunities_reports = 17
    regulatory_compliance_reports = 18

    @property
    def reports(self):
        return (report for report in ReportType if report.group == self)


@dataclass
class __ReportTypeDefinition:
    __group_index: int
    __report_index: int
    upload_name: str

    @property
    def index(self):
        return self.__group_index * 100 + self.__report_index

    @property
    def group(self) -> ReportTypeGroup:
        return ReportTypeGroup(self.__group_index)


class ReportType(__ReportTypeDefinition, Enum):
    market_basket_analysis = 1, 1, "GET_BRAND_ANALYTICS_MARKET_BASKET_REPORT"
    amazon_search_terms = 1, 2, "GET_BRAND_ANALYTICS_SEARCH_TERMS_REPORT"
    repeat_purchase = 1, 3, "GET_BRAND_ANALYTICS_REPEAT_PURCHASE_REPORT"
    vendor_sales = 2, 1, "GET_VENDOR_SALES_REPORT"
    net_pure_product_margin = 2, 2, "GET_VENDOR_NET_PURE_PRODUCT_MARGIN_REPORT"
    vendor_traffic = 2, 3, "GET_VENDOR_TRAFFIC_REPORT"
    vendor_forecasting = 2, 4, "GET_VENDOR_FORECASTING_REPORT"
    vendor_inventory = 2, 5, "GET_VENDOR_INVENTORY_REPORT"
    sales_and_traffic_business = 3, 1, "GET_SALES_AND_TRAFFIC_REPORT"
    inventory = 4, 1, "GET_FLAT_FILE_OPEN_LISTINGS_DATA"
    all_listings = 4, 2, "GET_MERCHANT_LISTINGS_ALL_DATA"
    active_listings = 4, 3, "GET_MERCHANT_LISTINGS_DATA"
    inactive_listings = 4, 4, "GET_MERCHANT_LISTINGS_INACTIVE_DATA"
    open_listings = 4, 5, "GET_MERCHANT_LISTINGS_DATA_BACK_COMPAT"
    open_listings_lite = 4, 6, "GET_MERCHANT_LISTINGS_DATA_LITE"
    open_listings_liter = 4, 7, "GET_MERCHANT_LISTINGS_DATA_LITER"
    canceled_listings = 4, 8, "GET_MERCHANT_CANCELLED_LISTINGS_DATA"
    suppressed_listings = 4, 9, "GET_MERCHANTS_LISTINGS_FYP_REPORT"
    pan_european_eligibility_fba_asins = 4, 10, "GET_PAN_EU_OFFER_STATUS"
    pan_european_eligibility_self_fulfilled_asins = 4, 11, "GET_MFN_PANEU_OFFER_STATUS"
    referral_fee_preview = 4, 12, "GET_REFERRAL_FEE_PREVIEW_REPORT"
    unshipped_orders = 5, 1, "GET_FLAT_FILE_ACTIONABLE_ORDER_DATA_SHIPPING"
    xml_order_invoicing = 5, 2, "GET_ORDER_REPORT_DATA_INVOICING"
    xml_order_tax = 5, 3, "GET_ORDER_REPORT_DATA_TAX"
    xml_order_shipping = 5, 4, "GET_ORDER_REPORT_DATA_SHIPPING"
    flat_file_order_invoicing = 5, 5, "GET_FLAT_FILE_ORDER_REPORT_DATA_INVOICING"
    flat_file_order_shipping = 5, 6, "GET_FLAT_FILE_ORDER_REPORT_DATA_SHIPPING"
    flat_file_order_tax = 5, 7, "GET_FLAT_FILE_ORDER_REPORT_DATA_TAX"
    flat_file_orders_by_last_update = 6, 1, "GET_FLAT_FILE_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL"
    flat_file_orders_by_order_date = 6, 2, "GET_FLAT_FILE_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL"
    flat_file_archived_orders = 6, 3, "GET_FLAT_FILE_ARCHIVED_ORDERS_DATA_BY_ORDER_DATE"
    xml_orders_by_last_update = 6, 4, "GET_XML_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL"
    xml_orders_by_order_date = 6, 5, "GET_XML_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL"
    flat_file_pending_orders = 7, 1, "GET_FLAT_FILE_PENDING_ORDERS_DATA"
    xml_pending_orders = 7, 2, "GET_PENDING_ORDERS_DATA"
    converged_flat_file_pending_orders = 7, 3, "GET_CONVERGED_FLAT_FILE_PENDING_ORDERS_DATA"
    xml_returns_by_return_date = 8, 1, "GET_XML_RETURNS_DATA_BY_RETURN_DATE"
    flat_file_returns_by_return_date = 8, 2, "GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE"
    xml_prime_returns_by_return_date = 8, 3, "GET_XML_MFN_PRIME_RETURNS_REPORT"
    csv_prime_returns_by_return_date = 8, 4, "GET_CSV_MFN_PRIME_RETURNS_REPORT"
    xml_return_attributes_by_return_date = 8, 5, "GET_XML_MFN_SKU_RETURN_ATTRIBUTES_REPORT"
    flat_file_return_attributes_by_return_date = 8, 6, "GET_FLAT_FILE_MFN_SKU_RETURN_ATTRIBUTES_REPORT"
    flat_file_feedback = 9, 1, "GET_SELLER_FEEDBACK_DATA"
    xml_customer_metrics = 9, 2, "GET_V1_SELLER_PERFORMANCE_REPORT"
    seller_performance = 9, 3, "GET_V2_SELLER_PERFORMANCE_REPORT"
    promotions_performance = 9, 4, "GET_PROMOTION_PERFORMANCE_REPORT"
    coupons_performance = 9, 5, "GET_COUPON_PERFORMANCE_REPORT"
    flat_file_settlement = 10, 1, "GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE"
    xml_settlement = 10, 2, "GET_V2_SETTLEMENT_REPORT_DATA_XML"
    flat_file_v2_settlement = 10, 3, "GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2"
    fba_amazon_fulfilled_shipments = 11, 1, "GET_AMAZON_FULFILLED_SHIPMENTS_DATA_GENERAL"
    fba_amazon_fulfilled_shipments_invoicing = 11, 2, "GET_AMAZON_FULFILLED_SHIPMENTS_DATA_INVOICING"
    fba_amazon_fulfilled_shipments_tax = 11, 3, "GET_AMAZON_FULFILLED_SHIPMENTS_DATA_TAX"
    flat_file_all_orders_by_last_update = 11, 4, "GET_FLAT_FILE_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL"
    flat_file_all_orders_by_order_date = 11, 5, "GET_FLAT_FILE_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL"
    xml_all_orders_by_last_update = 11, 6, "GET_XML_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL"
    xml_all_orders_by_order_date = 11, 7, "GET_XML_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL"
    fba_customer_shipment_sales = 11, 8, "GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_SALES_DATA"
    fba_promotions = 11, 9, "GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_PROMOTION_DATA"
    fba_customer_taxes = 11, 10, "GET_FBA_FULFILLMENT_CUSTOMER_TAXES_DATA"
    remote_fulfillment_eligibility = 11, 11, "GET_REMOTE_FULFILLMENT_ELIGIBILITY"
    fba_amazon_fulfilled_inventory = 11, 12, "GET_AFN_INVENTORY_DATA"
    fba_multi_country_inventory = 11, 13, "GET_AFN_INVENTORY_DATA_BY_COUNTRY"
    inventory_ledger_summary_view = 11, 14, "GET_LEDGER_SUMMARY_VIEW_DATA"
    inventory_ledger_detailed_view = 11, 15, "GET_LEDGER_DETAIL_VIEW_DATA"
    fba_daily_inventory_history = 11, 16, "GET_FBA_FULFILLMENT_CURRENT_INVENTORY_DATA"
    fba_monthly_inventory_history = 11, 17, "GET_FBA_FULFILLMENT_MONTHLY_INVENTORY_DATA"
    fba_received_inventory = 11, 18, "GET_FBA_FULFILLMENT_INVENTORY_RECEIPTS_DATA"
    fba_reserved_inventory = 11, 19, "GET_RESERVED_INVENTORY_DATA"
    fba_inventory_event_detail = 11, 20, "GET_FBA_FULFILLMENT_INVENTORY_SUMMARY_DATA"
    fba_inventory_adjustments = 11, 21, "GET_FBA_FULFILLMENT_INVENTORY_ADJUSTMENTS_DATA"
    fba_inventory_health = 11, 22, "GET_FBA_FULFILLMENT_INVENTORY_HEALTH_DATA"
    fba_manage_inventory = 11, 23, "GET_FBA_MYI_UNSUPPRESSED_INVENTORY_DATA"
    fba_manage_inventory_archived = 11, 24, "GET_FBA_MYI_ALL_INVENTORY_DATA"
    restock_inventory = 11, 25, "GET_RESTOCK_INVENTORY_RECOMMENDATIONS_REPORT"
    fba_inbound_performance = 11, 26, "GET_FBA_FULFILLMENT_INBOUND_NONCOMPLIANCE_DATA"
    fba_stranded_inventory = 11, 27, "GET_STRANDED_INVENTORY_UI_DATA"
    fba_bulk_fix_stranded_inventory = 11, 28, "GET_STRANDED_INVENTORY_LOADER_DATA"
    fba_inventory_age = 11, 29, "GET_FBA_INVENTORY_AGED_DATA"
    fba_manage_excess_inventory = 11, 30, "GET_EXCESS_INVENTORY_DATA"
    fba_storage_fees = 11, 31, "GET_FBA_STORAGE_FEE_CHARGES_DATA"
    get_exchange_data = 11, 32, "GET_PRODUCT_EXCHANGE_DATA"
    fba_manage_inventory_health = 11, 33, "GET_FBA_INVENTORY_PLANNING_DATA"
    fba_inventory_storage_overage_fees = 11, 34, "GET_FBA_OVERAGE_FEE_CHARGES_DATA"
    fba_fee_preview = 11, 35, "GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA"
    fba_reimbursements = 11, 36, "GET_FBA_REIMBURSEMENTS_DATA"
    fba_long_term_storage_fee_charges = 11, 37, "GET_FBA_FULFILLMENT_LONGTERM_STORAGE_FEE_CHARGES_DATA"
    fba_returns = 11, 38, "GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA"
    fba_replacements = 11, 39, "GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_REPLACEMENT_DATA"
    fba_recommended_removal = 11, 40, "GET_FBA_RECOMMENDED_REMOVAL_DATA"
    fba_removal_order_detail = 11, 41, "GET_FBA_FULFILLMENT_REMOVAL_ORDER_DETAIL_DATA"
    fba_removal_shipment_detail = 11, 42, "GET_FBA_FULFILLMENT_REMOVAL_SHIPMENT_DETAIL_DATA"
    small_light_inventory = 11, 43, "GET_FBA_UNO_INVENTORY_DATA"
    sales_tax = 12, 1, "GET_FLAT_FILE_SALES_TAX_DATA"
    amazon_vat_calculation = 12, 2, "SC_VAT_TAX_REPORT"
    amazon_vat_transactions = 12, 3, "GET_VAT_TRANSACTION_DATA"
    on_demand_gst_merchant_tax_b2b = 12, 4, "GET_GST_MTR_B2B_CUSTOM"
    on_demand_gst_merchant_tax_b2c = 12, 5, "GET_GST_MTR_B2C_CUSTOM"
    on_demand_stock_transfer = 12, 6, "GET_GST_STR_ADHOC"
    flat_file_vat_invoice_data_vidr = 13, 1, "GET_FLAT_FILE_VAT_INVOICE_DATA_REPORT"
    xml_vat_invoice_data_vidr = 13, 2, "GET_XML_VAT_INVOICE_DATA_REPORT"
    browse_tree = 14, 1, "GET_XML_BROWSE_TREE_DATA"
    easyship = 15, 1, "GET_EASYSHIP_DOCUMENTS"
    easyship_picked_up = 15, 2, "GET_EASYSHIP_PICKEDUP"
    easyship_waiting_for_pick_up = 15, 3, "GET_EASYSHIP_WAITING_FOR_PICKUP"
    manage_quotes = 16, 1, "RFQD_BULK_DOWNLOAD"
    referral_fee_discounts = 16, 2, "FEE_DISCOUNTS_REPORT"
    b2b_product_opportunities_recommended_for_you = 17, 1, "GET_B2B_PRODUCT_OPPORTUNITIES_RECOMMENDED_FOR_YOU"
    b2b_product_opportunities_not_yet_on_amazon = 17, 2, "GET_B2B_PRODUCT_OPPORTUNITIES_NOT_YET_ON_AMAZON"
    epr_monthly = 18, 1, "GET_EPR_MONTHLY_REPORTS"
    epr_quarterly = 18, 2, "GET_EPR_QUARTERLY_REPORTS"
    epr_annual = 18, 3, "GET_EPR_ANNUAL_REPORTS"
