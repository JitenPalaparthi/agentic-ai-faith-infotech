"""13 — PCA

PCA creates new orthogonal components that capture variance.
Scaling is usually important before PCA when feature units differ.
"""
import numpy as np
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

X = np.array([
    [1, 10, 100],
    [2, 20, 200],
    [3, 31, 290],
    [4, 39, 410],
    [5, 51, 495]
], dtype=float)

pipe = Pipeline([
    ("scale", StandardScaler()),
    ("pca", PCA(n_components=2))
])

Xt = pipe.fit_transform(X)
pca = pipe.named_steps["pca"]

print("Reduced shape:", Xt.shape)
print("Transformed:\n", Xt)
print("Explained variance ratio:", pca.explained_variance_ratio_)
