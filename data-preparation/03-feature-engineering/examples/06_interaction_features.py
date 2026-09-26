"""06 — Interaction features."""
import pandas as pd
df = pd.read_csv("data/customers.csv")

df["salary_x_experience"] = (
    df["annual_salary"] * df["years_experience"]
)
df["age_x_orders"] = df["age"] * df["num_orders"]

print(df[["annual_salary", "years_experience",
          "salary_x_experience", "age", "num_orders", "age_x_orders"]])

print("""
An interaction represents the combined effect of two variables.
Whether it helps depends on the model and the problem.
""")
