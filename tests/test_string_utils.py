import pytest
from src.string_utils import string_transform

def test_string_transform_basic():
    """Test basic string transformation"""
    result = string_transform("Hello World")
    print(f"Basic test result: {result}")
    assert result == "dlrow*lleh"

def test_string_transform_mixed_case():
    """Test mixed case input"""
    result = string_transform("Hello WORLD")
    print(f"Mixed case test result: {result}")
    assert result == "dlrow*lleh"

def test_string_transform_with_multiple_spaces():
    """Test input with multiple spaces"""
    result = string_transform("  Hello   World  ")
    print(f"Multiple spaces test result: {result}")
    assert result == "dlrow*lleh"

def test_string_transform_with_special_chars():
    """Test input with special characters"""
    result = string_transform("Hello, World! 123")
    print(f"Special chars test result: {result}")
    assert result == "321!dlrow*lleh"

def test_string_transform_empty_string():
    """Test empty string input"""
    assert string_transform("") == ""

def test_string_transform_no_modification_needed():
    """Test string with no 'a' or spaces"""
    assert string_transform("xyz") == "zyx"