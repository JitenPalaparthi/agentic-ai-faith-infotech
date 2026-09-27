# Linear Regression: Python Training -> Pickle/ONNX -> Go/C# Inference

## What is inside
- `house_prices_10000.csv`: 10,000 synthetic records.
- `linear_regression_model.pkl`: trained Python/scikit-learn model.
- `linear_regression_model.onnx`: portable ONNX model for non-Python inference.
- `model_metrics.json`: coefficients, intercept, RMSE and R².
- `sample_predictions.csv`: actual vs predicted examples.
- `python/`: training and inference.
- `go/`: ONNX Runtime inference example.
- `csharp/`: ONNX Runtime inference example.

## Dataset
We predict `price_lakhs` using four inputs:
1. `area_sqft` — larger houses generally cost more.
2. `bedrooms` — additional bedrooms add value.
3. `age_years` — older houses reduce the synthetic price.
4. `distance_city_km` — farther houses reduce the synthetic price.

The data is synthetic and generated for teaching. It is NOT real property-market data.

## The basic mathematics
For one feature, linear regression is:

`predicted_y = b0 + b1*x`

For this dataset there are four features:

`predicted_price = b0 + b1*area + b2*bedrooms + b3*age + b4*distance`

The trained model in this bundle learned approximately:

`price = 11.9087 + 0.04492*area + 7.50055*bedrooms - 0.63986*age - 1.14062*distance`

For `[1800, 3, 5, 8]`:

- Base/intercept = 11.9087
- Area contribution = 0.04492 * 1800 = 80.8594
- Bedrooms = 7.50055 * 3 = 22.5016
- Age = -0.63986 * 5 = -3.1993
- Distance = -1.14062 * 8 = -9.1249
- Prediction ≈ 102.95 lakhs

### Error / residual
`residual = actual - predicted`

If actual=108 and predicted=103, residual=5 lakhs.

### Why square errors?
Positive and negative errors should not cancel. Squaring also penalizes large mistakes more strongly.

`MSE = sum((actual-predicted)^2) / n`

`RMSE = sqrt(MSE)`

RMSE is convenient because it returns to the target's original unit (lakhs here).

### R²
R² compares the regression model with a simple baseline that always predicts the mean target. R² close to 1 means the model explains much of the variation in this dataset. It does not by itself prove that the model will generalize to unrelated real-world data.

## Training flow, line by line
Open `python/train.py`.

1. `pd.read_csv(...)` loads the 10,000 rows.
2. `features = [...]` defines what information the model may use.
3. `X = ...` creates the input matrix. Each row has four numbers.
4. `y = ...` creates the target vector: the price we want to learn.
5. `train_test_split(...)` keeps 80% for learning and 20% for an unbiased test.
6. `LinearRegression()` creates an untrained estimator.
7. `model.fit(X_train,y_train)` finds coefficients/intercept that minimize squared errors.
8. `model.predict(X_test)` applies the learned equation to unseen test rows.
9. RMSE measures typical prediction error; R² measures explained variation.
10. `pickle.dump(...)` stores the Python model. Pickle is Python-specific and should only be loaded from trusted sources.
11. `to_onnx(...)` converts the fitted estimator to the interoperable ONNX representation.
12. The `.onnx` file can then be loaded by ONNX Runtime from Python, Go, C#, Java, C++, etc.

## Inference flow
Inference means using a trained model, not training again.

`[1800, 3, 5, 8] -> ONNX Runtime -> linear equation -> predicted price`

The feature ORDER is critical. Go and C# must send exactly:
`area_sqft, bedrooms, age_years, distance_city_km`.

## Python
From `python/`:

```bash
pip install numpy pandas scikit-learn skl2onnx onnxruntime
python train.py
python infer_pickle.py
python infer_onnx.py
```

## Go
ONNX Runtime's native shared library must be installed/downloaded for your OS and its path supplied to the Go wrapper. Then from `go/`:

```bash
go mod tidy
go run .
```

Line-by-line logic in `main.go`: initialize ONNX Runtime; create a `[1,4]` float tensor; create a `[1,1]` output tensor; open the model with the exact input/output names; run; read the first prediction.

## C#
From `csharp/`:

```bash
dotnet restore
dotnet run
```

Line-by-line logic: create an `InferenceSession`; allocate `[1,4]`; place four features in training order; name it `float_input`; call `Run`; get `variable`; print its first float.

## Important production lessons
- Never change feature order between training and inference.
- Use the same preprocessing in every language.
- Validate input ranges/types before inference.
- Pickle can execute code while loading: never load an untrusted `.pkl` file.
- ONNX is the portable artifact to prefer for Go/C# inference.
- Real datasets need missing-value handling, categorical encoding, outlier analysis, drift monitoring, and realistic validation.
