import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

FEATURES = ["monthly_spend","tenure_months","support_calls","usage_hours_week",
            "late_payments","satisfaction_score","num_products","discount_percent"]

df = pd.read_csv("../data/customer_churn_15000.csv")
X = df[FEATURES]
y = df["churned"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

models = {
    "logistic_regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000))
    ]),
    "decision_tree": DecisionTreeClassifier(max_depth=7, min_samples_leaf=10, random_state=42),
    "random_forest": RandomForestClassifier(n_estimators=150, max_depth=12, random_state=42),
    "knn": Pipeline([("scaler", StandardScaler()), ("model", KNeighborsClassifier(n_neighbors=9))]),
    "svm": Pipeline([("scaler", StandardScaler()), ("model", SVC(kernel="rbf", probability=True))]),
    "naive_bayes": GaussianNB(),
    "gradient_boosting": GradientBoostingClassifier(n_estimators=120, learning_rate=0.06, random_state=42),
}

for name, model in models.items():
    print("\n==========", name, "==========")
    model.fit(X_train, y_train)             # Learn patterns from labelled training records
    prediction = model.predict(X_test)      # Predict class 0 or 1
    probability = model.predict_proba(X_test)[:, 1]  # Probability of churn class
    print(confusion_matrix(y_test, prediction))
    print(classification_report(y_test, prediction))
    print("ROC-AUC:", roc_auc_score(y_test, probability))
    joblib.dump(model, "../models/" + name + ".pkl")
