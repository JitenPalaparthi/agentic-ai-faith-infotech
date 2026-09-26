"""18 — Inspect model-ready feature names."""
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.read_csv("data/customers.csv")
df["avg_order_value"] = df["total_spend"] / df["num_orders"]

numeric = ["age", "annual_salary", "avg_order_value"]
categorical = ["city", "education"]

ct = ColumnTransformer([
    ("num", StandardScaler(), numeric),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical)
])

Xt = ct.fit_transform(df)
print("Input shape:", df.shape)
print("Model feature matrix shape:", Xt.shape)
print("\nFeature names:")
for name in ct.get_feature_names_out():
    print(name)
