#!/usr/bin/python3
"""
Module Doc: Minimum Operations
Execute minimmum required operations
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result
    in exactly n H characters in the file.
    """
    if n == 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        # Check if the current divisor is a factor of n
        while n % divisor == 0:
            operations += divisor
            n //= divisor

        divisor += 1

    return operations
