def find_first_index(arr, target):
    """
    Find the index of the first occurrence of a target value in an array.
    
    Args:
        arr (list): The input array to search through
        target: The value to find in the array
    
    Returns:
        int: Index of the first occurrence of target, or -1 if not found
    """
    try:
        return arr.index(target)
    except ValueError:
        return -1