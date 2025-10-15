"""
лінійна регресія з нуля
автор: Андрій Будильников

проста реалізація лінійної регресії без використання бібліотек ml
"""

import math

class LinearRegression:
    """лінійна регресія з градієнтним спуском"""
    
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = [0.0]  # ініціалізуємо з дефолтним значенням
        self.bias = 0.0
        self.costs = []
    
    def fit(self, x, y):
        """навчання моделі"""
        # ініціалізація параметрів
        n_samples = len(x)
        # визначаємо кількість ознак
        if isinstance(x[0], (list, tuple)):
            n_features = len(x[0])
        else:
            n_features = 1
            # перетворюємо в 2d масив для уніфікації
            x = [[val] for val in x]
        
        self.weights = [0.0] * n_features
        self.bias = 0.0
        
        # градієнтний спуск
        for i in range(self.n_iterations):
            # передбачення
            y_predicted = []
            for j in range(n_samples):
                pred = sum(self.weights[k] * x[j][k] for k in range(n_features)) + self.bias
                y_predicted.append(pred)
            
            # обчислення функції втрат (mse)
            cost = sum((y_predicted[j] - y[j]) ** 2 for j in range(n_samples)) / (2 * n_samples)
            self.costs.append(cost)
            
            # обчислення градієнтів
            dw = [sum((y_predicted[j] - y[j]) * x[j][k] for j in range(n_samples)) / n_samples 
                  for k in range(n_features)]
            
            db = sum(y_predicted[j] - y[j] for j in range(n_samples)) / n_samples
            
            # оновлення параметрів
            for k in range(n_features):
                self.weights[k] -= self.learning_rate * dw[k]
            self.bias -= self.learning_rate * db
    
    def predict(self, x):
        """передбачення для нових даних"""
        # визначаємо кількість ознак
        if isinstance(x[0], (list, tuple)):
            n_features = len(x[0])
            # якщо передбачаємо для одного елемента, перетворюємо в список
            if len(x) == 0:
                x = [x]
        else:
            n_features = 1
            # перетворюємо в 2d масив для уніфікації
            x = [[val] for val in x]
        
        # робимо передбачення
        predictions = []
        for j in range(len(x)):
            pred = sum(self.weights[k] * x[j][k] for k in range(n_features)) + self.bias
            predictions.append(pred)
        
        return predictions

def main():
    """демонстрація роботи лінійної регресії"""
    print("лінійна регресія")
    print("==============")
    
    # генерація синтетичних даних
    x = [i * 0.1 for i in range(100)]
    y = [4 + 3 * x[i] + (i % 10 - 5) for i in range(100)]  # лінійна залежність з шумом
    
    # створення та навчання моделі
    model = LinearRegression(learning_rate=0.01, n_iterations=1000)
    model.fit(x, y)
    
    # передбачення
    predictions = model.predict(x)
    
    # вивід результатів
    print(f"ваги: {model.weights}")
    print(f"зміщення: {model.bias}")
    print(f"передбачення для x=5: {model.predict([5])[0]}")
    
    # вивід деяких передбачень
    print("\nперші 10 передбачень:")
    for i in range(10):
        print(f"x={x[i]:.1f}, реальне={y[i]:.1f}, передбачене={predictions[i]:.1f}")

if __name__ == "__main__":
    main()