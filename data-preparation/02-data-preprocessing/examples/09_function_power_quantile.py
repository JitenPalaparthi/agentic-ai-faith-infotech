"""09 — FunctionTransformer, PowerTransformer, QuantileTransformer"""
import numpy as np
from sklearn.preprocessing import FunctionTransformer, PowerTransformer, QuantileTransformer

X = np.array([[1.], [2.], [3.], [10.], [100.]])

log_transform = FunctionTransformer(np.log1p, feature_names_out="one-to-one")
print("log1p:\n", log_transform.fit_transform(X).ravel())

power = PowerTransformer(method="yeo-johnson")
print("\nYeo-Johnson:\n", power.fit_transform(X).ravel())

quantile = QuantileTransformer(
    n_quantiles=len(X),
    output_distribution="normal",
    random_state=42
)
print("\nQuantile -> normal:\n", quantile.fit_transform(X).ravel())

print("\nThese are nonlinear transformations; validate their effect rather than applying automatically.")
