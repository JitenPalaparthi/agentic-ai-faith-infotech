# Example 059: Natural Logarithm

## Learning objective

The natural logarithm ln(x) is the inverse of eˣ. It converts multiplication into addition and is widely used for skewed data and likelihoods.

## Mathematical formula / relationship

**ln(eˣ)=x**

## Mathematical interpretation

The code is intentionally based on a small dataset so that the calculation can be
verified manually during training. Learners should first understand the mathematical
relationship, then follow how the Python function implements the same operation.

## When should you use this?

Use natural logarithm when modeling mathematical change, relationships between variables, or numerical optimization.

## Simple real-world scenario

Start with a small x/y relationship, calculate natural logarithm manually, then use the Python function to show how the same mathematics scales to many values.

## Trainer explanation

A useful classroom sequence is:

1. State the real-world question first.
2. Write the mathematical formula or relationship on the board.
3. Calculate a tiny example manually.
4. Run `main.py` and compare the program output with the manual result.
5. Change one input and ask learners to predict what will happen before executing it.

## Important interpretation / caution

The mathematical assumptions of the function must match the real relationship; a convenient formula is not automatically a good model.

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
