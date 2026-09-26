# Feature Engineering — Step-by-Step Python Training Lab

## What is feature engineering?

Feature engineering is the process of using domain knowledge and mathematical/data transformations to create **useful model inputs (features)** from available data.

```text
RAW DATA
   ↓
DATA CLEANING
   ↓
PREPROCESSING
   ↓
FEATURE ENGINEERING
   ├── derive new numerical features
   ├── extract date/time information
   ├── ratios and rates
   ├── interactions
   ├── bins
   ├── aggregates
   ├── text-derived features
   ├── polynomial features
   └── domain features
   ↓
FEATURE SELECTION / DIMENSION REDUCTION
   ↓
MODEL
```

In practice these stages overlap. Scikit-learn pipelines often combine preprocessing and feature engineering.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run examples from the project root:

```bash
python examples/01_derived_features.py
```

or:

```bash
./run_all.sh
```

## Learning path

1. Derived numerical features
2. Ratios and rates
3. Date/time features
4. Age/tenure/recency features
5. Binning
6. Interaction features
7. Polynomial features
8. Log transformations
9. Categorical combination features
10. Frequency encoding
11. Group aggregation features
12. Text features
13. Domain features
14. Feature selection vs feature engineering
15. Leakage in feature engineering
16. Custom sklearn feature transformer
17. End-to-end feature pipeline
18. Feature names and model-ready output
