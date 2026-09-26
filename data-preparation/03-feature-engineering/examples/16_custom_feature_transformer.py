"""16 — Create an sklearn-compatible feature-engineering transformer."""
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class CustomerFeatureEngineer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        out = X.copy()
        out["monthly_salary"] = out["annual_salary"] / 12
        out["avg_order_value"] = out["total_spend"] / out["num_orders"]
        out["spend_per_visit"] = out["total_spend"] / out["website_visits"]
        return out

df = pd.read_csv("data/customers.csv")
engineer = CustomerFeatureEngineer()

result = engineer.fit_transform(df)
print(result[["monthly_salary", "avg_order_value", "spend_per_visit"]])
