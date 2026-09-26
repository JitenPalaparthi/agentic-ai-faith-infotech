# Trainer Notes — Feature Engineering

## Central idea

A raw column is not always the best representation of information for a model.

Example:

```text
annual_salary = 1,200,000
```

may be useful, but these derived features may expose additional structure:

```text
monthly_salary = annual_salary / 12
salary_per_year_experience = annual_salary / years_experience
```

Feature engineering is therefore about **representation**.

## Important distinction

### Data cleaning
Fix data-quality problems.

### Preprocessing
Make data usable by an algorithm: scaling, encoding, imputation, etc.

### Feature engineering
Create or derive features that may better express useful signal.

### Feature selection
Choose which features to keep.

---

## Recommended teaching sequence

### Derived features
Start with simple arithmetic because learners immediately understand the purpose.

### Ratios
Explain why a ratio can capture behavior that absolute values do not.

`average_order_value = total_spend / num_orders`

### Dates
A date such as `2025-07-10` is often less directly useful than:
- year
- month
- weekday
- quarter
- tenure
- recency

### Interactions
Sometimes the effect of one feature depends on another.

### Polynomial features
Show `x1*x2`, `x1²`, etc., but emphasize that blindly generating high-degree polynomials can cause dimensional explosion and overfitting.

### Log features
Useful for some strongly right-skewed positive quantities. Do not apply automatically.

### Aggregations
Powerful, but easy to leak target/future information. Aggregates must be constructed using information genuinely available at prediction time.

### Text
Simple text feature engineering can include:
- character count
- word count
- TF-IDF

### Leakage
This is the most important advanced lesson.

Never create a feature using information that would not exist at prediction time.

Bad example:
`days_until_customer_churned`

when predicting whether the customer will churn.

## Classroom question

Ask repeatedly:

> “Would this information be available at the exact moment we make the prediction?”

If no, the feature is likely leakage.

## Exercises

1. Create `spend_per_visit`.
2. Create an `experience_level` category.
3. Extract signup weekday.
4. Create `days_since_last_purchase` relative to a fixed reference date.
5. Combine city and education.
6. Create review word count.
7. Compare raw salary with `log1p(salary)`.
8. Create polynomial interactions for two numerical columns.
9. Write a custom transformer that adds `average_order_value`.
10. Identify three examples of target/future leakage.
