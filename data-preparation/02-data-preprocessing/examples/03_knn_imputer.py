"""03 — KNNImputer

Fills a missing value using nearby/similar observations.
Distance-based methods are sensitive to feature scale.
"""
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer

df = pd.DataFrame({
    "age": [25, 26, 27, 48],
    "experience": [2, 3, 3, 25],
    "salary": [30000, 32000, np.nan, 120000]
})
print("Before:\n", df)

imputer = KNNImputer(n_neighbors=2)
result = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

print("\nAfter KNN imputation:\n", result)
print("\nObserve how multiple feature values are used to determine neighbors.")
