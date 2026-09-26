"""01 — Inspect before cleaning."""
import pandas as pd

df = pd.read_csv("data/dirty_customers.csv")

print("FIRST ROWS")
print(df.head())

print("\nSHAPE:", df.shape)
print("\nCOLUMN NAMES:", df.columns.tolist())
print("\nDTYPES")
print(df.dtypes)

print("\nINFO")
df.info()

print("\nMISSING VALUES")
print(df.isna().sum())

print("\nNUMERICAL SUMMARY")
print(df.describe(include="all"))

print("\nUNIQUE VALUES PER COLUMN")
print(df.nunique(dropna=False))

print("\nSTATUS COUNTS")
print(df["status"].value_counts(dropna=False))
