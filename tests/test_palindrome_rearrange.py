import pytest
from src.palindrome_rearrange import can_form_palindrome, rearrange_to_palindrome

def test_can_form_palindrome():
    # Test cases where palindrome can be formed
    assert can_form_palindrome("racecar") == True
    assert can_form_palindrome("aab") == True
    assert can_form_palindrome("code") == False
    assert can_form_palindrome("aabbccc") == True
    assert can_form_palindrome("") == True
    assert can_form_palindrome("a") == True

def test_rearrange_to_palindrome():
    # Test successful rearrangements
    assert rearrange_to_palindrome("racecar") == "racecar"
    assert rearrange_to_palindrome("aab") == "aba"
    assert set(rearrange_to_palindrome("aabbccc")) == set("abcccba")
    assert rearrange_to_palindrome("a") == "a"
    
    # Test empty string
    assert rearrange_to_palindrome("") == ""

def test_rearrange_to_palindrome_impossible():
    # Test cases where palindrome cannot be formed
    with pytest.raises(ValueError):
        rearrange_to_palindrome("abc")
    
    with pytest.raises(ValueError):
        rearrange_to_palindrome("hello")

def test_rearrange_edge_cases():
    # Additional edge cases
    assert set(rearrange_to_palindrome("aaabbb")) == set("ababab")
    assert len(rearrange_to_palindrome("aaaaabbbbb")) == 10
    
    # Single character cases
    for char in "abcdefg":
        assert rearrange_to_palindrome(char) == char