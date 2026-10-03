import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("outputs/predictions_10000.csv")
plt.figure(figsize=(9,6))
for c,g in df.groupby("kmeans_cluster"):
    plt.scatter(g.annual_income,g.spending_score,s=10,alpha=.45,label=f"Cluster {c}")
plt.xlabel("Annual income"); plt.ylabel("Spending score"); plt.title("K-Means Customer Segments"); plt.legend(); plt.tight_layout(); plt.savefig("outputs/kmeans_clusters.png",dpi=150)
print("Saved outputs/kmeans_clusters.png")
