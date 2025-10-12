"""
Prime Factorization Calculator
Author: Андрій Будильников

This program calculates the prime factorization of a given number.
"""

from collections import Counter

class PrimeFactorization:
    """
    Provides methods for calculating prime factorization of numbers
    """
    
    @staticmethod
    def get_prime_factors(number):
        """
        Calculates the prime factors of a given number
        :param number: The number to factorize
        :return: A list of prime factors
        """
        factors = []
        
        # Handle special cases
        if number <= 1:
            return factors
        
        # Check for factor 2
        while number % 2 == 0:
            factors.append(2)
            number //= 2
        
        # Check for odd factors from 3 onwards
        i = 3
        while i * i <= number:
            while number % i == 0:
                factors.append(i)
                number //= i
            i += 2
        
        # If number is still greater than 1, then it's a prime factor
        if number > 1:
            factors.append(number)
        
        return factors
    
    @staticmethod
    def format_factorization(factors):
        """
        Formats the prime factorization as a string
        :param factors: List of prime factors
        :return: Formatted string representation
        """
        if not factors:
            return "No prime factors"
        
        # Count occurrences of each factor
        factor_counts = Counter(factors)
        
        # Build the formatted string
        result_parts = []
        for factor, count in sorted(factor_counts.items()):
            if count == 1:
                result_parts.append(str(factor))
            else:
                result_parts.append(f"{factor}^{count}")
        
        return " × ".join(result_parts)

def main():
    """
    Main function to demonstrate the prime factorization calculator
    """
    print("Prime Factorization Calculator")
    print("=============================")
    
    # Test cases
    test_numbers = [12, 315, 1024, 97, 1000, 2310]
    
    for number in test_numbers:
        factors = PrimeFactorization.get_prime_factors(number)
        formatted = PrimeFactorization.format_factorization(factors)
        print(f"{number} = {formatted}")
    
    # Interactive mode
    print("\nEnter a number to factorize (or 'quit' to exit):")
    while True:
        try:
            user_input = input().strip()
            if user_input == 'quit':
                break
            
            number = int(user_input)
            if number > 0:
                factors = PrimeFactorization.get_prime_factors(number)
                formatted = PrimeFactorization.format_factorization(factors)
                print(f"{number} = {formatted}")
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
        print("Enter another number (or 'quit' to exit):")

if __name__ == "__main__":
    main()