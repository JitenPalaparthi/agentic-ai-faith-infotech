import joblib
import pandas as pd

FEATURES = ["monthly_spend","tenure_months","support_calls","usage_hours_week",
            "late_payments","satisfaction_score","num_products","discount_percent"]

model = joblib.load("../models/03_random_forest.pkl")

customer = pd.DataFrame([{
    "monthly_spend": 145.0,
    "tenure_months": 12,
    "support_calls": 7,
    "usage_hours_week": 18.0,
    "late_payments": 5,
    "satisfaction_score": 3.0,
    "num_products": 2,
    "discount_percent": 5.0
}])

prediction = model.predict(customer)[0]
probability = model.predict_proba(customer)[0][1]

print("Churn probability:", probability)
print("Predicted class:", prediction)
print("Meaning:", "LIKELY TO CHURN" if prediction == 1 else "LIKELY TO STAY")
