# Complex Number Implementation (Java)

<div align="center">
  
[![English](https://img.shields.io/badge/English-blue)](#english)
[![Українська](https://img.shields.io/badge/Українська-blue)](#українська)
[![Русский](https://img.shields.io/badge/Русский-blue)](#русский)

</div>

<!-- English -->
<div id="english">

## Description

This program provides a [ComplexNumber](file:///c%3A/Users/%D0%91%D0%BE%D0%B3%D0%B4%D0%B0%D0%BD/Desktop/Sbornik-Algebra-Sparky/Java%20and%20Kotlin/Other/ComplexNumber.java#L7-L190) class for working with complex numbers in Java. It includes all basic arithmetic operations, properties like conjugate, magnitude, and phase, and conversion to/from polar form.

## Features

- Addition, subtraction, multiplication, and division of complex numbers
- Conjugate, magnitude, and phase calculations
- Conversion to and from polar form
- Method-based operations (since Java doesn't support operator overloading)

## Usage

```java
public class Main {
    public static void main(String[] args) {
        // Create complex numbers
        ComplexNumber z1 = new ComplexNumber(3, 4);   // 3 + 4i
        ComplexNumber z2 = new ComplexNumber(1, -2);  // 1 - 2i

        // Perform operations
        ComplexNumber result = z1.add(z2);
        System.out.println(result);  // Output: 4.0 + 2.0i

        // Access properties
        System.out.println(z1.magnitude());  // Output: 5.0
    }
}
```

## Author

Andriy Budilnikov (Андрій Будильников)

</div>

<!-- Українська -->
<div id="українська">

## Опис

Ця програма надає клас [ComplexNumber](file:///c%3A/Users/%D0%91%D0%BE%D0%B3%D0%B4%D0%B0%D0%BD/Desktop/Sbornik-Algebra-Sparky/Java%20and%20Kotlin/Other/ComplexNumber.java#L7-L190) для роботи з комплексними числами в Java. Вона включає всі базові арифметичні операції, властивості, такі як спряжене, модуль та фаза, а також перетворення в/з полярної форми.

## Особливості

- Додавання, віднімання, множення та ділення комплексних чисел
- Обчислення спряженого, модуля та фази
- Перетворення в та з полярної форми
- Операції на основі методів (оскільки Java не підтримує перевантаження операторів)

## Використання

```java
public class Main {
    public static void main(String[] args) {
        // Створення комплексних чисел
        ComplexNumber z1 = new ComplexNumber(3, 4);   // 3 + 4i
        ComplexNumber z2 = new ComplexNumber(1, -2);  // 1 - 2i

        // Виконання операцій
        ComplexNumber result = z1.add(z2);
        System.out.println(result);  // Вивід: 4.0 + 2.0i

        // Доступ до властивостей
        System.out.println(z1.magnitude());  // Вивід: 5.0
    }
}
```

## Автор

Андрій Будильников

</div>

<!-- Русский -->
<div id="русский">

## Описание

Эта программа предоставляет класс [ComplexNumber](file:///c%3A/Users/%D0%91%D0%BE%D0%B3%D0%B4%D0%B0%D0%BD/Desktop/Sbornik-Algebra-Sparky/Java%20and%20Kotlin/Other/ComplexNumber.java#L7-L190) для работы с комплексными числами в Java. Она включает все базовые арифметические операции, свойства, такие как сопряженное, модуль и фаза, а также преобразование в/из полярной формы.

## Особенности

- Сложение, вычитание, умножение и деление комплексных чисел
- Вычисление сопряженного, модуля и фазы
- Преобразование в и из полярной формы
- Операции на основе методов (поскольку Java не поддерживает перегрузку операторов)

## Использование

```java
public class Main {
    public static void main(String[] args) {
        // Создание комплексных чисел
        ComplexNumber z1 = new ComplexNumber(3, 4);   // 3 + 4i
        ComplexNumber z2 = new ComplexNumber(1, -2);  // 1 - 2i

        // Выполнение операций
        ComplexNumber result = z1.add(z2);
        System.out.println(result);  // Вывод: 4.0 + 2.0i

        // Доступ к свойствам
        System.out.println(z1.magnitude());  // Вывод: 5.0
    }
}
```

## Автор

Андрій Будильников

</div>