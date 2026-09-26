"""15 — Complete data-cleaning workflow."""
from pathlib import Path
import pandas as pd

INPUT = Path("data/dirty_customers.csv")
OUTPUT = Path("data/clean_customers.csv")

df = pd.read_csv(INPUT)

print("Raw rows:", len(df))

# 1. Preserve raw data; work on a copy.
clean = df.copy()

# 2. Remove exact duplicates.
clean = clean.drop_duplicates()

# 3. Normalize strings.
clean["name"] = clean["name"].str.strip().str.title()
clean["email"] = clean["email"].str.strip().str.lower()
clean["city"] = clean["city"].str.strip().str.title()
clean["status"] = clean["status"].str.strip().str.lower()

# 4. Canonical category mappings.
clean["city"] = clean["city"].replace({"Bangalore": "Bengaluru"})

# 5. Convert numerical columns.
clean["age"] = pd.to_numeric(clean["age"], errors="coerce")
clean["salary"] = pd.to_numeric(clean["salary"], errors="coerce")

# 6. Mark impossible age values as missing.
bad_age = (clean["age"] < 0) | (clean["age"] > 120)
clean.loc[bad_age, "age"] = pd.NA

# 7. Parse dates. Invalid dates become NaT.
clean["join_date"] = pd.to_datetime(
    clean["join_date"],
    errors="coerce",
    format="mixed"
)

# 8. Add a basic email-quality flag.
email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
clean["email_valid"] = clean["email"].str.match(email_pattern, na=False)

# 9. Save clean data separately.
clean.to_csv(OUTPUT, index=False)

print("Clean rows:", len(clean))
print("\nMissing values after cleaning:")
print(clean.isna().sum())

print("\nCleaned data:")
print(clean)

print("\nSaved to:", OUTPUT)
