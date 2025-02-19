import pytest
from src.string_utils import string_transform

def test_string_transform_basic():
    """Test basic string transformation"""
    assert string_transform("Hello World") == "dlrow*lleh"

def test_string_transform_mixed_case():
    """Test mixed case input"""
    assert string_transform("Hello WORLD") == "dlrow*lleh"

def test_string_transform_with_multiple_spaces():
    """Test input with multiple spaces"""
    assert string_transform("  Hello   World  ") == "dlrow*lleh"

def test_string_transform_with_special_chars():
    """Test input with special characters"""
    assert string_transform("Hello, World! 123") == "321!dlrow*lleh"

def test_string_transform_empty_string():
    """Test empty string input"""
    assert string_transform("") == ""

def test_string_transform_no_modification_needed():
    """Test string with no 'a' or spaces"""
    assert string_transform("xyz") == "xyz"