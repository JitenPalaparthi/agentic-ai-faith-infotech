# Example 097: Einstein Summation

## Learning objective

Einstein notation labels dimensions with indices and states which indices are summed. It provides a compact way to express matrix products and tensor contractions.

## Mathematical formula / relationship

**Cᵢₖ = Σⱼ AᵢⱼBⱼₖ**

## Mathematical interpretation

The code is intentionally based on a small dataset so that the calculation can be
verified manually during training. Learners should first understand the mathematical
relationship, then follow how the Python function implements the same operation.

## When should you use this?

Use einstein summation when building an analytical or regression workflow where this concept answers a specific modeling or evaluation question.

## Simple real-world scenario

Apply einstein summation to a small sales, latency, pricing, or sensor dataset and compare the mathematical result with the Python output.

## Trainer explanation

A useful classroom sequence is:

1. State the real-world question first.
2. Write the mathematical formula or relationship on the board.
3. Calculate a tiny example manually.
4. Run `main.py` and compare the program output with the manual result.
5. Change one input and ask learners to predict what will happen before executing it.

## Important interpretation / caution

Interpret the result in context and validate assumptions before using it for decisions or predictive conclusions.

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
