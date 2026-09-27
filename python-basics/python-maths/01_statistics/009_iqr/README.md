# Example 009: Interquartile Range

## Learning objective

IQR is Q3-Q1 and measures the width of the middle 50% of the data. Because it ignores the outer quarters, it is much more robust to extreme values than the range.

## Mathematical formula / relationship

**IQR = Q3 - Q1**

## Mathematical interpretation

The code is intentionally based on a small dataset so that the calculation can be
verified manually during training. Learners should first understand the mathematical
relationship, then follow how the Python function implements the same operation.

## When should you use this?

Use IQR to measure spread robustly or identify potential outliers in skewed data.

## Simple real-world scenario

For house prices, Q1 and Q3 describe the middle half of the market without being dominated by a few luxury properties.

## Trainer explanation

A useful classroom sequence is:

1. State the real-world question first.
2. Write the mathematical formula or relationship on the board.
3. Calculate a tiny example manually.
4. Run `main.py` and compare the program output with the manual result.
5. Change one input and ask learners to predict what will happen before executing it.

## Important interpretation / caution

The 1.5×IQR outlier rule flags unusual values; it does not prove those values are errors.

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
