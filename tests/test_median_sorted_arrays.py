import pytest
from src.median_sorted_arrays import find_median_sorted_arrays

def test_basic_even_length_arrays():
    """Test median of two even-length sorted arrays"""
    assert find_median_sorted_arrays([1, 3], [2, 4]) == 2.5

def test_basic_odd_length_arrays():
    """Test median of two odd-length sorted arrays"""
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0

def test_different_length_arrays():
    """Test arrays of different lengths"""
    assert find_median_sorted_arrays([1, 2], [3, 4, 5]) == 3.0

def test_one_empty_array():
    """Test when one array is empty"""
    assert find_median_sorted_arrays([], [1, 2, 3, 4, 5]) == 3.0

def test_both_empty_arrays():
    """Test raising an error when both arrays are empty"""
    with pytest.raises(ValueError):
        find_median_sorted_arrays([], [])

def test_invalid_input_type():
    """Test raising an error for non-list inputs"""
    with pytest.raises(TypeError):
        find_median_sorted_arrays(1, [2])

def test_non_numeric_input():
    """Test raising an error for non-numeric inputs"""
    with pytest.raises(ValueError):
        find_median_sorted_arrays(['a'], [1, 2])

def test_large_arrays():
    """Test with larger arrays"""
    large_arr1 = list(range(0, 1000, 2))
    large_arr2 = list(range(1, 1000, 2))
    assert find_median_sorted_arrays(large_arr1, large_arr2) == 499.5

def test_negative_numbers():
    """Test arrays with negative numbers"""
    assert find_median_sorted_arrays([-5, -3, -1], [-2, 0, 2]) == -1.5

def test_floating_point_numbers():
    """Test arrays with floating point numbers"""
    assert find_median_sorted_arrays([1.5, 2.5], [3.5, 4.5]) == 3.0