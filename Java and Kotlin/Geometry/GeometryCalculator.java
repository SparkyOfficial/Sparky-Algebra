/*
 * Geometry Calculator
 * Author: Андрій Будильников
 * 
 * This program calculates geometric properties of various shapes including
 * areas, perimeters, volumes, and surface areas.
 */

/* Provides methods for calculating geometric properties of various shapes */
public class GeometryCalculator {
    
    /* Mathematical constant Pi */
    private static final double PI = 3.14159265359;
    
    /* Calculates the area of a circle */
    public static double circleArea(double radius) {
        if (radius < 0) {
            throw new IllegalArgumentException("Radius cannot be negative");
        }
        
        return PI * radius * radius;
    }
    
    /* Calculates the circumference of a circle */
    public static double circleCircumference(double radius) {
        if (radius < 0) {
            throw new IllegalArgumentException("Radius cannot be negative");
        }
        
        return 2 * PI * radius;
    }
    
    /* Calculates the area of a triangle using Heron's formula */
    public static double triangleArea(double sideA, double sideB, double sideC) {
        if (sideA <= 0 || sideB <= 0 || sideC <= 0) {
            throw new IllegalArgumentException("All sides must be positive");
        }
        
        /* Check triangle inequality */
        if (sideA + sideB <= sideC || sideA + sideC <= sideB || sideB + sideC <= sideA) {
            throw new IllegalArgumentException("Invalid triangle: sides do not satisfy triangle inequality");
        }
        
        /* Heron's formula */
        double semiPerimeter = (sideA + sideB + sideC) / 2;
        return Math.sqrt(semiPerimeter * (semiPerimeter - sideA) * (semiPerimeter - sideB) * (semiPerimeter - sideC));
    }
    
    /* Calculates the perimeter of a triangle */
    public static double trianglePerimeter(double sideA, double sideB, double sideC) {
        if (sideA <= 0 || sideB <= 0 || sideC <= 0) {
            throw new IllegalArgumentException("All sides must be positive");
        }
        
        return sideA + sideB + sideC;
    }
    
    /* Calculates the area of a rectangle */
    public static double rectangleArea(double length, double width) {
        if (length < 0 || width < 0) {
            throw new IllegalArgumentException("Length and width cannot be negative");
        }
        
        return length * width;
    }
    
    /* Calculates the perimeter of a rectangle */
    public static double rectanglePerimeter(double length, double width) {
        if (length < 0 || width < 0) {
            throw new IllegalArgumentException("Length and width cannot be negative");
        }
        
        return 2 * (length + width);
    }
    
    /* Calculates the volume of a sphere */
    public static double sphereVolume(double radius) {
        if (radius < 0) {
            throw new IllegalArgumentException("Radius cannot be negative");
        }
        
        return (4.0 / 3.0) * PI * Math.pow(radius, 3);
    }
    
    /* Calculates the surface area of a sphere */
    public static double sphereSurfaceArea(double radius) {
        if (radius < 0) {
            throw new IllegalArgumentException("Radius cannot be negative");
        }
        
        return 4 * PI * radius * radius;
    }
    
    /* Main method to demonstrate geometry calculations */
    public static void main(String[] args) {
        System.out.println("Geometry Calculator Demo");
        System.out.println("======================");
        
        /* Circle calculations */
        double circleRadius = 5.0;
        System.out.println("Circle with radius " + circleRadius + ":");
        System.out.println("  Area: " + circleArea(circleRadius));
        System.out.println("  Circumference: " + circleCircumference(circleRadius));
        
        /* Triangle calculations */
        double sideA = 3.0, sideB = 4.0, sideC = 5.0;
        System.out.println("\nTriangle with sides " + sideA + ", " + sideB + ", " + sideC + ":");
        System.out.println("  Area: " + triangleArea(sideA, sideB, sideC));
        System.out.println("  Perimeter: " + trianglePerimeter(sideA, sideB, sideC));
        
        /* Rectangle calculations */
        double length = 6.0, width = 4.0;
        System.out.println("\nRectangle with length " + length + " and width " + width + ":");
        System.out.println("  Area: " + rectangleArea(length, width));
        System.out.println("  Perimeter: " + rectanglePerimeter(length, width));
        
        /* Sphere calculations */
        double sphereRadius = 3.0;
        System.out.println("\nSphere with radius " + sphereRadius + ":");
        System.out.println("  Volume: " + sphereVolume(sphereRadius));
        System.out.println("  Surface Area: " + sphereSurfaceArea(sphereRadius));
    }
}