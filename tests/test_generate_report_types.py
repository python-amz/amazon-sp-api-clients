from pprint import pprint

from scripts.generate_report_types import Script

script = Script()


def test_parsed_data():
    print()
    assert isinstance(script.parsed_data, dict)


def test_group_enum():
    print()
    assert isinstance(script.group_enum, dict)
    assert len(script.group_enum) > 0


def test_report_enum():
    print()
    assert isinstance(script.report_enum, dict)
    for i in script.report_enum.values():
        print(f'{i.group_name:>40} {i.name:>60} {i.group_index:>2} {i.report_index:>2}')


def test_relation():
    print()
    pprint(script.relation)
