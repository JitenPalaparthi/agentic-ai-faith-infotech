# Example 010: Z-Score

## Learning objective

A z-score standardizes an observation by subtracting the mean and dividing by the standard deviation. A z-score of +2 means the observation lies two standard deviations above the mean.

## Mathematical formula / relationship

**z = (x - μ) / σ**

## Mathematical interpretation

The code is intentionally based on a small dataset so that the calculation can be
verified manually during training. Learners should first understand the mathematical
relationship, then follow how the Python function implements the same operation.

## When should you use this?

Use z-scores when observations measured on a scale need to be expressed relative to their mean and standard deviation.

## Simple real-world scenario

If an exam score has z=2, that score is two standard deviations above the class mean, making relative performance easier to compare across exams.

## Trainer explanation

A useful classroom sequence is:

1. State the real-world question first.
2. Write the mathematical formula or relationship on the board.
3. Calculate a tiny example manually.
4. Run `main.py` and compare the program output with the manual result.
5. Change one input and ask learners to predict what will happen before executing it.

## Important interpretation / caution

Interpretation depends on the underlying distribution; a z-score alone is not automatically an outlier.

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
