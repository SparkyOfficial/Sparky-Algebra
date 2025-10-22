# Other Mathematical Implementations (Python)

<div align="center">
  
[![English](https://img.shields.io/badge/English-blue)](#english)
[![Українська](https://img.shields.io/badge/Українська-blue)](#українська)
[![Русский](https://img.shields.io/badge/Русский-blue)](#русский)

</div>

<!-- English -->
<div id="english">

## Description

This directory contains various mathematical implementations in Python, including:

1. A [ComplexNumber](file:///c%3A/Users/%D0%91%D0%BE%D0%B3%D0%B4%D0%B0%D0%BD/Desktop/Sbornik-Algebra-Sparky/Python/Other/complex_number.py#L7-L186) class for working with complex numbers
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
```python
from complex_number import ComplexNumber

# Create complex numbers
z1 = ComplexNumber(3, 4)   # 3 + 4i
z2 = ComplexNumber(1, -2)  # 1 - 2i

# Perform operations
result = z1 + z2
print(result)  # Output: 4 + 2i

# Access properties
print(z1.magnitude())  # Output: 5.0
```

### Fast Fourier Transform
```python
from fft import FFT

# Basic FFT
x = [1, 2, 3, 4]
X = FFT.fft(x)

# Inverse FFT
x_recovered = FFT.ifft(X)

# Polynomial multiplication
poly1 = [2, 3, 1]  # 2x² + 3x + 1
poly2 = [1, 2, 4]  # x² + 2x + 4
result = FFT.polynomial_multiply(poly1, poly2)
```

## Author

Andriy Budilnikov (Андрій Будильников)

</div>

<!-- Українська -->
<div id="українська">

## Опис

Цей модуль надає клас [ComplexNumber](file:///c%3A/Users/%D0%91%D0%BE%D0%B3%D0%B4%D0%B0%D0%BD/Desktop/Sbornik-Algebra-Sparky/Python/Other/complex_number.py#L7-L186) для роботи з комплексними числами в Python. Він включає всі базові арифметичні операції, властивості, такі як спряжене, модуль та фаза, а також перетворення в/з полярної форми.

## Особливості

- Додавання, віднімання, множення та ділення комплексних чисел
- Обчислення спряженого, модуля та фази
- Перетворення в та з полярної форми
- Перевантаження операторів для інтуїтивного використання

## Використання

```python
from complex_number import ComplexNumber

# Створення комплексних чисел
z1 = ComplexNumber(3, 4)   # 3 + 4i
z2 = ComplexNumber(1, -2)  # 1 - 2i

# Виконання операцій
result = z1 + z2
print(result)  # Вивід: 4 + 2i

# Доступ до властивостей
print(z1.magnitude())  # Вивід: 5.0
```

## Автор

Андрій Будильников

</div>

<!-- Русский -->
<div id="русский">

## Описание

Этот модуль предоставляет класс [ComplexNumber](file:///c%3A/Users/%D0%91%D0%BE%D0%B3%D0%B4%D0%B0%D0%BD/Desktop/Sbornik-Algebra-Sparky/Python/Other/complex_number.py#L7-L186) для работы с комплексными числами в Python. Он включает все базовые арифметические операции, свойства, такие как сопряженное, модуль и фаза, а также преобразование в/из полярной формы.

## Особенности

- Сложение, вычитание, умножение и деление комплексных чисел
- Вычисление сопряженного, модуля и фазы
- Преобразование в и из полярной формы
- Перегрузка операторов для интуитивного использования

## Использование

```python
from complex_number import ComplexNumber

# Создание комплексных чисел
z1 = ComplexNumber(3, 4)   # 3 + 4i
z2 = ComplexNumber(1, -2)  # 1 - 2i

# Выполнение операций
result = z1 + z2
print(result)  # Вывод: 4 + 2i

# Доступ к свойствам
print(z1.magnitude())  # Вывод: 5.0
```

## Автор

Андрій Будильников

</div>