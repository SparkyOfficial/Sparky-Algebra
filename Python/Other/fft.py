import cmath
import math

class FFT:
    
    @staticmethod
    def fft(x):
        x = [complex(val) for val in x]
        
        N = len(x)
        
        if N & (N - 1) != 0:
            next_power_of_2 = 1
            while next_power_of_2 < N:
                next_power_of_2 <<= 1
            x.extend([0] * (next_power_of_2 - N))
            N = len(x)
        
        if N <= 1:
            return x
        
        even = FFT.fft(x[0::2])
        odd = FFT.fft(x[1::2])
        
        T = [cmath.exp(-2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]
        return [even[k] + T[k] for k in range(N // 2)] + \
               [even[k] - T[k] for k in range(N // 2)]

    @staticmethod
    def ifft(X):
        N = len(X)
        X_conj = [x.conjugate() for x in X]
        result = FFT.fft(X_conj)
        return [x.conjugate() / N for x in result]

    @staticmethod
    def polynomial_multiply(poly1, poly2):
        n = len(poly1) + len(poly2) - 1
        next_power_of_2 = 1
        while next_power_of_2 < n:
            next_power_of_2 <<= 1
        
        p1 = poly1 + [0] * (next_power_of_2 - len(poly1))
        p2 = poly2 + [0] * (next_power_of_2 - len(poly2))
        
        fft1 = FFT.fft(p1)
        fft2 = FFT.fft(p2)
        
        fft_product = [a * b for a, b in zip(fft1, fft2)]
        
        result = FFT.ifft(fft_product)
        
        return [round(x.real, 10) for x in result[:n]]

def main():
    print("=== Fast Fourier Transform Demo ===\n")
    
    print("Example 1: Computing FFT of [1, 2, 3, 4]")
    x = [1, 2, 3, 4]
    X = FFT.fft(x)
    print(f"Input: {x}")
    print(f"FFT:  {[round(v.real, 5) + round(v.imag, 5)*1j for v in X]}")
    
    x_recovered = FFT.ifft(X)
    print(f"IFFT: {[round(v.real, 5) for v in x_recovered]}\n")
    
    print("Example 2: Polynomial multiplication using FFT")
    print("Multiplying (2x^2 + 3x + 1) and (x^2 + 2x + 4)")
    poly1 = [2, 3, 1]
    poly2 = [1, 2, 4]
    
    result = FFT.polynomial_multiply(poly1, poly2)
    print(f"First polynomial:  {poly1}")
    print(f"Second polynomial: {poly2}")
    print(f"Product:           {result}")
    print("(Should be: 2x^4 + 7x^3 + 15x^2 + 14x + 4 -> [2, 7, 15, 14, 4])\n")
    
    print("Example 3: Frequency analysis of a signal")
    # Simple signal: sum of two sine waves
    samples = 8
    signal = []
    for i in range(samples):
        t = i / samples
        value = math.sin(2 * math.pi * 1 * t) + 0.5 * math.sin(2 * math.pi * 3 * t)
        signal.append(value)
    
    print("Signal samples:")
    for i, s in enumerate(signal):
        print(f"  t[{i}] = {s:.3f}")
    
    spectrum = FFT.fft(signal)
    print("\nFrequency spectrum (magnitudes):")
    for i, freq in enumerate(spectrum):
        magnitude = abs(freq)
        print(f"  F[{i}] = {magnitude:.3f}")

if __name__ == "__main__":
    main()