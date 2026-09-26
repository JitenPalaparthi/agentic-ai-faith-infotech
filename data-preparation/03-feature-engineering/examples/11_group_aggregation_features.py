"""11 — Group aggregation features.

Demonstration only: aggregates must obey prediction-time boundaries.
"""
import pandas as pd
df = pd.read_csv("data/customers.csv")

city_stats = (
    df.groupby("city")["total_spend"]
      .agg(["mean", "median", "count"])
      .rename(columns={
          "mean": "city_mean_spend",
          "median": "city_median_spend",
          "count": "city_customer_count"
      })
)

out = df.merge(city_stats, on="city", how="left")
print(out[["city", "total_spend", "city_mean_spend",
           "city_median_spend", "city_customer_count"]])

print("""
WARNING:
For actual model evaluation, learn group statistics from the training fold only.
For time-dependent problems, use only historical information available before
the prediction timestamp.
""")
