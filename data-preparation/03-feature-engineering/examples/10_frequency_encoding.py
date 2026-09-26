"""10 — Frequency encoding.

Replace a category with how frequently it occurs in the TRAINING data.
"""
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/customers.csv")
train, test = train_test_split(df, test_size=.25, random_state=42)

freq = train["city"].value_counts(normalize=True)

train["city_frequency"] = train["city"].map(freq)
test["city_frequency"] = test["city"].map(freq).fillna(0)

print("Learned training frequencies:")
print(freq)
print("\nTest encoding:")
print(test[["city", "city_frequency"]])

print("\nImportant: mapping was learned from TRAINING data, not test data.")
