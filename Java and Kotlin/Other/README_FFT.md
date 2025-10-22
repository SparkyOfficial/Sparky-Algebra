# Fast Fourier Transform (FFT) - Java Implementation

## Опис
Ця реалізація забезпечує алгоритм швидкого перетворення Фур'є (ШПФ) для ефективного обчислення дискретного перетворення Фур'є (ДПФ). Алгоритм Коулі-Тьюкі використовується для досягнення складності O(n log n) замість O(n²) наївного підходу.

## Описание
Эта реализация обеспечивает алгоритм быстрого преобразования Фурье (БПФ) для эффективного вычисления дискретного преобразования Фурье (ДПФ). Алгоритм Кули-Туки используется для достижения сложности O(n log n) вместо O(n²) наивного подхода.

## Description
This implementation provides the Fast Fourier Transform algorithm for efficiently computing the Discrete Fourier Transform (DFT). The Cooley-Tukey algorithm is used to achieve O(n log n) complexity instead of O(n²) naive approach.

## Основні можливості
- Обчислення FFT для послідовностей комплексних чисел
- Зворотне FFT для відновлення оригінального сигналу
- Множення поліномів з використанням FFT
- Автоматичне доповнення нулями для вхідних даних не степеня 2

## Основные возможности
- Вычисление БПФ для последовательностей комплексных чисел
- Обратное БПФ для восстановления исходного сигнала
- Умножение полиномов с использованием БПФ
- Автоматическое дополнение нулями для входных данных не степени 2

## Key Features
- FFT computation for sequences of complex numbers
- Inverse FFT for signal reconstruction
- Polynomial multiplication using FFT
- Automatic zero-padding for non-power-of-2 input sizes

## Використання
```java
// Basic FFT
FFT.Complex[] x = { 
    new FFT.Complex(1, 0), 
    new FFT.Complex(2, 0), 
    new FFT.Complex(3, 0), 
    new FFT.Complex(4, 0) 
};
FFT.Complex[] X = FFT.computeFFT(x);

// Inverse FFT
FFT.Complex[] xRecovered = FFT.computeInverseFFT(X);

// Polynomial multiplication
double[] poly1 = { 2, 3, 1 };  // 2x² + 3x + 1
double[] poly2 = { 1, 2, 4 };  // x² + 2x + 4
double[] result = FFT.polynomialMultiply(poly1, poly2);
```

## Приклади
Дивіться `FFT.java` для повного прикладу використання, включаючи:
- Базове обчислення FFT
- Множення поліномів
- Частотний аналіз сигналу

## Примеры
Смотрите `FFT.java` для полного примера использования, включая:
- Базовое вычисление БПФ
- Умножение полиномов
- Частотный анализ сигнала

## Examples
See `FFT.java` for a complete usage example, including:
- Basic FFT computation
- Polynomial multiplication
- Signal frequency analysis

## Складність
- Час: O(n log n)
- Пам'ять: O(n)

## Сложность
- Время: O(n log n)
- Память: O(n)

## Complexity
- Time: O(n log n)
- Memory: O(n)