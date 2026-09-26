"""03 — Exact duplicates and duplicate keys."""
import pandas as pd

df = pd.read_csv("data/dirty_customers.csv")

print("Exact duplicate rows:")
print(df[df.duplicated(keep=False)])

print("\nNumber of exact duplicate rows:", df.duplicated().sum())

no_exact_duplicates = df.drop_duplicates()
print("Rows before:", len(df))
print("Rows after exact de-duplication:", len(no_exact_duplicates))

print("\nDuplicate customer IDs:")
print(df[df.duplicated(subset=["customer_id"], keep=False)])

print("""
Important:
An exact duplicate is easier to handle.
Repeated business keys can represent:
- accidental duplication
- updates
- multiple legitimate events
- conflicting records

Use domain rules before dropping by key.
""")
