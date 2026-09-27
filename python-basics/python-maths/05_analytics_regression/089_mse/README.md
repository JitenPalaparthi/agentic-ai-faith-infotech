# Example 089: Mean Squared Error

## Learning objective

MSE averages squared residuals. Squaring makes all errors nonnegative and penalizes large errors more strongly.

## Mathematical formula / relationship

**MSE=(1/n)Σ(yᵢ-ŷᵢ)²**

## Mathematical interpretation

The code is intentionally based on a small dataset so that the calculation can be
verified manually during training. Learners should first understand the mathematical
relationship, then follow how the Python function implements the same operation.

## When should you use this?

Use MSE when evaluating numerical predictions and you want large errors to receive disproportionately high penalty.

## Simple real-world scenario

For house-price predictions, an error of ₹10 lakh contributes 100 times the squared loss of an error of ₹1 lakh.

## Trainer explanation

A useful classroom sequence is:

1. State the real-world question first.
2. Write the mathematical formula or relationship on the board.
3. Calculate a tiny example manually.
4. Run `main.py` and compare the program output with the manual result.
5. Change one input and ask learners to predict what will happen before executing it.

## Important interpretation / caution

Because errors are squared, MSE is sensitive to outliers and is expressed in squared target units.

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
