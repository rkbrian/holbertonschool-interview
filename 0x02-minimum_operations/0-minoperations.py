#!/usr/bin/python3
"""
method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    copyi = 0
    pastei = 0
    """multiple paste"""
    factory = 2
    """edge case: 0 or 1"""
    if n < 2:
        return 0
    """first factor"""
    while (n % factory > 0):
        factory += 1
    while n % factory == 0:
        copyi += 1
        pastei += (factory - 1)
        n = n / factory
        if n == 1:
            return copyi + pastei
        while n % factory > 0:
            factory += 1
    return copyi + pastei
