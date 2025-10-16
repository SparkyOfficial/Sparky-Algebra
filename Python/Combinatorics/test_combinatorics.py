"""
test_combinatorics.py
Author: Андрій Будильников

Test file for combinatorics module
"""

from combinatorics import factorial, permutation, combination, catalan_number

def test_factorial():
    """test factorial function"""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    print("factorial tests passed")

def test_permutation():
    """test permutation function"""
    assert permutation(5, 0) == 1
    assert permutation(5, 1) == 5
    assert permutation(5, 3) == 60
    assert permutation(10, 2) == 90
    print("permutation tests passed")

def test_combination():
    """test combination function"""
    assert combination(5, 0) == 1
    assert combination(5, 1) == 5
    assert combination(5, 3) == 10
    assert combination(10, 2) == 45
    print("combination tests passed")

def test_catalan_number():
    """test catalan number function"""
    # first few catalan numbers: 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862
    assert catalan_number(0) == 1
    assert catalan_number(1) == 1
    assert catalan_number(2) == 2
    assert catalan_number(3) == 5
    assert catalan_number(4) == 14
    assert catalan_number(5) == 42
    print("catalan number tests passed")

if __name__ == "__main__":
    test_factorial()
    test_permutation()
    test_combination()
    test_catalan_number()
    print("all tests passed! 🎉")