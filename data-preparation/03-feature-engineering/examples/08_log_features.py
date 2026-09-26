"""08 — Log transformation as feature engineering."""
import numpy as np
import pandas as pd
df = pd.read_csv("data/customers.csv")

df["log_total_spend"] = np.log1p(df["total_spend"])
df["log_salary"] = np.log1p(df["annual_salary"])

print(df[["total_spend", "log_total_spend",
          "annual_salary", "log_salary"]])

print("""
log1p(x) = log(1+x)
It safely handles zero for non-negative features.
A log feature compresses large positive values and can help represent
multiplicative/right-skewed relationships. Validate rather than applying blindly.
""")
