/*
 * Prime Factorization Calculator
 * Author: Андрій Будильников
 * 
 * This program calculates the prime factorization of a given number.
 */

#include <iostream>
#include <vector>
#include <map>
#include <string>

// Provides methods for calculating prime factorization of numbers
class PrimeFactorization {
public:
    // Calculates the prime factors of a given number
    static std::vector<int> getPrimeFactors(long long number) {
        std::vector<int> factors;
        
        // Handle special cases
        if (number <= 1) {
            return factors;
        }
        
        // Check for factor 2
        while (number % 2 == 0) {
            factors.push_back(2);
            number /= 2;
        }
        
        // Check for odd factors from 3 onwards
        for (int i = 3; i * i <= number; i += 2) {
            while (number % i == 0) {
                factors.push_back(i);
                number /= i;
            }
        }
        
        // If number is still greater than 1, then it's a prime factor
        if (number > 1) {
            factors.push_back((int)number);
        }
        
        return factors;
    }
    
    // Formats the prime factorization as a string
    static std::string formatFactorization(const std::vector<int>& factors) {
        if (factors.empty()) {
            return "No prime factors";
        }
        
        // Count occurrences of each factor
        std::map<int, int> factorCounts;
        for (int factor : factors) {
            factorCounts[factor]++;
        }
        
        // Build the formatted string
        std::string result = "";
        bool first = true;
        for (const auto& pair : factorCounts) {
            if (!first) {
                result += " × ";
            }
            
            if (pair.second == 1) {
                result += std::to_string(pair.first);
            } else {
                result += std::to_string(pair.first) + "^" + std::to_string(pair.second);
            }
            
            first = false;
        }
        
        return result;
    }
};

// Main method to demonstrate the prime factorization calculator
int main() {
    std::cout << "Prime Factorization Calculator" << std::endl;
    std::cout << "=============================" << std::endl;
    
    // Test cases
    long long testNumbers[] = { 12, 315, 1024, 97, 1000, 2310 };
    int numTests = sizeof(testNumbers) / sizeof(testNumbers[0]);
    
    for (int i = 0; i < numTests; i++) {
        long long number = testNumbers[i];
        std::vector<int> factors = PrimeFactorization::getPrimeFactors(number);
        std::string formatted = PrimeFactorization::formatFactorization(factors);
        std::cout << number << " = " << formatted << std::endl;
    }
    
    // Interactive mode
    std::cout << "\nEnter a number to factorize (or 'quit' to exit):" << std::endl;
    std::string input;
    while (std::getline(std::cin, input) && input != "quit") {
        try {
            long long number = std::stoll(input);
            if (number > 0) {
                std::vector<int> factors = PrimeFactorization::getPrimeFactors(number);
                std::string formatted = PrimeFactorization::formatFactorization(factors);
                std::cout << number << " = " << formatted << std::endl;
            } else {
                std::cout << "Please enter a positive number." << std::endl;
            }
        } catch (const std::exception& e) {
            std::cout << "Invalid input. Please enter a valid number." << std::endl;
        }
        
        std::cout << "Enter another number (or 'quit' to exit):" << std::endl;
    }
    
    return 0;
}