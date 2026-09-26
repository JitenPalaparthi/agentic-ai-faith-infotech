"""14 — Write reusable cleaning functions."""
import pandas as pd

def clean_text(series):
    return series.str.strip()

def normalize_customer_data(df):
    out = df.copy()

    out["name"] = clean_text(out["name"]).str.title()
    out["email"] = clean_text(out["email"]).str.lower()
    out["city"] = clean_text(out["city"]).str.title().replace({
        "Bangalore": "Bengaluru"
    })
    out["status"] = clean_text(out["status"]).str.lower()

    out["age"] = pd.to_numeric(out["age"], errors="coerce")
    out["salary"] = pd.to_numeric(out["salary"], errors="coerce")

    invalid_age = (out["age"] < 0) | (out["age"] > 120)
    out.loc[invalid_age, "age"] = pd.NA

    return out

df = pd.read_csv("data/dirty_customers.csv")
clean = normalize_customer_data(df)

print(clean)
