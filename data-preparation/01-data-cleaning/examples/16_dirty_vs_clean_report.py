"""16 — Compare data quality before and after cleaning."""
import pandas as pd

raw = pd.read_csv("data/dirty_customers.csv")
clean = raw.copy()

clean = clean.drop_duplicates()
clean["name"] = clean["name"].str.strip().str.title()
clean["email"] = clean["email"].str.strip().str.lower()
clean["city"] = clean["city"].str.strip().str.title().replace({"Bangalore": "Bengaluru"})
clean["status"] = clean["status"].str.strip().str.lower()
clean["age"] = pd.to_numeric(clean["age"], errors="coerce")
clean["salary"] = pd.to_numeric(clean["salary"], errors="coerce")
clean.loc[(clean["age"] < 0) | (clean["age"] > 120), "age"] = pd.NA
clean["join_date"] = pd.to_datetime(clean["join_date"], errors="coerce", format="mixed")

print("DATA QUALITY REPORT")
print("===================")
print("Raw rows:", len(raw))
print("Clean rows:", len(clean))
print("Exact duplicates removed:", len(raw) - len(raw.drop_duplicates()))
print("\nRaw missing values:")
print(raw.isna().sum())
print("\nClean missing/invalid-to-missing values:")
print(clean.isna().sum())
print("\nCanonical cities:")
print(clean["city"].value_counts(dropna=False))
print("\nCanonical statuses:")
print(clean["status"].value_counts(dropna=False))
