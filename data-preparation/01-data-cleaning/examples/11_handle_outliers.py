"""11 — Common outlier decisions: keep, remove, or cap."""
import pandas as pd

df = pd.read_csv("data/dirty_customers.csv")
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

q1 = df["salary"].quantile(.25)
q3 = df["salary"].quantile(.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

print("Original salaries:")
print(df["salary"])

# OPTION 1: Keep them after investigation.
kept = df.copy()

# OPTION 2: Remove flagged observations.
removed = df[df["salary"].between(lower, upper) | df["salary"].isna()].copy()

# OPTION 3: Cap/winsorize to the IQR fences for demonstration.
capped = df.copy()
capped["salary"] = capped["salary"].clip(lower=lower, upper=upper)

print("\nAfter removal, rows:", len(removed))
print("\nCapped salaries:")
print(capped["salary"])

print("\nThere is no universally correct outlier treatment. Use domain and modeling context.")
