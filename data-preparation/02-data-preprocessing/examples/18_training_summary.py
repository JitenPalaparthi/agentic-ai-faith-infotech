"""18 — Quick revision sheet printed from Python"""

print(r"""
SCIKIT-LEARN TRANSFORMER REVISION
=================================

MISSING VALUES
SimpleImputer      -> mean / median / most_frequent / constant
KNNImputer         -> estimate from neighboring samples
IterativeImputer   -> estimate missing features using other features
MissingIndicator   -> add information about where values were missing

SCALING
StandardScaler     -> (x - mean) / standard deviation
MinMaxScaler       -> maps training range, normally to [0,1]
RobustScaler       -> (x - median) / IQR
MaxAbsScaler       -> x / max(abs(x))

CATEGORICAL
OneHotEncoder      -> nominal categories
OrdinalEncoder     -> ordered categories
LabelEncoder       -> target labels

FEATURE ENGINEERING
PolynomialFeatures -> powers and interactions
FunctionTransformer-> custom callable transformation
PowerTransformer   -> Yeo-Johnson / Box-Cox
QuantileTransformer-> rank/quantile based nonlinear mapping
Binarizer          -> threshold to 0/1
KBinsDiscretizer   -> continuous -> bins
Normalizer         -> normalize each sample/vector

COMPOSITION
ColumnTransformer  -> transformations by column
Pipeline           -> chain preprocessing and estimator

DIMENSION / SELECTION
PCA                -> new lower-dimensional components
VarianceThreshold  -> remove low-variance features
SelectKBest        -> select by univariate score
SelectFromModel    -> model-based selection
RFE                -> recursive feature elimination

MOST IMPORTANT PRACTICE
Split data first and fit preprocessing only on training data.
Use Pipeline to reduce leakage risk and keep training/inference consistent.
""")
