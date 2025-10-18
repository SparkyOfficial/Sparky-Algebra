"""
Polynomial Root Finder using Newton-Raphson Method
Author: Андрій Будильников

This program finds roots of polynomials using the Newton-Raphson numerical method.
"""

class PolynomialRootFinder:
    """
    Finds roots of polynomials using the Newton-Raphson method
    """
    
    def __init__(self, coefficients):
        """
        Initialize with polynomial coefficients
        coefficients: list of coefficients from highest degree to constant term
        e.g., [1, -6, 11, -6] represents x^3 - 6x^2 + 11x - 6
        """
        self.coefficients = coefficients
        self.degree = len(coefficients) - 1
    
    def evaluate(self, x):
        """
        Evaluate the polynomial at point x
        """
        result = 0
        for i, coeff in enumerate(self.coefficients):
            result += coeff * (x ** (self.degree - i))
        return result
    
    def derivative(self, x):
        """
        Evaluate the derivative of the polynomial at point x
        """
        result = 0
        for i, coeff in enumerate(self.coefficients[:-1]):  # Skip constant term
            power = self.degree - i
            result += coeff * power * (x ** (power - 1))
        return result
    
    def newton_raphson(self, initial_guess, tolerance=1e-7, max_iterations=1000):
        """
        Find a root using the Newton-Raphson method
        """
        x = initial_guess
        
        for i in range(max_iterations):
            fx = self.evaluate(x)
            fpx = self.derivative(x)
            
            # Check if derivative is too close to zero
            if abs(fpx) < 1e-15:
                print("Derivative too close to zero. Try a different initial guess.")
                return None
            
            # Newton-Raphson formula
            x_new = x - fx / fpx
            
            # Check for convergence
            if abs(x_new - x) < tolerance:
                return x_new
            
            x = x_new
        
        print("Maximum iterations reached. May not have converged.")
        return x
    
    def find_roots(self, initial_guesses):
        """
        Find multiple roots using different initial guesses
        """
        roots = []
        for guess in initial_guesses:
            root = self.newton_raphson(guess)
            if root is not None:
                # Check if this root is already found (within tolerance)
                is_new = True
                for found_root in roots:
                    if abs(root - found_root) < 1e-6:
                        is_new = False
                        break
                
                if is_new:
                    roots.append(root)
        
        return roots

def main():
    """
    Main function to demonstrate the polynomial root finder
    Example: x^3 - 6x^2 + 11x - 6 = 0 (roots are 1, 2, 3)
    """
    # Coefficients for x^3 - 6x^2 + 11x - 6
    coefficients = [1, -6, 11, -6]
    
    finder = PolynomialRootFinder(coefficients)
    
    print("Finding roots of polynomial: x^3 - 6x^2 + 11x - 6 = 0")
    print("Expected roots: 1, 2, 3")
    
    # Try multiple initial guesses
    initial_guesses = [0, 1.5, 2.5, 4]
    roots = finder.find_roots(initial_guesses)
    
    print(f"\nFound roots: {[round(root, 6) for root in roots]}")

if __name__ == "__main__":
    main()