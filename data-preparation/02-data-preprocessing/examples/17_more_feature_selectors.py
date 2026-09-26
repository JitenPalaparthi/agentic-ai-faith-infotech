"""17 — SelectFromModel and RFE

Model-based feature selection examples.
"""
from sklearn.datasets import load_breast_cancer
from sklearn.feature_selection import SelectFromModel, RFE
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

X, y = load_breast_cancer(return_X_y=True)

sfm = Pipeline([
    ("scale", StandardScaler()),
    ("select", SelectFromModel(
        LogisticRegression(max_iter=5000),
        threshold="median"
    ))
])
Xt = sfm.fit_transform(X, y)
print("Original features:", X.shape[1])
print("After SelectFromModel:", Xt.shape[1])

# RFE recursively removes less-important features according to an estimator.
rfe = Pipeline([
    ("scale", StandardScaler()),
    ("select", RFE(
        estimator=LogisticRegression(max_iter=5000),
        n_features_to_select=5
    ))
])
Xr = rfe.fit_transform(X, y)
print("After RFE:", Xr.shape[1])
