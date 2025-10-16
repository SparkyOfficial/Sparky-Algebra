/*
 * test_combinatorics.cpp
 * Author: Андрій Будильников
 * 
 * Test program for combinatorics functions
 */

#include <iostream>
#include "Combinatorics.h"

int main() {
    std::cout << "Testing combinatorics functions...\n\n";
    
    // test factorial
    std::cout << "Factorial(0) = " << Combinatorics::factorial(0) << std::endl;
    std::cout << "Factorial(1) = " << Combinatorics::factorial(1) << std::endl;
    std::cout << "Factorial(5) = " << Combinatorics::factorial(5) << std::endl;
    std::cout << "Factorial(10) = " << Combinatorics::factorial(10) << std::endl;
    
    std::cout << std::endl;
    
    // test permutation
    std::cout << "Permutation(5, 0) = " << Combinatorics::permutation(5, 0) << std::endl;
    std::cout << "Permutation(5, 1) = " << Combinatorics::permutation(5, 1) << std::endl;
    std::cout << "Permutation(5, 3) = " << Combinatorics::permutation(5, 3) << std::endl;
    std::cout << "Permutation(10, 2) = " << Combinatorics::permutation(10, 2) << std::endl;
    
    std::cout << std::endl;
    
    // test combination
    std::cout << "Combination(5, 0) = " << Combinatorics::combination(5, 0) << std::endl;
    std::cout << "Combination(5, 1) = " << Combinatorics::combination(5, 1) << std::endl;
    std::cout << "Combination(5, 3) = " << Combinatorics::combination(5, 3) << std::endl;
    std::cout << "Combination(10, 2) = " << Combinatorics::combination(10, 2) << std::endl;
    
    std::cout << std::endl;
    
    // test catalan number
    std::cout << "CatalanNumber(0) = " << Combinatorics::catalanNumber(0) << std::endl;
    std::cout << "CatalanNumber(1) = " << Combinatorics::catalanNumber(1) << std::endl;
    std::cout << "CatalanNumber(2) = " << Combinatorics::catalanNumber(2) << std::endl;
    std::cout << "CatalanNumber(3) = " << Combinatorics::catalanNumber(3) << std::endl;
    std::cout << "CatalanNumber(4) = " << Combinatorics::catalanNumber(4) << std::endl;
    std::cout << "CatalanNumber(5) = " << Combinatorics::catalanNumber(5) << std::endl;
    
    std::cout << "\nAll tests completed! 🎉" << std::endl;
    
    return 0;
}