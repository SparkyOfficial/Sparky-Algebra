/*
 * Combinatorics.h
 * Author: Андрій Будильников
 * 
 * Basic combinatorics functions implementation
 */

#ifndef COMBINATORICS_H
#define COMBINATORICS_H

class Combinatorics {
public:
    /**
     * calculate factorial of n
     * @param n non-negative integer
     * @return factorial of n
     */
    static long long factorial(int n);
    
    /**
     * calculate permutations p(n,r) = n!/(n-r)!
     * @param n total number of items
     * @param r number of items to choose
     * @return number of permutations
     */
    static long long permutation(int n, int r);
    
    /**
     * calculate combinations c(n,r) = n!/((n-r)!*r!)
     * @param n total number of items
     * @param r number of items to choose
     * @return number of combinations
     */
    static long long combination(int n, int r);
    
    /**
     * calculate nth catalan number
     * @param n index of catalan number
     * @return nth catalan number
     */
    static long long catalanNumber(int n);
};

#endif // COMBINATORICS_H