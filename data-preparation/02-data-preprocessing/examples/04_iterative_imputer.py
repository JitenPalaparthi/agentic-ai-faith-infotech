"""04 — IterativeImputer

Estimates a feature with missing values from the other features.
It is experimental in sklearn, so enable_iterative_imputer must be imported.
"""
import numpy as np
import pandas as pd
from sklearn.experimental import enable_iterative_imputer  # noqa: F401
from sklearn.impute import IterativeImputer

df = pd.DataFrame({
    "age": [25, 30, 40, 50, 35],
    "experience": [2, 7, 15, 25, 10],
    "salary": [35000, 60000, np.nan, 120000, 75000]
})
print("Before:\n", df)

imp = IterativeImputer(random_state=42, max_iter=10)
out = pd.DataFrame(imp.fit_transform(df), columns=df.columns)

print("\nAfter:\n", out)
