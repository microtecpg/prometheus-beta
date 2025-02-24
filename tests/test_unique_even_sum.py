import pytest
from src.unique_even_sum import sum_unique_even_numbers

def test_unique_even_numbers():
    """Test basic functionality of sum_unique_even_numbers."""
    assert sum_unique_even_numbers([1, 2, 3, 4, 2, 6]) == 6

def test_no_even_numbers():
    """Test input with no even numbers."""
    assert sum_unique_even_numbers([1, 3, 5, 7]) == 0

def test_repeated_even_numbers():
    """Test input with repeated even numbers."""
    assert sum_unique_even_numbers([2, 4, 6, 2, 4]) == 0

def test_empty_list():
    """Test input with an empty list."""
    assert sum_unique_even_numbers([]) == 0

def test_mixed_numbers():
    """Test with a mix of unique and repeated even and odd numbers."""
    assert sum_unique_even_numbers([1, 2, 2, 3, 4, 4, 5, 6, 6]) == 2

def test_negative_numbers():
    """Test with negative numbers."""
    assert sum_unique_even_numbers([-2, 2, -4, 4, -2, -4]) == 0