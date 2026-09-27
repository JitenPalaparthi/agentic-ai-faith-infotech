import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("../loan_approval_12000.csv")
X = df.drop(columns=["approved"])
y = df["approved"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)
model = Pipeline(
    [
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000, random_state=42)),
    ]
)
model.fit(X_train, y_train)
probability = model.predict_proba(X_test)[:, 1]
prediction = (probability >= 0.50).astype(int)
print(classification_report(y_test, prediction))
print("Confusion matrix:\n", confusion_matrix(y_test, prediction))
print("ROC-AUC:", roc_auc_score(y_test, probability))
joblib.dump(model, "../logistic_regression_model.pkl")
