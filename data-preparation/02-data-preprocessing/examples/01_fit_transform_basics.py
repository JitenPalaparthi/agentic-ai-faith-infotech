"""01 — fit(), transform(), fit_transform()

fit(): learns parameters.
transform(): applies what was learned.
fit_transform(): fit + transform, normally used on training data.
"""
import numpy as np
from sklearn.preprocessing import StandardScaler

X_train = np.array([[10.0], [20.0], [30.0]])
X_test = np.array([[40.0]])

scaler = StandardScaler()

# Learn mean and standard deviation ONLY from training data.
scaler.fit(X_train)
print("Learned mean:", scaler.mean_)
print("Learned variance:", scaler.var_)

print("\nTraining transformed:")
print(scaler.transform(X_train))

# Important: transform test data with the SAME fitted scaler.
print("\nTest transformed:")
print(scaler.transform(X_test))

print("\nEquivalent training operation:")
print(StandardScaler().fit_transform(X_train))
