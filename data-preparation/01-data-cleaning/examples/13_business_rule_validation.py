"""13 — Validate explicit business rules."""
import pandas as pd

df = pd.read_csv("data/dirty_customers.csv")
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

rules = pd.DataFrame(index=df.index)
rules["age_valid"] = df["age"].isna() | df["age"].between(0, 120)
rules["salary_valid"] = df["salary"].isna() | (df["salary"] >= 0)
rules["customer_id_present"] = df["customer_id"].notna()

rules["row_valid"] = rules.all(axis=1)

print(pd.concat([df[["customer_id", "age", "salary"]], rules], axis=1))

print("\nRows failing at least one rule:")
print(df.loc[~rules["row_valid"]])

print("""
Validation is strongest when rules come from a data contract:
type, allowed range, allowed categories, uniqueness, nullability, format, etc.
""")
