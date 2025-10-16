/*
 * Combinatorics.cpp
 * Author: Андрій Будильников
 * 
 * Basic combinatorics functions implementation
 */

#include "Combinatorics.h"
#include <stdexcept>

long long Combinatorics::factorial(int n) {
    if (n < 0) {
        throw std::invalid_argument("factorial is not defined for negative numbers");
    }
    
    if (n == 0 || n == 1) {
        return 1;
    }
    
    long long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

long long Combinatorics::permutation(int n, int r) {
    if (n < 0 || r < 0) {
        throw std::invalid_argument("n and r must be non-negative");
    }
    
    if (r > n) {
        throw std::invalid_argument("r cannot be greater than n");
    }
    
    return factorial(n) / factorial(n - r);
}

long long Combinatorics::combination(int n, int r) {
    if (n < 0 || r < 0) {
        throw std::invalid_argument("n and r must be non-negative");
    }
    
    if (r > n) {
        throw std::invalid_argument("r cannot be greater than n");
    }
    
    return factorial(n) / (factorial(n - r) * factorial(r));
}

long long Combinatorics::catalanNumber(int n) {
    if (n < 0) {
        throw std::invalid_argument("n must be non-negative");
    }
    
    return combination(2 * n, n) / (n + 1);
}