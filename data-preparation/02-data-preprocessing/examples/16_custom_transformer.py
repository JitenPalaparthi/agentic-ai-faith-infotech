"""16 — Build your own sklearn-compatible transformer"""
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class MultiplyBy(BaseEstimator, TransformerMixin):
    def __init__(self, factor=2):
        self.factor = factor

    def fit(self, X, y=None):
        # Nothing to learn in this transformer.
        return self

    def transform(self, X):
        return np.asarray(X) * self.factor

X = np.array([[1, 2], [3, 4]])
transformer = MultiplyBy(factor=10)

print(transformer.fit_transform(X))
print("\nBecause it follows sklearn's estimator API, it can be placed in a Pipeline.")
