from enum import IntEnum, Enum
from dataclasses import dataclass

class ReportTypeGroup(IntEnum):
{% for group_name, group_index in groups.items() %}
    {{ group_name }} = {{ group_index }}
{% endfor %}

    @property
    def reports(self):
        return tuple(ReportType.get_by_index(i) for i in _group_report_relation.get(self.value, ()))


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
{% for report in reports.values() %}
    {{ report.name }} = {{ report.group_index }}, {{ report.report_index }}, "{{ report.upload_name }}"
{% endfor %}

    # for compatibility reasons, keep the previous name
    inventory_report = get_flat_file_open_listings_data
    all_listings_report = get_merchant_listings_all_data
    active_listings_report = get_merchant_listings_data
    inactive_listings_report = get_merchant_listings_inactive_data
    open_listings_report = get_merchant_listings_data_back_compat
    open_listings_report_lite = get_merchant_listings_data_lite
    open_listings_report_liter = get_merchant_listings_data_liter
    canceled_listings_report = get_merchant_cancelled_listings_data
    listing_quality_and_suppressed_listing_report = get_merchant_listings_defect_data
    global_expansion_opportunities_report = get_flat_file_geo_opportunities
    referral_fee_preview_report = get_referral_fee_preview_report
    unshipped_orders_report = get_flat_file_actionable_order_data_shipping
    requested_or_scheduled_flat_file_order_report_shipping = get_flat_file_order_report_data_shipping
    flat_file_orders_by_last_update_report = get_flat_file_all_orders_data_by_last_update_general
    flat_file_orders_by_order_date_report = get_flat_file_all_orders_data_by_order_date_general
    flat_file_archived_orders_report = get_flat_file_archived_orders_data_by_order_date
    xml_orders_by_last_update_report = get_xml_all_orders_data_by_last_update_general
    xml_orders_by_order_date_report = get_xml_all_orders_data_by_order_date_general
    flat_file_pending_orders_report = get_flat_file_pending_orders_data
    xml_pending_orders_report = get_pending_orders_data
    converged_flat_file_pending_orders_report = get_converged_flat_file_pending_orders_data
    xml_returns_report_by_return_date = get_xml_returns_data_by_return_date
    flat_file_returns_report_by_return_date = get_flat_file_returns_data_by_return_date
    xml_prime_returns_report_by_return_date = get_xml_mfn_prime_returns_report
    csv_prime_returns_report_by_return_date = get_csv_mfn_prime_returns_report
    xml_return_attributes_report_by_return_date = get_xml_mfn_sku_return_attributes_report
    flat_file_return_attributes_report_by_return_date = get_flat_file_mfn_sku_return_attributes_report
    flat_file_feedback_report = get_seller_feedback_data
    xml_customer_metrics_report = get_v1_seller_performance_report
    seller_performance_report = get_v2_seller_performance_report
    flat_file_settlement_report = get_v2_settlement_report_data_flat_file
    xml_settlement_report = get_v2_settlement_report_data_xml
    flat_file_v2_settlement_report = get_v2_settlement_report_data_flat_file_v2
    fba_amazon_fulfilled_shipments_report = get_amazon_fulfilled_shipments_data_general
    fba_amazon_fulfilled_shipments_report_invoicing = get_amazon_fulfilled_shipments_data_invoicing
    fba_amazon_fulfilled_shipments_report_tax = get_amazon_fulfilled_shipments_data_tax
    flat_file_all_orders_report_by_last_update = get_flat_file_all_orders_data_by_last_update_general
    flat_file_all_orders_report_by_order_date = get_flat_file_all_orders_data_by_order_date_general
    xml_all_orders_report_by_last_update = get_xml_all_orders_data_by_last_update_general
    xml_all_orders_report_by_order_date = get_xml_all_orders_data_by_order_date_general
    fba_customer_shipment_sales_report = get_fba_fulfillment_customer_shipment_sales_data
    fba_promotions_report = get_fba_fulfillment_customer_shipment_promotion_data
    fba_customer_taxes = get_fba_fulfillment_customer_taxes_data
    remote_fulfillment_eligibility = get_remote_fulfillment_eligibility
    sales_tax_report = get_flat_file_sales_tax_data
    amazon_vat_calculation_report = sc_vat_tax_report
    amazon_vat_transactions_report = get_vat_transaction_data
    on_demand_gst_merchant_tax_report_b2b = get_gst_mtr_b2b_custom
    on_demand_gst_merchant_tax_report_b2c = get_gst_mtr_b2c_custom
    browse_tree_report = get_xml_browse_tree_data
    easyship_report = get_easyship_documents
    easyship_picked_up_report = get_easyship_pickedup
    easyship_waiting_for_pick_up_report = get_easyship_waiting_for_pickup
    manage_quotes_report = rfqd_bulk_download
    referral_fee_discounts_report = fee_discounts_report
    amazonpay_sandbox_settlement_report = get_flat_file_offamazonpayments_sandbox_settlement_data
    b2b_product_opportunities_recommended_for_you_report = get_b2b_product_opportunities_recommended_for_you
    b2b_product_opportunities_not_yet_on_amazon = get_b2b_product_opportunities_not_yet_on_amazon
    @classmethod
    def get_by_index(cls, index: int) -> "ReportType":
        # for compatibility. The reports are found in two groups, so in the previous the reports are defined twice.
        # In current version, the reports should only defined once.
        index = {804: 301, 805: 302, 806: 304, 807: 305}.get(index,index)
        return _index_report_map[index]


_index_report_map = {i.index: i for i in ReportType}
_group_report_relation = {{ relation }}