import pytest
import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from array_sum import sum_array_elements

def test_sum_positive_integers():
    assert sum_array_elements([1, 2, 3, 4, 5]) == 15

def test_sum_negative_integers():
    assert sum_array_elements([-1, -2, -3]) == -6

def test_sum_mixed_integers():
    assert sum_array_elements([-1, 0, 1]) == 0

def test_sum_empty_array():
    assert sum_array_elements([]) == 0

def test_invalid_input_not_list():
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_array_elements("not a list")

def test_invalid_input_non_numeric():
    with pytest.raises(TypeError, match="All elements in the array must be numeric"):
        sum_array_elements([1, 2, "3"])