# Python Mathematics & Statistics — 100 Training Examples

Every example is an independent mini-project with `README.md`, `main.py`, and `requirements.txt`.

## 001. Arithmetic Mean
The arithmetic mean is the balance point of a dataset. For n observations, add all
observations and divide by n. It is sensitive to extreme values, so it should be
interpreted together with robust measures such as the median when data is skewed.
**Formula:** `x̄ = (x₁ + x₂ + ... + xₙ) / n`
**Folder:** `01_statistics/001_mean/`

## 002. Median
The median is the central ordered observation. For an odd number of observations it
is the middle value; for an even number it is the average of the two middle values.
Unlike the mean, a very large outlier has limited effect on the median.
**Formula:** `Median = middle ordered value`
**Folder:** `01_statistics/002_median/`

## 003. Mode
The mode is the value occurring most frequently. It is especially useful for categorical or discrete data where an arithmetic mean may have no useful interpretation.
**Formula:** `Mode = value with highest frequency`
**Folder:** `01_statistics/003_mode/`

## 004. Range
The range is the simplest measure of dispersion. It uses only the two extreme observations, so it is easy to calculate but highly sensitive to outliers.
**Formula:** `Range = max(x) - min(x)`
**Folder:** `01_statistics/004_range/`

## 005. Population Variance
Variance measures average squared distance from the population mean. Squaring prevents positive and negative deviations from cancelling and gives greater weight to large deviations.
**Formula:** `σ² = Σ(xᵢ - μ)² / N`
**Folder:** `01_statistics/005_population_variance/`

## 006. Sample Variance
When data is a sample used to estimate population variance, division by n-1 rather than n applies Bessel's correction. This corrects the systematic downward bias of the naive sample variance estimator.
**Formula:** `s² = Σ(xᵢ - x̄)² / (n - 1)`
**Folder:** `01_statistics/006_sample_variance/`

## 007. Standard Deviation
Standard deviation is the square root of variance. It describes spread in the same units as the original variable, making it easier to interpret than variance.
**Formula:** `σ = √σ²`
**Folder:** `01_statistics/007_standard_deviation/`

## 008. Percentiles
The p-th percentile is a value below which approximately p percent of observations fall. Percentiles describe position without assuming a particular probability distribution.
**Formula:** `P25, P50, P75 = 25th, 50th, 75th percentiles`
**Folder:** `01_statistics/008_percentiles/`

## 009. Interquartile Range
IQR is Q3-Q1 and measures the width of the middle 50% of the data. Because it ignores the outer quarters, it is much more robust to extreme values than the range.
**Formula:** `IQR = Q3 - Q1`
**Folder:** `01_statistics/009_iqr/`

## 010. Z-Score
A z-score standardizes an observation by subtracting the mean and dividing by the standard deviation. A z-score of +2 means the observation lies two standard deviations above the mean.
**Formula:** `z = (x - μ) / σ`
**Folder:** `01_statistics/010_z_score/`

## 011. Weighted Mean
A weighted mean allows observations to contribute unequally. It is used for grade calculations, portfolio returns, survey weighting, and aggregated metrics.
**Formula:** `x̄w = Σ(wᵢxᵢ) / Σwᵢ`
**Folder:** `01_statistics/011_weighted_mean/`

## 012. Covariance
Covariance measures whether two variables move together. Positive covariance indicates that larger values of one tend to accompany larger values of the other; its magnitude depends on the variables' units.
**Formula:** `cov(X,Y) = Σ[(xᵢ-x̄)(yᵢ-ȳ)] / (n-1)`
**Folder:** `01_statistics/012_covariance/`

## 013. Pearson Correlation
Pearson correlation normalizes covariance by the variables' standard deviations, producing a dimensionless value between -1 and +1. It measures linear association, not causation.
**Formula:** `r = cov(X,Y) / (sₓsᵧ)`
**Folder:** `01_statistics/013_correlation/`

## 014. Expected Value
Expected value is the probability-weighted long-run average of a random variable. Probabilities must sum to one.
**Formula:** `E[X] = Σ xᵢP(X=xᵢ)`
**Folder:** `01_statistics/014_expected_value/`

## 015. Empirical Probability
Empirical probability estimates event probability from observed relative frequency. With more representative observations, it often approaches the underlying probability.
**Formula:** `P̂(A) = count(A) / total observations`
**Folder:** `01_statistics/015_empirical_probability/`

## 016. Normal Distribution
A normal distribution is symmetric around its mean and is parameterized by mean μ and standard deviation σ. Many statistical procedures use normality exactly or approximately.
**Formula:** `X ~ N(μ, σ²)`
**Folder:** `01_statistics/016_normal_distribution/`

## 017. Binomial Distribution
A binomial random variable counts successes in n independent Bernoulli trials where each trial has the same success probability p.
**Formula:** `X ~ Binomial(n,p), E[X]=np`
**Folder:** `01_statistics/017_binomial_distribution/`

## 018. IQR Outlier Rule
The common 1.5×IQR rule flags observations below Q1-1.5IQR or above Q3+1.5IQR. It is a diagnostic rule, not proof that an observation is erroneous.
**Formula:** `Lower=Q1-1.5IQR; Upper=Q3+1.5IQR`
**Folder:** `01_statistics/018_outlier_iqr/`

## 019. Random Sampling
Sampling selects a subset of a population. Sampling without replacement prevents the same population element from appearing twice in one sample.
**Formula:** `sample ⊂ population`
**Folder:** `01_statistics/019_sampling/`

## 020. Bootstrap Mean
Bootstrap resampling repeatedly samples with replacement from observed data. The resulting distribution of a statistic can approximate its sampling uncertainty without deriving a closed-form formula.
**Formula:** `Bootstrap statistic = statistic(resample with replacement)`
**Folder:** `01_statistics/020_bootstrap/`

## 021. Vector Creation
A vector is an ordered collection of numbers. Geometrically it can represent magnitude and direction; in data science it often represents one observation or one feature vector.
**Formula:** `v = [v₁,v₂,...,vₙ]`
**Folder:** `02_vectors_matrices/021_vector_creation/`

## 022. Vector Addition
Vectors of equal dimension add component by component. Geometrically, addition combines displacements.
**Formula:** `a+b = [a₁+b₁,...,aₙ+bₙ]`
**Folder:** `02_vectors_matrices/022_vector_addition/`

## 023. Vector Subtraction
Subtracting vectors produces the component-wise difference. For coordinate vectors, b-a is the displacement from point a to point b.
**Formula:** `b-a = [b₁-a₁,...]`
**Folder:** `02_vectors_matrices/023_vector_subtraction/`

## 024. Scalar Multiplication
Multiplying by a scalar changes a vector's magnitude; a negative scalar also reverses its direction.
**Formula:** `kv = [kv₁,...,kvₙ]`
**Folder:** `02_vectors_matrices/024_scalar_multiplication/`

## 025. Vector Magnitude
The Euclidean norm is the square root of the sum of squared components. It generalizes the Pythagorean theorem to n dimensions.
**Formula:** `||v||₂ = √Σvᵢ²`
**Folder:** `02_vectors_matrices/025_magnitude/`

## 026. Unit Vector
A unit vector has magnitude one. Dividing a nonzero vector by its norm preserves direction while removing magnitude.
**Formula:** `v̂ = v / ||v||`
**Folder:** `02_vectors_matrices/026_unit_vector/`

## 027. Dot Product
The dot product is the sum of pairwise products. Geometrically a·b=||a||||b||cosθ, connecting algebra to the angle between vectors. It appears in similarity, projections and linear models.
**Formula:** `a·b = Σaᵢbᵢ`
**Folder:** `02_vectors_matrices/027_dot_product/`

## 028. Cross Product
For 3-D vectors, the cross product produces a vector perpendicular to both inputs. Its magnitude equals the area of the parallelogram formed by the vectors.
**Formula:** `||a×b|| = ||a||||b||sinθ`
**Folder:** `02_vectors_matrices/028_cross_product/`

## 029. Cosine Similarity
Cosine similarity is the cosine of the angle between two nonzero vectors. Values near 1 indicate similar direction, 0 orthogonality, and -1 opposite direction.
**Formula:** `cosθ = (a·b)/(||a||||b||)`
**Folder:** `02_vectors_matrices/029_cosine_similarity/`

## 030. Angle Between Vectors
Rearranging the dot-product identity yields the angle between vectors. Numerical clipping protects arccos from tiny floating-point errors outside [-1,1].
**Formula:** `θ = arccos((a·b)/(||a||||b||))`
**Folder:** `02_vectors_matrices/030_angle_vectors/`

## 031. Matrix Creation
A matrix is a rectangular array with m rows and n columns. In analytics, rows commonly represent observations and columns features.
**Formula:** `A ∈ ℝ^(m×n)`
**Folder:** `02_vectors_matrices/031_matrix_creation/`

## 032. Matrix Indexing
Matrix indexing identifies an element by row and column. Slices select whole rows, columns or rectangular regions.
**Formula:** `A[i,j] = element at row i, column j`
**Folder:** `02_vectors_matrices/032_matrix_indexing/`

## 033. Matrix Addition
Matrices can be added when their shapes match. Addition occurs independently at each position.
**Formula:** `Cᵢⱼ = Aᵢⱼ + Bᵢⱼ`
**Folder:** `02_vectors_matrices/033_matrix_addition/`

## 034. Hadamard Product
Element-wise multiplication multiplies corresponding entries. It differs fundamentally from matrix multiplication.
**Formula:** `Cᵢⱼ = AᵢⱼBᵢⱼ`
**Folder:** `02_vectors_matrices/034_hadamard_product/`

## 035. Matrix Multiplication
For A(m×n) and B(n×p), AB is m×p. Each output cell is the dot product of one row of A and one column of B.
**Formula:** `Cᵢⱼ = Σₖ AᵢₖBₖⱼ`
**Folder:** `02_vectors_matrices/035_matrix_multiplication/`

## 036. Matrix-Vector Product
Multiplying A by vector x forms a linear combination of A's columns. Linear regression predictions can be written in this form.
**Formula:** `y = Ax`
**Folder:** `02_vectors_matrices/036_matrix_vector/`

## 037. Transpose
Transposition exchanges rows and columns. If A is m×n, Aᵀ is n×m.
**Formula:** `(Aᵀ)ᵢⱼ = Aⱼᵢ`
**Folder:** `02_vectors_matrices/037_transpose/`

## 038. Identity Matrix
The identity matrix has ones on the main diagonal and zeros elsewhere. Multiplying by it leaves a compatible vector or matrix unchanged.
**Formula:** `AI = IA = A`
**Folder:** `02_vectors_matrices/038_identity/`

## 039. Determinant
The determinant is a scalar associated with a square matrix. A zero determinant means the matrix is singular and has no inverse.
**Formula:** `det([[a,b],[c,d]]) = ad-bc`
**Folder:** `02_vectors_matrices/039_determinant/`

## 040. Matrix Inverse
For a nonsingular square matrix A, A⁻¹ reverses the linear transformation: AA⁻¹=I. In numerical work, solve(A,b) is usually preferable to computing an inverse just to solve equations.
**Formula:** `AA⁻¹ = I`
**Folder:** `02_vectors_matrices/040_inverse/`

## 041. Matrix Rank
Rank is the dimension of the matrix's row/column space. Rank deficiency indicates linear dependence among rows or columns.
**Formula:** `rank(A) ≤ min(m,n)`
**Folder:** `02_vectors_matrices/041_rank/`

## 042. Matrix Trace
The trace is the sum of diagonal elements of a square matrix. It equals the sum of eigenvalues when counted with algebraic multiplicity.
**Formula:** `tr(A) = ΣAᵢᵢ`
**Folder:** `02_vectors_matrices/042_trace/`

## 043. Solving Linear Equations
A system of simultaneous linear equations can be written Ax=b. A direct solver is numerically preferable to forming A⁻¹b explicitly.
**Formula:** `Ax = b`
**Folder:** `02_vectors_matrices/043_linear_system/`

## 044. Eigenvalues and Eigenvectors
An eigenvector keeps its direction under transformation A; it is only scaled by eigenvalue λ. This concept underlies PCA and many dynamical systems.
**Formula:** `Av = λv`
**Folder:** `02_vectors_matrices/044_eigen/`

## 045. Outer Product
The outer product takes an m-vector and n-vector and creates an m×n matrix containing every pairwise product.
**Formula:** `(abᵀ)ᵢⱼ = aᵢbⱼ`
**Folder:** `02_vectors_matrices/045_outer_product/`

## 046. Vector Projection
Projection finds the component of vector b that lies along vector a. It is a direct application of the dot product.
**Formula:** `projₐ(b) = (b·a)/(a·a) a`
**Folder:** `02_vectors_matrices/046_projection/`

## 047. Orthogonality
Two nonzero vectors are orthogonal when their angle is 90 degrees. Algebraically, this is equivalent to a zero dot product.
**Formula:** `a ⟂ b ⇔ a·b = 0`
**Folder:** `02_vectors_matrices/047_orthogonality/`

## 048. Frobenius Norm
The Frobenius norm measures matrix size by treating all entries like components of one long vector.
**Formula:** `||A||F = √ΣᵢΣⱼ Aᵢⱼ²`
**Folder:** `02_vectors_matrices/048_frobenius_norm/`

## 049. Singular Value Decomposition
SVD factors any m×n matrix into orthogonal directions and nonnegative singular values. It is fundamental to dimensionality reduction, least squares and compression.
**Formula:** `A = UΣVᵀ`
**Folder:** `02_vectors_matrices/049_svd/`

## 050. Matrix Power
A matrix power Aᵏ repeatedly composes the same linear transformation. It is not element-wise exponentiation.
**Formula:** `A³ = A·A·A`
**Folder:** `02_vectors_matrices/050_matrix_power/`

## 051. Matrix Stacking
Stacking joins compatible matrices along a chosen direction. It is useful for assembling batches or feature blocks.
**Formula:** `vertical: rows increase; horizontal: columns increase`
**Folder:** `02_vectors_matrices/051_stacking/`

## 052. Slope Between Two Points
Slope measures the rate of change of y with respect to x. Positive slope rises left-to-right; negative slope falls; zero slope is horizontal.
**Formula:** `m = (y₂-y₁)/(x₂-x₁)`
**Folder:** `03_algebra_calculus/052_slope/`

## 053. Linear Equation y = mx + c
The slope-intercept form describes a straight line. m controls change in y for each unit change in x, while c is the y value when x=0.
**Formula:** `y = mx + c`
**Folder:** `03_algebra_calculus/053_linear_equation/`

## 054. Deriving y = mx + c
Two distinct nonvertical points determine one line. First compute slope m; then substitute either point into y=mx+c to solve for c.
**Formula:** `m=(y₂-y₁)/(x₂-x₁), c=y₁-mx₁`
**Folder:** `03_algebra_calculus/054_line_from_points/`

## 055. Quadratic Function
A quadratic has degree two and forms a parabola. The sign of a determines whether the parabola opens upward or downward.
**Formula:** `y = ax² + bx + c`
**Folder:** `03_algebra_calculus/055_quadratic/`

## 056. Quadratic Roots
Roots are x-values where the quadratic equals zero. The discriminant b²-4ac determines whether real roots are distinct, repeated, or absent.
**Formula:** `x = (-b ± √(b²-4ac))/(2a)`
**Folder:** `03_algebra_calculus/056_quadratic_roots/`

## 057. Polynomial Evaluation
A polynomial combines powers of x with coefficients. Vectorized evaluation is useful for curves and numerical modeling.
**Formula:** `p(x)=aₙxⁿ+...+a₁x+a₀`
**Folder:** `03_algebra_calculus/057_polynomial/`

## 058. Exponential Function
In exponential growth, the rate of change is proportional to the current value. eˣ is central to continuous growth, probability and optimization.
**Formula:** `y = eˣ`
**Folder:** `03_algebra_calculus/058_exponential/`

## 059. Natural Logarithm
The natural logarithm ln(x) is the inverse of eˣ. It converts multiplication into addition and is widely used for skewed data and likelihoods.
**Formula:** `ln(eˣ)=x`
**Folder:** `03_algebra_calculus/059_logarithm/`

## 060. Sigmoid Function
The logistic sigmoid smoothly maps every real number to (0,1). It is mathematically useful for converting an unbounded score into a probability-like scale.
**Formula:** `σ(x)=1/(1+e⁻ˣ)`
**Folder:** `03_algebra_calculus/060_sigmoid/`

## 061. Numerical Derivative
A derivative is the limiting rate of change. A central finite difference estimates it using function values just to the left and right of x.
**Formula:** `f'(x) ≈ [f(x+h)-f(x-h)]/(2h)`
**Folder:** `03_algebra_calculus/061_derivative/`

## 062. Partial Derivatives
For a multivariable function, a partial derivative changes one variable while holding the others fixed. The collection of partial derivatives forms the gradient.
**Formula:** `∇f = [∂f/∂x, ∂f/∂y, ...]`
**Folder:** `03_algebra_calculus/062_partial_derivatives/`

## 063. Numerical Integration
A definite integral represents signed area accumulated under a curve. The trapezoidal rule approximates this area by summing trapezoids.
**Formula:** `∫ₐᵇ f(x)dx ≈ trapezoidal sum`
**Folder:** `03_algebra_calculus/063_integration/`

## 064. Gradient Descent
Gradient descent minimizes a differentiable function by repeatedly moving opposite the gradient. The learning rate controls step size.
**Formula:** `xₜ₊₁ = xₜ - η f'(xₜ)`
**Folder:** `03_algebra_calculus/064_gradient_descent/`

## 065. Euclidean Distance
Euclidean distance is the straight-line distance between points and equals the norm of their difference vector.
**Formula:** `d(p,q)=√Σ(qᵢ-pᵢ)²`
**Folder:** `03_algebra_calculus/065_euclidean_distance/`

## 066. Plane Equation
A plane is the two-dimensional analogue of a line embedded in three-dimensional space. In regression, z=ax+by+c is a linear model with two predictors.
**Formula:** `z = ax + by + c`
**Folder:** `03_algebra_calculus/066_plane/`

## 067. 2-D Arrays
A 2-D array has two axes. For a data matrix X with shape (n,p), axis 0 usually indexes observations and axis 1 features.
**Formula:** `shape = (rows, columns)`
**Folder:** `04_multidimensional_arrays/067_array_2d/`

## 068. 3-D Arrays
A 3-D array adds another axis. It can represent batch×rows×columns or time×entities×features, depending on the problem.
**Formula:** `shape = (d₀,d₁,d₂)`
**Folder:** `04_multidimensional_arrays/068_array_3d/`

## 069. 4-D Tensors
A 4-D array is often called a tensor in data-science contexts. Image batches commonly use batch×height×width×channels.
**Formula:** `shape = (batch,height,width,channels)`
**Folder:** `04_multidimensional_arrays/069_array_4d/`

## 070. Reshaping Arrays
Reshape changes the interpretation of dimensions without changing the number or order of elements. The product of dimensions must remain constant.
**Formula:** `∏ old_shape = ∏ new_shape`
**Folder:** `04_multidimensional_arrays/070_reshape/`

## 071. Flattening
Flattening converts a multidimensional array into one dimension. ravel often returns a view when possible; flatten returns a copy.
**Formula:** `(d₀,d₁,...,dₖ) → (product of dimensions,)`
**Folder:** `04_multidimensional_arrays/071_flatten/`

## 072. Axis 0 Reduction
Reducing axis 0 collapses the first dimension. For a rows×columns matrix, a column statistic remains.
**Formula:** `mean(X,axis=0) → one value per column`
**Folder:** `04_multidimensional_arrays/072_axis0/`

## 073. Axis 1 Reduction
Reducing axis 1 collapses columns. For a 2-D matrix, the result contains one statistic per row.
**Formula:** `mean(X,axis=1) → one value per row`
**Folder:** `04_multidimensional_arrays/073_axis1/`

## 074. Multiple-Axis Reduction
NumPy can reduce several axes simultaneously. In a batch tensor, reducing non-batch axes can produce one summary per batch.
**Formula:** `mean(X,axis=(1,2))`
**Folder:** `04_multidimensional_arrays/074_multi_axis/`

## 075. Broadcasting
Broadcasting aligns array shapes from the trailing dimensions. Dimensions are compatible when equal or when one of them is 1.
**Formula:** `(m,n) + (n,) → (m,n)`
**Folder:** `04_multidimensional_arrays/075_broadcasting/`

## 076. Column Broadcasting
A shape (m,1) array broadcasts across n columns of an (m,n) matrix. Singleton dimensions are deliberately inserted to control broadcasting.
**Formula:** `(m,n) + (m,1) → (m,n)`
**Folder:** `04_multidimensional_arrays/076_column_broadcast/`

## 077. Adding a New Axis
np.newaxis inserts a dimension of size one. This is useful for converting a 1-D vector into an explicit row or column for broadcasting.
**Formula:** `(n,) → (n,1) or (1,n)`
**Folder:** `04_multidimensional_arrays/077_newaxis/`

## 078. Reordering Tensor Axes
For tensors, transpose can specify an arbitrary axis permutation. Reordering axes changes layout but not the underlying mathematical values.
**Formula:** `(a,b,c) → permutation such as (c,a,b)`
**Folder:** `04_multidimensional_arrays/078_transpose_axes/`

## 079. Concatenation
Concatenation joins arrays along an existing axis. All other dimensions must be compatible.
**Formula:** `concat axis 0 adds rows; axis 1 adds columns`
**Folder:** `04_multidimensional_arrays/079_concatenate/`

## 080. Boolean Masking
A Boolean mask has True/False values aligned with data. Selecting with the mask keeps elements where the condition is True.
**Formula:** `maskᵢ = condition(xᵢ)`
**Folder:** `04_multidimensional_arrays/080_boolean_mask/`

## 081. Pairwise Distances with Broadcasting
By reshaping point arrays conceptually to n×1×d and 1×n×d, broadcasting creates every pairwise difference. Reducing the feature axis gives an n×n distance matrix.
**Formula:** `Dᵢⱼ = ||pᵢ-pⱼ||₂`
**Folder:** `04_multidimensional_arrays/081_pairwise_distance/`

## 082. Min-Max Normalization
Min-max normalization linearly maps the minimum to 0 and maximum to 1. It preserves ordering but is sensitive to extreme values.
**Formula:** `x'=(x-min)/(max-min)`
**Folder:** `05_analytics_regression/082_minmax/`

## 083. Feature Standardization
Standardization subtracts the mean and divides by standard deviation. Each transformed feature then has mean approximately zero and population SD one.
**Formula:** `z=(x-μ)/σ`
**Folder:** `05_analytics_regression/083_standardization/`

## 084. Missing Values and NaN
NaN is a floating-point representation commonly used for missing numerical data. Ordinary reductions propagate NaN; nan-aware reductions intentionally ignore it.
**Formula:** `nanmean ignores NaN observations`
**Folder:** `05_analytics_regression/084_nan_stats/`

## 085. Moving Average
A moving average replaces each point with the mean of a local window. It smooths short-term variation while introducing a window-dependent lag.
**Formula:** `MAₜ=(xₜ+...+xₜ₋w₊₁)/w`
**Folder:** `05_analytics_regression/085_moving_average/`

## 086. Cumulative Metrics
A cumulative sum at position t is the sum of all observations through t. Running totals are common in sales, finance and event analysis.
**Formula:** `Sₜ=Σᵢ₌₁ᵗ xᵢ`
**Folder:** `05_analytics_regression/086_cumulative/`

## 087. Least-Squares Line y = mx + c
Least squares chooses m and c to minimize the sum of squared vertical residuals. Writing the model as Xβ≈y turns line fitting into a linear algebra problem.
**Formula:** `min Σ[yᵢ-(mxᵢ+c)]²`
**Folder:** `05_analytics_regression/087_least_squares/`

## 088. Regression Residuals
A residual is observed minus predicted value. Positive residuals mean the model underpredicted; negative residuals mean it overpredicted.
**Formula:** `eᵢ = yᵢ - ŷᵢ`
**Folder:** `05_analytics_regression/088_residuals/`

## 089. Mean Squared Error
MSE averages squared residuals. Squaring makes all errors nonnegative and penalizes large errors more strongly.
**Formula:** `MSE=(1/n)Σ(yᵢ-ŷᵢ)²`
**Folder:** `05_analytics_regression/089_mse/`

## 090. Mean Absolute Error
MAE averages absolute residuals. Unlike MSE, it remains directly in the target variable's units and does not square large errors.
**Formula:** `MAE=(1/n)Σ|yᵢ-ŷᵢ|`
**Folder:** `05_analytics_regression/090_mae/`

## 091. R-Squared
R² compares model residual variation with total variation around the target mean. R²=1 is perfect fit; 0 matches the mean-only baseline on the evaluated data.
**Formula:** `R²=1-SSres/SStot`
**Folder:** `05_analytics_regression/091_r_squared/`

## 092. Multiple Linear Regression
Multiple regression extends a line to several predictors. The coefficient vector β is chosen to minimize squared residuals of Xβ against y.
**Formula:** `y = β₀ + β₁x₁ + ... + βₚxₚ`
**Folder:** `05_analytics_regression/092_multiple_regression/`

## 093. Gradient Descent for Linear Regression
For MSE loss, derivatives with respect to m and c indicate how to adjust parameters. Repeated small steps can approach the least-squares solution.
**Formula:** `m←m-η∂MSE/∂m; c←c-η∂MSE/∂c`
**Folder:** `05_analytics_regression/093_gradient_descent_line/`

## 094. Covariance Matrix
For p features, the covariance matrix contains every pairwise covariance. Diagonal entries are feature variances.
**Formula:** `Σᵢⱼ = cov(Xᵢ,Xⱼ)`
**Folder:** `05_analytics_regression/094_cov_matrix/`

## 095. Correlation Matrix
A correlation matrix normalizes each covariance by the corresponding standard deviations, making associations comparable across differently scaled features.
**Formula:** `Rᵢⱼ = cov(Xᵢ,Xⱼ)/(sᵢsⱼ)`
**Folder:** `05_analytics_regression/095_corr_matrix/`

## 096. PCA Foundations
PCA finds orthogonal directions that capture decreasing amounts of variance. After centering, eigenvectors of the covariance matrix give principal directions and eigenvalues give variance along them.
**Formula:** `Cov(X)v = λv`
**Folder:** `05_analytics_regression/096_pca/`

## 097. Einstein Summation
Einstein notation labels dimensions with indices and states which indices are summed. It provides a compact way to express matrix products and tensor contractions.
**Formula:** `Cᵢₖ = Σⱼ AᵢⱼBⱼₖ`
**Folder:** `05_analytics_regression/097_einsum/`

## 098. Histogram
A histogram partitions a numerical range into bins and counts observations in each interval. It approximates the shape of a distribution, with appearance depending on bin choice.
**Formula:** `frequency(bin j) = count{x in interval j}`
**Folder:** `05_analytics_regression/098_histogram/`

## 099. Grouped Statistics
Grouped analysis partitions observations by category and computes statistics within each group. It is the statistical version of split-apply-combine.
**Formula:** `group → statistic(group values)`
**Folder:** `05_analytics_regression/099_group_stats/`

## 100. Meshgrid and Surfaces
Meshgrid turns two coordinate vectors into coordinate matrices. A function z=f(x,y) can then be evaluated at every point on the grid.
**Formula:** `Zᵢⱼ = f(Xᵢⱼ,Yᵢⱼ)`
**Folder:** `05_analytics_regression/100_meshgrid/`
