import pytest
from src.text_utils import is_palindrome

@pytest.mark.parametrize("text, expected", [
    ("radar", True),
    ("Radar", True),
    ("esope reste ici et se repose", True),
    ("", True),
    ("hello", False),
])
def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected