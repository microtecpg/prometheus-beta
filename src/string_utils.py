def string_transform(s: str) -> str:
    """
    Transform the input string by:
    1. Removing all spaces
    2. Converting to lowercase
    3. Reversing the order of characters
    4. Replacing 'a' with '*'
    
    Args:
        s (str): Input string to transform
    
    Returns:
        str: Transformed string
    """
    # Remove spaces and convert to lowercase
    transformed = s.replace(' ', '').lower()
    
    # Reverse the string
    transformed = transformed[::-1]
    
    # Replace 'a' with '*' after reversal
    transformed = transformed.replace('a', '*')
    
    return transformed