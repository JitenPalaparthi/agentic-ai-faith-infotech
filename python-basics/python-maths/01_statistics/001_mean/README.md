# Example 001: Arithmetic Mean

## Learning objective

The arithmetic mean is the balance point of a dataset. For n observations, add all
observations and divide by n. It is sensitive to extreme values, so it should be
interpreted together with robust measures such as the median when data is skewed.

## Mathematical formula / relationship

**x̄ = (x₁ + x₂ + ... + xₙ) / n**

## Mathematical interpretation

The code is intentionally based on a small dataset so that the calculation can be
verified manually during training. Learners should first understand the mathematical
relationship, then follow how the Python function implements the same operation.

## When should you use this?

Use the mean when numerical observations are reasonably balanced and you want one value representing the overall level.

## Simple real-world scenario

A trainer has five batch-processing times: 10, 20, 30, 40 and 50 ms. The mean, 30 ms, gives the average processing time.

## Trainer explanation

A useful classroom sequence is:

1. State the real-world question first.
2. Write the mathematical formula or relationship on the board.
3. Calculate a tiny example manually.
4. Run `main.py` and compare the program output with the manual result.
5. Change one input and ask learners to predict what will happen before executing it.

## Important interpretation / caution

Avoid relying on the mean alone when extreme outliers strongly distort it.

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
