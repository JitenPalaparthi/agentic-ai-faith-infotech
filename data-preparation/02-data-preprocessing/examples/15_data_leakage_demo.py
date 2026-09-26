"""15 — Why fit preprocessing only on training data?

The test set represents unseen future data. If its statistics influence
preprocessing during training/evaluation, information has leaked.
"""
import numpy as np
from sklearn.preprocessing import StandardScaler

train = np.array([[10.], [20.], [30.]])
test = np.array([[1000.]])

correct = StandardScaler().fit(train)
wrong = StandardScaler().fit(np.vstack([train, test]))

print("Training-only mean:", correct.mean_[0])
print("Leaky full-data mean:", wrong.mean_[0])

print("\nCorrect transformed test:", correct.transform(test).ravel())
print("Leaky transformed test:  ", wrong.transform(test).ravel())

print("\nUse Pipeline + train/test split/CV to keep preprocessing inside training.")
