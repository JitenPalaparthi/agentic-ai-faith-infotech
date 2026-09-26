"""05 — Strip whitespace and normalize text."""
import pandas as pd

df = pd.read_csv("data/dirty_customers.csv")

print("Names before:")
print(df["name"].tolist())

df["name"] = df["name"].str.strip().str.title()

print("\nNames after strip + title:")
print(df["name"].tolist())

print("\nEmails before:")
print(df["email"].tolist())

df["email"] = df["email"].str.strip().str.lower()

print("\nEmails after:")
print(df["email"].tolist())
