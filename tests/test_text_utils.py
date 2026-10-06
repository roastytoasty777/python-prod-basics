from src.text_utils import is_palindrome

def test_simple_word():
    assert is_palindrome("radar")

def test_uppercase():
    assert is_palindrome("Radar")

def test_with_spaces():
    assert is_palindrome("esope reste ici et se repose")

def test_empty():
    assert is_palindrome("")