import os
import pytest
import tempfile
from datetime import datetime, timedelta
from src.file_utils import get_file_creation_date

def test_get_file_creation_date_existing_file():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Get the file creation date
        creation_date = get_file_creation_date(temp_path)
        
        # Check that creation date is a datetime object and is recent
        assert isinstance(creation_date, datetime)
        assert datetime.now() - creation_date < timedelta(minutes=1)
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def test_get_file_creation_date_nonexistent_file():
    # Test for FileNotFoundError when file doesn't exist
    with pytest.raises(FileNotFoundError):
        get_file_creation_date('nonexistent_file_123456.txt')

def test_get_file_creation_date_directory():
    # Test attempting to get creation date of a directory
    with pytest.raises(RuntimeError):
        get_file_creation_date(os.path.dirname(__file__))

def test_get_file_creation_date_return_type():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Verify return type is datetime
        creation_date = get_file_creation_date(temp_path)
        assert isinstance(creation_date, datetime)
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)