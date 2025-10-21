"""
Complex Number Implementation
Author: Андрій Будильников

This module provides a ComplexNumber class for working with complex numbers.
"""

import math

class ComplexNumber:
    """
    A class representing a complex number with real and imaginary parts.
    """
    
    def __init__(self, real=0, imag=0):
        """
        Initialize a complex number with real and imaginary parts.
        """
        self.real = real
        self.imag = imag
    
    def __str__(self):
        """
        Return a string representation of the complex number.
        """
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"
    
    def __repr__(self):
        """
        Return a string representation for debugging.
        """
        return f"ComplexNumber({self.real}, {self.imag})"
    
    def __add__(self, other):
        """
        Add two complex numbers.
        """
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real + other, self.imag)
        else:
            raise TypeError("Unsupported operand type for +")
    
    def __radd__(self, other):
        """
        Right addition (when complex number is on the right side of +).
        """
        return self.__add__(other)
    
    def __sub__(self, other):
        """
        Subtract two complex numbers.
        """
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real - other, self.imag)
        else:
            raise TypeError("Unsupported operand type for -")
    
    def __rsub__(self, other):
        """
        Right subtraction (when complex number is on the right side of -).
        """
        if isinstance(other, (int, float)):
            return ComplexNumber(other - self.real, -self.imag)
        else:
            raise TypeError("Unsupported operand type for -")
    
    def __mul__(self, other):
        """
        Multiply two complex numbers.
        """
        if isinstance(other, ComplexNumber):
            # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return ComplexNumber(real_part, imag_part)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real * other, self.imag * other)
        else:
            raise TypeError("Unsupported operand type for *")
    
    def __rmul__(self, other):
        """
        Right multiplication (when complex number is on the right side of *).
        """
        return self.__mul__(other)
    
    def __truediv__(self, other):
        """
        Divide two complex numbers.
        """
        if isinstance(other, ComplexNumber):
            # (a + bi) / (c + di) = [(a + bi)(c - di)] / (c² + d²)
            denominator = other.real**2 + other.imag**2
            if denominator == 0:
                raise ZeroDivisionError("Division by zero complex number")
            
            real_part = (self.real * other.real + self.imag * other.imag) / denominator
            imag_part = (self.imag * other.real - self.real * other.imag) / denominator
            return ComplexNumber(real_part, imag_part)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero")
            return ComplexNumber(self.real / other, self.imag / other)
        else:
            raise TypeError("Unsupported operand type for /")
    
    def __rtruediv__(self, other):
        """
        Right division (when complex number is on the right side of /).
        """
        if isinstance(other, (int, float)):
            # other / self
            denominator = self.real**2 + self.imag**2
            if denominator == 0:
                raise ZeroDivisionError("Division by zero complex number")
            
            real_part = (other * self.real) / denominator
            imag_part = (-other * self.imag) / denominator
            return ComplexNumber(real_part, imag_part)
        else:
            raise TypeError("Unsupported operand type for /")
    
    def __eq__(self, other):
        """
        Check equality of two complex numbers.
        """
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imag == other.imag
        elif isinstance(other, (int, float)):
            return self.real == other and self.imag == 0
        else:
            return False
    
    def conjugate(self):
        """
        Return the complex conjugate of this complex number.
        """
        return ComplexNumber(self.real, -self.imag)
    
    def magnitude(self):
        """
        Return the magnitude (absolute value) of the complex number.
        """
        return math.sqrt(self.real**2 + self.imag**2)
    
    def phase(self):
        """
        Return the phase (argument) of the complex number in radians.
        """
        return math.atan2(self.imag, self.real)
    
    def to_polar(self):
        """
        Convert to polar form (magnitude, phase).
        """
        return (self.magnitude(), self.phase())
    
    @staticmethod
    def from_polar(magnitude, phase):
        """
        Create a complex number from polar coordinates.
        """
        real = magnitude * math.cos(phase)
        imag = magnitude * math.sin(phase)
        return ComplexNumber(real, imag)

def main():
    """
    Main function to demonstrate the complex number class.
    """
    # Create some complex numbers
    z1 = ComplexNumber(3, 4)  # 3 + 4i
    z2 = ComplexNumber(1, -2) # 1 - 2i
    
    print("Complex Numbers:")
    print(f"z1 = {z1}")
    print(f"z2 = {z2}")
    
    # Basic operations
    print("\nBasic Operations:")
    print(f"z1 + z2 = {z1 + z2}")
    print(f"z1 - z2 = {z1 - z2}")
    print(f"z1 * z2 = {z1 * z2}")
    print(f"z1 / z2 = {z1 / z2}")
    
    # Properties
    print("\nProperties:")
    print(f"Conjugate of z1 = {z1.conjugate()}")
    print(f"Magnitude of z1 = {z1.magnitude()}")
    print(f"Phase of z1 = {z1.phase()} radians")
    
    # Polar form
    mag, phase = z1.to_polar()
    print(f"Polar form of z1: magnitude = {mag}, phase = {phase} radians")
    
    # Create from polar
    z3 = ComplexNumber.from_polar(5, 0.927)  # Should be close to 3 + 4i
    print(f"From polar (5, 0.927): {z3}")

if __name__ == "__main__":
    main()