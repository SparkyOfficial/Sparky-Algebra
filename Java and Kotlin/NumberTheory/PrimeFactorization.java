/*
 * Prime Factorization Calculator
 * Author: Андрій Будильников
 * 
 * This program calculates the prime factorization of a given number.
 */

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

// Provides methods for calculating prime factorization of numbers
public class PrimeFactorization {
    
    // Calculates the prime factors of a given number
    public static List<Integer> getPrimeFactors(long number) {
        List<Integer> factors = new ArrayList<>();
        
        // Handle special cases
        if (number <= 1) {
            return factors;
        }
        
        // Check for factor 2
        while (number % 2 == 0) {
            factors.add(2);
            number /= 2;
        }
        
        // Check for odd factors from 3 onwards
        for (int i = 3; i * i <= number; i += 2) {
            while (number % i == 0) {
                factors.add(i);
                number /= i;
            }
        }
        
        // If number is still greater than 1, then it's a prime factor
        if (number > 1) {
            factors.add((int)number);
        }
        
        return factors;
    }
    
    // Formats the prime factorization as a string
    public static String formatFactorization(List<Integer> factors) {
        if (factors.isEmpty()) {
            return "No prime factors";
        }
        
        // Count occurrences of each factor
        Map<Integer, Integer> factorCounts = new HashMap<>();
        for (int factor : factors) {
            factorCounts.put(factor, factorCounts.getOrDefault(factor, 0) + 1);
        }
        
        // Build the formatted string
        StringBuilder result = new StringBuilder();
        boolean first = true;
        for (Map.Entry<Integer, Integer> entry : factorCounts.entrySet()) {
            if (!first) {
                result.append(" × ");
            }
            
            if (entry.getValue() == 1) {
                result.append(entry.getKey());
            } else {
                result.append(entry.getKey()).append("^").append(entry.getValue());
            }
            
            first = false;
        }
        
        return result.toString();
    }
    
    // Main method to demonstrate the prime factorization calculator
    public static void main(String[] args) {
        System.out.println("Prime Factorization Calculator");
        System.out.println("=============================");
        
        // Test cases
        long[] testNumbers = { 12, 315, 1024, 97, 1000, 2310 };
        
        for (long number : testNumbers) {
            List<Integer> factors = getPrimeFactors(number);
            String formatted = formatFactorization(factors);
            System.out.println(number + " = " + formatted);
        }
        
        // Interactive mode
        Scanner scanner = new Scanner(System.in);
        System.out.println("\nEnter a number to factorize (or 'quit' to exit):");
        
        String input;
        while (!(input = scanner.nextLine()).equals("quit")) {
            try {
                long number = Long.parseLong(input);
                if (number > 0) {
                    List<Integer> factors = getPrimeFactors(number);
                    String formatted = formatFactorization(factors);
                    System.out.println(number + " = " + formatted);
                } else {
                    System.out.println("Please enter a positive number.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a valid number.");
            }
            
            System.out.println("Enter another number (or 'quit' to exit):");
        }
        
        scanner.close();
    }
}