from unittest import TestCase
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from knnClassifier import KnnClassifier


class TestKnnClassifier(TestCase):
    def setUp(self):
        # Inicjalizacja klasyfikatora przed każdym testem
        self.classifier = KnnClassifier(n_neighbors=3, distance_metric='euclidean')

    def test_train_1(self):
        X_train = np.array([[1, 2], [2, 3], [3, 4]])
        y_train = np.array([0, 0, 1])

        self.classifier.train(X_train, y_train)
        print(self.classifier.X_train)
        print(self.classifier.y_train)

        self.assertTrue(np.array_equal(self.classifier.X_train, X_train))
        self.assertTrue(np.array_equal(self.classifier.y_train, y_train))

    def test_train_2(self):
        X_train = np.array([[1, 2], [2, 3], [3, 4]])
        X_train2 = np.array([[1, 2], [2, 3]])
        y_train = np.array([0, 0, 1])
        y_train2 = np.array([0, 1])

        self.classifier.train(X_train, y_train)
        self.classifier.train(X_train2, y_train2)
        print(self.classifier.X_train)
        print(self.classifier.y_train)

        self.assertTrue(np.array_equal(self.classifier.X_train, np.concatenate([X_train, X_train2])))
        self.assertTrue(np.array_equal(self.classifier.y_train, np.concatenate([y_train, y_train2])))

    def test_calculate_distances(self):
        # Test obliczania odległości dla różnych metryk
        point1 = np.array([[1, 2]])
        point2 = np.array([[3, 4]])

        # Test dla metryki euclidean
        self.classifier.distance_metric = 'euclidean'
        distance_euclidean = self.classifier.calculate_distances(point1, point2)

        # Test dla metryki manhattan
        self.classifier.distance_metric = 'manhattan'
        distance_manhattan = self.classifier.calculate_distances(point1, point2)

        # Test dla metryki maximum
        self.classifier.distance_metric = 'maximum'
        distance_maximum = self.classifier.calculate_distances(point1, point2)

        # Test dla metryki cosine
        self.classifier.distance_metric = 'cosine'
        distance_cosine = self.classifier.calculate_distances(point1, point2)

        # Sprawdzenie, czy wyniki są zgodne z oczekiwaniami

        # Dla metryki euclidean
        self.assertEqual(distance_euclidean, np.sqrt(8))

        # Dla metryki manhattan
        self.assertEqual(distance_manhattan, 4)

        # Dla metryki maximum
        self.assertEqual(distance_maximum, 2)

        # Dla metryki cosine
        self.assertEqual(distance_cosine, 0.01613008990009257)

    def test_predict(self):
        X_train = np.array([[1, 2], [2, 3], [3, 4]])
        y_train = np.array([0, 0, 1])
        self.classifier.train(X_train, y_train)

        X_test = np.array([[2.5, 3.5]])

        predictions = self.classifier.predict(X_test)
        self.assertEqual(predictions[0], 0)

    def test_predict_classes_with_different_neighbors_and_metrics(self):
        # Test przewidywania klas dla różnych ilości sąsiadów i metryk na przykładowych danych (Iris dataset)
        iris_data = datasets.load_iris()
        X, y = iris_data.data, iris_data.target
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.classifier.train(X_train, y_train)

        # Test dla różnej ilości sąsiadów
        self.classifier.n_neighbors = 2
        predictions_2_neighbors = self.classifier.predict(X_test)

        self.classifier.n_neighbors = 4
        predictions_4_neighbors = self.classifier.predict(X_test)

        # Test dla różnych metryk
        self.classifier.n_neighbors = 3
        self.classifier.distance_metric = 'manhattan'
        predictions_manhattan = self.classifier.predict(X_test)

        self.classifier.distance_metric = 'cosine'
        predictions_cosine = self.classifier.predict(X_test)

        # Sprawdzenie, czy wyniki są zgodne z oczekiwaniami

        # Dla różnej ilości sąsiadów
        self.assertTrue(np.array_equal(predictions_2_neighbors, predictions_4_neighbors))

        # Dla różnych metryk
        self.assertFalse(np.array_equal(predictions_manhattan, predictions_cosine))
