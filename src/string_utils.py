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
    # Remove spaces
    transformed = s.replace(' ', '')
    
    # Convert to lowercase
    transformed = transformed.lower()
    
    # Replace 'a' with '*'
    transformed = transformed.replace('a', '*')
    
    # Reverse the string
    transformed = transformed[::-1]
    
    return transformed