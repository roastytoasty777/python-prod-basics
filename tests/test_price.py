import pytest
from src.price import parse_price


@pytest.mark.parametrize("text, expected", [
    ("12,50 DT", 12.5),
    ("7 DT", 7.0),
])
def test_parse_price_valid(text, expected):
    assert parse_price(text) == expected


@pytest.mark.parametrize("text", [
    "abc",
    "",
])
def test_parse_price_invalid(text):
    with pytest.raises(ValueError):
        parse_price(text)


@pytest.mark.parametrize("text, expected", [
    ("-5 DT", -5.0),
    ("-12,50 DT", -12.5),
])
def test_parse_price_negative(text, expected):
    assert parse_price(text) == expected