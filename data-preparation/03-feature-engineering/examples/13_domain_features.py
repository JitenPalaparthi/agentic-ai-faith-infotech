"""13 — Domain-driven features."""
import numpy as np
import pandas as pd
df = pd.read_csv("data/customers.csv")

df["avg_order_value"] = df["total_spend"] / df["num_orders"]
df["engagement_rate"] = df["num_orders"] / df["website_visits"]
df["salary_per_experience_year"] = np.where(
    df["years_experience"] > 0,
    df["annual_salary"] / df["years_experience"],
    np.nan
)

print(df[["avg_order_value", "engagement_rate",
          "salary_per_experience_year"]])

print("""
The best feature engineering is often domain-specific.
A meaningful business ratio can be more useful than a complicated generic transform.
""")
