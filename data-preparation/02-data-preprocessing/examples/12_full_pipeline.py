"""12 — Complete preprocessing + LogisticRegression Pipeline

Key production lesson:
Split first. Fit the pipeline on training data only.
The pipeline learns imputation/scaling/categories from training data.
"""
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.read_csv("data/employees.csv")

X = df.drop(columns="bought")
y = df["bought"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42, stratify=y
)

numeric = ["age", "salary", "experience"]
categorical = ["city", "education"]

numeric_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_pipe, numeric),
    ("cat", categorical_pipe, categorical)
])

model = Pipeline([
    ("preprocessing", preprocessor),
    ("model", LogisticRegression())
])

model.fit(X_train, y_train)

print("Predictions:", model.predict(X_test))
print("Actual:     ", y_test.to_numpy())
print("Score (tiny demo dataset only):", model.score(X_test, y_test))

new_employee = pd.DataFrame([{
    "age": 33,
    "salary": 52000,
    "experience": 7,
    "city": "Pune",          # unseen city: handle_unknown='ignore'
    "education": "Master"
}])

print("\nNew employee prediction:", model.predict(new_employee))
