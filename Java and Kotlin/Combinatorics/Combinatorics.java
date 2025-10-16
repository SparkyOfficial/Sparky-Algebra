/*
 * Combinatorics.java
 * Author: Андрій Будильников
 * 
 * Basic combinatorics functions implementation
 */

public class Combinatorics {
    
    /**
     * calculate factorial of n
     * @param n non-negative integer
     * @return factorial of n
     */
    public static long factorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("factorial is not defined for negative numbers");
        }
        
        if (n == 0 || n == 1) {
            return 1;
        }
        
        long result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
    
    /**
     * calculate permutations p(n,r) = n!/(n-r)!
     * @param n total number of items
     * @param r number of items to choose
     * @return number of permutations
     */
    public static long permutation(int n, int r) {
        if (n < 0 || r < 0) {
            throw new IllegalArgumentException("n and r must be non-negative");
        }
        
        if (r > n) {
            throw new IllegalArgumentException("r cannot be greater than n");
        }
        
        return factorial(n) / factorial(n - r);
    }
    
    /**
     * calculate combinations c(n,r) = n!/((n-r)!*r!)
     * @param n total number of items
     * @param r number of items to choose
     * @return number of combinations
     */
    public static long combination(int n, int r) {
        if (n < 0 || r < 0) {
            throw new IllegalArgumentException("n and r must be non-negative");
        }
        
        if (r > n) {
            throw new IllegalArgumentException("r cannot be greater than n");
        }
        
        return factorial(n) / (factorial(n - r) * factorial(r));
    }
    
    /**
     * calculate nth catalan number
     * @param n index of catalan number
     * @return nth catalan number
     */
    public static long catalanNumber(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("n must be non-negative");
        }
        
        return combination(2 * n, n) / (n + 1);
    }
}