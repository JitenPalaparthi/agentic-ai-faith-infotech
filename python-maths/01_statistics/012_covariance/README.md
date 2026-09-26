# Example 012: Covariance

## Learning objective

Covariance measures whether two variables move together. Positive covariance indicates that larger values of one tend to accompany larger values of the other; its magnitude depends on the variables' units.

## Mathematical formula / relationship

**cov(X,Y) = Σ[(xᵢ-x̄)(yᵢ-ȳ)] / (n-1)**

## Mathematical interpretation

The code is intentionally based on a small dataset so that the calculation can be
verified manually during training. Learners should first understand the mathematical
relationship, then follow how the Python function implements the same operation.

## When should you use this?

Use covariance to determine whether two variables tend to move in the same or opposite directions.

## Simple real-world scenario

Daily temperature and electricity usage may have negative covariance in a heating-dominated season: as temperature rises, heating demand tends to fall.

## Trainer explanation

A useful classroom sequence is:

1. State the real-world question first.
2. Write the mathematical formula or relationship on the board.
3. Calculate a tiny example manually.
4. Run `main.py` and compare the program output with the manual result.
5. Change one input and ask learners to predict what will happen before executing it.

## Important interpretation / caution

Its magnitude depends on measurement units, so correlation is usually easier for comparing relationships.

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
