from amazon_sp_api_static.report_types import ReportType, ReportTypeGroup


def test_types():
    t = ReportType.active_listings_report
    print()
    assert t.index == 103
    assert t.name == 'get_merchant_listings_data', t.name
    assert t.upload_name == 'GET_MERCHANT_LISTINGS_DATA'
    assert t.group == ReportTypeGroup.inventory_reports
    assert t is ReportType.get_by_index(103)


def test_query_type_from_group():
    for group in ReportTypeGroup:
        print(group.name, tuple(r.index for r in group.reports))
        for r in group.reports:
            assert isinstance(r.index, int)
