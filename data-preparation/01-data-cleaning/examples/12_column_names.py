"""12 — Standardize column names."""
import pandas as pd

df = pd.DataFrame(columns=[
    "Customer ID",
    " Full Name ",
    "Annual-Salary",
    "Join Date"
])

print("Before:", df.columns.tolist())

df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(r"[^a-z0-9]+", "_", regex=True)
      .str.strip("_")
)

print("After:", df.columns.tolist())
