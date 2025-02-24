def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Find the median of two sorted arrays.

    This function finds the median of two sorted arrays in O(log(min(m,n)) time complexity.
    
    Args:
        nums1 (list[int]): First sorted input array
        nums2 (list[int]): Second sorted input array
    
    Returns:
        float: Median of the two sorted arrays
    
    Raises:
        TypeError: If inputs are not lists
        ValueError: If inputs contain non-numeric types or both arrays are empty
    
    Examples:
        >>> find_median_sorted_arrays([1, 3], [2])
        2.0
        >>> find_median_sorted_arrays([1, 2], [3, 4])
        2.5
    """
    # Validate input types
    if not (isinstance(nums1, list) and isinstance(nums2, list)):
        raise TypeError("Inputs must be lists")
    
    # Validate input contents
    if not (all(isinstance(x, (int, float)) for x in nums1 + nums2)):
        raise ValueError("Lists must contain only numeric types")
    
    # Check for both empty
    if len(nums1) == 0 and len(nums2) == 0:
        raise ValueError("Both input arrays cannot be empty")
    
    # Ensure nums1 is the smaller array for efficiency
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    
    # Handle empty array cases
    if m == 0:
        mid = n // 2
        if n % 2 == 0:
            return (nums2[mid - 1] + nums2[mid]) / 2
        else:
            return float(nums2[mid])
    
    # Binary search on the smaller array
    low, high = 0, m
    
    while low <= high:
        partition_x = (low + high) // 2
        partition_y = (m + n + 1) // 2 - partition_x
        
        # Edge case checks
        max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
        min_right_x = float('inf') if partition_x == m else nums1[partition_x]
        
        max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
        min_right_y = float('inf') if partition_y == n else nums2[partition_y]
        
        # Check if we have found the correct partition
        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            # If total length is even
            if (m + n) % 2 == 0:
                return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
            # If total length is odd
            else:
                return float(max(max_left_x, max_left_y))
        
        # Adjust binary search
        elif max_left_x > min_right_y:
            high = partition_x - 1
        else:
            low = partition_x + 1
    
    # If no valid partition found (should not happen with valid inputs)
    raise ValueError("Unable to find median")