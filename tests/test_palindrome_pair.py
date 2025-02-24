import pytest
from src.palindrome_pair import palindrome_pair, is_palindrome

def test_is_palindrome():
    """Test the is_palindrome helper function."""
    assert is_palindrome(11) == True
    assert is_palindrome(12) == False
    assert is_palindrome(0) == True
    assert is_palindrome(121) == True
    assert is_palindrome(123) == False

def test_palindrome_pair_basic():
    """Test basic scenarios for palindrome_pair."""
    assert palindrome_pair([1, 2, 3, 4, 5]) == True    # 4-3 = 1 is palindrome
    assert palindrome_pair([1, 2, 3, 4, 6]) == False   # No palindrome difference
    assert palindrome_pair([10, 20, 30, 40]) == True   # 30-20 = 10 is palindrome

def test_palindrome_pair_edge_cases():
    """Test edge cases for palindrome_pair."""
    assert palindrome_pair([]) == False
    assert palindrome_pair([5]) == False
    assert palindrome_pair([0, 1, 11]) == True  # 11-0 = 11 is palindrome

def test_palindrome_pair_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        palindrome_pair("not a list")
    
    with pytest.raises(ValueError):
        palindrome_pair([1, 2, '3'])

def test_palindrome_pair_negative_numbers():
    """Test cases with negative numbers."""
    assert palindrome_pair([-5, -4, -3, -2, -1]) == True  # -3 - (-4) = 1 is palindrome
    assert palindrome_pair([-11, 0, 11]) == True  # 11 - 0 = 11 is palindrome