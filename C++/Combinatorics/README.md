# Combinatorics / Комбінаторика / Комбинаторика

## English

This section contains implementations of basic combinatorics algorithms in C++.

### Functions Included:
- `factorial(n)` - Calculates the factorial of n
- `permutation(n, r)` - Calculates permutations P(n,r) = n!/(n-r)!
- `combination(n, r)` - Calculates combinations C(n,r) = n!/((n-r)!*r!)
- `catalanNumber(n)` - Calculates the nth Catalan number

### Usage:
```cpp
#include "Combinatorics.h"

long long fact = Combinatorics::factorial(5);  // 120
long long perm = Combinatorics::permutation(5, 3);  // 60
long long comb = Combinatorics::combination(5, 3);  // 10
long long catalan = Combinatorics::catalanNumber(5);  // 42
```

---

## Українська

Цей розділ містить реалізації базових алгоритмів комбінаторики на C++.

### Включені функції:
- `factorial(n)` - Обчислює факторіал n
- `permutation(n, r)` - Обчислює перестановки P(n,r) = n!/(n-r)!
- `combination(n, r)` - Обчислює комбінації C(n,r) = n!/((n-r)!*r!)
- `catalanNumber(n)` - Обчислює n-те число Каталана

### Використання:
```cpp
#include "Combinatorics.h"

long long fact = Combinatorics::factorial(5);  // 120
long long perm = Combinatorics::permutation(5, 3);  // 60
long long comb = Combinatorics::combination(5, 3);  // 10
long long catalan = Combinatorics::catalanNumber(5);  // 42
```

---

## Русский

Этот раздел содержит реализации базовых алгоритмов комбинаторики на C++.

### Включенные функции:
- `factorial(n)` - Вычисляет факториал n
- `permutation(n, r)` - Вычисляет перестановки P(n,r) = n!/(n-r)!
- `combination(n, r)` - Вычисляет комбинации C(n,r) = n!/((n-r)!*r!)
- `catalanNumber(n)` - Вычисляет n-ое число Каталана

### Использование:
```cpp
#include "Combinatorics.h"

long long fact = Combinatorics::factorial(5);  // 120
long long perm = Combinatorics::permutation(5, 3);  // 60
long long comb = Combinatorics::combination(5, 3);  // 10
long long catalan = Combinatorics::catalanNumber(5);  // 42
```