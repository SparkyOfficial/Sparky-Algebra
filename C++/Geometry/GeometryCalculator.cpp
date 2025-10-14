/*
 * Geometry Calculator
 * Author: Андрій Будильников
 * 
 * This program calculates geometric properties of various shapes including
 * areas, perimeters, volumes, and surface areas.
 */

#include <iostream>
#include <cmath>
#include <stdexcept>

/* Provides methods for calculating geometric properties of various shapes */
class GeometryCalculator {
private:
    /* Mathematical constant Pi */
    static constexpr double PI = 3.14159265359;
    
public:
    /* Calculates the area of a circle */
    static double circleArea(double radius) {
        if (radius < 0) {
            throw std::invalid_argument("Radius cannot be negative");
        }
        
        return PI * radius * radius;
    }
    
    /* Calculates the circumference of a circle */
    static double circleCircumference(double radius) {
        if (radius < 0) {
            throw std::invalid_argument("Radius cannot be negative");
        }
        
        return 2 * PI * radius;
    }
    
    /* Calculates the area of a triangle using Heron's formula */
    static double triangleArea(double sideA, double sideB, double sideC) {
        if (sideA <= 0 || sideB <= 0 || sideC <= 0) {
            throw std::invalid_argument("All sides must be positive");
        }
        
        /* Check triangle inequality */
        if (sideA + sideB <= sideC || sideA + sideC <= sideB || sideB + sideC <= sideA) {
            throw std::invalid_argument("Invalid triangle: sides do not satisfy triangle inequality");
        }
        
        /* Heron's formula */
        double semiPerimeter = (sideA + sideB + sideC) / 2;
        return sqrt(semiPerimeter * (semiPerimeter - sideA) * (semiPerimeter - sideB) * (semiPerimeter - sideC));
    }
    
    /* Calculates the perimeter of a triangle */
    static double trianglePerimeter(double sideA, double sideB, double sideC) {
        if (sideA <= 0 || sideB <= 0 || sideC <= 0) {
            throw std::invalid_argument("All sides must be positive");
        }
        
        return sideA + sideB + sideC;
    }
    
    /* Calculates the area of a rectangle */
    static double rectangleArea(double length, double width) {
        if (length < 0 || width < 0) {
            throw std::invalid_argument("Length and width cannot be negative");
        }
        
        return length * width;
    }
    
    /* Calculates the perimeter of a rectangle */
    static double rectanglePerimeter(double length, double width) {
        if (length < 0 || width < 0) {
            throw std::invalid_argument("Length and width cannot be negative");
        }
        
        return 2 * (length + width);
    }
    
    /* Calculates the volume of a sphere */
    static double sphereVolume(double radius) {
        if (radius < 0) {
            throw std::invalid_argument("Radius cannot be negative");
        }
        
        return (4.0 / 3.0) * PI * pow(radius, 3);
    }
    
    /* Calculates the surface area of a sphere */
    static double sphereSurfaceArea(double radius) {
        if (radius < 0) {
            throw std::invalid_argument("Radius cannot be negative");
        }
        
        return 4 * PI * radius * radius;
    }
};

/* Main method to demonstrate geometry calculations */
int main() {
    std::cout << "Geometry Calculator Demo" << std::endl;
    std::cout << "======================" << std::endl;
    
    /* Circle calculations */
    double circleRadius = 5.0;
    std::cout << "Circle with radius " << circleRadius << ":" << std::endl;
    std::cout << "  Area: " << GeometryCalculator::circleArea(circleRadius) << std::endl;
    std::cout << "  Circumference: " << GeometryCalculator::circleCircumference(circleRadius) << std::endl;
    
    /* Triangle calculations */
    double sideA = 3.0, sideB = 4.0, sideC = 5.0;
    std::cout << std::endl << "Triangle with sides " << sideA << ", " << sideB << ", " << sideC << ":" << std::endl;
    std::cout << "  Area: " << GeometryCalculator::triangleArea(sideA, sideB, sideC) << std::endl;
    std::cout << "  Perimeter: " << GeometryCalculator::trianglePerimeter(sideA, sideB, sideC) << std::endl;
    
    /* Rectangle calculations */
    double length = 6.0, width = 4.0;
    std::cout << std::endl << "Rectangle with length " << length << " and width " << width << ":" << std::endl;
    std::cout << "  Area: " << GeometryCalculator::rectangleArea(length, width) << std::endl;
    std::cout << "  Perimeter: " << GeometryCalculator::rectanglePerimeter(length, width) << std::endl;
    
    /* Sphere calculations */
    double sphereRadius = 3.0;
    std::cout << std::endl << "Sphere with radius " << sphereRadius << ":" << std::endl;
    std::cout << "  Volume: " << GeometryCalculator::sphereVolume(sphereRadius) << std::endl;
    std::cout << "  Surface Area: " << GeometryCalculator::sphereSurfaceArea(sphereRadius) << std::endl;
    
    return 0;
}