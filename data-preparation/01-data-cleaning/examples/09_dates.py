"""09 — Parse and validate dates."""
import pandas as pd

df = pd.read_csv("data/dirty_customers.csv")

print("Original dates:")
print(df["join_date"])

# mixed allows pandas to infer formats element-by-element.
df["join_date_parsed"] = pd.to_datetime(
    df["join_date"],
    errors="coerce",
    format="mixed",
    dayfirst=False
)

print("\nParsed dates:")
print(df[["join_date", "join_date_parsed"]])

print("\nInvalid dates became NaT:")
print(df[df["join_date_parsed"].isna()][["customer_id", "join_date"]])

print("""
Dates are dangerous when formats are ambiguous.
For example 10/02/2024 could mean October 2 or February 10.
Prefer explicit source formats when the contract is known.
""")
