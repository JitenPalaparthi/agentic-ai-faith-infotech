# Logistic Regression — End-to-End Training Bundle

## Goal
Predict whether a loan application is approved (`1`) or rejected (`0`) using five numeric features.

Dataset: `loan_approval_12000.csv` (12,000 rows)

Features:
1. `annual_income_lakh`
2. `credit_score`
3. `debt_ratio`
4. `employment_years`
5. `loan_amount_lakh`

Target: `approved` (`0` or `1`). This is a synthetic educational dataset, not a lending policy or real-world approval system.

## 1. Why logistic regression?
Linear regression predicts an unrestricted number. Logistic regression predicts the probability of a class. It computes a linear score:

`z = b0 + b1*x1 + b2*x2 + ... + bn*xn`

Then sigmoid converts the score to a probability:

`p = 1 / (1 + e^(-z))`

If `p >= 0.50`, classify as 1. Otherwise classify as 0.

Example: if `z = 1.5`, then `p = 1/(1+e^-1.5) ≈ 0.818`. The model says about 81.8% probability of class 1.

## 2. What training learns
The model learns `b0, b1, ... bn`. Positive coefficients push the probability toward 1; negative coefficients push it toward 0. Because this example uses `StandardScaler`, coefficients apply to standardized features, not directly to the original units.

Standardization is:

`standardized_x = (x - mean) / standard_deviation`

The pipeline saves both the scaler and logistic model, so inference automatically applies exactly the same transformation.

## 3. Basic maths
### Mean
`mean = sum(values) / count(values)`

### Variance
Measures how spread out values are around the mean.

### Standard deviation
`sigma = sqrt(variance)`

### Linear score
Multiply every input by its learned weight, then add the intercept.

### Sigmoid
Maps any score from `-infinity ... +infinity` into `0 ... 1`.

- z = 0 -> p = 0.5
- positive z -> p > 0.5
- negative z -> p < 0.5

### Log-odds
`log(p/(1-p)) = z`

This is why the algorithm is called logistic regression even though it performs classification.

### Binary cross-entropy / log loss
For one sample:

`loss = -( y*ln(p) + (1-y)*ln(1-p) )`

A confident correct prediction has low loss. A confident wrong prediction is penalized heavily. Training searches for coefficients that minimize the total/average loss.

## 4. Evaluation
Confusion matrix:

- TP: predicted 1, actually 1
- TN: predicted 0, actually 0
- FP: predicted 1, actually 0
- FN: predicted 0, actually 1

`accuracy = (TP + TN) / all`

`precision = TP / (TP + FP)` — when the model says 1, how often is it right?

`recall = TP / (TP + FN)` — of all actual 1s, how many did it find?

`F1 = 2 * precision * recall / (precision + recall)`

ROC-AUC evaluates ranking quality across many possible thresholds.

## 5. Threshold matters
0.50 is not a law. At 0.70 the model needs stronger evidence before returning class 1, usually reducing positive predictions. At 0.30 it returns class 1 more readily. Which threshold is appropriate depends on the business cost of false positives versus false negatives.

## 6. Python training, line by line
`pd.read_csv(...)` loads the 12,000 rows.

`X = df.drop(columns=['approved'])` creates input features.

`y = df['approved']` creates the answer column.

`train_test_split(...)` keeps 80% for learning and 20% for an unseen test.

`StandardScaler()` learns training-set means and standard deviations.

`LogisticRegression(...)` learns the coefficients.

`Pipeline(...)` guarantees scaling happens before prediction both during training and inference.

`model.fit(X_train, y_train)` performs training.

`predict_proba(...)[:,1]` returns P(class=1).

`probability >= 0.50` converts probability into a binary decision.

`joblib.dump(...)` serializes the Python pipeline to PKL.

## 7. PKL vs ONNX
PKL is convenient for Python but is Python-specific and should only be loaded from a trusted source.

ONNX is the portable representation used here for Go and C#. `python/export_onnx.py` converts the trained scikit-learn pipeline to `logistic_regression_model.onnx`.

## 8. Run
Python:

```bash
cd python
python -m venv .venv
source .venv/bin/activate
pip install -r ../requirements.txt
python train.py
python export_onnx.py
python infer_pickle.py
python infer_onnx.py
```

C#:

```bash
cd csharp
dotnet restore
dotnet run
```

Go requires the ONNX Runtime shared library in the path configured in `main.go`, then:

```bash
cd go
go mod tidy
go run .
```

## 9. Production inference flow
`Application -> collect 5 values -> float tensor [1,5] -> ONNX Runtime -> probabilities -> threshold -> class`

No training happens in Go or C#. They only execute the already-trained model.

## 10. Files
- `loan_approval_12000.csv` — dataset
- `logistic_regression_model.pkl` — trained Python pipeline
- `model_metrics.json` — measured test metrics
- `sample_predictions.csv` — example test predictions
- `python/train.py` — training
- `python/export_onnx.py` — ONNX exporter
- `python/infer_pickle.py` — PKL inference
- `python/infer_onnx.py` — ONNX inference
- `go/` — Go ONNX Runtime example
- `csharp/` — C# ONNX Runtime example

Note: the execution environment used to assemble this ZIP did not contain the ONNX Python packages, so the binary `.onnx` file is generated by `export_onnx.py` after installing `requirements.txt`. The trained PKL and measured metrics are already included.


Metric

Question it answers

Accuracy

How many predictions were correct overall?

Precision

When I predicted positive, how often was I right?

Recall

Of all actual positives, how many did I find?

F1

How well am I balancing precision and recall?

Confusion Matrix

Exactly what kinds of correct/wrong predictions did I make?

ROC

How does TPR(True Positive Rate) vs FPR(False Positive Rate) change as I move the threshold?

AUC

How well does the model rank positives above negatives across thresholds?
