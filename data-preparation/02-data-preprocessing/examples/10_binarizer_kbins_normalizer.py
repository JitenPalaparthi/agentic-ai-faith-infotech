"""10 — Binarizer, KBinsDiscretizer, Normalizer"""
import numpy as np
from sklearn.preprocessing import Binarizer, KBinsDiscretizer, Normalizer

X = np.array([[20.], [40.], [60.], [90.]])
print("Binarizer threshold=50:")
print(Binarizer(threshold=50).fit_transform(X).ravel())

ages = np.array([[18.], [23.], [35.], [42.], [57.], [68.]])
kb = KBinsDiscretizer(n_bins=3, strategy="quantile", encode="ordinal")
print("\nAge quantile bins:")
print(kb.fit_transform(ages).ravel())
print("Bin edges:", kb.bin_edges_)

vectors = np.array([[3., 4.], [5., 12.]])
print("\nL2 row normalization:")
print(Normalizer(norm="l2").fit_transform(vectors))
