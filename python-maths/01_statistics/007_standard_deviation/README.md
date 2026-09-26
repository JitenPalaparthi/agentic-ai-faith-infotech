# Example 007: Standard Deviation

## Learning objective

Standard deviation is the square root of variance. It describes spread in the same units as the original variable, making it easier to interpret than variance.

## Mathematical formula / relationship

**σ = √σ²**

## Mathematical interpretation

The code is intentionally based on a small dataset so that the calculation can be
verified manually during training. Learners should first understand the mathematical
relationship, then follow how the Python function implements the same operation.

## When should you use this?

Use standard deviation when you need to describe how tightly numerical observations cluster around their mean.

## Simple real-world scenario

Two servers can both average 100 ms latency, but one may have SD 5 ms and another SD 80 ms. The first is much more consistent.

## Trainer explanation

A useful classroom sequence is:

1. State the real-world question first.
2. Write the mathematical formula or relationship on the board.
3. Calculate a tiny example manually.
4. Run `main.py` and compare the program output with the manual result.
5. Change one input and ask learners to predict what will happen before executing it.

## Important interpretation / caution

It is sensitive to outliers and is most interpretable alongside the mean and distribution shape.

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
