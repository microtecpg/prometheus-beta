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
    # Remove spaces
    transformed = s.replace(' ', '')
    
    # Convert to lowercase
    transformed = transformed.lower()
    
    # Reverse the string first
    transformed = transformed[::-1]
    
    # Replace 'a' with '*' after reversal
    transformed = transformed.replace('a', '*')
    
    return transformed