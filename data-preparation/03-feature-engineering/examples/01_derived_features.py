"""01 — Create simple derived numerical features."""
import pandas as pd
df = pd.read_csv("data/customers.csv")

df["monthly_salary"] = df["annual_salary"] / 12
df["career_start_age"] = df["age"] - df["years_experience"]

print(df[["annual_salary", "monthly_salary", "age",
          "years_experience", "career_start_age"]])

print("""
A derived feature expresses existing information in a potentially more useful form.
Always ask whether the derived feature has domain meaning.
""")
