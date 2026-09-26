"""03 — Extract features from dates."""
import pandas as pd
df = pd.read_csv("data/customers.csv")
df["signup_date"] = pd.to_datetime(df["signup_date"])

df["signup_year"] = df["signup_date"].dt.year
df["signup_month"] = df["signup_date"].dt.month
df["signup_day"] = df["signup_date"].dt.day
df["signup_weekday"] = df["signup_date"].dt.dayofweek
df["signup_quarter"] = df["signup_date"].dt.quarter
df["signup_is_weekend"] = df["signup_weekday"].isin([5, 6]).astype(int)

print(df[["signup_date", "signup_year", "signup_month",
          "signup_weekday", "signup_quarter", "signup_is_weekend"]])

print("\nMonday=0 ... Sunday=6 for pandas dayofweek.")
