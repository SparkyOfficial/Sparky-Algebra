"""
combinatorics.py
Author: Андрій Будильников

Basic combinatorics functions implementation
"""

import math

def factorial(n):
    """calculate factorial of n"""
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def permutation(n, r):
    """calculate permutations p(n,r) = n!/(n-r)!"""
    if n < 0 or r < 0:
        raise ValueError("n and r must be non-negative")
    if r > n:
        raise ValueError("r cannot be greater than n")
    return factorial(n) // factorial(n - r)

def combination(n, r):
    """calculate combinations c(n,r) = n!/((n-r)!*r!)"""
    if n < 0 or r < 0:
        raise ValueError("n and r must be non-negative")
    if r > n:
        raise ValueError("r cannot be greater than n")
    return factorial(n) // (factorial(n - r) * factorial(r))

def catalan_number(n):
    """calculate nth catalan number"""
    if n < 0:
        raise ValueError("n must be non-negative")
    return combination(2 * n, n) // (n + 1)
