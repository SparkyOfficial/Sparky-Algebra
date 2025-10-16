"""
example.py
Author: Андрій Будильников

Example usage of combinatorics module
"""

from combinatorics import factorial, permutation, combination, catalan_number

# Example: Calculate number of ways to arrange 3 books out of 5 on a shelf
# This is a permutation problem: P(5,3)
arrangements = permutation(5, 3)
print(f"Number of ways to arrange 3 books out of 5: {arrangements}")

# Example: Calculate number of ways to choose 3 members from a group of 10
# This is a combination problem: C(10,3)
teams = combination(10, 3)
print(f"Number of ways to choose 3 members from 10: {teams}")

# Example: Calculate the number of possible passwords with 4 distinct digits
# This is a permutation problem: P(10,4)
passwords = permutation(10, 4)
print(f"Number of 4-digit passwords with distinct digits: {passwords}")

# Example: Calculate the 6th Catalan number
catalan = catalan_number(6)
print(f"The 6th Catalan number is: {catalan}")