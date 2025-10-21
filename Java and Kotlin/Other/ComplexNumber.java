/*
 * Complex Number Implementation
 * Author: Андрій Будильников
 * 
 * This program provides a ComplexNumber class for working with complex numbers.
 */

import java.util.Objects;

public class ComplexNumber {
    private double real;
    private double imaginary;

    // Constructor
    public ComplexNumber(double real, double imaginary) {
        this.real = real;
        this.imaginary = imaginary;
    }

    // Default constructor
    public ComplexNumber() {
        this(0, 0);
    }

    // Getters
    public double getReal() {
        return real;
    }

    public double getImaginary() {
        return imaginary;
    }

    // Setters
    public void setReal(double real) {
        this.real = real;
    }

    public void setImaginary(double imaginary) {
        this.imaginary = imaginary;
    }

    // String representation
    @Override
    public String toString() {
        if (imaginary >= 0) {
            return real + " + " + imaginary + "i";
        } else {
            return real + " - " + Math.abs(imaginary) + "i";
        }
    }

    // Addition
    public ComplexNumber add(ComplexNumber other) {
        return new ComplexNumber(this.real + other.real, this.imaginary + other.imaginary);
    }

    public ComplexNumber add(double scalar) {
        return new ComplexNumber(this.real + scalar, this.imaginary);
    }

    // Subtraction
    public ComplexNumber subtract(ComplexNumber other) {
        return new ComplexNumber(this.real - other.real, this.imaginary - other.imaginary);
    }

    public ComplexNumber subtract(double scalar) {
        return new ComplexNumber(this.real - scalar, this.imaginary);
    }

    // Multiplication
    public ComplexNumber multiply(ComplexNumber other) {
        // (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        double r = this.real * other.real - this.imaginary * other.imaginary;
        double i = this.real * other.imaginary + this.imaginary * other.real;
        return new ComplexNumber(r, i);
    }

    public ComplexNumber multiply(double scalar) {
        return new ComplexNumber(this.real * scalar, this.imaginary * scalar);
    }

    // Division
    public ComplexNumber divide(ComplexNumber other) {
        // (a + bi) / (c + di) = [(a + bi)(c - di)] / (c² + d²)
        double denominator = other.real * other.real + other.imaginary * other.imaginary;
        if (denominator == 0) {
            throw new ArithmeticException("Division by zero complex number");
        }

        double r = (this.real * other.real + this.imaginary * other.imaginary) / denominator;
        double i = (this.imaginary * other.real - this.real * other.imaginary) / denominator;
        return new ComplexNumber(r, i);
    }

    public ComplexNumber divide(double scalar) {
        if (scalar == 0) {
            throw new ArithmeticException("Division by zero");
        }
        return new ComplexNumber(this.real / scalar, this.imaginary / scalar);
    }

    // Equality
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        ComplexNumber that = (ComplexNumber) obj;
        return Double.compare(that.real, real) == 0 && Double.compare(that.imaginary, imaginary) == 0;
    }

    @Override
    public int hashCode() {
        return Objects.hash(real, imaginary);
    }

    // Conjugate
    public ComplexNumber conjugate() {
        return new ComplexNumber(real, -imaginary);
    }

    // Magnitude
    public double magnitude() {
        return Math.sqrt(real * real + imaginary * imaginary);
    }

    // Phase
    public double phase() {
        return Math.atan2(imaginary, real);
    }

    // To polar form
    public double[] toPolar() {
        return new double[]{magnitude(), phase()};
    }

    // Create from polar coordinates
    public static ComplexNumber fromPolar(double magnitude, double phase) {
        double r = magnitude * Math.cos(phase);
        double i = magnitude * Math.sin(phase);
        return new ComplexNumber(r, i);
    }

    // Static methods for operations (to mimic operator overloading)
    public static ComplexNumber add(ComplexNumber c1, ComplexNumber c2) {
        return c1.add(c2);
    }

    public static ComplexNumber subtract(ComplexNumber c1, ComplexNumber c2) {
        return c1.subtract(c2);
    }

    public static ComplexNumber multiply(ComplexNumber c1, ComplexNumber c2) {
        return c1.multiply(c2);
    }

    public static ComplexNumber divide(ComplexNumber c1, ComplexNumber c2) {
        return c1.divide(c2);
    }

    // Main method to demonstrate the complex number class
    public static void main(String[] args) {
        // Create some complex numbers
        ComplexNumber z1 = new ComplexNumber(3, 4);   // 3 + 4i
        ComplexNumber z2 = new ComplexNumber(1, -2);  // 1 - 2i

        System.out.println("Complex Numbers:");
        System.out.println("z1 = " + z1);
        System.out.println("z2 = " + z2);

        // Basic operations
        System.out.println("\nBasic Operations:");
        System.out.println("z1 + z2 = " + z1.add(z2));
        System.out.println("z1 - z2 = " + z1.subtract(z2));
        System.out.println("z1 * z2 = " + z1.multiply(z2));
        System.out.println("z1 / z2 = " + z1.divide(z2));

        // Properties
        System.out.println("\nProperties:");
        System.out.println("Conjugate of z1 = " + z1.conjugate());
        System.out.println("Magnitude of z1 = " + z1.magnitude());
        System.out.println("Phase of z1 = " + z1.phase() + " radians");

        // Polar form
        double[] polar = z1.toPolar();
        System.out.println("Polar form of z1: magnitude = " + polar[0] + ", phase = " + polar[1] + " radians");

        // Create from polar
        ComplexNumber z3 = ComplexNumber.fromPolar(5, 0.927);  // Should be close to 3 + 4i
        System.out.println("From polar (5, 0.927): " + z3);
    }
}