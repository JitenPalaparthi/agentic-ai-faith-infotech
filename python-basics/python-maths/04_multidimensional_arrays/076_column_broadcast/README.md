# Example 076: Column Broadcasting

## Learning objective

A shape (m,1) array broadcasts across n columns of an (m,n) matrix. Singleton dimensions are deliberately inserted to control broadcasting.

## Mathematical formula / relationship

**(m,n) + (m,1) → (m,n)**

## Mathematical interpretation

The code is intentionally based on a small dataset so that the calculation can be
verified manually during training. Learners should first understand the mathematical
relationship, then follow how the Python function implements the same operation.

## When should you use this?

Use column broadcasting when data has multiple axes such as observations, features, time, batches, images, or channels.

## Simple real-world scenario

Think of a batch of images or a table of observations and features; column broadcasting helps organize or calculate across the required dimensions efficiently.

## Trainer explanation

A useful classroom sequence is:

1. State the real-world question first.
2. Write the mathematical formula or relationship on the board.
3. Calculate a tiny example manually.
4. Run `main.py` and compare the program output with the manual result.
5. Change one input and ask learners to predict what will happen before executing it.

## Important interpretation / caution

Shape and axis mistakes are common. Print `.shape` and verify which real-world dimension each axis represents.

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
