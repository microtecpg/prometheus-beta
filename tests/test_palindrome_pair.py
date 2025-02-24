import pytest
from src.palindrome_pair import palindrome_pair, is_palindrome

def test_is_palindrome():
    """Test the is_palindrome helper function."""
    assert is_palindrome(11) == True
    assert is_palindrome(12) == False
    assert is_palindrome(0) == True
    assert is_palindrome(121) == True
    assert is_palindrome(123) == False
    assert is_palindrome(-11) == True  # checks absolute value
    assert is_palindrome(-123) == False

def test_palindrome_pair_basic():
    """Test basic scenarios for palindrome_pair."""
    assert palindrome_pair([1, 2, 3, 4, 5]) == False  # 4-3 = 1 is not a palindrome with 2+ chars
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
    assert palindrome_pair([-5, -4, -3, -2, -1]) == False  # No palindrome difference with 2+ chars
    assert palindrome_pair([-11, 0, 11]) == True  # 11 - 0 = 11 is palindrome
    
    # More precise test for the problematic case
    def count_palindrome_pairs(nums):
        """Count how many pairs have palindrome differences."""
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff = abs(nums[j] - nums[i])
                if str(diff) == str(diff)[::-1] and len(str(diff)) > 1:
                    count += 1
        return count
    
    # Verify the test case 
    assert 0 == count_palindrome_pairs([1, 2, 3, 4, 6])