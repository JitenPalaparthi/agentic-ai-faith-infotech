# Example 002: Median

## Learning objective

The median is the central ordered observation. For an odd number of observations it
is the middle value; for an even number it is the average of the two middle values.
Unlike the mean, a very large outlier has limited effect on the median.

## Mathematical formula / relationship

**Median = middle ordered value**

## Mathematical interpretation

The code is intentionally based on a small dataset so that the calculation can be
verified manually during training. Learners should first understand the mathematical
relationship, then follow how the Python function implements the same operation.

## When should you use this?

Use the median when data is skewed or contains extreme values and you need a robust central value.

## Simple real-world scenario

For salaries ₹30k, ₹35k, ₹40k, ₹45k and ₹5 lakh, the mean is pulled upward by the ₹5 lakh salary. The median better represents the typical employee.

## Trainer explanation

A useful classroom sequence is:

1. State the real-world question first.
2. Write the mathematical formula or relationship on the board.
3. Calculate a tiny example manually.
4. Run `main.py` and compare the program output with the manual result.
5. Change one input and ask learners to predict what will happen before executing it.

## Important interpretation / caution

Median ignores how far extreme values are from the center, so it does not describe total magnitude.

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
