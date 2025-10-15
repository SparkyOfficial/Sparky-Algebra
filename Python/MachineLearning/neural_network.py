"""
нейронна мережа з нуля
автор: Андрій Будильников

проста одношарова нейронна мережа для класифікації
"""

import random
import math

class NeuralNetwork:
    """одношарова нейронна мережа"""
    
    def __init__(self, n_inputs, n_hidden, n_outputs, learning_rate=0.1):
        self.n_inputs = n_inputs
        self.n_hidden = n_hidden
        self.n_outputs = n_outputs
        self.learning_rate = learning_rate
        
        # ініціалізація ваг та зміщень
        # ваги між вхідним та прихованим шаром
        self.weights_ih = [[random.uniform(-1, 1) for _ in range(n_hidden)] for _ in range(n_inputs)]
        # ваги між прихованим та вихідним шаром
        self.weights_ho = [[random.uniform(-1, 1) for _ in range(n_outputs)] for _ in range(n_hidden)]
        # зміщення прихованого шару
        self.bias_h = [random.uniform(-1, 1) for _ in range(n_hidden)]
        # зміщення вихідного шару
        self.bias_o = [random.uniform(-1, 1) for _ in range(n_outputs)]
    
    def sigmoid(self, x):
        """сигмоїдальна функція активації"""
        # обмежуємо значення щоб уникнути переповнення
        if x > 700:
            return 1.0
        elif x < -700:
            return 0.0
        else:
            return 1 / (1 + math.exp(-x))
    
    def sigmoid_derivative(self, x):
        """похідна сигмоїди"""
        return x * (1 - x)
    
    def forward(self, inputs):
        """прямий прохід через мережу"""
        # обчислення виходу прихованого шару
        hidden = []
        for i in range(self.n_hidden):
            activation = self.bias_h[i]
            for j in range(self.n_inputs):
                activation += inputs[j] * self.weights_ih[j][i]
            hidden.append(self.sigmoid(activation))
        
        # обчислення виходу вихідного шару
        outputs = []
        for i in range(self.n_outputs):
            activation = self.bias_o[i]
            for j in range(self.n_hidden):
                activation += hidden[j] * self.weights_ho[j][i]
            outputs.append(self.sigmoid(activation))
        
        return hidden, outputs
    
    def train(self, training_data, epochs):
        """навчання мережі методом зворотного поширення"""
        for epoch in range(epochs):
            total_error = 0
            
            for inputs, targets in training_data:
                # прямий прохід
                hidden, outputs = self.forward(inputs)
                
                # обчислення помилки вихідного шару
                output_errors = [targets[i] - outputs[i] for i in range(self.n_outputs)]
                output_deltas = [output_errors[i] * self.sigmoid_derivative(outputs[i]) 
                                for i in range(self.n_outputs)]
                
                # обчислення помилки прихованого шару
                hidden_errors = [0] * self.n_hidden
                for i in range(self.n_hidden):
                    for j in range(self.n_outputs):
                        hidden_errors[i] += output_deltas[j] * self.weights_ho[i][j]
                
                hidden_deltas = [hidden_errors[i] * self.sigmoid_derivative(hidden[i]) 
                                for i in range(self.n_hidden)]
                
                # оновлення ваг між прихованим та вихідним шаром
                for i in range(self.n_hidden):
                    for j in range(self.n_outputs):
                        self.weights_ho[i][j] += self.learning_rate * output_deltas[j] * hidden[i]
                
                # оновлення ваг між вхідним та прихованим шаром
                for i in range(self.n_inputs):
                    for j in range(self.n_hidden):
                        self.weights_ih[i][j] += self.learning_rate * hidden_deltas[j] * inputs[i]
                
                # оновлення зміщень
                for i in range(self.n_outputs):
                    self.bias_o[i] += self.learning_rate * output_deltas[i]
                
                for i in range(self.n_hidden):
                    self.bias_h[i] += self.learning_rate * hidden_deltas[i]
                
                # обчислення загальної помилки
                total_error += sum(error ** 2 for error in output_errors)
            
            # вивід прогресу кожні 100 епох
            if (epoch + 1) % 100 == 0:
                print(f"епоха {epoch + 1}, помилка: {total_error:.4f}")
    
    def predict(self, inputs):
        """передбачення для нових даних"""
        _, outputs = self.forward(inputs)
        return outputs

def main():
    """демонстрація роботи нейронної мережі"""
    print("нейронна мережа")
    print("=============")
    
    # задача xor - класична задача для демонстрації нейронних мереж
    training_data = [
        ([0, 0], [0]),
        ([0, 1], [1]),
        ([1, 0], [1]),
        ([1, 1], [0])
    ]
    
    # створення нейронної мережі
    # 2 входи, 4 нейрони в прихованому шарі, 1 вихід
    nn = NeuralNetwork(n_inputs=2, n_hidden=4, n_outputs=1, learning_rate=1.0)
    
    print("навчання мережі на задачі xor...")
    nn.train(training_data, epochs=1000)
    
    # тестування
    print("\nрезультати передбачень:")
    for inputs, expected in training_data:
        prediction = nn.predict(inputs)
        print(f"вхід: {inputs}, очікуване: {expected[0]}, передбачене: {prediction[0]:.3f}")

if __name__ == "__main__":
    main()