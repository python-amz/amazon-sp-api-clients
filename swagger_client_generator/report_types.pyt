from enum import IntEnum, Enum
from dataclasses import dataclass

class ReportTypeGroup(IntEnum):
{% for group, reports in groups.items() %}
    {{ group }} = {{ loop.index }}
{% endfor %}

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
{% for group, reports in groups.items() %}
    {% set outer = loop %}
    {% for report, value in reports.items() %}
    {{ report }} = {{ outer.index }}, {{ loop.index }}, "{{ value }}"
    {% endfor %}
{% endfor %}

    # for compatibility reasons, keep the previous name
    market_basket_analysis = get_brand_analytics_market_basket_report
    amazon_search_terms = get_brand_analytics_search_terms_report
    repeat_purchase = get_brand_analytics_repeat_purchase_report
    vendor_sales = get_vendor_sales_report
    net_pure_product_margin = get_vendor_net_pure_product_margin_report
    vendor_traffic = get_vendor_traffic_report
    vendor_forecasting = get_vendor_forecasting_report
    vendor_inventory = get_vendor_inventory_report
    sales_and_traffic_business = get_sales_and_traffic_report
    inventory = get_flat_file_open_listings_data
    all_listings = get_merchant_listings_all_data
    active_listings = get_merchant_listings_data
    inactive_listings = get_merchant_listings_inactive_data
    open_listings = get_merchant_listings_data_back_compat
    open_listings_lite = get_merchant_listings_data_lite
    open_listings_liter = get_merchant_listings_data_liter
    canceled_listings = get_merchant_cancelled_listings_data
    suppressed_listings = get_merchants_listings_fyp_report
    pan_european_eligibility_fba_asins = get_pan_eu_offer_status
    pan_european_eligibility_self_fulfilled_asins = get_mfn_paneu_offer_status
    referral_fee_preview = get_referral_fee_preview_report
    unshipped_orders = get_flat_file_actionable_order_data_shipping
    xml_order_invoicing = get_order_report_data_invoicing
    xml_order_tax = get_order_report_data_tax
    xml_order_shipping = get_order_report_data_shipping
    flat_file_order_invoicing = get_flat_file_order_report_data_invoicing
    flat_file_order_shipping = get_flat_file_order_report_data_shipping
    flat_file_order_tax = get_flat_file_order_report_data_tax
    flat_file_orders_by_last_update = get_flat_file_all_orders_data_by_last_update_general
    flat_file_orders_by_order_date = get_flat_file_all_orders_data_by_order_date_general
    flat_file_archived_orders = get_flat_file_archived_orders_data_by_order_date
    xml_orders_by_last_update = get_xml_all_orders_data_by_last_update_general
    xml_orders_by_order_date = get_xml_all_orders_data_by_order_date_general
    flat_file_pending_orders = get_flat_file_pending_orders_data
    xml_pending_orders = get_pending_orders_data
    converged_flat_file_pending_orders = get_converged_flat_file_pending_orders_data
    xml_returns_by_return_date = get_xml_returns_data_by_return_date
    flat_file_returns_by_return_date = get_flat_file_returns_data_by_return_date
    xml_prime_returns_by_return_date = get_xml_mfn_prime_returns_report
    csv_prime_returns_by_return_date = get_csv_mfn_prime_returns_report
    xml_return_attributes_by_return_date = get_xml_mfn_sku_return_attributes_report
    flat_file_return_attributes_by_return_date = get_flat_file_mfn_sku_return_attributes_report
    flat_file_feedback = get_seller_feedback_data
    xml_customer_metrics = get_v1_seller_performance_report
    seller_performance = get_v2_seller_performance_report
    promotions_performance = get_promotion_performance_report
    coupons_performance = get_coupon_performance_report
    flat_file_settlement = get_v2_settlement_report_data_flat_file
    xml_settlement = get_v2_settlement_report_data_xml
    flat_file_v2_settlement = get_v2_settlement_report_data_flat_file_v2
    fba_amazon_fulfilled_shipments = get_amazon_fulfilled_shipments_data_general
    fba_amazon_fulfilled_shipments_invoicing = get_amazon_fulfilled_shipments_data_invoicing
    fba_amazon_fulfilled_shipments_tax = get_amazon_fulfilled_shipments_data_tax
    flat_file_all_orders_by_last_update = get_flat_file_all_orders_data_by_last_update_general
    flat_file_all_orders_by_order_date = get_flat_file_all_orders_data_by_order_date_general
    xml_all_orders_by_last_update = get_xml_all_orders_data_by_last_update_general
    xml_all_orders_by_order_date = get_xml_all_orders_data_by_order_date_general
    fba_customer_shipment_sales = get_fba_fulfillment_customer_shipment_sales_data
    fba_promotions = get_fba_fulfillment_customer_shipment_promotion_data
    fba_customer_taxes = get_fba_fulfillment_customer_taxes_data
    remote_fulfillment_eligibility = get_remote_fulfillment_eligibility
    fba_amazon_fulfilled_inventory = get_afn_inventory_data
    fba_multi_country_inventory = get_afn_inventory_data_by_country
    inventory_ledger_summary_view = get_ledger_summary_view_data
    inventory_ledger_detailed_view = get_ledger_detail_view_data
    fba_daily_inventory_history = get_fba_fulfillment_current_inventory_data
    fba_monthly_inventory_history = get_fba_fulfillment_monthly_inventory_data
    fba_received_inventory = get_fba_fulfillment_inventory_receipts_data
    fba_reserved_inventory = get_reserved_inventory_data
    fba_inventory_event_detail = get_fba_fulfillment_inventory_summary_data
    fba_inventory_adjustments = get_fba_fulfillment_inventory_adjustments_data
    fba_inventory_health = get_fba_fulfillment_inventory_health_data
    fba_manage_inventory = get_fba_myi_unsuppressed_inventory_data
    fba_manage_inventory_archived = get_fba_myi_all_inventory_data
    restock_inventory = get_restock_inventory_recommendations_report
    fba_inbound_performance = get_fba_fulfillment_inbound_noncompliance_data
    fba_stranded_inventory = get_stranded_inventory_ui_data
    fba_bulk_fix_stranded_inventory = get_stranded_inventory_loader_data
    fba_inventory_age = get_fba_inventory_aged_data
    fba_manage_excess_inventory = get_excess_inventory_data
    fba_storage_fees = get_fba_storage_fee_charges_data
    get_exchange_data = get_product_exchange_data
    fba_manage_inventory_health = get_fba_inventory_planning_data
    fba_inventory_storage_overage_fees = get_fba_overage_fee_charges_data
    fba_fee_preview = get_fba_estimated_fba_fees_txt_data
    fba_reimbursements = get_fba_reimbursements_data
    fba_long_term_storage_fee_charges = get_fba_fulfillment_longterm_storage_fee_charges_data
    fba_returns = get_fba_fulfillment_customer_returns_data
    fba_replacements = get_fba_fulfillment_customer_shipment_replacement_data
    fba_recommended_removal = get_fba_recommended_removal_data
    fba_removal_order_detail = get_fba_fulfillment_removal_order_detail_data
    fba_removal_shipment_detail = get_fba_fulfillment_removal_shipment_detail_data
    small_light_inventory = get_fba_uno_inventory_data
    sales_tax = get_flat_file_sales_tax_data
    amazon_vat_calculation = sc_vat_tax_report
    amazon_vat_transactions = get_vat_transaction_data
    on_demand_gst_merchant_tax_b2b = get_gst_mtr_b2b_custom
    on_demand_gst_merchant_tax_b2c = get_gst_mtr_b2c_custom
    on_demand_stock_transfer = get_gst_str_adhoc
    flat_file_vat_invoice_data_vidr = get_flat_file_vat_invoice_data_report
    xml_vat_invoice_data_vidr = get_xml_vat_invoice_data_report
    browse_tree = get_xml_browse_tree_data
    easyship = get_easyship_documents
    easyship_picked_up = get_easyship_pickedup
    easyship_waiting_for_pick_up = get_easyship_waiting_for_pickup
    manage_quotes = rfqd_bulk_download
    referral_fee_discounts = fee_discounts_report
    b2b_product_opportunities_recommended_for_you = get_b2b_product_opportunities_recommended_for_you
    b2b_product_opportunities_not_yet_on_amazon = get_b2b_product_opportunities_not_yet_on_amazon
    epr_monthly = get_epr_monthly_reports
    epr_quarterly = get_epr_quarterly_reports
    epr_annual = get_epr_annual_reports