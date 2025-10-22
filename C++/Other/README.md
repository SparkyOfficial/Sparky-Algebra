# Other Mathematical Implementations (C++)

<div align="center">
  
[![English](https://img.shields.io/badge/English-blue)](#english)
[![Українська](https://img.shields.io/badge/Українська-blue)](#українська)
[![Русский](https://img.shields.io/badge/Русский-blue)](#русский)

</div>

<!-- English -->
<div id="english">

## Description

This directory contains various mathematical implementations in C++, including:

1. A [ComplexNumber](file:///c%3A/Users/%D0%91%D0%BE%D0%B3%D0%B4%D0%B0%D0%BD/Desktop/Sbornik-Algebra-Sparky/C%2B%2B/Other/ComplexNumber.cpp#L9-L175) class for working with complex numbers
2. Fast Fourier Transform (FFT) implementation for efficient signal processing and polynomial multiplication

## Features

### Complex Numbers
- Addition, subtraction, multiplication, and division of complex numbers
- Conjugate, magnitude, and phase calculations
- Conversion to and from polar form
- Operator overloading for intuitive usage

### Fast Fourier Transform
- FFT computation for sequences of complex numbers
- Inverse FFT for signal reconstruction
- Polynomial multiplication using FFT
- Automatic zero-padding for non-power-of-2 input sizes

## Usage

### Complex Numbers
```cpp
#include "ComplexNumber.cpp"

int main() {
    // Create complex numbers
    ComplexNumber z1(3, 4);   // 3 + 4i
    ComplexNumber z2(1, -2);  // 1 - 2i

    // Perform operations
    ComplexNumber result = z1 + z2;
    std::cout << result << std::endl;  // Output: 4 + 2i

    // Access properties
    std::cout << z1.magnitude() << std::endl;  // Output: 5

    return 0;
}
```

### Fast Fourier Transform
```cpp
#include <vector>
#include <complex>

// Basic FFT
std::vector<std::complex<double>> x = { 
    std::complex<double>(1, 0), 
    std::complex<double>(2, 0), 
    std::complex<double>(3, 0), 
    std::complex<double>(4, 0) 
};
std::vector<std::complex<double>> X = FFT::computeFFT(x);

// Inverse FFT
std::vector<std::complex<double>> xRecovered = FFT::computeInverseFFT(X);

// Polynomial multiplication
std::vector<double> poly1 = { 2, 3, 1 };  // 2x² + 3x + 1
std::vector<double> poly2 = { 1, 2, 4 };  // x² + 2x + 4
std::vector<double> result = FFT::polynomialMultiply(poly1, poly2);
```

## Author

Andriy Budilnikov (Андрій Будильников)

</div>

<!-- Українська -->
<div id="українська">

## Опис

Ця програма надає клас [ComplexNumber](file:///c%3A/Users/%D0%91%D0%BE%D0%B3%D0%B4%D0%B0%D0%BD/Desktop/Sbornik-Algebra-Sparky/C%2B%2B/Other/ComplexNumber.cpp#L9-L175) для роботи з комплексними числами в C++. Вона включає всі базові арифметичні операції, властивості, такі як спряжене, модуль та фаза, а також перетворення в/з полярної форми.

## Особливості

- Додавання, віднімання, множення та ділення комплексних чисел
- Обчислення спряженого, модуля та фази
- Перетворення в та з полярної форми
- Перевантаження операторів для інтуїтивного використання

## Використання

```cpp
#include "ComplexNumber.cpp"

int main() {
    // Створення комплексних чисел
    ComplexNumber z1(3, 4);   // 3 + 4i
    ComplexNumber z2(1, -2);  // 1 - 2i

    // Виконання операцій
    ComplexNumber result = z1 + z2;
    std::cout << result << std::endl;  // Вивід: 4 + 2i

    // Доступ до властивостей
    std::cout << z1.magnitude() << std::endl;  // Вивід: 5

    return 0;
}
```

## Автор

Андрій Будильников

</div>

<!-- Русский -->
<div id="русский">

## Описание

Эта программа предоставляет класс [ComplexNumber](file:///c%3A/Users/%D0%91%D0%BE%D0%B3%D0%B4%D0%B0%D0%BD/Desktop/Sbornik-Algebra-Sparky/C%2B%2B/Other/ComplexNumber.cpp#L9-L175) для работы с комплексными числами в C++. Она включает все базовые арифметические операции, свойства, такие как сопряженное, модуль и фаза, а также преобразование в/из полярной формы.

## Особенности

- Сложение, вычитание, умножение и деление комплексных чисел
- Вычисление сопряженного, модуля и фазы
- Преобразование в и из полярной формы
- Перегрузка операторов для интуитивного использования

## Использование

```cpp
#include "ComplexNumber.cpp"

int main() {
    // Создание комплексных чисел
    ComplexNumber z1(3, 4);   // 3 + 4i
    ComplexNumber z2(1, -2);  // 1 - 2i

    // Выполнение операций
    ComplexNumber result = z1 + z2;
    std::cout << result << std::endl;  // Вывод: 4 + 2i

    // Доступ к свойствам
    std::cout << z1.magnitude() << std::endl;  // Вывод: 5

    return 0;
}
```

## Автор

Андрій Будильников

</div>