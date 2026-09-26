# Scikit-learn Transformers — Step-by-Step Training Lab

This lab teaches preprocessing transformers with small, runnable examples.

## Learning path

1. Understand `fit()`, `transform()`, and `fit_transform()`
2. Handle missing values
3. Scale numerical features
4. Encode categorical features
5. Transform distributions and generate features
6. Apply different transformations to different columns
7. Build a production-style preprocessing + model Pipeline
8. Explore dimensionality reduction and feature selection

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
pip install -r requirements.txt
```

Run examples from the project root:

```bash
python examples/01_fit_transform_basics.py
python examples/02_simple_imputer.py
```

## Core idea

A transformer normally follows:

```python
transformer.fit(X_train)          # learn parameters from training data
X_train_t = transformer.transform(X_train)
X_test_t = transformer.transform(X_test)
```

or:

```python
X_train_t = transformer.fit_transform(X_train)
X_test_t = transformer.transform(X_test)
```

**Never fit preprocessing independently on test/production data.**

## Transformer map

| Topic | Main classes |
|---|---|
| Missing values | SimpleImputer, KNNImputer, IterativeImputer, MissingIndicator |
| Scaling | StandardScaler, MinMaxScaler, RobustScaler, MaxAbsScaler |
| Categories | OneHotEncoder, OrdinalEncoder, LabelEncoder |
| Feature transformations | PolynomialFeatures, FunctionTransformer, PowerTransformer, QuantileTransformer |
| Binning / normalization | Binarizer, KBinsDiscretizer, Normalizer |
| Mixed columns | ColumnTransformer |
| Workflow | Pipeline |
| Dimensionality reduction | PCA |
| Feature selection | VarianceThreshold, SelectKBest, SelectFromModel, RFE |

## Suggested training sequence

Run files `01` through `18` in order. Each example prints the input and transformed output and contains teaching comments.
