/*
 * Combinatorics.kt
 * Author: Андрій Будильников
 * 
 * Basic combinatorics functions implementation in Kotlin
 */

class Combinatorics {
    companion object {
        /**
         * calculate factorial of n
         * @param n non-negative integer
         * @return factorial of n
         */
        fun factorial(n: Int): Long {
            if (n < 0) {
                throw IllegalArgumentException("factorial is not defined for negative numbers")
            }
            
            if (n == 0 || n == 1) {
                return 1
            }
            
            var result = 1L
            for (i in 2..n) {
                result *= i
            }
            return result
        }
        
        /**
         * calculate permutations p(n,r) = n!/(n-r)!
         * @param n total number of items
         * @param r number of items to choose
         * @return number of permutations
         */
        fun permutation(n: Int, r: Int): Long {
            if (n < 0 || r < 0) {
                throw IllegalArgumentException("n and r must be non-negative")
            }
            
            if (r > n) {
                throw IllegalArgumentException("r cannot be greater than n")
            }
            
            return factorial(n) / factorial(n - r)
        }
        
        /**
         * calculate combinations c(n,r) = n!/((n-r)!*r!)
         * @param n total number of items
         * @param r number of items to choose
         * @return number of combinations
         */
        fun combination(n: Int, r: Int): Long {
            if (n < 0 || r < 0) {
                throw IllegalArgumentException("n and r must be non-negative")
            }
            
            if (r > n) {
                throw IllegalArgumentException("r cannot be greater than n")
            }
            
            return factorial(n) / (factorial(n - r) * factorial(r))
        }
        
        /**
         * calculate nth catalan number
         * @param n index of catalan number
         * @return nth catalan number
         */
        fun catalanNumber(n: Int): Long {
            if (n < 0) {
                throw IllegalArgumentException("n must be non-negative")
            }
            
            return combination(2 * n, n) / (n + 1)
        }
    }
}