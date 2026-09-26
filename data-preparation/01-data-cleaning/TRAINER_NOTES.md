# Trainer Notes — Data Cleaning

## Core teaching message

Do not start by deleting rows.

Start with:

> **What is wrong with the data, why is it wrong, and what does the domain say the correct action should be?**

A missing value, an outlier, and an invalid value are different problems.

### Missing
`age = NaN`

We do not know the age.

### Invalid
`age = -5`

We have a value, but it violates the expected domain.

### Outlier
`salary = 9,999,999`

It may be wrong, or it may be a genuine high salary. Investigate before removing it.

---

## Recommended classroom sequence

### 1. Inspect first

Use:
- `head()`
- `shape`
- `columns`
- `dtypes`
- `info()`
- `describe()`
- `isna().sum()`
- `nunique()`
- `value_counts()`

### 2. Missing values

Teach learners to distinguish:
- actual `NaN`
- empty strings
- sentinel strings such as `N/A`, `NA`, `unknown`, `?`

Pandas may automatically interpret some tokens as missing while reading CSV.

### 3. Duplicates

Discuss:
- exact row duplicates
- duplicate business keys
- conflicting duplicates

`customer_id` repeated twice may require different logic from an exactly repeated row.

### 4. Types

A numeric-looking column can become `object` because of one bad token.
Use `pd.to_numeric(..., errors="coerce")` deliberately.

### 5. Text normalization

Whitespace and capitalization frequently create false categories:

`Hyderabad`, ` hyderabad `, `HYDERABAD`

These should often map to one canonical category.

### 6. Invalid values

Domain rules matter.

Examples:
- age < 0 -> invalid
- percentage > 100 -> often invalid
- quantity < 0 -> perhaps invalid, unless negatives represent returns

Never invent business rules without domain knowledge.

### 7. Outliers

Teach IQR:

`IQR = Q3 - Q1`

Lower fence:

`Q1 - 1.5 * IQR`

Upper fence:

`Q3 + 1.5 * IQR`

An IQR flag identifies unusual values; it does **not prove that they are errors**.

### 8. Dates

`pd.to_datetime(..., errors="coerce")` is useful because malformed dates become `NaT`, which can then be inspected.

### 9. Reusable workflow

The final examples combine operations into functions and a complete cleaning flow.

---

## Exercises

1. Add `"unknown"` to the city column and convert it to missing.
2. Create two rows with the same ID but different salaries. Decide how to handle them.
3. Add `"forty"` to age and use `pd.to_numeric`.
4. Add multiple spellings of Bengaluru and canonicalize them.
5. Add an age of 150 and flag it using a business rule.
6. Add a very large salary and calculate its IQR status.
7. Add three date formats and normalize them.
8. Add an invalid email and flag it.
9. Build a `clean_customer_data(df)` function.
10. Save the clean dataset separately; never silently overwrite raw source data.
