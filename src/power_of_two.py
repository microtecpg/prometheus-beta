def is_power_of_two(n):
    """
    Check if a given number is a power of two.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is a power of two, False otherwise.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is negative.

    Examples:
        >>> is_power_of_two(1)
        True
        >>> is_power_of_two(16)
        True
        >>> is_power_of_two(0)
        False
        >>> is_power_of_two(7)
        False
    """
    # Check input type and value
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Handle special cases
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # 0 and 1 are special cases
    if n <= 1:
        return n == 1
    
    # A power of two will have only one bit set in its binary representation
    # This can be checked by using bitwise AND with (n-1)
    return (n & (n - 1)) == 0