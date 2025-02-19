def string_transform(s: str) -> str:
    """
    Transform the input string by:
    1. Removing all spaces
    2. Converting to lowercase
    3. Replacing 'a' with '*'
    4. Reversing the order of characters
    
    Args:
        s (str): Input string to transform
    
    Returns:
        str: Transformed string
    """
    # Remove spaces and convert to lowercase
    transformed = s.replace(' ', '').lower()
    
    # Replace 'a' with '*'
    transformed = transformed.replace('a', '*')
    
    # Reverse the string
    transformed = transformed[::-1]
    
    return transformed