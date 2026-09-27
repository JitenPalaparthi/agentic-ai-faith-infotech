# Trainer Notes — line-by-line mental model

`df = pd.read_csv(...)`
Loads labelled historical examples.

`X = df[FEATURES]`
X contains information given to the classifier.

`y = df["churned"]`
y contains the correct answer used during supervised learning.

`train_test_split(...)`
Keeps some records unseen during training. This is essential for honest evaluation.

`model.fit(X_train, y_train)`
Learning happens here. Each algorithm learns differently: coefficients, tree splits, neighbours, support vectors, distributions, or sequential trees.

`model.predict(X_test)`
Returns the final class, normally 0 or 1.

`model.predict_proba(X_test)[:,1]`
Returns estimated probability for class 1 when the estimator supports probabilities.

`confusion_matrix(...)`
Counts TN, FP, FN and TP rather than hiding errors behind one accuracy number.

`joblib.dump(...)`
Serializes the Python model for later Python inference.

ONNX export
Converts a supported trained estimator into a portable computation graph. Go/C# load that graph with ONNX Runtime; they do not retrain it.
