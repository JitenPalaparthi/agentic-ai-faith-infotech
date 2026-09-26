# Python Data Cleaning — Step-by-Step Training Lab

This bundle teaches **data cleaning before machine-learning preprocessing**.

## What is data cleaning?

Data cleaning is the process of detecting and correcting/removing inaccurate,
incomplete, duplicated, inconsistent, malformed, or otherwise unusable data.

A useful distinction:

```text
RAW DATA
   |
   v
DATA CLEANING
   |-- inspect quality
   |-- missing values
   |-- duplicates
   |-- wrong types
   |-- inconsistent strings/categories
   |-- impossible/invalid values
   |-- malformed dates/emails
   |-- investigate outliers
   v
CLEAN DATA
   |
   v
ML PREPROCESSING
   |-- imputation
   |-- scaling
   |-- encoding
   |-- transformations
   v
FEATURE ENGINEERING / MODELING
```

Cleaning and preprocessing overlap in real projects. The distinction is useful
for teaching: cleaning focuses on **data quality**, while preprocessing focuses
on producing the representation needed by an algorithm.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run from the project root:

```bash
python examples/01_inspect_dirty_data.py
```

Or:

```bash
./run_all.sh
```

## Training order

1. Inspect dirty data
2. Understand missing values
3. Remove duplicates
4. Fix data types
5. Clean strings
6. Standardize categorical values
7. Detect invalid numerical values
8. Detect and validate emails
9. Parse and validate dates
10. Understand outliers with IQR
11. Decide whether to remove/cap/keep outliers
12. Rename and standardize columns
13. Validate ranges and business rules
14. Build reusable cleaning functions
15. Run a complete cleaning pipeline
16. Compare dirty vs clean data
