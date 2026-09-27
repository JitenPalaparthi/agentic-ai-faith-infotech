import numpy as np
from sklearn.linear_model import LinearRegression
X=np.array([[1],[2],[3],[4],[5]],dtype=float)
y=np.array([2,3,5,4,6],dtype=float)
m=LinearRegression().fit(X,y)
print("intercept",m.intercept_,"slope",m.coef_[0])
print("prediction for x=4",m.predict([[4]])[0])
