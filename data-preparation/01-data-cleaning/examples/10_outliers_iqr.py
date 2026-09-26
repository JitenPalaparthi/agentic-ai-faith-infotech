"""10 — Detect possible outliers using IQR."""
import pandas as pd

df = pd.read_csv("data/dirty_customers.csv")
salary = pd.to_numeric(df["salary"], errors="coerce")

q1 = salary.quantile(0.25)
q3 = salary.quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outlier = (salary < lower) | (salary > upper)

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower fence:", lower)
print("Upper fence:", upper)

print("\nPossible outliers:")
print(df.loc[outlier, ["customer_id", "salary"]])

print("""
CRITICAL:
IQR identifies statistically unusual observations.
It does NOT prove they are wrong.

Investigate before deleting.
""")
