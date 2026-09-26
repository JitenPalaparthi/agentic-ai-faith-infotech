# Data Cleaning — Quick Revision

## What is data cleaning?

**Data cleaning** is the process of identifying and correcting or appropriately handling data-quality problems before analysis or modeling.

## Common problems

| Problem | Example | Typical action |
|---|---|---|
| Missing value | `age = NaN` | investigate, remove, or impute |
| Duplicate | same row twice | identify cause; de-duplicate if appropriate |
| Wrong type | `"50000"` as text | convert type |
| Dirty text | `" Hyderabad "` | strip/normalize |
| Inconsistent category | `Bangalore`, `Bengaluru` | map to canonical value |
| Invalid value | `age = -5` | flag/correct/set missing |
| Malformed date | `not-a-date` | parse/flag |
| Malformed email | `abc@` | validate/flag |
| Outlier | salary `9,999,999` | investigate; keep/remove/cap based on context |

## Essential Pandas operations

```python
df.info()
df.describe(include="all")
df.isna().sum()
df.duplicated()
df.drop_duplicates()
pd.to_numeric(..., errors="coerce")
pd.to_datetime(..., errors="coerce")
series.str.strip()
series.str.lower()
series.replace(...)
series.value_counts(dropna=False)
```

## Important distinction

```text
MISSING != INVALID != OUTLIER
```

- **Missing**: value is absent.
- **Invalid**: value violates a known rule.
- **Outlier**: value is unusually far from typical observations; it may still be valid.

## IQR

```text
IQR = Q3 - Q1
Lower fence = Q1 - 1.5 * IQR
Upper fence = Q3 + 1.5 * IQR
```

Use IQR to **flag candidates for investigation**, not as automatic proof that rows should be deleted.

## Final principle

> Preserve raw data, make cleaning decisions explicit and reproducible, validate them against domain rules, and save cleaned output separately.
