# Frequently Used Classification Algorithms — Training Bundle

## Goal
Predict whether a customer will churn:
- `0` = customer stays
- `1` = customer churns

Dataset: **15,000 rows**, 8 input features, one binary target.

## Algorithms included
1. Logistic Regression — linear probabilistic classifier; excellent baseline and interpretable.
2. Decision Tree — learns if/else rules; very easy to visualize/explain.
3. Random Forest — combines many decision trees; robust and widely used on tabular data.
4. K-Nearest Neighbors (KNN) — classifies from nearby examples; excellent for teaching distance.
5. Support Vector Machine (SVM) — finds a separating boundary/margin; kernels handle nonlinear boundaries.
6. Gaussian Naive Bayes — Bayes theorem + conditional independence assumption; fast and useful for probabilistic classification.
7. Gradient Boosting — trees are built sequentially to correct previous errors; foundation for the boosting family.

## One common workflow
CSV -> X/features + y/label -> train/test split -> fit classifier -> probability -> threshold -> class -> evaluate -> save -> inference

## Core classification mathematics

### Probability
A classifier may estimate P(y=1 | x).
At threshold 0.5:
- probability >= 0.5 => class 1
- probability < 0.5 => class 0

Changing the threshold changes false positives and false negatives.

### Confusion matrix
                 Predicted 0   Predicted 1
Actual 0              TN            FP
Actual 1              FN            TP

Accuracy = (TP + TN) / (TP + TN + FP + FN)
Precision = TP / (TP + FP)
Recall = TP / (TP + FN)
F1 = 2 * Precision * Recall / (Precision + Recall)

### Decision Tree
A tree asks questions such as:
    satisfaction_score <= 4.2 ?
and repeatedly splits records.

A common split-quality measure is Gini impurity:
    Gini = 1 - sum(p_i^2)

For binary classes with 70% class 0 and 30% class 1:
    Gini = 1 - (0.7^2 + 0.3^2)
         = 1 - (0.49 + 0.09)
         = 0.42
A pure node has Gini = 0.

### Random Forest
Train many decision trees on different bootstrap samples and feature subsets.
Classification is aggregated across trees (conceptually a vote; implementations can aggregate class probabilities).
This reduces the instability/variance of one decision tree.

### KNN
Distance between two records can use Euclidean distance:
    d = sqrt((x1-x2)^2 + (y1-y2)^2 + ...)
Find the K closest training records and use their classes.
Scaling matters because a feature with large numerical units can dominate distance.

### SVM
SVM seeks a decision boundary with a large margin between classes.
For a linear SVM, a boundary can be represented by:
    w.x + b = 0
Kernel SVMs implicitly create nonlinear decision boundaries.

### Naive Bayes
Bayes theorem:
    P(Class|Features) = P(Features|Class) * P(Class) / P(Features)
"Naive" refers to the simplifying conditional-independence assumption between features given the class.

### Gradient Boosting
Build a weak model, inspect its errors, then add another model that helps correct them.
Final prediction combines the sequence of weak learners.
Modern libraries such as XGBoost, LightGBM and CatBoost use sophisticated boosting approaches.

## Why scaling?
Logistic Regression, KNN and SVM are sensitive to feature scale, so this bundle uses StandardScaler in their pipelines.
Tree, Random Forest and Gradient Boosting generally do not require feature standardization.

## Test results generated with this bundle
                 model  accuracy  precision   recall       f1  roc_auc   TN  FP  FN   TP
                05_svm  0.932000   0.889803 0.939236 0.913851 0.967012 1714 134  70 1082
      03_random_forest  0.926333   0.893491 0.917535 0.905353 0.968675 1722 126  95 1057
                04_knn  0.923000   0.878389 0.927951 0.902491 0.961881 1700 148  83 1069
  07_gradient_boosting  0.917333   0.885009 0.901910 0.893379 0.959150 1713 135 113 1039
      02_decision_tree  0.898000   0.837859 0.910590 0.872712 0.946737 1645 203 103 1049
01_logistic_regression  0.888667   0.846610 0.867188 0.856775 0.941308 1667 181 153  999
        06_naive_bayes  0.845000   0.822535 0.760417 0.790257 0.921212 1659 189 276  876

Do NOT choose a classifier only from accuracy.
For churn/fraud/disease-like problems, inspect precision, recall, F1, ROC-AUC and the confusion matrix.

## PKL versus ONNX
PKL/joblib is convenient for Python and preserves sklearn objects.
ONNX is designed for portable inference and is the better format for the Go/C# examples.

The ONNX exporter is included rather than a pre-generated ONNX binary because skl2onnx/onnxruntime availability varies by environment.

## Run
Python:
    cd python
    pip install pandas numpy scikit-learn joblib skl2onnx onnx onnxruntime
    python train_all.py
    python predict_random_forest.py
    python export_random_forest_onnx.py

C#:
    cd csharp
    dotnet restore
    dotnet run

Go:
Install ONNX Runtime native library, configure its shared-library path, then:
    cd go
    go mod tidy
    go run .

## Teaching order
Start with Logistic Regression -> Decision Tree -> Random Forest -> KNN -> Naive Bayes -> SVM -> Gradient Boosting.
Decision Tree and KNN make the mechanics easiest to see; Random Forest/Boosting show how ensembles improve robustness.
