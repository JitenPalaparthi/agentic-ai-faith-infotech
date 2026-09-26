"""09 — Combine categorical information."""
import pandas as pd
df = pd.read_csv("data/customers.csv")

df["city_education"] = (
    df["city"].astype(str) + "_" + df["education"].astype(str)
)

print(df[["city", "education", "city_education"]])

print("""
Combined categories can expose interactions, but may create high cardinality.
For large-cardinality columns, monitor the number of unique combinations.
""")
