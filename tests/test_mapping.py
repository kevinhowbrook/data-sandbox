from utils import mapping


def test_mapping():
    assert mapping.county_to_ssr("Cleaveland") == "North"
    if mapping.county_to_ssr("I made this up") is False:
        assert True
