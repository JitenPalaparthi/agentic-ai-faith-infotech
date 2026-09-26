"""05 — MissingIndicator and add_indicator

Sometimes 'this value was missing' is itself predictive information.
"""
import numpy as np
import pandas as pd
from sklearn.impute import MissingIndicator, SimpleImputer

X = pd.DataFrame({"income": [50000, np.nan, 70000, np.nan]})
print("Original:\n", X)

indicator = MissingIndicator()
print("\nMissing flags:")
print(indicator.fit_transform(X).astype(int))

imp = SimpleImputer(strategy="median", add_indicator=True)
print("\nImputed value + automatically added missing flag:")
print(imp.fit_transform(X))
