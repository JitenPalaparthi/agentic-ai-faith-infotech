"""02 — SimpleImputer

Use simple statistics to replace missing values.
Numerical: mean/median are common.
Categorical: most_frequent or a constant such as "Unknown".
"""
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.DataFrame({
    "age": [25, 30, np.nan, 40, 35],
    "salary": [30000, np.nan, 50000, 60000, 45000],
    "city": ["Delhi", "Mumbai", np.nan, "Delhi", "Chennai"]
})
print("Original:\n", df)

mean_imp = SimpleImputer(strategy="mean")
print("\nAge with mean imputation:")
print(mean_imp.fit_transform(df[["age"]]))

median_imp = SimpleImputer(strategy="median")
print("\nSalary with median imputation:")
print(median_imp.fit_transform(df[["salary"]]))

cat_imp = SimpleImputer(strategy="constant", fill_value="Unknown")
print("\nCity with constant imputation:")
print(cat_imp.fit_transform(df[["city"]]))

# Trainer note:
# Median is often preferred to mean for skewed numerical data/outliers.
