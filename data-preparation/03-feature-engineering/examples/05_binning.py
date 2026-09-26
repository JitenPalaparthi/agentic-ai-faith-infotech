"""05 — Convert continuous values into bins."""
import pandas as pd
df = pd.read_csv("data/customers.csv")

df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 25, 35, 50, float("inf")],
    labels=["<=25", "26-35", "36-50", "50+"]
)

df["salary_quantile"] = pd.qcut(
    df["annual_salary"],
    q=4,
    labels=["Q1", "Q2", "Q3", "Q4"]
)

print(df[["age", "age_group", "annual_salary", "salary_quantile"]])

print("""
pd.cut  -> domain-defined intervals.
pd.qcut -> intervals based on sample quantiles.
Binning loses numerical detail, so use it only when it has a reason.
""")
