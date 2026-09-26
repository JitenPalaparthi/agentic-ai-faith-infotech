"""04 — Tenure and recency features.

Use a fixed reference date in reproducible training examples.
In production, reference time must match the prediction timestamp.
"""
import pandas as pd
df = pd.read_csv("data/customers.csv")
df["signup_date"] = pd.to_datetime(df["signup_date"])
df["last_purchase_date"] = pd.to_datetime(df["last_purchase_date"])

reference_date = pd.Timestamp("2025-09-01")

df["customer_tenure_days"] = (reference_date - df["signup_date"]).dt.days
df["days_since_last_purchase"] = (
    reference_date - df["last_purchase_date"]
).dt.days

print(df[["signup_date", "last_purchase_date",
          "customer_tenure_days", "days_since_last_purchase"]])
