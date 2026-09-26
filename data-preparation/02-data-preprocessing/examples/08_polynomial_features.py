"""08 — PolynomialFeatures

For x1 and x2, degree=2 can create:
1, x1, x2, x1^2, x1*x2, x2^2
"""
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

X = np.array([[2, 3], [4, 5]])
poly = PolynomialFeatures(degree=2)

Xt = poly.fit_transform(X)
print("Feature names:")
print(poly.get_feature_names_out(["x1", "x2"]))
print("\nTransformed:")
print(Xt)
