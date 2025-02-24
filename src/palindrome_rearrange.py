from collections import Counter

def can_form_palindrome(s: str) -> bool:
    """
    Determine if the characters in the given string can be rearranged to form a palindrome.
    
    Args:
        s (str): Input string to check for palindrome rearrangement possibility
    
    Returns:
        bool: True if characters can be rearranged to form a palindrome, False otherwise
    
    Examples:
        >>> can_form_palindrome("racecar")
        True
        >>> can_form_palindrome("hello")
        False
    """
    # Count the frequency of each character
    char_counts = Counter(s)
    
    # Count characters with odd frequency
    odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)
    
    # A string can be rearranged to a palindrome if:
    # 1. All characters have even frequency, OR
    # 2. Only one character has an odd frequency
    return odd_count <= 1

def rearrange_to_palindrome(s: str) -> str:
    """
    Rearrange characters in the input string to form a palindrome.
    
    Args:
        s (str): Input string to rearrange
    
    Returns:
        str: A palindrome formed by rearranging the input string's characters
             Returns an empty string if no palindrome can be formed
    
    Raises:
        ValueError: If no palindrome can be formed from the input characters
    
    Examples:
        >>> rearrange_to_palindrome("racecar")
        'racecar'
        >>> rearrange_to_palindrome("aab")
        'aba'
    """
    # Handle empty string and single character cases
    if len(s) <= 1:
        return s
    
    # If the string is already a palindrome, return it
    if s == s[::-1]:
        return s
    
    # Strict check for palindrome possibility
    if not can_form_palindrome(s):
        raise ValueError("Cannot form a palindrome from the given characters")
    
    # Count character frequencies
    char_counts = Counter(s)
    
    # Prepare the palindrome components
    left_half = []
    odd_char = None
    
    # Sorted to ensure consistent output
    for char, count in sorted(char_counts.items()):
        # Add half the count of each character
        half_count = count // 2
        left_half.extend([char] * half_count)
        
        # Check for odd count character
        if count % 2 != 0:
            if odd_char is not None:
                # More than one odd count character
                raise ValueError("Cannot form a palindrome from the given characters")
            odd_char = char
    
    # Create right half (reverse of left half)
    right_half = left_half[::-1]
    
    # Construct palindrome with optional middle character
    if odd_char is not None:
        return ''.join(left_half + [odd_char] + right_half)
    else:
        return ''.join(left_half + right_half)