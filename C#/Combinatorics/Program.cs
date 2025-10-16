/*
 * Program.cs
 * Author: Андрій Будильников
 * 
 * Test program for combinatorics functions
 */

using System;
using Combinatorics;

namespace CombinatoricsTest
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Testing combinatorics functions...\n");
            
            // test factorial
            Console.WriteLine($"Factorial(0) = {CombinatoricsCalculator.Factorial(0)}");
            Console.WriteLine($"Factorial(1) = {CombinatoricsCalculator.Factorial(1)}");
            Console.WriteLine($"Factorial(5) = {CombinatoricsCalculator.Factorial(5)}");
            Console.WriteLine($"Factorial(10) = {CombinatoricsCalculator.Factorial(10)}");
            
            Console.WriteLine();
            
            // test permutation
            Console.WriteLine($"Permutation(5, 0) = {CombinatoricsCalculator.Permutation(5, 0)}");
            Console.WriteLine($"Permutation(5, 1) = {CombinatoricsCalculator.Permutation(5, 1)}");
            Console.WriteLine($"Permutation(5, 3) = {CombinatoricsCalculator.Permutation(5, 3)}");
            Console.WriteLine($"Permutation(10, 2) = {CombinatoricsCalculator.Permutation(10, 2)}");
            
            Console.WriteLine();
            
            // test combination
            Console.WriteLine($"Combination(5, 0) = {CombinatoricsCalculator.Combination(5, 0)}");
            Console.WriteLine($"Combination(5, 1) = {CombinatoricsCalculator.Combination(5, 1)}");
            Console.WriteLine($"Combination(5, 3) = {CombinatoricsCalculator.Combination(5, 3)}");
            Console.WriteLine($"Combination(10, 2) = {CombinatoricsCalculator.Combination(10, 2)}");
            
            Console.WriteLine();
            
            // test catalan number
            Console.WriteLine($"CatalanNumber(0) = {CombinatoricsCalculator.CatalanNumber(0)}");
            Console.WriteLine($"CatalanNumber(1) = {CombinatoricsCalculator.CatalanNumber(1)}");
            Console.WriteLine($"CatalanNumber(2) = {CombinatoricsCalculator.CatalanNumber(2)}");
            Console.WriteLine($"CatalanNumber(3) = {CombinatoricsCalculator.CatalanNumber(3)}");
            Console.WriteLine($"CatalanNumber(4) = {CombinatoricsCalculator.CatalanNumber(4)}");
            Console.WriteLine($"CatalanNumber(5) = {CombinatoricsCalculator.CatalanNumber(5)}");
            
            Console.WriteLine("\nAll tests completed! 🎉");
        }
    }
}