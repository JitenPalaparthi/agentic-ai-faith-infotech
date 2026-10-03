import joblib
import pandas as pd
FEATURES=["age","annual_income","spending_score","monthly_visits","monthly_purchases"]
sample=pd.DataFrame([[29,48000,82,8,11]],columns=FEATURES)
km=joblib.load("models/kmeans_pipeline.pkl")
iso=joblib.load("models/isolation_forest_pipeline.pkl")
print("Input:", sample.to_dict(orient="records")[0])
print("K-Means cluster:", int(km.predict(sample)[0]))
print("Isolation Forest prediction (1=normal, -1=anomaly):", int(iso.predict(sample)[0]))
print("Isolation Forest score:", float(iso.decision_function(sample)[0]))
