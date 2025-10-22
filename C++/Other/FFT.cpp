#include <iostream>
#include <vector>
#include <complex>
#include <cmath>
#include <algorithm>
#include <iomanip>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

class FFT {
public:
    static std::vector<std::complex<double>> computeFFT(std::vector<std::complex<double>> x) {
        size_t N = x.size();
        
        if ((N & (N - 1)) != 0) {
            size_t nextPowerOf2 = 1;
            while (nextPowerOf2 < N)
                nextPowerOf2 <<= 1;
            x.resize(nextPowerOf2, std::complex<double>(0, 0));
            N = x.size();
        }
        
        if (N <= 1)
            return x;
        
        std::vector<std::complex<double>> even(N/2);
        std::vector<std::complex<double>> odd(N/2);
        
        for (size_t i = 0; i < N/2; i++) {
            even[i] = x[2*i];
            odd[i] = x[2*i + 1];
        }
        
        std::vector<std::complex<double>> fftEven = computeFFT(even);
        std::vector<std::complex<double>> fftOdd = computeFFT(odd);
        
        std::vector<std::complex<double>> result(N);
        for (size_t k = 0; k < N/2; k++) {
            std::complex<double> t = std::exp(std::complex<double>(0, -2 * M_PI * k / N)) * fftOdd[k];
            result[k] = fftEven[k] + t;
            result[k + N/2] = fftEven[k] - t;
        }
        
        return result;
    }
    
    static std::vector<std::complex<double>> computeInverseFFT(std::vector<std::complex<double>> X) {
        size_t N = X.size();        
        std::vector<std::complex<double>> XConj(N);
        for (size_t i = 0; i < N; i++) {
            XConj[i] = std::conj(X[i]);
        }
        
        std::vector<std::complex<double>> result = computeFFT(XConj);
        
        std::vector<std::complex<double>> normalized(N);
        for (size_t i = 0; i < N; i++) {
            normalized[i] = std::conj(result[i]) / static_cast<double>(N);
        }
        
        return normalized;
    }
    
    static std::vector<double> polynomialMultiply(const std::vector<double>& poly1, 
                                                 const std::vector<double>& poly2) {
        size_t n = poly1.size() + poly2.size() - 1;
        size_t nextPowerOf2 = 1;
        while (nextPowerOf2 < n)
            nextPowerOf2 <<= 1;
        
        std::vector<double> p1 = poly1;
        std::vector<double> p2 = poly2;
        p1.resize(nextPowerOf2, 0);
        p2.resize(nextPowerOf2, 0);
        
        std::vector<std::complex<double>> cp1(nextPowerOf2);
        std::vector<std::complex<double>> cp2(nextPowerOf2);
        for (size_t i = 0; i < nextPowerOf2; i++) {
            cp1[i] = std::complex<double>(p1[i], 0);
            cp2[i] = std::complex<double>(p2[i], 0);
        }
        
        std::vector<std::complex<double>> fft1 = computeFFT(cp1);
        std::vector<std::complex<double>> fft2 = computeFFT(cp2);
        
        std::vector<std::complex<double>> fftProduct(nextPowerOf2);
        for (size_t i = 0; i < nextPowerOf2; i++) {
            fftProduct[i] = fft1[i] * fft2[i];
        }
        
        std::vector<std::complex<double>> result = computeInverseFFT(fftProduct);
        
        std::vector<double> realResult(n);
        for (size_t i = 0; i < n; i++) {
            realResult[i] = std::round(result[i].real() * 1e10) / 1e10;
        }
        
        return realResult;
    }
    
    static void main() {
        std::cout << "=== Fast Fourier Transform Demo ===\n" << std::endl;
        
        std::cout << "Example 1: Computing FFT of [1, 2, 3, 4]" << std::endl;
        std::vector<std::complex<double>> x = { 
            std::complex<double>(1, 0), 
            std::complex<double>(2, 0), 
            std::complex<double>(3, 0), 
            std::complex<double>(4, 0) 
        };
        std::vector<std::complex<double>> X = computeFFT(x);
        std::cout << "Input: [1, 2, 3, 4]" << std::endl;
        std::cout << "FFT:  [";
        for (size_t i = 0; i < X.size(); i++) {
            if (i > 0) std::cout << ", ";
            std::cout << std::fixed << std::setprecision(5) << X[i].real() 
                      << (X[i].imag() >= 0 ? "+" : "") << X[i].imag() << "i";
        }
        std::cout << "]" << std::endl;
        
        std::vector<std::complex<double>> xRecovered = computeInverseFFT(X);
        std::cout << "IFFT: [";
        for (size_t i = 0; i < xRecovered.size(); i++) {
            if (i > 0) std::cout << ", ";
            std::cout << std::fixed << std::setprecision(5) << xRecovered[i].real();
        }
        std::cout << "]\n" << std::endl;
        
        std::cout << "Example 2: Polynomial multiplication using FFT" << std::endl;
        std::cout << "Multiplying (2x^2 + 3x + 1) and (x^2 + 2x + 4)" << std::endl;
        std::vector<double> poly1 = { 2, 3, 1 };
        std::vector<double> poly2 = { 1, 2, 4 };
        
        std::vector<double> result = polynomialMultiply(poly1, poly2);
        std::cout << "First polynomial:  [";
        for (size_t i = 0; i < poly1.size(); i++) {
            if (i > 0) std::cout << ", ";
            std::cout << poly1[i];
        }
        std::cout << "]" << std::endl;
        
        std::cout << "Second polynomial: [";
        for (size_t i = 0; i < poly2.size(); i++) {
            if (i > 0) std::cout << ", ";
            std::cout << poly2[i];
        }
        std::cout << "]" << std::endl;
        
        std::cout << "Product:           [";
        for (size_t i = 0; i < result.size(); i++) {
            if (i > 0) std::cout << ", ";
            std::cout << result[i];
        }
        std::cout << "]" << std::endl;
        std::cout << "(Should be: 2x^4 + 7x^3 + 15x^2 + 14x + 4 -> [2, 7, 15, 14, 4])\n" << std::endl;
        
        std::cout << "Example 3: Frequency analysis of a signal" << std::endl;
        size_t samples = 8;
        std::vector<std::complex<double>> signal(samples);
        for (size_t i = 0; i < samples; i++) {
            double t = static_cast<double>(i) / samples;
            double value = sin(2 * M_PI * 1 * t) + 0.5 * sin(2 * M_PI * 3 * t);
            signal[i] = std::complex<double>(value, 0);
            std::cout << "  t[" << i << "] = " << std::fixed << std::setprecision(3) << value << std::endl;
        }
        
        std::vector<std::complex<double>> spectrum = computeFFT(signal);
        std::cout << "\nFrequency spectrum (magnitudes):" << std::endl;
        for (size_t i = 0; i < spectrum.size(); i++) {
            double magnitude = std::abs(spectrum[i]);
            std::cout << "  F[" << i << "] = " << std::fixed << std::setprecision(3) << magnitude << std::endl;
        }
    }
};

int main() {
    FFT::main();
    return 0;
}