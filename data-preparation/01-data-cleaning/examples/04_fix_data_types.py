"""04 — Convert columns to correct data types."""
import pandas as pd

df = pd.read_csv("data/dirty_customers.csv")

print("Before:")
print(df.dtypes)

# Invalid numeric tokens become NaN rather than crashing.
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

print("\nAfter numeric conversion:")
print(df.dtypes)
print(df[["age", "salary"]])

print("""
errors='coerce' is powerful:
valid number -> number
invalid token -> NaN

But always inspect what was coerced; otherwise data problems can be hidden.
""")
