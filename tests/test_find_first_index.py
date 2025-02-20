import pytest
from src.find_first_index import find_first_index

def test_find_first_index():
    # Test finding an existing element
    assert find_first_index([1, 2, 3, 4, 5], 3) == 2
    
    # Test finding the first occurrence in repeated elements
    assert find_first_index([1, 2, 2, 3, 2], 2) == 1
    
    # Test element not in array
    assert find_first_index([1, 2, 3], 4) == -1
    
    # Test with empty array
    assert find_first_index([], 1) == -1
    
    # Test with different types
    assert find_first_index(["a", "b", "c"], "b") == 1
    
    # Test with mixed types
    assert find_first_index([1, "a", 2, "b"], "a") == 1

def test_edge_cases():
    # Test with None values
    assert find_first_index([None, 1, 2], None) == 0
    
    # Test with objects
    class TestClass:
        def __init__(self, val):
            self.val = val
        
        def __eq__(self, other):
            return self.val == other.val
    
    obj1 = TestClass(1)
    obj2 = TestClass(2)
    obj3 = TestClass(1)
    
    assert find_first_index([obj1, obj2, obj3], obj1) == 0
    assert find_first_index([obj1, obj2, obj3], obj3) == 0