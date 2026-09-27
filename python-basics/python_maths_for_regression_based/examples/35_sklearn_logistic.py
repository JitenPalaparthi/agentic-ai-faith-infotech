import numpy as np
from sklearn.linear_model import LogisticRegression
X=np.array([[1],[2],[3],[4],[5],[6]],dtype=float)
y=np.array([0,0,0,1,1,1])
m=LogisticRegression().fit(X,y)
print("intercept",m.intercept_[0],"coefficient",m.coef_[0,0])
print("probabilities",m.predict_proba(X)[:,1])
print("classes",m.predict(X))
