# Feature Engineering — Quick Revision

## Definition

**Feature engineering** creates or derives useful model inputs from available data.

## Common techniques

| Technique | Example |
|---|---|
| Arithmetic feature | `monthly_salary = annual_salary / 12` |
| Ratio | `average_order_value = spend / orders` |
| Rate | `orders_per_visit = orders / visits` |
| Date extraction | month, weekday, quarter |
| Recency | days since last purchase |
| Tenure | days since signup |
| Binning | age → age group |
| Interaction | salary × experience |
| Polynomial | x², x1×x2 |
| Log feature | log(1 + spend) |
| Category combination | city + education |
| Frequency encoding | category → training frequency |
| Aggregation | historical group mean/count |
| Text features | word count, TF-IDF |
| Domain feature | business-specific ratio |

## Feature engineering vs preprocessing

```text
Preprocessing:
"How do I make the data usable/appropriate for the algorithm?"

Feature engineering:
"Can I represent the information in a more useful way?"
```

They often overlap.

## Feature engineering vs selection

```text
Feature Engineering -> CREATE / DERIVE features
Feature Selection   -> CHOOSE features
PCA                 -> CREATE lower-dimensional components
```

## Leakage rule

Before creating any feature, ask:

> **Would this information exist at prediction time?**

If not, it should not be used.

## Practical principle

Do not create features merely because you can. A feature should have a statistical, temporal, or domain rationale, and its value should be validated using proper train/validation methodology.
