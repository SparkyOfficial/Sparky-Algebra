using System;
using System.Collections.Generic;
using System.Numerics;

public class FFT
{
    public static Complex[] ComputeFFT(Complex[] x)
    {
        int N = x.Length;

        if ((N & (N - 1)) != 0)
        {
            int nextPowerOf2 = 1;
            while (nextPowerOf2 < N)
                nextPowerOf2 <<= 1;
            Array.Resize(ref x, nextPowerOf2);
            N = x.Length;
        }

        if (N <= 1)
            return x;

        Complex[] even = new Complex[N / 2];
        Complex[] odd = new Complex[N / 2];
        
        for (int i = 0; i < N / 2; i++)
        {
            even[i] = x[2 * i];
            odd[i] = x[2 * i + 1];
        }

        Complex[] fftEven = ComputeFFT(even);
        Complex[] fftOdd = ComputeFFT(odd);

        Complex[] result = new Complex[N];
        for (int k = 0; k < N / 2; k++)
        {
            Complex t = Complex.Exp(new Complex(0, -2 * Math.PI * k / N)) * fftOdd[k];
            result[k] = fftEven[k] + t;
            result[k + N / 2] = fftEven[k] - t;
        }

        return result;
    }

    public static Complex[] ComputeInverseFFT(Complex[] X)
    {
        int N = X.Length;
        Complex[] XConj = new Complex[N];
        for (int i = 0; i < N; i++)
        {
            XConj[i] = Complex.Conjugate(X[i]);
        }
        
        Complex[] result = ComputeFFT(XConj);
        
        Complex[] normalized = new Complex[N];
        for (int i = 0; i < N; i++)
        {
            normalized[i] = Complex.Conjugate(result[i]) / N;
        }
        
        return normalized;
    }

    public static double[] PolynomialMultiply(double[] poly1, double[] poly2)
    {
        int n = poly1.Length + poly2.Length - 1;
        int nextPowerOf2 = 1;
        while (nextPowerOf2 < n)
            nextPowerOf2 <<= 1;

        double[] p1 = new double[nextPowerOf2];
        double[] p2 = new double[nextPowerOf2];
        Array.Copy(poly1, p1, poly1.Length);
        Array.Copy(poly2, p2, poly2.Length);

        Complex[] cp1 = new Complex[nextPowerOf2];
        Complex[] cp2 = new Complex[nextPowerOf2];
        for (int i = 0; i < nextPowerOf2; i++)
        {
            cp1[i] = new Complex(p1[i], 0);
            cp2[i] = new Complex(p2[i], 0);
        }

        Complex[] fft1 = ComputeFFT(cp1);
        Complex[] fft2 = ComputeFFT(cp2);

        Complex[] fftProduct = new Complex[nextPowerOf2];
        for (int i = 0; i < nextPowerOf2; i++)
        {
            fftProduct[i] = fft1[i] * fft2[i];
        }

        Complex[] result = ComputeInverseFFT(fftProduct);

        double[] realResult = new double[n];
        for (int i = 0; i < n; i++)
        {
            realResult[i] = Math.Round(result[i].Real, 10);
        }

        return realResult;
    }

    public static void Main(string[] args)
    {
        Console.WriteLine("=== Fast Fourier Transform Demo ===\n");

        Console.WriteLine("Example 1: Computing FFT of [1, 2, 3, 4]");
        Complex[] x = { new Complex(1, 0), new Complex(2, 0), new Complex(3, 0), new Complex(4, 0) };
        Complex[] X = ComputeFFT(x);
        Console.WriteLine($"Input: [1, 2, 3, 4]");
        Console.Write("FFT:  [");
        for (int i = 0; i < X.Length; i++)
        {
            if (i > 0) Console.Write(", ");
            Console.Write($"{Math.Round(X[i].Real, 5)}+{Math.Round(X[i].Imaginary, 5)}i");
        }
        Console.WriteLine("]");

        Complex[] xRecovered = ComputeInverseFFT(X);
        Console.Write("IFFT: [");
        for (int i = 0; i < xRecovered.Length; i++)
        {
            if (i > 0) Console.Write(", ");
            Console.Write($"{Math.Round(xRecovered[i].Real, 5)}");
        }
        Console.WriteLine("]\n");

        Console.WriteLine("Example 2: Polynomial multiplication using FFT");
        Console.WriteLine("Multiplying (2x^2 + 3x + 1) and (x^2 + 2x + 4)");
        double[] poly1 = { 2, 3, 1 };
        double[] poly2 = { 1, 2, 4 };

        double[] result = PolynomialMultiply(poly1, poly2);
        Console.WriteLine($"First polynomial:  [{string.Join(", ", poly1)}]");
        Console.WriteLine($"Second polynomial: [{string.Join(", ", poly2)}]");
        Console.WriteLine($"Product:           [{string.Join(", ", result)}]");
        Console.WriteLine("(Should be: 2x^4 + 7x^3 + 15x^2 + 14x + 4 -> [2, 7, 15, 14, 4])\n");

        Console.WriteLine("Example 3: Frequency analysis of a signal");
        int samples = 8;
        Complex[] signal = new Complex[samples];
        for (int i = 0; i < samples; i++)
        {
            double t = (double)i / samples;
            signal[i] = new Complex(
                Math.Sin(2 * Math.PI * 1 * t) + 0.5 * Math.Sin(2 * Math.PI * 3 * t),
                0
            );
            Console.WriteLine($"  t[{i}] = {Math.Round(signal[i].Real, 3)}");
        }

        Complex[] spectrum = ComputeFFT(signal);
        Console.WriteLine("\nFrequency spectrum (magnitudes):");
        for (int i = 0; i < spectrum.Length; i++)
        {
            double magnitude = Complex.Abs(spectrum[i]);
            Console.WriteLine($"  F[{i}] = {Math.Round(magnitude, 3)}");
        }
    }
}