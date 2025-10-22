# Other Mathematical Implementations (C#)

<div align="center">
  
[![English](https://img.shields.io/badge/English-blue)](#english)
[![Українська](https://img.shields.io/badge/Українська-blue)](#українська)
[![Русский](https://img.shields.io/badge/Русский-blue)](#русский)

</div>

<!-- English -->
<div id="english">

## Description

This directory contains various mathematical implementations in C#, including:

1. A [ComplexNumber](file:///c%3A/Users/%D0%91%D0%BE%D0%B3%D0%B4%D0%B0%D0%BD/Desktop/Sbornik-Algebra-Sparky/C%23/Other/ComplexNumber.cs#L7-L212) class for working with complex numbers
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
```csharp
using System;

class Program {
    static void Main() {
        // Create complex numbers
        ComplexNumber z1 = new ComplexNumber(3, 4);   // 3 + 4i
        ComplexNumber z2 = new ComplexNumber(1, -2);  // 1 - 2i

        // Perform operations
        ComplexNumber result = z1 + z2;
        Console.WriteLine(result);  // Output: 4 + 2i

        // Access properties
        Console.WriteLine(z1.Magnitude());  // Output: 5
    }
}
```

### Fast Fourier Transform
```csharp
using System.Numerics;

// Basic FFT
Complex[] x = { new Complex(1, 0), new Complex(2, 0), new Complex(3, 0), new Complex(4, 0) };
Complex[] X = FFT.ComputeFFT(x);

// Inverse FFT
Complex[] xRecovered = FFT.ComputeInverseFFT(X);

// Polynomial multiplication
double[] poly1 = { 2, 3, 1 };  // 2x² + 3x + 1
double[] poly2 = { 1, 2, 4 };  // x² + 2x + 4
double[] result = FFT.PolynomialMultiply(poly1, poly2);
```

## Author

Andriy Budilnikov (Андрій Будильников)

</div>

<!-- Українська -->
<div id="українська">

## Опис

Ця програма надає клас [ComplexNumber](file:///c%3A/Users/%D0%91%D0%BE%D0%B3%D0%B4%D0%B0%D0%BD/Desktop/Sbornik-Algebra-Sparky/C%23/Other/ComplexNumber.cs#L7-L212) для роботи з комплексними числами в C#. Вона включає всі базові арифметичні операції, властивості, такі як спряжене, модуль та фаза, а також перетворення в/з полярної форми.

## Особливості

- Додавання, віднімання, множення та ділення комплексних чисел
- Обчислення спряженого, модуля та фази
- Перетворення в та з полярної форми
- Перевантаження операторів для інтуїтивного використання

## Використання

```csharp
using System;

class Program {
    static void Main() {
        // Створення комплексних чисел
        ComplexNumber z1 = new ComplexNumber(3, 4);   // 3 + 4i
        ComplexNumber z2 = new ComplexNumber(1, -2);  // 1 - 2i

        // Виконання операцій
        ComplexNumber result = z1 + z2;
        Console.WriteLine(result);  // Вивід: 4 + 2i

        // Доступ до властивостей
        Console.WriteLine(z1.Magnitude());  // Вивід: 5
    }
}
```

## Автор

Андрій Будильников

</div>

<!-- Русский -->
<div id="русский">

## Описание

Эта программа предоставляет класс [ComplexNumber](file:///c%3A/Users/%D0%91%D0%BE%D0%B3%D0%B4%D0%B0%D0%BD/Desktop/Sbornik-Algebra-Sparky/C%23/Other/ComplexNumber.cs#L7-L212) для работы с комплексными числами в C#. Она включает все базовые арифметические операции, свойства, такие как сопряженное, модуль и фаза, а также преобразование в/из полярной формы.

## Особенности

- Сложение, вычитание, умножение и деление комплексных чисел
- Вычисление сопряженного, модуля и фазы
- Преобразование в и из полярной формы
- Перегрузка операторов для интуитивного использования

## Использование

```csharp
using System;

class Program {
    static void Main() {
        // Создание комплексных чисел
        ComplexNumber z1 = new ComplexNumber(3, 4);   // 3 + 4i
        ComplexNumber z2 = new ComplexNumber(1, -2);  // 1 - 2i

        // Выполнение операций
        ComplexNumber result = z1 + z2;
        Console.WriteLine(result);  // Вывод: 4 + 2i

        // Доступ к свойствам
        Console.WriteLine(z1.Magnitude());  // Вывод: 5
    }
}
```

## Автор

Андрій Будильников

</div>