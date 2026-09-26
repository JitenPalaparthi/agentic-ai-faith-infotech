"""07 — OneHotEncoder, OrdinalEncoder and LabelEncoder"""
import numpy as np
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, LabelEncoder

cities = np.array([["Delhi"], ["Mumbai"], ["Chennai"], ["Delhi"]])
onehot = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
print("One-hot categories:", onehot.fit(cities).categories_)
print(onehot.transform(cities))

education = np.array([["Bachelor"], ["Master"], ["PhD"], ["Bachelor"]])
ordinal = OrdinalEncoder(categories=[["Bachelor", "Master", "PhD"]])
print("\nOrdinal encoding:")
print(ordinal.fit_transform(education))

target = np.array(["No", "Yes", "No", "Yes"])
labels = LabelEncoder()
print("\nTarget LabelEncoder:")
print(labels.fit_transform(target))
print("Classes:", labels.classes_)

print("""
Rule of thumb:
Nominal X -> OneHotEncoder
Ordered X -> OrdinalEncoder
Target y  -> LabelEncoder (when target labels need encoding)
""")
