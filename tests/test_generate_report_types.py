from scripts.generate_report_types import Script

script = Script()


def test_group_enum():
    print()
    assert isinstance(script.group_enum, dict)
    assert len(script.group_enum) > 0
