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
    # Get the set of even numbers and track frequencies
    even_freq = {}
    for num in numbers:
        if num % 2 == 0:
            even_freq[num] = even_freq.get(num, 0) + 1
    
    # Sum unique even numbers (those with frequency of 1)
    return sum(num for num, freq in even_freq.items() if freq == 1)