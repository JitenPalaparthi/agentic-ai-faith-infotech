# Example 018: IQR Outlier Rule

## Learning objective

The common 1.5×IQR rule flags observations below Q1-1.5IQR or above Q3+1.5IQR. It is a diagnostic rule, not proof that an observation is erroneous.

## Mathematical formula / relationship

**Lower=Q1-1.5IQR; Upper=Q3+1.5IQR**

## Mathematical interpretation

The code is intentionally based on a small dataset so that the calculation can be
verified manually during training. Learners should first understand the mathematical
relationship, then follow how the Python function implements the same operation.

## When should you use this?

Use iqr outlier rule when summarizing or interpreting numerical data and this mathematical property matches the question you are asking.

## Simple real-world scenario

During exploratory analysis, calculate iqr outlier rule on a small business dataset, verify the result manually, and then apply it to the complete dataset.

## Trainer explanation

A useful classroom sequence is:

1. State the real-world question first.
2. Write the mathematical formula or relationship on the board.
3. Calculate a tiny example manually.
4. Run `main.py` and compare the program output with the manual result.
5. Change one input and ask learners to predict what will happen before executing it.

## Important interpretation / caution

Do not interpret a single statistic in isolation; consider distribution shape, sample size, units, and data quality.

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
