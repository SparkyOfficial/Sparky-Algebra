"""
pi calculator
author: Андрій Будильников

this program calculates pi using several different methods
"""

import random
import math

class PiCalculator:
    """pi calculator class with multiple methods"""
    
    @staticmethod
    def leibniz_formula(iterations):
        """leibniz formula for pi: pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ..."""
        pi = 0
        for i in range(iterations):
            if i % 2 == 0:
                pi += 1.0 / (2 * i + 1)
            else:
                pi -= 1.0 / (2 * i + 1)
        return pi * 4
    
    @staticmethod
    def monte_carlo_method(samples):
        """monte carlo method for pi"""
        inside_circle = 0
        
        for _ in range(samples):
            x = random.random() * 2 - 1  # -1 to 1
            y = random.random() * 2 - 1  # -1 to 1
            
            if x * x + y * y <= 1:
                inside_circle += 1
        
        return 4.0 * inside_circle / samples
    
    @staticmethod
    def nilakantha_series(iterations):
        """nilakantha series: pi = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - ..."""
        pi = 3
        for i in range(1, iterations + 1):
            denominator = 2 * i * (2 * i + 1) * (2 * i + 2)
            if i % 2 == 1:
                pi += 4.0 / denominator
            else:
                pi -= 4.0 / denominator
        return pi

def main():
    """main function to demonstrate pi calculation methods"""
    print("pi calculation methods")
    print("====================")
    
    iterations = 1000000
    print(f"leibniz formula ({iterations} iterations): {PiCalculator.leibniz_formula(iterations)}")
    
    samples = 1000000
    print(f"monte carlo method ({samples} samples): {PiCalculator.monte_carlo_method(samples)}")
    
    print(f"nilakantha series ({iterations} iterations): {PiCalculator.nilakantha_series(iterations)}")
    
    print(f"actual value of pi: {math.pi}")

if __name__ == "__main__":
    main()