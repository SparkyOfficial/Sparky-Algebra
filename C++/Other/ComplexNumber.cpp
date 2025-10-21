/*
 * Complex Number Implementation
 * Author: Андрій Будильников
 * 
 * This program provides a ComplexNumber class for working with complex numbers.
 */

#include <iostream>
#include <cmath>
#include <stdexcept>
#include <string>
#include <sstream>

class ComplexNumber {
private:
    double real;
    double imag;

public:
    // Constructor
    ComplexNumber(double r = 0, double i = 0) : real(r), imag(i) {}

    // Getters
    double getReal() const { return real; }
    double getImag() const { return imag; }

    // Setters
    void setReal(double r) { real = r; }
    void setImag(double i) { imag = i; }

    // String representation
    std::string toString() const {
        std::stringstream ss;
        if (imag >= 0) {
            ss << real << " + " << imag << "i";
        } else {
            ss << real << " - " << -imag << "i";
        }
        return ss.str();
    }

    // Addition
    ComplexNumber operator+(const ComplexNumber& other) const {
        return ComplexNumber(real + other.real, imag + other.imag);
    }

    ComplexNumber operator+(double scalar) const {
        return ComplexNumber(real + scalar, imag);
    }

    friend ComplexNumber operator+(double scalar, const ComplexNumber& cn) {
        return ComplexNumber(cn.real + scalar, cn.imag);
    }

    // Subtraction
    ComplexNumber operator-(const ComplexNumber& other) const {
        return ComplexNumber(real - other.real, imag - other.imag);
    }

    ComplexNumber operator-(double scalar) const {
        return ComplexNumber(real - scalar, imag);
    }

    friend ComplexNumber operator-(double scalar, const ComplexNumber& cn) {
        return ComplexNumber(scalar - cn.real, -cn.imag);
    }

    // Multiplication
    ComplexNumber operator*(const ComplexNumber& other) const {
        // (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        double r = real * other.real - imag * other.imag;
        double i = real * other.imag + imag * other.real;
        return ComplexNumber(r, i);
    }

    ComplexNumber operator*(double scalar) const {
        return ComplexNumber(real * scalar, imag * scalar);
    }

    friend ComplexNumber operator*(double scalar, const ComplexNumber& cn) {
        return ComplexNumber(cn.real * scalar, cn.imag * scalar);
    }

    // Division
    ComplexNumber operator/(const ComplexNumber& other) const {
        // (a + bi) / (c + di) = [(a + bi)(c - di)] / (c² + d²)
        double denominator = other.real * other.real + other.imag * other.imag;
        if (denominator == 0) {
            throw std::runtime_error("Division by zero complex number");
        }

        double r = (real * other.real + imag * other.imag) / denominator;
        double i = (imag * other.real - real * other.imag) / denominator;
        return ComplexNumber(r, i);
    }

    ComplexNumber operator/(double scalar) const {
        if (scalar == 0) {
            throw std::runtime_error("Division by zero");
        }
        return ComplexNumber(real / scalar, imag / scalar);
    }

    friend ComplexNumber operator/(double scalar, const ComplexNumber& cn) {
        double denominator = cn.real * cn.real + cn.imag * cn.imag;
        if (denominator == 0) {
            throw std::runtime_error("Division by zero complex number");
        }

        double r = (scalar * cn.real) / denominator;
        double i = (-scalar * cn.imag) / denominator;
        return ComplexNumber(r, i);
    }

    // Equality
    bool operator==(const ComplexNumber& other) const {
        return (real == other.real) && (imag == other.imag);
    }

    bool operator==(double scalar) const {
        return (real == scalar) && (imag == 0);
    }

    friend bool operator==(double scalar, const ComplexNumber& cn) {
        return (cn.real == scalar) && (cn.imag == 0);
    }

    // Conjugate
    ComplexNumber conjugate() const {
        return ComplexNumber(real, -imag);
    }

    // Magnitude
    double magnitude() const {
        return std::sqrt(real * real + imag * imag);
    }

    // Phase
    double phase() const {
        return std::atan2(imag, real);
    }

    // To polar form
    std::pair<double, double> toPolar() const {
        return std::make_pair(magnitude(), phase());
    }

    // Create from polar coordinates
    static ComplexNumber fromPolar(double magnitude, double phase) {
        double r = magnitude * std::cos(phase);
        double i = magnitude * std::sin(phase);
        return ComplexNumber(r, i);
    }
};

// Overload << operator for easy printing
std::ostream& operator<<(std::ostream& os, const ComplexNumber& cn) {
    os << cn.toString();
    return os;
}

// Main function to demonstrate the complex number class
int main() {
    // Create some complex numbers
    ComplexNumber z1(3, 4);   // 3 + 4i
    ComplexNumber z2(1, -2);  // 1 - 2i

    std::cout << "Complex Numbers:" << std::endl;
    std::cout << "z1 = " << z1 << std::endl;
    std::cout << "z2 = " << z2 << std::endl;

    // Basic operations
    std::cout << "\nBasic Operations:" << std::endl;
    std::cout << "z1 + z2 = " << (z1 + z2) << std::endl;
    std::cout << "z1 - z2 = " << (z1 - z2) << std::endl;
    std::cout << "z1 * z2 = " << (z1 * z2) << std::endl;
    std::cout << "z1 / z2 = " << (z1 / z2) << std::endl;

    // Properties
    std::cout << "\nProperties:" << std::endl;
    std::cout << "Conjugate of z1 = " << z1.conjugate() << std::endl;
    std::cout << "Magnitude of z1 = " << z1.magnitude() << std::endl;
    std::cout << "Phase of z1 = " << z1.phase() << " radians" << std::endl;

    // Polar form
    auto polar = z1.toPolar();
    std::cout << "Polar form of z1: magnitude = " << polar.first 
              << ", phase = " << polar.second << " radians" << std::endl;

    // Create from polar
    ComplexNumber z3 = ComplexNumber::fromPolar(5, 0.927);  // Should be close to 3 + 4i
    std::cout << "From polar (5, 0.927): " << z3 << std::endl;

    return 0;
}