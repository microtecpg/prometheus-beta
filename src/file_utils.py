import os
import platform
from datetime import datetime

def get_file_creation_date(file_path):
    """
    Get the creation date of a file across different operating systems.

    Args:
        file_path (str): Path to the file to check.

    Returns:
        datetime: The creation date of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If there's no permission to access the file.
    """
    # Validate file existence first
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Platform-specific file creation time retrieval
    system = platform.system()
    
    try:
        if system == 'Windows':
            # Windows-specific method to get creation time
            creation_time = os.path.getctime(file_path)
        elif system == 'Darwin':  # macOS
            # macOS uses stat for creation time
            stat = os.stat(file_path)
            creation_time = stat.st_birthtime
        else:  # Linux and other Unix-like systems
            # Linux often uses metadata change time as closest to creation time
            stat = os.stat(file_path)
            creation_time = stat.st_ctime
        
        return datetime.fromtimestamp(creation_time)
    
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot access {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error retrieving file creation date: {str(e)}")