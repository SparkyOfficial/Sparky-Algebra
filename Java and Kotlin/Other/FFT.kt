

import kotlin.math.*

data class Complex(val real: Double, val imaginary: Double) {
    operator fun plus(other: Complex): Complex {
        return Complex(this.real + other.real, this.imaginary + other.imaginary)
    }
    
    operator fun minus(other: Complex): Complex {
        return Complex(this.real - other.real, this.imaginary - other.imaginary)
    }
    
    operator fun times(other: Complex): Complex {
        val r = this.real * other.real - this.imaginary * other.imaginary
        val i = this.real * other.imaginary + this.imaginary * other.real
        return Complex(r, i)
    }
    
    operator fun div(scalar: Double): Complex {
        return Complex(this.real / scalar, this.imaginary / scalar)
    }
    
    fun conjugate(): Complex {
        return Complex(real, -imaginary)
    }
    
    fun magnitude(): Double {
        return sqrt(real * real + imaginary * imaginary)
    }
    
    override fun toString(): String {
        return if (imaginary >= 0) {
            "%.5f+%.5fi".format(real, imaginary)
        } else {
            "%.5f%.5fi".format(real, imaginary)
        }
    }
    
    companion object {
        fun exp(exponent: Complex): Complex {
            if (exponent.real != 0.0) {
                throw IllegalArgumentException("This exp implementation only works for purely imaginary exponents")
            }
            val theta = exponent.imaginary
            return Complex(cos(theta), sin(theta))
        }
        
        val ZERO = Complex(0.0, 0.0)
        val ONE = Complex(1.0, 0.0)
    }
}

class FFT {
    companion object {
        fun computeFFT(x: List<Complex>): List<Complex> {
            var x = x.toMutableList()
            var N = x.size
            
            if ((N and (N - 1)) != 0) {
                var nextPowerOf2 = 1
                while (nextPowerOf2 < N)
                    nextPowerOf2 = nextPowerOf2 shl 1
                while (x.size < nextPowerOf2) {
                    x.add(Complex.ZERO)
                }
                N = x.size
            }
            
            if (N <= 1)
                return x
            
            val even = mutableListOf<Complex>()
            val odd = mutableListOf<Complex>()
            
            for (i in 0 until N / 2) {
                even.add(x[2 * i])
                odd.add(x[2 * i + 1])
            }
            
            val fftEven = computeFFT(even)
            val fftOdd = computeFFT(odd)
            
            val result = MutableList(N) { Complex.ZERO }
            for (k in 0 until N / 2) {
                val t = Complex.exp(Complex(0.0, -2 * PI * k / N)) * fftOdd[k]
                result[k] = fftEven[k] + t
                result[k + N / 2] = fftEven[k] - t
            }
            
            return result
        }
        
        fun computeInverseFFT(X: List<Complex>): List<Complex> {
            val N = X.size
            val XConj = X.map { it.conjugate() }
            
            val result = computeFFT(XConj)
            
            return result.map { it.conjugate() / N.toDouble() }
        }
        
        fun polynomialMultiply(poly1: List<Double>, poly2: List<Double>): List<Double> {
            var n = poly1.size + poly2.size - 1
            var nextPowerOf2 = 1
            while (nextPowerOf2 < n)
                nextPowerOf2 = nextPowerOf2 shl 1
            
            val p1 = poly1.toMutableList().apply { while (size < nextPowerOf2) add(0.0) }
            val p2 = poly2.toMutableList().apply { while (size < nextPowerOf2) add(0.0) }
            
            val cp1 = p1.map { Complex(it, 0.0) }
            val cp2 = p2.map { Complex(it, 0.0) }
            
            val fft1 = computeFFT(cp1)
            val fft2 = computeFFT(cp2)
            
            val fftProduct = fft1.zip(fft2) { a, b -> a * b }
            
            val result = computeInverseFFT(fftProduct)
            
            return result.take(n).map { round(it.real * 1e10) / 1e10 }
        }
        

        @JvmStatic
        fun main(args: Array<String>) {
            println("=== Fast Fourier Transform Demo ===\n")
            
            println("Example 1: Computing FFT of [1, 2, 3, 4]")
            val x = listOf(
                Complex(1.0, 0.0),
                Complex(2.0, 0.0),
                Complex(3.0, 0.0),
                Complex(4.0, 0.0)
            )
            val X = computeFFT(x)
            println("Input: [1, 2, 3, 4]")
            print("FFT:  [")
            X.forEachIndexed { i, value ->
                if (i > 0) print(", ")
                print(value)
            }
            println("]")
            
            val xRecovered = computeInverseFFT(X)
            print("IFFT: [")
            xRecovered.forEachIndexed { i, value ->
                if (i > 0) print(", ")
                print("%.5f".format(value.real))
            }
            println("]\n")
            
            println("Example 2: Polynomial multiplication using FFT")
            println("Multiplying (2x^2 + 3x + 1) and (x^2 + 2x + 4)")
            val poly1 = listOf(2.0, 3.0, 1.0)
            val poly2 = listOf(1.0, 2.0, 4.0)
            
            val result = polynomialMultiply(poly1, poly2)
            println("First polynomial:  $poly1")
            println("Second polynomial: $poly2")
            println("Product:           $result")
            println("(Should be: 2x^4 + 7x^3 + 15x^2 + 14x + 4 -> [2.0, 7.0, 15.0, 14.0, 4.0])\n")
            
            println("Example 3: Frequency analysis of a signal")
            val samples = 8
            val signal = MutableList(samples) { i ->
                val t = i.toDouble() / samples
                val value = sin(2 * PI * 1 * t) + 0.5 * sin(2 * PI * 3 * t)
                Complex(value, 0.0).also {
                    println("  t[$i] = %.3f".format(value))
                }
            }
            
            val spectrum = computeFFT(signal)
            println("\nFrequency spectrum (magnitudes):")
            spectrum.forEachIndexed { i, freq ->
                val magnitude = freq.magnitude()
                println("  F[$i] = %.3f".format(magnitude))
            }
        }
    }
}