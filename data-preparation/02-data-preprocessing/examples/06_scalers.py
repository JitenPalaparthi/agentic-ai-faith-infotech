"""06 — StandardScaler, MinMaxScaler, RobustScaler, MaxAbsScaler"""
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, MaxAbsScaler

X = np.array([[30000.], [32000.], [35000.], [38000.], [5000000.]])
print("Original:\n", X.ravel())

for scaler in [
    StandardScaler(),
    MinMaxScaler(),
    RobustScaler(),
    MaxAbsScaler()
]:
    print(f"\n{scaler.__class__.__name__}:")
    print(scaler.fit_transform(X).ravel())

print("""
Teaching points:
StandardScaler -> mean 0, variance-based scaling.
MinMaxScaler   -> usually maps observed training range to [0,1].
RobustScaler   -> median/IQR; useful when outliers are a concern.
MaxAbsScaler   -> divide by maximum absolute value; preserves zero/sparsity.
""")
