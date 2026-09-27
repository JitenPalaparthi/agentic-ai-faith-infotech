"""Train linear regression and export Pickle + ONNX. Run: pip install numpy pandas scikit-learn skl2onnx onnxruntime"""

import pickle

import numpy as np
import pandas as pd
from skl2onnx import to_onnx
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("../house_prices_10000.csv")
features = ["area_sqft", "bedrooms", "age_years", "distance_city_km"]
X = df[features].astype(np.float32)
y = df["price_lakhs"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)
pred = model.predict(X_test)
print("Intercept:", model.intercept_)
print("Coefficients:", dict(zip(features, model.coef_)))
print("RMSE:", mean_squared_error(y_test, pred) ** 0.5)
print("R2:", r2_score(y_test, pred))
with open("../linear_regression_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Take my already-trained scikit-learn model, use one float32 training row to describe/infer the expected input tensor, convert the model into ONNX format, and target the specified ONNX operator-set versions.

onnx_model = to_onnx(
    model,
    X_train[:1].to_numpy(dtype=np.float32),
    target_opset={"": 15, "ai.onnx.ml": 1},
)
open("../linear_regression_model.onnx", "wb").write(onnx_model.SerializeToString())
