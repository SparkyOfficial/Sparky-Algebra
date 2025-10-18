/*
 * Polynomial Root Finder using Newton-Raphson Method
 * Author: Андрій Будильников
 * 
 * This program finds roots of polynomials using the Newton-Raphson numerical method.
 */

import java.util.ArrayList;
import java.util.List;

public class PolynomialRootFinder {
    private double[] coefficients;
    private int degree;

    /*
     * Initialize with polynomial coefficients
     * coefficients: array of coefficients from highest degree to constant term
     * e.g., [1, -6, 11, -6] represents x^3 - 6x^2 + 11x - 6
     */
    public PolynomialRootFinder(double[] coefficients) {
        this.coefficients = coefficients;
        this.degree = coefficients.length - 1;
    }

    /*
     * Evaluate the polynomial at point x
     */
    public double evaluate(double x) {
        double result = 0;
        for (int i = 0; i < coefficients.length; i++) {
            result += coefficients[i] * Math.pow(x, degree - i);
        }
        return result;
    }

    /*
     * Evaluate the derivative of the polynomial at point x
     */
    public double derivative(double x) {
        double result = 0;
        // Skip constant term
        for (int i = 0; i < coefficients.length - 1; i++) {
            int power = degree - i;
            result += coefficients[i] * power * Math.pow(x, power - 1);
        }
        return result;
    }

    /*
     * Find a root using the Newton-Raphson method
     */
    public Double newtonRaphson(double initialGuess, double tolerance, int maxIterations) {
        double x = initialGuess;

        for (int i = 0; i < maxIterations; i++) {
            double fx = evaluate(x);
            double fpx = derivative(x);

            // Check if derivative is too close to zero
            if (Math.abs(fpx) < 1e-15) {
                System.out.println("Derivative too close to zero. Try a different initial guess.");
                return null;
            }

            // Newton-Raphson formula
            double xNew = x - fx / fpx;

            // Check for convergence
            if (Math.abs(xNew - x) < tolerance) {
                return xNew;
            }

            x = xNew;
        }

        System.out.println("Maximum iterations reached. May not have converged.");
        return x;
    }

    /*
     * Overloaded method with default parameters
     */
    public Double newtonRaphson(double initialGuess) {
        return newtonRaphson(initialGuess, 1e-7, 1000);
    }

    /*
     * Find multiple roots using different initial guesses
     */
    public List<Double> findRoots(double[] initialGuesses) {
        List<Double> roots = new ArrayList<>();
        for (double guess : initialGuesses) {
            Double root = newtonRaphson(guess);
            if (root != null) {
                // Check if this root is already found (within tolerance)
                boolean isNew = true;
                for (Double foundRoot : roots) {
                    if (Math.abs(root - foundRoot) < 1e-6) {
                        isNew = false;
                        break;
                    }
                }

                if (isNew) {
                    roots.add(root);
                }
            }
        }

        return roots;
    }

    /*
     * Main method to demonstrate the polynomial root finder
     * Example: x^3 - 6x^2 + 11x - 6 = 0 (roots are 1, 2, 3)
     */
    public static void main(String[] args) {
        // Coefficients for x^3 - 6x^2 + 11x - 6
        double[] coefficients = { 1, -6, 11, -6 };

        PolynomialRootFinder finder = new PolynomialRootFinder(coefficients);

        System.out.println("Finding roots of polynomial: x^3 - 6x^2 + 11x - 6 = 0");
        System.out.println("Expected roots: 1, 2, 3");

        // Try multiple initial guesses
        double[] initialGuesses = { 0, 1.5, 2.5, 4 };
        List<Double> roots = finder.findRoots(initialGuesses);

        System.out.print("\nFound roots: ");
        for (Double root : roots) {
            System.out.print(Math.round(root * 1e6) / 1e6 + " ");
        }
        System.out.println();
    }
}