"""06 — Standardize inconsistent categorical values."""
import pandas as pd

df = pd.read_csv("data/dirty_customers.csv")

print("Cities before:")
print(df["city"].value_counts(dropna=False))

# First normalize spacing/case.
df["city"] = df["city"].str.strip().str.title()

# Then apply known canonical mappings.
city_map = {
    "Bangalore": "Bengaluru"
}
df["city"] = df["city"].replace(city_map)

df["status"] = df["status"].str.strip().str.lower()

print("\nCities after:")
print(df["city"].value_counts(dropna=False))

print("\nStatuses after:")
print(df["status"].value_counts(dropna=False))
