# Example 013: Pearson Correlation

## Learning objective

Pearson correlation normalizes covariance by the variables' standard deviations, producing a dimensionless value between -1 and +1. It measures linear association, not causation.

## Mathematical formula / relationship

**r = cov(X,Y) / (sₓsᵧ)**

## Mathematical interpretation

The code is intentionally based on a small dataset so that the calculation can be
verified manually during training. Learners should first understand the mathematical
relationship, then follow how the Python function implements the same operation.

## When should you use this?

Use correlation when you want to quantify the strength and direction of a linear relationship between numerical variables.

## Simple real-world scenario

Compare advertising spend with monthly sales. A strong positive correlation indicates that higher spend tends to occur with higher sales.

## Trainer explanation

A useful classroom sequence is:

1. State the real-world question first.
2. Write the mathematical formula or relationship on the board.
3. Calculate a tiny example manually.
4. Run `main.py` and compare the program output with the manual result.
5. Change one input and ask learners to predict what will happen before executing it.

## Important interpretation / caution

Correlation does not establish causation and can miss strong nonlinear relationships.

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
