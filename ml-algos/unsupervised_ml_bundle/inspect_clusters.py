import pandas as pd
df=pd.read_csv("outputs/predictions_10000.csv")
features=["age","annual_income","spending_score","monthly_visits","monthly_purchases"]
print("Cluster sizes:")
print(df.groupby("kmeans_cluster").size())
print("\nCluster feature averages:")
print(df.groupby("kmeans_cluster")[features].mean().round(2))
