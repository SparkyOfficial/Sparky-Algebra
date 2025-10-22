# Fast Fourier Transform (FFT) - Kotlin Implementation

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
```kotlin
// Basic FFT
val x = listOf(
    Complex(1.0, 0.0),
    Complex(2.0, 0.0),
    Complex(3.0, 0.0),
    Complex(4.0, 0.0)
)
val X = FFT.computeFFT(x)

// Inverse FFT
val xRecovered = FFT.computeInverseFFT(X)

// Polynomial multiplication
val poly1 = listOf(2.0, 3.0, 1.0)  // 2x² + 3x + 1
val poly2 = listOf(1.0, 2.0, 4.0)  // x² + 2x + 4
val result = FFT.polynomialMultiply(poly1, poly2)
```

## Приклади
Дивіться `FFT.kt` для повного прикладу використання, включаючи:
- Базове обчислення FFT
- Множення поліномів
- Частотний аналіз сигналу

## Примеры
Смотрите `FFT.kt` для полного примера использования, включая:
- Базовое вычисление БПФ
- Умножение полиномов
- Частотный анализ сигнала

## Examples
See `FFT.kt` for a complete usage example, including:
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