# Scikit-learn Transformers --- `fit()`, `transform()` and Why We Transform Data

## Question 1: In Example 01, what does this do?

``` python
print("\nTraining transformed:")
print(scaler.transform(X_train))
```

Assume:

``` python
import numpy as np
from sklearn.preprocessing import StandardScaler

X_train = np.array([
    [10.0],
    [20.0],
    [30.0]
])

scaler = StandardScaler()
scaler.fit(X_train)
```

### What does `fit()` learn?

For `StandardScaler`, `fit()` learns statistics from the training data.

The mean is:

\[ `\mu `{=tex}= `\frac{10 + 20 + 30}{3}`{=tex} = 20 \]

The population variance used by `StandardScaler` is:

\[ `\sigma`{=tex}\^2 =
`\frac{(10-20)^2 + (20-20)^2 + (30-20)^2}{3}`{=tex} = 66.6667 \]

Therefore:

\[ `\sigma `{=tex}= `\sqrt{66.6667}`{=tex} `\approx 8.165`{=tex} \]

So the scaler has approximately learned:

``` text
mean  = 20
scale = 8.165
```

You can inspect these learned values:

``` python
print(scaler.mean_)
print(scaler.var_)
print(scaler.scale_)
```

------------------------------------------------------------------------

## Question 2: What happens when we call `transform()`?

``` python
scaler.transform(X_train)
```

`StandardScaler` applies the transformation:

\[ z = `\frac{x-\mu}{\sigma}`{=tex} \]

It uses the mean and scale learned during `fit()`.

### For 10

\[ `\frac{10-20}{8.165}`{=tex} `\approx -1.2247`{=tex} \]

### For 20

\[ `\frac{20-20}{8.165}`{=tex} = 0 \]

### For 30

\[ `\frac{30-20}{8.165}`{=tex} `\approx 1.2247`{=tex} \]

Therefore:

``` python
print(scaler.transform(X_train))
```

returns approximately:

``` text
[[-1.22474487]
 [ 0.        ]
 [ 1.22474487]]
```

Conceptually:

``` text
Original value       Transformed value

10          -------->   -1.2247
20          -------->    0.0000
30          -------->   +1.2247
```

------------------------------------------------------------------------

# Question 3: What exactly do we get after `transform()`?

We get a **new representation of the feature data**.

The original values:

``` text
10
20
30
```

become:

``` text
-1.2247
 0
+1.2247
```

For `StandardScaler`, the transformed number tells us approximately how
many standard deviations a value lies above or below the training mean.

``` text
-1.2247  -> 1.2247 standard deviations below the mean
 0       -> at the mean
+1.2247  -> 1.2247 standard deviations above the mean
```

The underlying observation has not changed. Its **numerical
representation** has changed.

------------------------------------------------------------------------

# Question 4: Why do we transform data?

Consider two features:

``` text
Age        Salary

25         30,000
30         50,000
40         90,000
```

The numerical scales are very different:

``` text
Age     -> tens
Salary  -> tens of thousands
```

Suppose we compare two people:

``` text
Person A:
Age    = 25
Salary = 30,000

Person B:
Age    = 35
Salary = 60,000
```

A Euclidean-distance calculation contains:

\[ `\sqrt{(35-25)^2 + (60000-30000)^2}`{=tex} \]

or:

\[ `\sqrt{10^2 + 30000^2}`{=tex} \]

The salary difference numerically dominates the age difference.

That does **not automatically mean salary is more important**. It can
happen simply because salary is measured using much larger numbers.

After standardization, the features may look more like:

``` text
Age        Salary

-1.1       -0.9
-0.2       -0.1
 1.3        1.2
```

Now both features operate on comparable numerical scales.

This matters especially for scale-sensitive methods such as:

-   K-Nearest Neighbors (KNN)
-   K-Means
-   Support Vector Machines (SVM)
-   PCA
-   Logistic Regression with regularization
-   Linear models with regularization
-   many gradient-based models

Decision Trees and many tree-based ensembles generally do not require
standardization for this reason.

------------------------------------------------------------------------

# Question 5: Does `transform()` calculate everything again?

No.

This distinction is extremely important.

``` python
scaler.fit(X_train)
```

means:

> Learn the required parameters from the training data.

For `StandardScaler`, that includes the training feature mean and scale.

Then:

``` python
scaler.transform(X_train)
```

means:

> Use the parameters already learned and transform this data.

So:

``` text
fit()
  |
  +--> learn mean
  +--> learn variance / scale
              |
              v
transform()
  |
  +--> apply those learned values
```

------------------------------------------------------------------------

# Question 6: What happens with test data?

Suppose:

``` python
X_test = np.array([
    [40.0]
])
```

We should normally **not fit another scaler on the test data**.

Instead:

``` python
X_test_scaled = scaler.transform(X_test)
```

The scaler continues using the statistics learned from `X_train`.

From training:

``` text
mean  = 20
scale ≈ 8.165
```

Therefore:

\[ z = `\frac{40-20}{8.165}`{=tex} `\approx 2.4495`{=tex} \]

The result is approximately:

``` text
[[2.44948974]]
```

This means the test value 40 is about 2.45 training standard deviations
above the training mean.

------------------------------------------------------------------------

# Question 7: Why not call `fit()` again on the test data?

Because the test set is supposed to represent **unseen data**.

The normal pattern is:

``` python
scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Or more compactly:

``` python
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Notice:

``` text
TRAINING DATA
    |
    +---- fit() --------> learn parameters
    |
    +---- transform() --> transformed training data


TEST DATA
    |
    +---- transform() --> transformed test data
                          using TRAINING parameters
```

Fitting preprocessing on test data can contaminate evaluation and cause
**data leakage**.

------------------------------------------------------------------------

# Question 8: What is `fit_transform()`?

This:

``` python
scaler.fit_transform(X_train)
```

is essentially a convenient combination of:

``` python
scaler.fit(X_train)
scaler.transform(X_train)
```

Therefore a common training pattern is:

``` python
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Remember:

``` text
fit()           -> LEARN
transform()     -> APPLY
fit_transform() -> LEARN + APPLY
```

------------------------------------------------------------------------

# Question 9: Is `transform()` only about scaling?

No.

This is the broader scikit-learn concept.

A transformer converts:

``` text
X  --->  X'
```

where `X'` is a new representation of the input.

Different transformers perform different operations.

## Missing-value transformation

Input:

``` text
Age

20
30
NaN
40
```

An imputer might produce:

``` text
Age

20
30
30
40
```

Example:

``` python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="median")
X_new = imputer.fit_transform(X)
```

------------------------------------------------------------------------

## Categorical transformation

Input:

``` text
City

Delhi
Mumbai
Chennai
```

`OneHotEncoder` may transform it into:

``` text
Delhi    Mumbai    Chennai

1        0         0
0        1         0
0        0         1
```

This converts categorical information into a numerical representation
usable by many estimators.

------------------------------------------------------------------------

## PCA transformation

PCA might transform:

``` text
100 original features
        |
        v
       PCA
        |
        v
10 principal components
```

PCA creates a new lower-dimensional representation.

------------------------------------------------------------------------

# Question 10: What is the general meaning of a transformer?

Think of it as:

``` text
                 RAW DATA
                    |
                    v
             Transformer.fit()
                    |
             "Learn what I need"
                    |
                    v
          Transformer.transform()
                    |
             "Apply what I learned"
                    |
                    v
           MODEL-READY FEATURES
                    |
                    v
                ML MODEL
```

Different transformers learn different things:

``` text
StandardScaler
    |
    +--> learns mean and scale

SimpleImputer
    |
    +--> learns replacement statistics such as median

OneHotEncoder
    |
    +--> learns known categories

PCA
    |
    +--> learns principal component directions
```

Then `transform()` uses those learned parameters to produce the new
feature representation.

------------------------------------------------------------------------

# Complete Example

``` python
import numpy as np
from sklearn.preprocessing import StandardScaler

X_train = np.array([
    [10.0],
    [20.0],
    [30.0]
])

X_test = np.array([
    [40.0]
])

scaler = StandardScaler()

# STEP 1:
# Learn statistics from training data.
scaler.fit(X_train)

print("Mean:")
print(scaler.mean_)

print("Scale:")
print(scaler.scale_)

# STEP 2:
# Transform training data using learned statistics.
X_train_scaled = scaler.transform(X_train)

print("\nTraining transformed:")
print(X_train_scaled)

# STEP 3:
# Transform unseen test data using EXACTLY the same learned statistics.
X_test_scaled = scaler.transform(X_test)

print("\nTest transformed:")
print(X_test_scaled)
```

Expected approximate output:

``` text
Mean:
[20.]

Scale:
[8.16496581]

Training transformed:
[[-1.22474487]
 [ 0.        ]
 [ 1.22474487]]

Test transformed:
[[2.44948974]]
```

------------------------------------------------------------------------

# Training Summary

The most important concepts to remember are:

``` text
fit()
   =
Learn something from training data.


transform()
   =
Use what was learned to create a new representation.


fit_transform()
   =
Learn + transform the same data.


Training:
fit_transform(X_train)


Testing / Production:
transform(X_test)
transform(new_production_data)
```

## One-line definition

> **A transformer learns the rules/parameters of a data transformation
> during `fit()` and applies those learned rules during `transform()` to
> produce a representation suitable for subsequent preprocessing or
> machine learning.**

## Most important rule

> **Learn preprocessing parameters from training data and reuse them for
> validation, test, and production data.**
