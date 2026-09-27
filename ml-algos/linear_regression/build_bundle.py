import csv, random, math, pickle, json, os
from pathlib import Path
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

ROOT=Path('/mnt/data/linear_regression_bundle'); ROOT.mkdir(exist_ok=True)
random.seed(42); np.random.seed(42)
# Synthetic data in INR lakhs
rows=[]
for i in range(1,10001):
    area=random.randint(500,3500); beds=random.randint(1,5); age=random.randint(0,30); dist=round(random.uniform(1,35),2)
    noise=random.gauss(0,5)
    price=round(12 + 0.045*area + 7.5*beds - 0.65*age - 1.15*dist + noise,2)
    rows.append([i,area,beds,age,dist,max(price,8)])
with open(ROOT/'house_prices_10000.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['id','area_sqft','bedrooms','age_years','distance_city_km','price_lakhs']); w.writerows(rows)
X=np.array([[r[1],r[2],r[3],r[4]] for r in rows],dtype=np.float32); y=np.array([r[5] for r in rows],dtype=np.float32)
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,random_state=42)
model=LinearRegression().fit(Xtr,ytr); pred=model.predict(Xte)
with open(ROOT/'linear_regression_model.pkl','wb') as f: pickle.dump(model,f)
metrics={'features':['area_sqft','bedrooms','age_years','distance_city_km'],'intercept':float(model.intercept_),'coefficients':[float(x) for x in model.coef_], 'rmse':float(mean_squared_error(yte,pred)**0.5),'r2':float(r2_score(yte,pred))}
(ROOT/'model_metrics.json').write_text(json.dumps(metrics,indent=2))
with open(ROOT/'sample_predictions.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['area_sqft','bedrooms','age_years','distance_city_km','actual_price_lakhs','predicted_price_lakhs','residual'])
    for a,b,c in zip(Xte[:25],yte[:25],pred[:25]): w.writerow([*map(float,a),float(b),round(float(c),3),round(float(b-c),3)])
print(metrics)
