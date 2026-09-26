"""14 — Feature engineering vs feature selection."""
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif

df = pd.read_csv("data/customers.csv")

# ENGINEERING: create new features.
df["avg_order_value"] = df["total_spend"] / df["num_orders"]
df["spend_per_visit"] = df["total_spend"] / df["website_visits"]

features = [
    "age", "annual_salary", "years_experience", "total_spend",
    "num_orders", "website_visits", "avg_order_value", "spend_per_visit"
]
X = df[features]
y = df["bought"]

# SELECTION: choose a subset from available features.
selector = SelectKBest(score_func=f_classif, k=4)
selector.fit(X, y)

scores = pd.DataFrame({
    "feature": features,
    "score": selector.scores_,
    "selected": selector.get_support()
}).sort_values("score", ascending=False)

print(scores)
print("\nEngineering creates features; selection chooses among features.")
