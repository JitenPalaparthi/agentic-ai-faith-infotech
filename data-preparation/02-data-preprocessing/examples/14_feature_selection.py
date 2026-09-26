"""14 — Feature selection examples"""
import numpy as np
from sklearn.feature_selection import VarianceThreshold, SelectKBest, f_classif

X = np.array([
    [1, 10, 0],
    [1, 20, 1],
    [1, 30, 0],
    [1, 40, 1],
    [1, 50, 1],
    [1, 60, 0],
])
y = np.array([0, 0, 0, 1, 1, 1])

variance = VarianceThreshold(threshold=0.0)
Xv = variance.fit_transform(X)
print("VarianceThreshold kept columns:", variance.get_support(indices=True))
print(Xv)

selector = SelectKBest(score_func=f_classif, k=1)
Xk = selector.fit_transform(Xv, y)
print("\nSelectKBest selected index (within Xv):", selector.get_support(indices=True))
print(Xk)
