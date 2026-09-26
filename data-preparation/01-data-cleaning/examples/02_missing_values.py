"""02 — Find and understand missing values."""
import pandas as pd
import numpy as np

df = pd.read_csv("data/dirty_customers.csv")

print("Missing count:")
print(df.isna().sum())

print("\nMissing percentage:")
print((df.isna().mean() * 100).round(2))

print("\nRows containing at least one missing value:")
print(df[df.isna().any(axis=1)])

# Convert selected sentinel text values to true missing values.
demo = pd.DataFrame({
    "value": ["100", "N/A", "unknown", "?", "", None]
})

demo["cleaned"] = demo["value"].replace(
    ["N/A", "unknown", "?", ""],
    np.nan
)

print("\nSentinel values -> NaN:")
print(demo)

print("""
Teaching point:
Finding missing data is cleaning.
Filling missing data is often called imputation and overlaps with preprocessing.
Do not automatically fill every missing value without understanding the column.
""")
