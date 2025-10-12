/*
 * Prime Factorization Calculator
 * Author: Андрій Будильников
 * 
 * This program calculates the prime factorization of a given number.
 */

using System;
using System.Collections.Generic;

namespace NumberTheory
{
    /// <summary>
    /// Provides methods for calculating prime factorization of numbers
    /// </summary>
    public class PrimeFactorization
    {
        /// <summary>
        /// Calculates the prime factors of a given number
        /// </summary>
        /// <param name="number">The number to factorize</param>
        /// <returns>A list of prime factors</returns>
        public static List<int> GetPrimeFactors(long number)
        {
            List<int> factors = new List<int>();
            
            // Handle special cases
            if (number <= 1)
            {
                return factors;
            }
            
            // Check for factor 2
            while (number % 2 == 0)
            {
                factors.Add(2);
                number /= 2;
            }
            
            // Check for odd factors from 3 onwards
            for (int i = 3; i * i <= number; i += 2)
            {
                while (number % i == 0)
                {
                    factors.Add(i);
                    number /= i;
                }
            }
            
            // If number is still greater than 1, then it's a prime factor
            if (number > 1)
            {
                factors.Add((int)number);
            }
            
            return factors;
        }
        
        /// <summary>
        /// Formats the prime factorization as a string
        /// </summary>
        /// <param name="factors">List of prime factors</param>
        /// <returns>Formatted string representation</returns>
        public static string FormatFactorization(List<int> factors)
        {
            if (factors.Count == 0)
            {
                return "No prime factors";
            }
            
            // Count occurrences of each factor
            Dictionary<int, int> factorCounts = new Dictionary<int, int>();
            foreach (int factor in factors)
            {
                if (factorCounts.ContainsKey(factor))
                {
                    factorCounts[factor]++;
                }
                else
                {
                    factorCounts[factor] = 1;
                }
            }
            
            // Build the formatted string
            string result = "";
            bool first = true;
            foreach (var kvp in factorCounts)
            {
                if (!first)
                {
                    result += " × ";
                }
                
                if (kvp.Value == 1)
                {
                    result += kvp.Key.ToString();
                }
                else
                {
                    result += $"{kvp.Key}^{kvp.Value}";
                }
                
                first = false;
            }
            
            return result;
        }
        
        /// <summary>
        /// Main method to demonstrate the prime factorization calculator
        /// </summary>
        public static void Main(string[] args)
        {
            Console.WriteLine("Prime Factorization Calculator");
            Console.WriteLine("=============================");
            
            // Test cases
            long[] testNumbers = { 12, 315, 1024, 97, 1000, 2310 };
            
            foreach (long number in testNumbers)
            {
                List<int> factors = GetPrimeFactors(number);
                string formatted = FormatFactorization(factors);
                Console.WriteLine($"{number} = {formatted}");
            }
            
            // Interactive mode
            Console.WriteLine("\nEnter a number to factorize (or 'quit' to exit):");
            string input;
            while ((input = Console.ReadLine()) != "quit")
            {
                if (long.TryParse(input, out long number))
                {
                    if (number > 0)
                    {
                        List<int> factors = GetPrimeFactors(number);
                        string formatted = FormatFactorization(factors);
                        Console.WriteLine($"{number} = {formatted}");
                    }
                    else
                    {
                        Console.WriteLine("Please enter a positive number.");
                    }
                }
                else
                {
                    Console.WriteLine("Invalid input. Please enter a valid number.");
                }
                
                Console.WriteLine("Enter another number (or 'quit' to exit):");
            }
        }
    }
}