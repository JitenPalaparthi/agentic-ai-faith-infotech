"""02 — Ratios and rates."""
import numpy as np
import pandas as pd
df = pd.read_csv("data/customers.csv")

# Avoid division by zero explicitly.
df["avg_order_value"] = np.where(
    df["num_orders"] > 0,
    df["total_spend"] / df["num_orders"],
    np.nan
)
df["spend_per_visit"] = np.where(
    df["website_visits"] > 0,
    df["total_spend"] / df["website_visits"],
    np.nan
)
df["orders_per_visit"] = np.where(
    df["website_visits"] > 0,
    df["num_orders"] / df["website_visits"],
    np.nan
)

print(df[["total_spend", "num_orders", "website_visits",
          "avg_order_value", "spend_per_visit", "orders_per_visit"]])
