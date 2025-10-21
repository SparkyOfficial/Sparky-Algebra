/*
 * Complex Number Implementation
 * Author: Андрій Будильников
 * 
 * This program provides a ComplexNumber class for working with complex numbers.
 */

using System;

public class ComplexNumber
{
    public double Real { get; set; }
    public double Imaginary { get; set; }

    // Constructor
    public ComplexNumber(double real = 0, double imaginary = 0)
    {
        Real = real;
        Imaginary = imaginary;
    }

    // String representation
    public override string ToString()
    {
        if (Imaginary >= 0)
        {
            return $"{Real} + {Imaginary}i";
        }
        else
        {
            return $"{Real} - {Math.Abs(Imaginary)}i";
        }
    }

    // Addition
    public static ComplexNumber operator +(ComplexNumber c1, ComplexNumber c2)
    {
        return new ComplexNumber(c1.Real + c2.Real, c1.Imaginary + c2.Imaginary);
    }

    public static ComplexNumber operator +(ComplexNumber c, double scalar)
    {
        return new ComplexNumber(c.Real + scalar, c.Imaginary);
    }

    public static ComplexNumber operator +(double scalar, ComplexNumber c)
    {
        return new ComplexNumber(c.Real + scalar, c.Imaginary);
    }

    // Subtraction
    public static ComplexNumber operator -(ComplexNumber c1, ComplexNumber c2)
    {
        return new ComplexNumber(c1.Real - c2.Real, c1.Imaginary - c2.Imaginary);
    }

    public static ComplexNumber operator -(ComplexNumber c, double scalar)
    {
        return new ComplexNumber(c.Real - scalar, c.Imaginary);
    }

    public static ComplexNumber operator -(double scalar, ComplexNumber c)
    {
        return new ComplexNumber(scalar - c.Real, -c.Imaginary);
    }

    // Multiplication
    public static ComplexNumber operator *(ComplexNumber c1, ComplexNumber c2)
    {
        // (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        double real = c1.Real * c2.Real - c1.Imaginary * c2.Imaginary;
        double imaginary = c1.Real * c2.Imaginary + c1.Imaginary * c2.Real;
        return new ComplexNumber(real, imaginary);
    }

    public static ComplexNumber operator *(ComplexNumber c, double scalar)
    {
        return new ComplexNumber(c.Real * scalar, c.Imaginary * scalar);
    }

    public static ComplexNumber operator *(double scalar, ComplexNumber c)
    {
        return new ComplexNumber(c.Real * scalar, c.Imaginary * scalar);
    }

    // Division
    public static ComplexNumber operator /(ComplexNumber c1, ComplexNumber c2)
    {
        // (a + bi) / (c + di) = [(a + bi)(c - di)] / (c² + d²)
        double denominator = c2.Real * c2.Real + c2.Imaginary * c2.Imaginary;
        if (denominator == 0)
        {
            throw new DivideByZeroException("Division by zero complex number");
        }

        double real = (c1.Real * c2.Real + c1.Imaginary * c2.Imaginary) / denominator;
        double imaginary = (c1.Imaginary * c2.Real - c1.Real * c2.Imaginary) / denominator;
        return new ComplexNumber(real, imaginary);
    }

    public static ComplexNumber operator /(ComplexNumber c, double scalar)
    {
        if (scalar == 0)
        {
            throw new DivideByZeroException("Division by zero");
        }
        return new ComplexNumber(c.Real / scalar, c.Imaginary / scalar);
    }

    public static ComplexNumber operator /(double scalar, ComplexNumber c)
    {
        double denominator = c.Real * c.Real + c.Imaginary * c.Imaginary;
        if (denominator == 0)
        {
            throw new DivideByZeroException("Division by zero complex number");
        }

        double real = (scalar * c.Real) / denominator;
        double imaginary = (-scalar * c.Imaginary) / denominator;
        return new ComplexNumber(real, imaginary);
    }

    // Equality
    public static bool operator ==(ComplexNumber c1, ComplexNumber c2)
    {
        if (ReferenceEquals(c1, null) && ReferenceEquals(c2, null)) return true;
        if (ReferenceEquals(c1, null) || ReferenceEquals(c2, null)) return false;
        return (c1.Real == c2.Real) && (c1.Imaginary == c2.Imaginary);
    }

    public static bool operator !=(ComplexNumber c1, ComplexNumber c2)
    {
        return !(c1 == c2);
    }

    public override bool Equals(object obj)
    {
        if (obj is ComplexNumber other)
        {
            return (Real == other.Real) && (Imaginary == other.Imaginary);
        }
        return false;
    }

    public override int GetHashCode()
    {
        return Real.GetHashCode() ^ Imaginary.GetHashCode();
    }

    // Conjugate
    public ComplexNumber Conjugate()
    {
        return new ComplexNumber(Real, -Imaginary);
    }

    // Magnitude
    public double Magnitude()
    {
        return Math.Sqrt(Real * Real + Imaginary * Imaginary);
    }

    // Phase
    public double Phase()
    {
        return Math.Atan2(Imaginary, Real);
    }

    // To polar form
    public Tuple<double, double> ToPolar()
    {
        return new Tuple<double, double>(Magnitude(), Phase());
    }

    // Create from polar coordinates
    public static ComplexNumber FromPolar(double magnitude, double phase)
    {
        double real = magnitude * Math.Cos(phase);
        double imaginary = magnitude * Math.Sin(phase);
        return new ComplexNumber(real, imaginary);
    }

    // Main method to demonstrate the complex number class
    public static void Main(string[] args)
    {
        // Create some complex numbers
        ComplexNumber z1 = new ComplexNumber(3, 4);   // 3 + 4i
        ComplexNumber z2 = new ComplexNumber(1, -2);  // 1 - 2i

        Console.WriteLine("Complex Numbers:");
        Console.WriteLine($"z1 = {z1}");
        Console.WriteLine($"z2 = {z2}");

        // Basic operations
        Console.WriteLine("\nBasic Operations:");
        Console.WriteLine($"z1 + z2 = {z1 + z2}");
        Console.WriteLine($"z1 - z2 = {z1 - z2}");
        Console.WriteLine($"z1 * z2 = {z1 * z2}");
        Console.WriteLine($"z1 / z2 = {z1 / z2}");

        // Properties
        Console.WriteLine("\nProperties:");
        Console.WriteLine($"Conjugate of z1 = {z1.Conjugate()}");
        Console.WriteLine($"Magnitude of z1 = {z1.Magnitude()}");
        Console.WriteLine($"Phase of z1 = {z1.Phase()} radians");

        // Polar form
        var polar = z1.ToPolar();
        Console.WriteLine($"Polar form of z1: magnitude = {polar.Item1}, phase = {polar.Item2} radians");

        // Create from polar
        ComplexNumber z3 = ComplexNumber.FromPolar(5, 0.927);  // Should be close to 3 + 4i
        Console.WriteLine($"From polar (5, 0.927): {z3}");
    }
}