import java.util.Arrays;

public class FFT {
    
    static class Complex {
        private final double real;
        private final double imaginary;
        
        public Complex(double real, double imaginary) {
            this.real = real;
            this.imaginary = imaginary;
        }
        
        public double getReal() {
            return real;
        }
        
        public double getImaginary() {
            return imaginary;
        }
        
        public Complex add(Complex other) {
            return new Complex(this.real + other.real, this.imaginary + other.imaginary);
        }
        
        public Complex subtract(Complex other) {
            return new Complex(this.real - other.real, this.imaginary - other.imaginary);
        }
        
        public Complex multiply(Complex other) {
            double r = this.real * other.real - this.imaginary * other.imaginary;
            double i = this.real * other.imaginary + this.imaginary * other.real;
            return new Complex(r, i);
        }
        
        public Complex divide(Complex other) {
            double denominator = other.real * other.real + other.imaginary * other.imaginary;
            if (denominator == 0) {
                throw new ArithmeticException("Division by zero complex number");
            }
            
            double r = (this.real * other.real + this.imaginary * other.imaginary) / denominator;
            double i = (this.imaginary * other.real - this.real * other.imaginary) / denominator;
            return new Complex(r, i);
        }
        
        public Complex conjugate() {
            return new Complex(real, -imaginary);
        }
        
        public double magnitude() {
            return Math.sqrt(real * real + imaginary * imaginary);
        }
        
        public static Complex exp(Complex exponent) {
            if (exponent.real != 0) {
                throw new IllegalArgumentException("This exp implementation only works for purely imaginary exponents");
            }
            double theta = exponent.imaginary;
            return new Complex(Math.cos(theta), Math.sin(theta));
        }
        
        @Override
        public String toString() {
            if (imaginary >= 0) {
                return String.format("%.5f+%.5fi", real, imaginary);
            } else {
                return String.format("%.5f%.5fi", real, imaginary);
            }
        }
    }
    
    public static Complex[] computeFFT(Complex[] x) {
        int N = x.length;
        
        if ((N & (N - 1)) != 0) {
            int nextPowerOf2 = 1;
            while (nextPowerOf2 < N)
                nextPowerOf2 <<= 1;
            x = Arrays.copyOf(x, nextPowerOf2);
            N = x.length;
        }
        
        if (N <= 1)
            return x;
        
        Complex[] even = new Complex[N / 2];
        Complex[] odd = new Complex[N / 2];
        
        for (int i = 0; i < N / 2; i++) {
            even[i] = x[2 * i];
            odd[i] = x[2 * i + 1];
        }
        
        Complex[] fftEven = computeFFT(even);
        Complex[] fftOdd = computeFFT(odd);
        
        Complex[] result = new Complex[N];
        for (int k = 0; k < N / 2; k++) {
            Complex t = Complex.exp(new Complex(0, -2 * Math.PI * k / N)).multiply(fftOdd[k]);
            result[k] = fftEven[k].add(t);
            result[k + N / 2] = fftEven[k].subtract(t);
        }
        
        return result;
    }
    
    public static Complex[] computeInverseFFT(Complex[] X) {
        int N = X.length;
        Complex[] XConj = new Complex[N];
        for (int i = 0; i < N; i++) {
            XConj[i] = X[i].conjugate();
        }
        
        Complex[] result = computeFFT(XConj);
        
        Complex[] normalized = new Complex[N];
        for (int i = 0; i < N; i++) {
            normalized[i] = result[i].conjugate().divide(new Complex(N, 0));
        }
        
        return normalized;
    }
    
    public static double[] polynomialMultiply(double[] poly1, double[] poly2) {
        int n = poly1.length + poly2.length - 1;
        int nextPowerOf2 = 1;
        while (nextPowerOf2 < n)
            nextPowerOf2 <<= 1;
        
        double[] p1 = Arrays.copyOf(poly1, nextPowerOf2);
        double[] p2 = Arrays.copyOf(poly2, nextPowerOf2);
        
        Complex[] cp1 = new Complex[nextPowerOf2];
        Complex[] cp2 = new Complex[nextPowerOf2];
        for (int i = 0; i < nextPowerOf2; i++) {
            cp1[i] = new Complex(p1[i], 0);
            cp2[i] = new Complex(p2[i], 0);
        }
        
        Complex[] fft1 = computeFFT(cp1);
        Complex[] fft2 = computeFFT(cp2);
        
        Complex[] fftProduct = new Complex[nextPowerOf2];
        for (int i = 0; i < nextPowerOf2; i++) {
            fftProduct[i] = fft1[i].multiply(fft2[i]);
        }
        
        Complex[] result = computeInverseFFT(fftProduct);
        
        double[] realResult = new double[n];
        for (int i = 0; i < n; i++) {
            realResult[i] = Math.round(result[i].getReal() * 1e10) / 1e10;
        }
        
        return realResult;
    }
    
    public static void main(String[] args) {
        System.out.println("=== Fast Fourier Transform Demo ===\n");
        
        System.out.println("Example 1: Computing FFT of [1, 2, 3, 4]");
        Complex[] x = { 
            new Complex(1, 0), 
            new Complex(2, 0), 
            new Complex(3, 0), 
            new Complex(4, 0) 
        };
        Complex[] X = computeFFT(x);
        System.out.println("Input: [1, 2, 3, 4]");
        System.out.print("FFT:  [");
        for (int i = 0; i < X.length; i++) {
            if (i > 0) System.out.print(", ");
            System.out.print(X[i]);
        }
        System.out.println("]");
        
        Complex[] xRecovered = computeInverseFFT(X);
        System.out.print("IFFT: [");
        for (int i = 0; i < xRecovered.length; i++) {
            if (i > 0) System.out.print(", ");
            System.out.printf("%.5f", xRecovered[i].getReal());
        }
        System.out.println("]\n");
        
        System.out.println("Example 2: Polynomial multiplication using FFT");
        System.out.println("Multiplying (2x^2 + 3x + 1) and (x^2 + 2x + 4)");
        double[] poly1 = { 2, 3, 1 };
        double[] poly2 = { 1, 2, 4 };
        
        double[] result = polynomialMultiply(poly1, poly2);
        System.out.println("First polynomial:  " + Arrays.toString(poly1));
        System.out.println("Second polynomial: " + Arrays.toString(poly2));
        System.out.println("Product:           " + Arrays.toString(result));
        System.out.println("(Should be: 2x^4 + 7x^3 + 15x^2 + 14x + 4 -> [2, 7, 15, 14, 4])\n");
        
        System.out.println("Example 3: Frequency analysis of a signal");
        int samples = 8;
        Complex[] signal = new Complex[samples];
        for (int i = 0; i < samples; i++) {
            double t = (double)i / samples;
            double value = Math.sin(2 * Math.PI * 1 * t) + 0.5 * Math.sin(2 * Math.PI * 3 * t);
            signal[i] = new Complex(value, 0);
            System.out.printf("  t[%d] = %.3f\n", i, value);
        }
        
        Complex[] spectrum = computeFFT(signal);
        System.out.println("\nFrequency spectrum (magnitudes):");
        for (int i = 0; i < spectrum.length; i++) {
            double magnitude = spectrum[i].magnitude();
            System.out.printf("  F[%d] = %.3f\n", i, magnitude);
        }
    }
}