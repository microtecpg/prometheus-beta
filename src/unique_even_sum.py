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
    # Track the unique even numbers by creating a set of duplicates
    duplicates = set(x for x in numbers if numbers.count(x) > 1)
    
    # Sum unique even numbers that don't appear in duplicates
    return sum(num for num in set(numbers) 
               if num % 2 == 0 and num not in duplicates)