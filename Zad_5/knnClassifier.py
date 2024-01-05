import numpy as np
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split

class KnnClassifier:
    def __init__(self, n_neighbors=None, distance_metric=None):
        self.n_neighbors = n_neighbors
        self.distance_metric = distance_metric
        self.X_train = None
        self.y_train = None

    def train(self, xtrain, ytrain):
        if self.X_train is None:
            self.X_train = xtrain
            self.y_train = ytrain
        else:
            self.X_train = np.concatenate([self.X_train, xtrain])
            self.y_train = np.concatenate([self.y_train, ytrain])

    def calculate_distances(self, test_vector, xtrain):
        if self.distance_metric == 'euclidean':
            return np.linalg.norm(xtrain - test_vector)
        elif self.distance_metric == 'manhattan':
            return np.sum(np.abs(xtrain - test_vector))
        elif self.distance_metric == 'maximum':
            return np.max(np.abs(xtrain - test_vector))
        elif self.distance_metric == 'cosine':
            dot_products = np.dot(xtrain, test_vector)
            norms_x = np.linalg.norm(test_vector)
            norms_X = np.linalg.norm(xtrain)
            cosine_similarities = dot_products / (norms_x * norms_X)
            return 1 - cosine_similarities

    def predict(self, xtest):
        predictions = [self._predict(x) for x in xtest]
        return predictions

    def _predict(self, x):
        distances = [self.calculate_distances(x, x_train) for x_train in self.X_train]
        indices = np.argsort(distances)[:self.n_neighbors]
        k_nearest_labels = [self.y_train[index] for index in indices]
        most_common_label = Counter(k_nearest_labels).most_common()
        return most_common_label[0][0]

#---------------dataset0--------------------------------------
data = pd.read_csv("dataset0.csv", header=None, delimiter=' ')

X = data.iloc[:, :-1]
X = np.array(X)
y = data.iloc[:, -1]
y = np.array(y)

classifier = KnnClassifier(4, 'maximum')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
classifier.train(X_train, y_train)

predictions = classifier.predict(X_test)
print("Predictions:", predictions)

accuracy = np.sum(predictions == y_test) / len(y_test)
print("Accuracy: ", accuracy)

#---------------dataset1--------------------------------------
"""
data = pd.read_csv("dataset1.csv", header=None, delimiter=' ')

X = data.iloc[:, :-1]
X = np.array(X)
y = data.iloc[:, -1]
y = np.array(y)

classifier = KnnClassifier(3, 'euclidean')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
classifier.train(X_train, y_train)

predictions = classifier.predict(X_test)
print("Predictions:", predictions)

accuracy = np.sum(predictions == y_test) / len(y_test)
print("Accuracy: ", accuracy)
"""
#---------------dataset2--------------------------------------
"""
data = pd.read_csv("dataset2.csv", header=None, delimiter=' ')

X = data.iloc[:, :-1]
X = np.array(X)
y = data.iloc[:, -1]
y = np.array(y)

classifier = KnnClassifier(4, 'cosine')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
classifier.train(X_train, y_train)

predictions = classifier.predict(X_test)
# print("Predictions:", predictions)

accuracy = np.sum(predictions == y_test) / len(y_test)
print("Accuracy: ",accuracy)
"""