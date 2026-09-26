"""11 — ColumnTransformer

Apply different preprocessing to different groups of columns.
This is one of the most useful sklearn preprocessing patterns.
"""
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.DataFrame({
    "age": [25, 35, np.nan],
    "salary": [50000, np.nan, 80000],
    "city": ["Delhi", "Mumbai", "Chennai"]
})

numeric = ["age", "salary"]
categorical = ["city"]

num_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

cat_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
])

preprocessor = ColumnTransformer([
    ("numeric", num_pipe, numeric),
    ("categorical", cat_pipe, categorical)
])

Xt = preprocessor.fit_transform(df)

print("Original:\n", df)
print("\nGenerated feature names:")
print(preprocessor.get_feature_names_out())
print("\nTransformed data:")
print(Xt)
