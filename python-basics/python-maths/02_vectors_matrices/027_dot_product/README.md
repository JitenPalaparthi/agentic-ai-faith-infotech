# Example 027: Dot Product

## Learning objective

The dot product is the sum of pairwise products. Geometrically a·b=||a||||b||cosθ, connecting algebra to the angle between vectors. It appears in similarity, projections and linear models.

## Mathematical formula / relationship

**a·b = Σaᵢbᵢ**

## Mathematical interpretation

The code is intentionally based on a small dataset so that the calculation can be
verified manually during training. Learners should first understand the mathematical
relationship, then follow how the Python function implements the same operation.

## When should you use this?

Use the dot product when combining weighted features, measuring directional similarity, calculating projections, or performing matrix multiplication.

## Simple real-world scenario

A model has feature values [2, 3, 4] and weights [0.5, 1.0, 2.0]. Their dot product gives the model's weighted score before adding an intercept.

## Trainer explanation

A useful classroom sequence is:

1. State the real-world question first.
2. Write the mathematical formula or relationship on the board.
3. Calculate a tiny example manually.
4. Run `main.py` and compare the program output with the manual result.
5. Change one input and ask learners to predict what will happen before executing it.

## Important interpretation / caution

The vectors must have compatible dimensions, and raw dot-product magnitude depends on vector scale.

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
