/*
 * Geometry Calculator
 * Author: Андрій Будильников
 * 
 * This program calculates geometric properties of various shapes including
 * areas, perimeters, volumes, and surface areas.
 */

using System;

namespace Geometry
{
    /// <summary>
    /// Provides methods for calculating geometric properties of various shapes
    /// </summary>
    public class GeometryCalculator
    {
        // Mathematical constant Pi
        private const double PI = 3.14159265359;
        
        /// <summary>
        /// Calculates the area of a circle
        /// </summary>
        /// <param name="radius">Radius of the circle</param>
        /// <returns>Area of the circle</returns>
        public static double CircleArea(double radius)
        {
            if (radius < 0)
            {
                throw new ArgumentException("Radius cannot be negative");
            }
            
            return PI * radius * radius;
        }
        
        /// <summary>
        /// Calculates the circumference of a circle
        /// </summary>
        /// <param name="radius">Radius of the circle</param>
        /// <returns>Circumference of the circle</returns>
        public static double CircleCircumference(double radius)
        {
            if (radius < 0)
            {
                throw new ArgumentException("Radius cannot be negative");
            }
            
            return 2 * PI * radius;
        }
        
        /// <summary>
        /// Calculates the area of a triangle using Heron's formula
        /// </summary>
        /// <param name="sideA">Length of side A</param>
        /// <param name="sideB">Length of side B</param>
        /// <param name="sideC">Length of side C</param>
        /// <returns>Area of the triangle</returns>
        public static double TriangleArea(double sideA, double sideB, double sideC)
        {
            if (sideA <= 0 || sideB <= 0 || sideC <= 0)
            {
                throw new ArgumentException("All sides must be positive");
            }
            
            // Check triangle inequality
            if (sideA + sideB <= sideC || sideA + sideC <= sideB || sideB + sideC <= sideA)
            {
                throw new ArgumentException("Invalid triangle: sides do not satisfy triangle inequality");
            }
            
            // Heron's formula
            double semiPerimeter = (sideA + sideB + sideC) / 2;
            return Math.Sqrt(semiPerimeter * (semiPerimeter - sideA) * (semiPerimeter - sideB) * (semiPerimeter - sideC));
        }
        
        /// <summary>
        /// Calculates the perimeter of a triangle
        /// </summary>
        /// <param name="sideA">Length of side A</param>
        /// <param name="sideB">Length of side B</param>
        /// <param name="sideC">Length of side C</param>
        /// <returns>Perimeter of the triangle</returns>
        public static double TrianglePerimeter(double sideA, double sideB, double sideC)
        {
            if (sideA <= 0 || sideB <= 0 || sideC <= 0)
            {
                throw new ArgumentException("All sides must be positive");
            }
            
            return sideA + sideB + sideC;
        }
        
        /// <summary>
        /// Calculates the area of a rectangle
        /// </summary>
        /// <param name="length">Length of the rectangle</param>
        /// <param name="width">Width of the rectangle</param>
        /// <returns>Area of the rectangle</returns>
        public static double RectangleArea(double length, double width)
        {
            if (length < 0 || width < 0)
            {
                throw new ArgumentException("Length and width cannot be negative");
            }
            
            return length * width;
        }
        
        /// <summary>
        /// Calculates the perimeter of a rectangle
        /// </summary>
        /// <param name="length">Length of the rectangle</param>
        /// <param name="width">Width of the rectangle</param>
        /// <returns>Perimeter of the rectangle</returns>
        public static double RectanglePerimeter(double length, double width)
        {
            if (length < 0 || width < 0)
            {
                throw new ArgumentException("Length and width cannot be negative");
            }
            
            return 2 * (length + width);
        }
        
        /// <summary>
        /// Calculates the volume of a sphere
        /// </summary>
        /// <param name="radius">Radius of the sphere</param>
        /// <returns>Volume of the sphere</returns>
        public static double SphereVolume(double radius)
        {
            if (radius < 0)
            {
                throw new ArgumentException("Radius cannot be negative");
            }
            
            return (4.0 / 3.0) * PI * Math.Pow(radius, 3);
        }
        
        /// <summary>
        /// Calculates the surface area of a sphere
        /// </summary>
        /// <param name="radius">Radius of the sphere</param>
        /// <returns>Surface area of the sphere</returns>
        public static double SphereSurfaceArea(double radius)
        {
            if (radius < 0)
            {
                throw new ArgumentException("Radius cannot be negative");
            }
            
            return 4 * PI * radius * radius;
        }
        
        /// <summary>
        /// Main method to demonstrate geometry calculations
        /// </summary>
        public static void Main(string[] args)
        {
            Console.WriteLine("Geometry Calculator Demo");
            Console.WriteLine("======================");
            
            // Circle calculations
            double circleRadius = 5.0;
            Console.WriteLine($"Circle with radius {circleRadius}:");
            Console.WriteLine($"  Area: {CircleArea(circleRadius):F2}");
            Console.WriteLine($"  Circumference: {CircleCircumference(circleRadius):F2}");
            
            // Triangle calculations
            double sideA = 3.0, sideB = 4.0, sideC = 5.0;
            Console.WriteLine($"\nTriangle with sides {sideA}, {sideB}, {sideC}:");
            Console.WriteLine($"  Area: {TriangleArea(sideA, sideB, sideC):F2}");
            Console.WriteLine($"  Perimeter: {TrianglePerimeter(sideA, sideB, sideC):F2}");
            
            // Rectangle calculations
            double length = 6.0, width = 4.0;
            Console.WriteLine($"\nRectangle with length {length} and width {width}:");
            Console.WriteLine($"  Area: {RectangleArea(length, width):F2}");
            Console.WriteLine($"  Perimeter: {RectanglePerimeter(length, width):F2}");
            
            // Sphere calculations
            double sphereRadius = 3.0;
            Console.WriteLine($"\nSphere with radius {sphereRadius}:");
            Console.WriteLine($"  Volume: {SphereVolume(sphereRadius):F2}");
            Console.WriteLine($"  Surface Area: {SphereSurfaceArea(sphereRadius):F2}");
        }
    }
}