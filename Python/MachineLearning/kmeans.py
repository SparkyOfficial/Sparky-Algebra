"""
k-середніх з нуля
автор: Андрій Будильников

реалізація алгоритму кластеризації k-середніх без зовнішніх бібліотек
"""

import random
import math

class KMeans:
    """k-середніх алгоритм кластеризації"""
    
    def __init__(self, k=3, max_iters=100):
        self.k = k
        self.max_iters = max_iters
    
    def euclidean_distance(self, point1, point2):
        """евклідова відстань між двома точками"""
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))
    
    def fit(self, data):
        """навчання моделі k-середніх"""
        self.data = data
        n_samples = len(data)
        n_features = len(data[0])
        
        # ініціалізація центрів кластерів випадковими точками
        self.centroids = random.sample(data, self.k)
        
        # ітераційне оновлення центрів
        for _ in range(self.max_iters):
            # призначення точок до кластерів
            clusters = [[] for _ in range(self.k)]
            
            for point in data:
                # знаходимо найближчий центр кластера
                distances = [self.euclidean_distance(point, centroid) for centroid in self.centroids]
                closest_cluster = distances.index(min(distances))
                clusters[closest_cluster].append(point)
            
            # оновлення центрів кластерів
            prev_centroids = self.centroids.copy()
            
            for i in range(self.k):
                if clusters[i]:  # якщо кластер не пустий
                    # новий центр - середнє значення всіх точок кластера
                    new_centroid = []
                    for j in range(n_features):
                        feature_values = [point[j] for point in clusters[i]]
                        new_centroid.append(sum(feature_values) / len(feature_values))
                    self.centroids[i] = new_centroid
            
            # перевірка збіжності
            if all(self.euclidean_distance(prev_centroids[i], self.centroids[i]) < 1e-6 
                   for i in range(self.k)):
                break
        
        # фінальне призначення точок до кластерів
        self.labels = []
        for point in data:
            distances = [self.euclidean_distance(point, centroid) for centroid in self.centroids]
            self.labels.append(distances.index(min(distances)))
        
        return self
    
    def predict(self, data):
        """передбачення кластерів для нових даних"""
        labels = []
        for point in data:
            distances = [self.euclidean_distance(point, centroid) for centroid in self.centroids]
            labels.append(distances.index(min(distances)))
        return labels

def main():
    """демонстрація роботи k-середніх"""
    print("k-середніх кластеризація")
    print("======================")
    
    # генерація тестових даних
    # кластер 1 (навколо (2, 2))
    cluster1 = [[2 + random.gauss(0, 0.5), 2 + random.gauss(0, 0.5)] for _ in range(30)]
    # кластер 2 (навколо (6, 6))
    cluster2 = [[6 + random.gauss(0, 0.5), 6 + random.gauss(0, 0.5)] for _ in range(30)]
    # кластер 3 (навколо (2, 6))
    cluster3 = [[2 + random.gauss(0, 0.5), 6 + random.gauss(0, 0.5)] for _ in range(30)]
    
    # об'єднуємо всі кластери
    data = cluster1 + cluster2 + cluster3
    
    # створення та навчання моделі
    kmeans = KMeans(k=3, max_iters=100)
    kmeans.fit(data)
    
    # вивід результатів
    print(f"центроїди кластерів: {kmeans.centroids}")
    print(f"кількість точок в кожному кластері: {[kmeans.labels.count(i) for i in range(3)]}")
    
    # приклад передбачення
    test_points = [[1, 1], [5, 5], [1, 6]]
    predictions = kmeans.predict(test_points)
    for i, point in enumerate(test_points):
        print(f"точка {point} належить до кластера {predictions[i]}")

if __name__ == "__main__":
    main()