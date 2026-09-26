"""07 — PolynomialFeatures."""
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("data/customers.csv")
X = df[["age", "years_experience"]]

poly = PolynomialFeatures(degree=2, include_bias=False)
Xt = poly.fit_transform(X)

result = pd.DataFrame(
    Xt,
    columns=poly.get_feature_names_out(X.columns)
)

print(result.head())
print("\nGenerated:", result.columns.tolist())

print("""
For two features x1 and x2, degree 2 can generate:
x1, x2, x1^2, x1*x2, x2^2

High degrees can create many features and increase overfitting risk.
""")
