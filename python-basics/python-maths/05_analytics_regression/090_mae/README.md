# Example 090: Mean Absolute Error

## Learning objective

MAE averages absolute residuals. Unlike MSE, it remains directly in the target variable's units and does not square large errors.

## Mathematical formula / relationship

**MAE=(1/n)Σ|yᵢ-ŷᵢ|**

## Mathematical interpretation

The code is intentionally based on a small dataset so that the calculation can be
verified manually during training. Learners should first understand the mathematical
relationship, then follow how the Python function implements the same operation.

## When should you use this?

Use MAE when you want prediction error expressed directly in the same units as the target and prefer a less outlier-sensitive metric than MSE.

## Simple real-world scenario

If delivery-time MAE is 4 minutes, predictions differ from actual delivery times by 4 minutes on average in absolute terms.

## Trainer explanation

A useful classroom sequence is:

1. State the real-world question first.
2. Write the mathematical formula or relationship on the board.
3. Calculate a tiny example manually.
4. Run `main.py` and compare the program output with the manual result.
5. Change one input and ask learners to predict what will happen before executing it.

## Important interpretation / caution

MAE does not penalize a few very large errors as aggressively as MSE.

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
