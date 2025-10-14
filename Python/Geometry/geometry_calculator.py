"""
Geometry Calculator
Author: Андрій Будильников

This program calculates geometric properties of various shapes including
areas, perimeters, volumes, and surface areas.
"""

import math

class GeometryCalculator:
    """
    Provides methods for calculating geometric properties of various shapes
    """
    
    """Mathematical constant Pi"""
    PI = 3.14159265359
    
    @staticmethod
    def circle_area(radius):
        """
        Calculates the area of a circle
        :param radius: Radius of the circle
        :return: Area of the circle
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        
        return GeometryCalculator.PI * radius * radius
    
    @staticmethod
    def circle_circumference(radius):
        """
        Calculates the circumference of a circle
        :param radius: Radius of the circle
        :return: Circumference of the circle
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        
        return 2 * GeometryCalculator.PI * radius
    
    @staticmethod
    def triangle_area(side_a, side_b, side_c):
        """
        Calculates the area of a triangle using Heron's formula
        :param side_a: Length of side A
        :param side_b: Length of side B
        :param side_c: Length of side C
        :return: Area of the triangle
        """
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("All sides must be positive")
        
        """Check triangle inequality"""
        if (side_a + side_b <= side_c or 
            side_a + side_c <= side_b or 
            side_b + side_c <= side_a):
            raise ValueError("Invalid triangle: sides do not satisfy triangle inequality")
        
        """Heron's formula"""
        semi_perimeter = (side_a + side_b + side_c) / 2
        return math.sqrt(semi_perimeter * (semi_perimeter - side_a) * 
                        (semi_perimeter - side_b) * (semi_perimeter - side_c))
    
    @staticmethod
    def triangle_perimeter(side_a, side_b, side_c):
        """
        Calculates the perimeter of a triangle
        :param side_a: Length of side A
        :param side_b: Length of side B
        :param side_c: Length of side C
        :return: Perimeter of the triangle
        """
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("All sides must be positive")
        
        return side_a + side_b + side_c
    
    @staticmethod
    def rectangle_area(length, width):
        """
        Calculates the area of a rectangle
        :param length: Length of the rectangle
        :param width: Width of the rectangle
        :return: Area of the rectangle
        """
        if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative")
        
        return length * width
    
    @staticmethod
    def rectangle_perimeter(length, width):
        """
        Calculates the perimeter of a rectangle
        :param length: Length of the rectangle
        :param width: Width of the rectangle
        :return: Perimeter of the rectangle
        """
        if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative")
        
        return 2 * (length + width)
    
    @staticmethod
    def sphere_volume(radius):
        """
        Calculates the volume of a sphere
        :param radius: Radius of the sphere
        :return: Volume of the sphere
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        
        return (4.0 / 3.0) * GeometryCalculator.PI * (radius ** 3)
    
    @staticmethod
    def sphere_surface_area(radius):
        """
        Calculates the surface area of a sphere
        :param radius: Radius of the sphere
        :return: Surface area of the sphere
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        
        return 4 * GeometryCalculator.PI * radius * radius

def main():
    """
    Main function to demonstrate geometry calculations
    """
    print("Geometry Calculator Demo")
    print("======================")
    
    """Circle calculations"""
    circle_radius = 5.0
    print(f"Circle with radius {circle_radius}:")
    print(f"  Area: {GeometryCalculator.circle_area(circle_radius)}")
    print(f"  Circumference: {GeometryCalculator.circle_circumference(circle_radius)}")
    
    """Triangle calculations"""
    side_a, side_b, side_c = 3.0, 4.0, 5.0
    print(f"\nTriangle with sides {side_a}, {side_b}, {side_c}:")
    print(f"  Area: {GeometryCalculator.triangle_area(side_a, side_b, side_c)}")
    print(f"  Perimeter: {GeometryCalculator.triangle_perimeter(side_a, side_b, side_c)}")
    
    """Rectangle calculations"""
    length, width = 6.0, 4.0
    print(f"\nRectangle with length {length} and width {width}:")
    print(f"  Area: {GeometryCalculator.rectangle_area(length, width)}")
    print(f"  Perimeter: {GeometryCalculator.rectangle_perimeter(length, width)}")
    
    """Sphere calculations"""
    sphere_radius = 3.0
    print(f"\nSphere with radius {sphere_radius}:")
    print(f"  Volume: {GeometryCalculator.sphere_volume(sphere_radius)}")
    print(f"  Surface Area: {GeometryCalculator.sphere_surface_area(sphere_radius)}")

if __name__ == "__main__":
    main()