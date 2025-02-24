def sum_unique_even_numbers(numbers):
    """
    Calculate the sum of unique even numbers in the given array.

    Args:
        numbers (list): A list of integers to process.

    Returns:
        int: Sum of even numbers that appear only once in the input list.

    Examples:
        >>> sum_unique_even_numbers([1, 2, 3, 4, 2, 6])
        6
        >>> sum_unique_even_numbers([1, 3, 5, 7])
        0
        >>> sum_unique_even_numbers([2, 4, 6, 2, 4])
        0
    """
    # Carefully track the count of each even number
    even_counts = {}
    
    # First pass: count even numbers
    for num in numbers:
        if num % 2 == 0:
            even_counts[num] = even_counts.get(num, 0) + 1
    
    # Second pass: sum unique even numbers
    return sum(num for num, count in even_counts.items() if count == 1)