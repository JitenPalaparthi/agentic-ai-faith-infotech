"""07 — Invalid values are not the same as missing values."""
import pandas as pd

df = pd.read_csv("data/dirty_customers.csv")
df["age"] = pd.to_numeric(df["age"], errors="coerce")

# Example business/domain rule for this teaching dataset:
invalid_age = (df["age"] < 0) | (df["age"] > 120)

print("Invalid ages:")
print(df.loc[invalid_age, ["customer_id", "age"]])

# One possible cleaning decision:
# convert impossible values to missing, then decide later whether/how to impute.
df.loc[invalid_age, "age"] = pd.NA

print("\nAfter invalid ages are marked missing:")
print(df[["customer_id", "age"]])

print("""
Do not blindly copy the 0..120 rule to every dataset.
Validation ranges should come from domain/business requirements.
""")
