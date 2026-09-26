# Example 035: Matrix Multiplication

## Learning objective

For A(m×n) and B(n×p), AB is m×p. Each output cell is the dot product of one row of A and one column of B.

## Mathematical formula / relationship

**Cᵢⱼ = Σₖ AᵢₖBₖⱼ**

## Mathematical interpretation

The code is intentionally based on a small dataset so that the calculation can be
verified manually during training. Learners should first understand the mathematical
relationship, then follow how the Python function implements the same operation.

## When should you use this?

Use matrix multiplication to apply linear transformations, combine layers of numerical relationships, or calculate many weighted sums at once.

## Simple real-world scenario

A data matrix containing 1,000 customers × 20 features multiplied by a 20 × 3 weight matrix produces three scores for every customer in one operation.

## Trainer explanation

A useful classroom sequence is:

1. State the real-world question first.
2. Write the mathematical formula or relationship on the board.
3. Calculate a tiny example manually.
4. Run `main.py` and compare the program output with the manual result.
5. Change one input and ask learners to predict what will happen before executing it.

## Important interpretation / caution

Inner dimensions must match; matrix multiplication is different from element-wise multiplication.

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
