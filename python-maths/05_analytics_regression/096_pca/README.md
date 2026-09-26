# Example 096: PCA Foundations

## Learning objective

PCA finds orthogonal directions that capture decreasing amounts of variance. After centering, eigenvectors of the covariance matrix give principal directions and eigenvalues give variance along them.

## Mathematical formula / relationship

**Cov(X)v = λv**

## Mathematical interpretation

The code is intentionally based on a small dataset so that the calculation can be
verified manually during training. Learners should first understand the mathematical
relationship, then follow how the Python function implements the same operation.

## When should you use this?

Use PCA when many correlated numerical features need a lower-dimensional representation while retaining as much variance as possible.

## Simple real-world scenario

A dataset with 50 correlated sensor measurements can be transformed into a smaller number of principal components for visualization or downstream analysis.

## Trainer explanation

A useful classroom sequence is:

1. State the real-world question first.
2. Write the mathematical formula or relationship on the board.
3. Calculate a tiny example manually.
4. Run `main.py` and compare the program output with the manual result.
5. Change one input and ask learners to predict what will happen before executing it.

## Important interpretation / caution

PCA components are combinations of original features and may be less interpretable; features should usually be appropriately scaled first.

## What the Python program demonstrates

- A clean function-oriented implementation where appropriate.
- A `main()` entry point so the example is directly runnable.
- Small input values suitable for manual verification.
- Intermediate or verification output where it improves understanding.
- NumPy or pandas only when the library meaningfully supports the mathematical concept.

## How to run

```bash
python -m pip install -r requirements.txt
python main.py
```

## Suggested trainer exercise

1. Calculate the result manually using the formula above.
2. Run `main.py` and compare the output.
3. Change the input data and predict the result before running again.
4. Discuss assumptions, dimensional requirements, and possible edge cases.
