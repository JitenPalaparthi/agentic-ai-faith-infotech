import pandas as pd
import numpy as np

df = pd.read_csv("data/dirty_customers.csv")

print("Missing count:")
print(df.isna().sum())

print("\nMissing percentage:")
print((df.isna().mean() * 100).round(2))

print("\nRows containing at least one missing value:")
print(df[df.isna().any(axis=1)])

# ---------------------------------------------------------
# Clean Invalid Age (<= 0 or >= 120) using .loc
# ---------------------------------------------------------
# Ensure age is numeric (converts any text errors to NaN)
df["age"] = pd.to_numeric(df["age"], errors="coerce")

# Replace impossible ages (<= 0 or >= 120) with NaN
df.loc[(df["age"] <= 0) | (df["age"] >= 120), "age"] = np.nan

print("\nAge after replacing invalid values (<= 0 or >= 120) with NaN:")
print(df[["name", "age"]])

# ---------------------------------------------------------
# Demo: Sentinel replacement using .loc
# ---------------------------------------------------------
demo = pd.DataFrame({
    "value": ["100", "N/A", "unknown", "?", "", None]
})

demo["cleaned"] = demo["value"]
sentinels = ["N/A", "unknown", "?", ""]
demo.loc[demo["cleaned"].isin(sentinels), "cleaned"] = np.nan

print("\nSentinel values -> NaN:")
print(demo)
