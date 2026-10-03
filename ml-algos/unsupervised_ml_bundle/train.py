import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest

FEATURES=["age","annual_income","spending_score","monthly_visits","monthly_purchases"]
df=pd.read_csv("data/customers_10000.csv")
X=df[FEATURES]
kmeans=Pipeline([("scaler",StandardScaler()),("model",KMeans(n_clusters=4,random_state=42,n_init=10))])
kmeans.fit(X)
joblib.dump(kmeans,"models/kmeans_pipeline.pkl")
iso=Pipeline([("scaler",StandardScaler()),("model",IsolationForest(contamination=0.01,random_state=42))])
iso.fit(X)
joblib.dump(iso,"models/isolation_forest_pipeline.pkl")
print("Models trained and saved.")
