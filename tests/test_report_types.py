from amazon_sp_api_static.report_types import ReportType, _ReportTypeGroup


def test_types():
    t = ReportType.active_listings_report
    print()
    assert t.index == 103
    assert t.name == 'active_listings_report'
    assert t.upload_name == 'GET_MERCHANT_LISTINGS_DATA'
    assert t.group == _ReportTypeGroup.inventory_reports
