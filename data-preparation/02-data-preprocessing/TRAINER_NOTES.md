# Trainer Notes

## Session 1 — What is a transformer?

Start with `01_fit_transform_basics.py`.

Explain:

- `fit(X)` learns parameters from data.
- `transform(X)` uses already learned parameters.
- `fit_transform(X)` performs both.
- An estimator predicts; a transformer changes representation. Some sklearn objects participate in both patterns.

Ask learners: **What exactly does StandardScaler learn during fit?**

Answer: per-feature statistics such as mean and variance/scale.

---

## Session 2 — Missing values

Use examples 02–05.

### SimpleImputer
Start here because it makes the idea of learned preprocessing obvious.

Mean example:

`[10, 20, NaN, 30] -> mean = 20 -> [10,20,20,30]`

Median is generally more robust than mean when extreme values/skew strongly affect the mean.

### KNNImputer
Explain that similarity among rows is used. Discuss distance and why scaling can matter.

### IterativeImputer
Explain it as multivariate/model-based imputation. Avoid presenting predicted missing values as known truth.

### MissingIndicator
Missingness can itself contain signal. Whether that signal is useful is a modeling question.

---

## Session 3 — Scaling

Use `06_scalers.py`.

Write on board:

`StandardScaler: z = (x - mean) / standard deviation`

`RobustScaler: (x - median) / IQR`

`MinMaxScaler: (x - min) / (max - min)` for the default [0,1] range.

Important discussion: scaling is particularly important for distance-based and scale-sensitive methods such as KNN, K-Means, SVM, PCA, and regularized linear models. Decision trees and many tree ensembles are generally invariant to monotonic rescaling of individual features.

---

## Session 4 — Categories

Use `07_categorical_encoders.py`.

Nominal:
`Delhi, Mumbai, Chennai` — no meaningful order -> OneHotEncoder.

Ordinal:
`Low < Medium < High` — meaningful order -> OrdinalEncoder.

Target:
`Spam / Not Spam` -> LabelEncoder if encoding is required.

Stress `handle_unknown="ignore"` for OneHotEncoder when inference may contain unseen categories.

---

## Session 5 — Feature transformations

Use examples 08–10.

Do not teach transformations as magic accuracy boosters. Every transformation encodes an assumption about useful representation.

---

## Session 6 — ColumnTransformer

Use `11_column_transformer.py`.

This is the bridge from isolated examples to realistic tabular ML:

Numerical columns:
`impute -> scale`

Categorical columns:
`impute -> encode`

Then combine both matrices.

---

## Session 7 — Pipeline

Use `12_full_pipeline.py` and `15_data_leakage_demo.py`.

Pipeline is essential because the exact same learned preprocessing can be applied during:
- training
- validation/cross-validation
- testing
- inference/production

Show why fitting a scaler/imputer on the complete dataset before evaluation is leakage.

---

## Session 8 — PCA and feature selection

Use examples 13, 14 and 17.

PCA creates **new features/components**.
Feature selection keeps a **subset of features**.

That distinction is important.

---

## Exercises

1. Change SimpleImputer from mean to median and compare.
2. Add an extreme salary and compare StandardScaler vs RobustScaler.
3. Send an unseen city through OneHotEncoder with and without `handle_unknown="ignore"`.
4. Add a new categorical feature to the ColumnTransformer.
5. Replace LogisticRegression with another sklearn estimator.
6. Deliberately create leakage, then repair it with Pipeline.
7. Compare PCA dimensionality reduction with SelectKBest feature selection.
