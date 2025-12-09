import math
from collections import Counter

class SimpleStatistics:
    def __init__(self, data):
        self.data = sorted(data)

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        n = len(self.data)
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        return self.data[mid]

    def mode(self):
        c = Counter(self.data)
        max_count = max(c.values())
        return [x for x in c if c[x] == max_count]

    def range(self):
        return max(self.data) - min(self.data)

    def variance(self):
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / (len(self.data) - 1)

    def standard_deviation(self):
        return math.sqrt(self.variance())
s = SimpleStatistics([1, 2, 2, 3, 5])

print("Среднее:", s.mean())
print("Медиана:", s.median())
print("Мода:", s.mode())
print("Размах:", s.range())
print("Дисперсия:", s.variance())
print("Станд. отклонение:", s.standard_deviation())



class FrequencyDistribution:
    def __init__(self, data):
        self.data = data
        self.freq = {}

    def calculate_frequencies(self):
        self.freq = Counter(self.data)

    def display_frequency_table(self):
        for key, value in self.freq.items():
            print(f"{key}: {value}")

    def get_most_frequent(self):
        max_v = max(self.freq.values())
        return [k for k, v in self.freq.items() if v == max_v]
f = FrequencyDistribution(["red", "blue", "red", "green", "blue", "red"])
f.calculate_frequencies()
f.display_frequency_table()

print("Самые частые:", f.get_most_frequent())





import numpy as np
from scipy.stats import pearsonr, spearmanr
import matplotlib.pyplot as plt

class Correlation:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def pearson_correlation(self):
        return pearsonr(self.X, self.Y)[0]

    def spearman_correlation(self):
        return spearmanr(self.X, self.Y)[0]

    def covariance(self):
        return np.cov(self.X, self.Y, ddof=1)[0][1]

    def plot_scatter(self):
        plt.scatter(self.X, self.Y)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Scatter plot")
        plt.show()
X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

c = Correlation(X, Y)
print("Пирсон:", c.pearson_correlation())
print("Спирмен:", c.spearman_correlation())
print("Ковариация:", c.covariance())
# c.plot_scatter()




from abc import ABC, abstractmethod
from scipy.stats import ttest_1samp, ttest_ind, ttest_rel, chi2_contingency

class HypothesisTest(ABC):

    @abstractmethod
    def run_test(self):
        pass

    @abstractmethod
    def get_p_value(self):
        pass

    def interpret_results(self, alpha=0.05):
        p = self.get_p_value()
        return "Гипотеза отвергается" if p < alpha else "Нет оснований отвергнуть гипотезу"


class TTest(HypothesisTest):
    def __init__(self, data1, data2=None, mean=None):
        self.data1 = data1
        self.data2 = data2
        self.mean = mean
        self.result = None

    def run_test(self):
        if self.data2 is None:  # одновыборочный
            self.result = ttest_1samp(self.data1, self.mean)
        else:
            # двухвыборочный независимый
            self.result = ttest_ind(self.data1, self.data2)
        return self.result

    def get_p_value(self):
        return self.result.pvalue


class ChiSquareTest(HypothesisTest):
    def __init__(self, table):
        self.table = table
        self.result = None

    def run_test(self):
        self.result = chi2_contingency(self.table)
        return self.result

    def get_p_value(self):
        return self.result[1]
t = TTest([1, 2, 3, 4, 5], mean=3)
t.run_test()
print("P-value:", t.get_p_value())
print(t.interpret_results())

table = [
    [10, 20],
    [20, 30]
]

c = ChiSquareTest(table)
c.run_test()
print("P-value:", c.get_p_value())
print(c.interpret_results())




from abc import ABC, abstractmethod
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error

class RegressionModel(ABC):

    @abstractmethod
    def fit(self, X, y):
        pass

    @abstractmethod
    def predict(self, X):
        pass

    @abstractmethod
    def evaluate(self, X, y):
        pass


class LinearRegressionModel(RegressionModel):
    def __init__(self):
        self.model = LinearRegression()

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def evaluate(self, X, y):
        pred = self.predict(X)
        return r2_score(y, pred), mean_squared_error(y, pred)

    def plot_regression(self, X, y):
        plt.scatter(X, y)
        plt.plot(X, self.predict(X))
        plt.show()


class PolynomialRegressionModel(RegressionModel):
    def __init__(self, degree):
        self.degree = degree
        self.poly = PolynomialFeatures(degree=self.degree)
        self.model = LinearRegression()

    def fit(self, X, y):
        X_trans = self.poly.fit_transform(X)
        self.model.fit(X_trans, y)

    def predict(self, X):
        X_trans = self.poly.transform(X)
        return self.model.predict(X_trans)

    def evaluate(self, X, y):
        pred = self.predict(X)
        return r2_score(y, pred), mean_squared_error(y, pred)

    def plot_regression(self, X, y):
        plt.scatter(X, y)
        plt.plot(X, self.predict(X))
        plt.show()
import numpy as np

X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 5, 4])

model = LinearRegressionModel()
model.fit(X, y)
print("Предсказания:", model.predict(X))
print("Оценка:", model.evaluate(X, y))



import random
import pandas as pd

class Sampling:

    @staticmethod
    def simple_random_sample(data, n):
        return random.sample(data, n)

    @staticmethod
    def stratified_sample(data, strata, n):
        result = []
        for group, count in n.items():
            subset = data[data[strata] == group]
            result.extend(subset.sample(count).to_dict("records"))
        return result

    @staticmethod
    def cluster_sample(data, cluster_column, n_clusters):
        clusters = data[cluster_column].unique()
        chosen = random.sample(list(clusters), n_clusters)
        return data[data[cluster_column].isin(chosen)]

    @staticmethod
    def systematic_sample(data, k):
        return data[::k]
data = [1, 2, 3, 4, 5, 6, 7]
print(Sampling.simple_random_sample(data, 3))
