/*
 * Combinatorics.cs
 * Author: Андрій Будильников
 * 
 * Basic combinatorics functions implementation
 */

using System;

namespace Combinatorics
{
    public class CombinatoricsCalculator
    {
        /// <summary>
        /// calculate factorial of n
        /// </summary>
        /// <param name="n">non-negative integer</param>
        /// <returns>factorial of n</returns>
        public static long Factorial(int n)
        {
            if (n < 0)
                throw new ArgumentException("factorial is not defined for negative numbers");
                
            if (n == 0 || n == 1)
                return 1;
                
            long result = 1;
            for (int i = 2; i <= n; i++)
            {
                result *= i;
            }
            return result;
        }

        /// <summary>
        /// calculate permutations p(n,r) = n!/(n-r)!
        /// </summary>
        /// <param name="n">total number of items</param>
        /// <param name="r">number of items to choose</param>
        /// <returns>number of permutations</returns>
        public static long Permutation(int n, int r)
        {
            if (n < 0 || r < 0)
                throw new ArgumentException("n and r must be non-negative");
                
            if (r > n)
                throw new ArgumentException("r cannot be greater than n");
                
            return Factorial(n) / Factorial(n - r);
        }

        /// <summary>
        /// calculate combinations c(n,r) = n!/((n-r)!*r!)
        /// </summary>
        /// <param name="n">total number of items</param>
        /// <param name="r">number of items to choose</param>
        /// <returns>number of combinations</returns>
        public static long Combination(int n, int r)
        {
            if (n < 0 || r < 0)
                throw new ArgumentException("n and r must be non-negative");
                
            if (r > n)
                throw new ArgumentException("r cannot be greater than n");
                
            return Factorial(n) / (Factorial(n - r) * Factorial(r));
        }

        /// <summary>
        /// calculate nth catalan number
        /// </summary>
        /// <param name="n">index of catalan number</param>
        /// <returns>nth catalan number</returns>
        public static long CatalanNumber(int n)
        {
            if (n < 0)
                throw new ArgumentException("n must be non-negative");
                
            return Combination(2 * n, n) / (n + 1);
        }
    }
}