def filter_even_numbers(numbers):
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    return list(even_numbers)
