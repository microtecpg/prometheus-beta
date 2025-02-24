def sum_unique_even_numbers(numbers):
    """
    Calculate the sum of unique even numbers in the given array.

    A unique even number is an even number that appears exactly once in the list.

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
    # Track occurrences of each number
    count = {}
    for num in numbers:
        count[num] = count.get(num, 0) + 1
    
    # Sum unique even numbers (frequency is exactly 1)
    return sum(
        num for num in count 
        if num % 2 == 0 and count[num] == 1
    )