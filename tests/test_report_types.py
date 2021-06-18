from amazon_sp_api_static.report_types import ReportType, ReportTypeGroup


def test_types():
    t = ReportType.active_listings_report
    print()
    assert t.index == 103
    assert t.name == 'active_listings_report'
    assert t.upload_name == 'GET_MERCHANT_LISTINGS_DATA'
    assert t.group == ReportTypeGroup.inventory_reports


def test_query_type_from_group():
    for group in ReportTypeGroup:
        for r in group.reports:
            assert isinstance(r.index, int)
