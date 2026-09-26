"""17 — Feature engineering + preprocessing + model pipeline."""
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

class FeatureEngineer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        out = X.copy()
        out["avg_order_value"] = out["total_spend"] / out["num_orders"]
        out["spend_per_visit"] = out["total_spend"] / out["website_visits"]
        return out

df = pd.read_csv("data/customers.csv")
X = df.drop(columns=["bought", "review_text", "customer_id",
                     "signup_date", "last_purchase_date"])
y = df["bought"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=.25, random_state=42, stratify=y
)

numeric = [
    "age", "annual_salary", "years_experience", "total_spend",
    "num_orders", "website_visits", "avg_order_value", "spend_per_visit"
]
categorical = ["city", "education"]

preprocess = ColumnTransformer([
    ("num", StandardScaler(), numeric),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical)
])

pipeline = Pipeline([
    ("feature_engineering", FeatureEngineer()),
    ("preprocessing", preprocess),
    ("model", LogisticRegression(max_iter=1000))
])

pipeline.fit(X_train, y_train)
print("Predictions:", pipeline.predict(X_test))
print("Actual:", y_test.to_numpy())
print("Demo score:", pipeline.score(X_test, y_test))
print("\nDataset is intentionally tiny; score is not meaningful.")
