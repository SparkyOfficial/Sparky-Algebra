/*
 * Polynomial Root Finder using Newton-Raphson Method
 * Author: Андрій Будильников
 * 
 * This program finds roots of polynomials using the Newton-Raphson numerical method.
 */

using System;
using System.Collections.Generic;

public class PolynomialRootFinder
{
    private double[] coefficients;
    private int degree;

    /*
     * Initialize with polynomial coefficients
     * coefficients: array of coefficients from highest degree to constant term
     * e.g., [1, -6, 11, -6] represents x^3 - 6x^2 + 11x - 6
     */
    public PolynomialRootFinder(double[] coefficients)
    {
        this.coefficients = coefficients;
        this.degree = coefficients.Length - 1;
    }

    /*
     * Evaluate the polynomial at point x
     */
    public double Evaluate(double x)
    {
        double result = 0;
        for (int i = 0; i < coefficients.Length; i++)
        {
            result += coefficients[i] * Math.Pow(x, degree - i);
        }
        return result;
    }

    /*
     * Evaluate the derivative of the polynomial at point x
     */
    public double Derivative(double x)
    {
        double result = 0;
        // Skip constant term
        for (int i = 0; i < coefficients.Length - 1; i++)
        {
            int power = degree - i;
            result += coefficients[i] * power * Math.Pow(x, power - 1);
        }
        return result;
    }

    /*
     * Find a root using the Newton-Raphson method
     */
    public double? NewtonRaphson(double initialGuess, double tolerance = 1e-7, int maxIterations = 1000)
    {
        double x = initialGuess;

        for (int i = 0; i < maxIterations; i++)
        {
            double fx = Evaluate(x);
            double fpx = Derivative(x);

            // Check if derivative is too close to zero
            if (Math.Abs(fpx) < 1e-15)
            {
                Console.WriteLine("Derivative too close to zero. Try a different initial guess.");
                return null;
            }

            // Newton-Raphson formula
            double xNew = x - fx / fpx;

            // Check for convergence
            if (Math.Abs(xNew - x) < tolerance)
            {
                return xNew;
            }

            x = xNew;
        }

        Console.WriteLine("Maximum iterations reached. May not have converged.");
        return x;
    }

    /*
     * Find multiple roots using different initial guesses
     */
    public List<double> FindRoots(double[] initialGuesses)
    {
        List<double> roots = new List<double>();
        foreach (double guess in initialGuesses)
        {
            double? root = NewtonRaphson(guess);
            if (root.HasValue)
            {
                // Check if this root is already found (within tolerance)
                bool isNew = true;
                foreach (double foundRoot in roots)
                {
                    if (Math.Abs(root.Value - foundRoot) < 1e-6)
                    {
                        isNew = false;
                        break;
                    }
                }

                if (isNew)
                {
                    roots.Add(root.Value);
                }
            }
        }

        return roots;
    }

    /*
     * Main method to demonstrate the polynomial root finder
     * Example: x^3 - 6x^2 + 11x - 6 = 0 (roots are 1, 2, 3)
     */
    public static void Main(string[] args)
    {
        // Coefficients for x^3 - 6x^2 + 11x - 6
        double[] coefficients = { 1, -6, 11, -6 };

        PolynomialRootFinder finder = new PolynomialRootFinder(coefficients);

        Console.WriteLine("Finding roots of polynomial: x^3 - 6x^2 + 11x - 6 = 0");
        Console.WriteLine("Expected roots: 1, 2, 3");

        // Try multiple initial guesses
        double[] initialGuesses = { 0, 1.5, 2.5, 4 };
        List<double> roots = finder.FindRoots(initialGuesses);

        Console.Write("\nFound roots: ");
        foreach (double root in roots)
        {
            Console.Write(Math.Round(root, 6) + " ");
        }
        Console.WriteLine();
    }
}