/*
 * Polynomial Root Finder using Newton-Raphson Method
 * Author: Андрій Будильников
 * 
 * This program finds roots of polynomials using the Newton-Raphson numerical method.
 */

#include <iostream>
#include <vector>
#include <cmath>
#include <limits>

class PolynomialRootFinder {
private:
    std::vector<double> coefficients;
    int degree;

public:
    /*
     * Initialize with polynomial coefficients
     * coefficients: vector of coefficients from highest degree to constant term
     * e.g., {1, -6, 11, -6} represents x^3 - 6x^2 + 11x - 6
     */
    PolynomialRootFinder(const std::vector<double>& coeffs) : coefficients(coeffs) {
        degree = coeffs.size() - 1;
    }

    /*
     * Evaluate the polynomial at point x
     */
    double evaluate(double x) {
        double result = 0;
        for (size_t i = 0; i < coefficients.size(); i++) {
            result += coefficients[i] * std::pow(x, degree - i);
        }
        return result;
    }

    /*
     * Evaluate the derivative of the polynomial at point x
     */
    double derivative(double x) {
        double result = 0;
        // Skip constant term
        for (size_t i = 0; i < coefficients.size() - 1; i++) {
            int power = degree - i;
            result += coefficients[i] * power * std::pow(x, power - 1);
        }
        return result;
    }

    /*
     * Find a root using the Newton-Raphson method
     */
    double newtonRaphson(double initialGuess, double tolerance = 1e-7, int maxIterations = 1000) {
        double x = initialGuess;

        for (int i = 0; i < maxIterations; i++) {
            double fx = evaluate(x);
            double fpx = derivative(x);

            // Check if derivative is too close to zero
            if (std::abs(fpx) < 1e-15) {
                std::cout << "Derivative too close to zero. Try a different initial guess." << std::endl;
                return std::numeric_limits<double>::quiet_NaN();
            }

            // Newton-Raphson formula
            double xNew = x - fx / fpx;

            // Check for convergence
            if (std::abs(xNew - x) < tolerance) {
                return xNew;
            }

            x = xNew;
        }

        std::cout << "Maximum iterations reached. May not have converged." << std::endl;
        return x;
    }

    /*
     * Find multiple roots using different initial guesses
     */
    std::vector<double> findRoots(const std::vector<double>& initialGuesses) {
        std::vector<double> roots;
        for (double guess : initialGuesses) {
            double root = newtonRaphson(guess);
            if (!std::isnan(root)) {
                // Check if this root is already found (within tolerance)
                bool isNew = true;
                for (double foundRoot : roots) {
                    if (std::abs(root - foundRoot) < 1e-6) {
                        isNew = false;
                        break;
                    }
                }

                if (isNew) {
                    roots.push_back(root);
                }
            }
        }

        return roots;
    }
};

/*
 * Main function to demonstrate the polynomial root finder
 * Example: x^3 - 6x^2 + 11x - 6 = 0 (roots are 1, 2, 3)
 */
int main() {
    // Coefficients for x^3 - 6x^2 + 11x - 6
    std::vector<double> coefficients = {1, -6, 11, -6};

    PolynomialRootFinder finder(coefficients);

    std::cout << "Finding roots of polynomial: x^3 - 6x^2 + 11x - 6 = 0" << std::endl;
    std::cout << "Expected roots: 1, 2, 3" << std::endl;

    // Try multiple initial guesses
    std::vector<double> initialGuesses = {0, 1.5, 2.5, 4};
    std::vector<double> roots = finder.findRoots(initialGuesses);

    std::cout << "\nFound roots: ";
    for (double root : roots) {
        std::cout << std::round(root * 1e6) / 1e6 << " ";
    }
    std::cout << std::endl;

    return 0;
}/*
 * Polynomial Root Finder using Newton-Raphson Method
 * Author: Андрій Будильников
 * 
 * This program finds roots of polynomials using the Newton-Raphson numerical method.
 */

#include <iostream>
#include <vector>
#include <cmath>
#include <limits>

class PolynomialRootFinder {
private:
    std::vector<double> coefficients;
    int degree;

public:
    /*
     * Initialize with polynomial coefficients
     * coefficients: vector of coefficients from highest degree to constant term
     * e.g., {1, -6, 11, -6} represents x^3 - 6x^2 + 11x - 6
     */
    PolynomialRootFinder(const std::vector<double>& coeffs) : coefficients(coeffs) {
        degree = coeffs.size() - 1;
    }

    /*
     * Evaluate the polynomial at point x
     */
    double evaluate(double x) {
        double result = 0;
        for (size_t i = 0; i < coefficients.size(); i++) {
            result += coefficients[i] * std::pow(x, degree - i);
        }
        return result;
    }

    /*
     * Evaluate the derivative of the polynomial at point x
     */
    double derivative(double x) {
        double result = 0;
        // Skip constant term
        for (size_t i = 0; i < coefficients.size() - 1; i++) {
            int power = degree - i;
            result += coefficients[i] * power * std::pow(x, power - 1);
        }
        return result;
    }

    /*
     * Find a root using the Newton-Raphson method
     */
    double newtonRaphson(double initialGuess, double tolerance = 1e-7, int maxIterations = 1000) {
        double x = initialGuess;

        for (int i = 0; i < maxIterations; i++) {
            double fx = evaluate(x);
            double fpx = derivative(x);

            // Check if derivative is too close to zero
            if (std::abs(fpx) < 1e-15) {
                std::cout << "Derivative too close to zero. Try a different initial guess." << std::endl;
                return std::numeric_limits<double>::quiet_NaN();
            }

            // Newton-Raphson formula
            double xNew = x - fx / fpx;

            // Check for convergence
            if (std::abs(xNew - x) < tolerance) {
                return xNew;
            }

            x = xNew;
        }

        std::cout << "Maximum iterations reached. May not have converged." << std::endl;
        return x;
    }

    /*
     * Find multiple roots using different initial guesses
     */
    std::vector<double> findRoots(const std::vector<double>& initialGuesses) {
        std::vector<double> roots;
        for (double guess : initialGuesses) {
            double root = newtonRaphson(guess);
            if (!std::isnan(root)) {
                // Check if this root is already found (within tolerance)
                bool isNew = true;
                for (double foundRoot : roots) {
                    if (std::abs(root - foundRoot) < 1e-6) {
                        isNew = false;
                        break;
                    }
                }

                if (isNew) {
                    roots.push_back(root);
                }
            }
        }

        return roots;
    }
};

/*
 * Main function to demonstrate the polynomial root finder
 * Example: x^3 - 6x^2 + 11x - 6 = 0 (roots are 1, 2, 3)
 */
int main() {
    // Coefficients for x^3 - 6x^2 + 11x - 6
    std::vector<double> coefficients = {1, -6, 11, -6};

    PolynomialRootFinder finder(coefficients);

    std::cout << "Finding roots of polynomial: x^3 - 6x^2 + 11x - 6 = 0" << std::endl;
    std::cout << "Expected roots: 1, 2, 3" << std::endl;

    // Try multiple initial guesses
    std::vector<double> initialGuesses = {0, 1.5, 2.5, 4};
    std::vector<double> roots = finder.findRoots(initialGuesses);

    std::cout << "\nFound roots: ";
    for (double root : roots) {
        std::cout << std::round(root * 1e6) / 1e6 << " ";
    }
    std::cout << std::endl;

    return 0;
}