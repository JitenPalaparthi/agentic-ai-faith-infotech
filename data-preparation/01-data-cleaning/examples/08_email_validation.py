"""08 — Basic email-format validation.

This checks a practical pattern, not whether an email account actually exists.
"""
import pandas as pd

df = pd.read_csv("data/dirty_customers.csv")
df["email"] = df["email"].str.strip().str.lower()

pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
valid = df["email"].str.match(pattern, na=False)

print("Invalid or missing emails:")
print(df.loc[~valid, ["customer_id", "email"]])

df["email_valid"] = valid
print("\nWith validation flag:")
print(df[["email", "email_valid"]])
