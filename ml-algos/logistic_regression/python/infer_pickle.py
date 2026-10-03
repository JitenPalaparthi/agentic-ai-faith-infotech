import joblib
import pandas as pd
model = joblib.load('../logistic_regression_model.pkl')
x = pd.DataFrame([[18.0, 760, 0.18, 8.0, 12.0]], columns=['annual_income_lakh','credit_score','debt_ratio','employment_years','loan_amount_lakh'])
p = model.predict_proba(x)[0, 1]
print(f'Approval probability: {p:.4f}')


print('Prediction:', 1 if p >= 0.5 else 0)
