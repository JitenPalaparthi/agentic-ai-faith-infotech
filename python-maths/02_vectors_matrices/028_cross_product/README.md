# Example 028: Cross Product

## Learning objective

For 3-D vectors, the cross product produces a vector perpendicular to both inputs. Its magnitude equals the area of the parallelogram formed by the vectors.

## Mathematical formula / relationship

**||a×b|| = ||a||||b||sinθ**

## Mathematical interpretation

The code is intentionally based on a small dataset so that the calculation can be
verified manually during training. Learners should first understand the mathematical
relationship, then follow how the Python function implements the same operation.

## When should you use this?

Use the cross product mainly with 3-D geometry when you need a vector perpendicular to two directions.

## Simple real-world scenario

In graphics or robotics, two vectors lying on a surface can be crossed to calculate the surface normal used for orientation or lighting.

## Trainer explanation

A useful classroom sequence is:

1. State the real-world question first.
2. Write the mathematical formula or relationship on the board.
3. Calculate a tiny example manually.
4. Run `main.py` and compare the program output with the manual result.
5. Change one input and ask learners to predict what will happen before executing it.

## Important interpretation / caution

The standard vector cross product is fundamentally a 3-D operation; do not use it as a generic similarity measure.

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
