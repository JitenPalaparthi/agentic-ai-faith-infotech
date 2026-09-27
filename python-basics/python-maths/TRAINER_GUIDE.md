# Trainer Guide — Mathematics Before Python

These examples are designed to teach **why the mathematics is useful before showing the Python API**.

For every example, use this flow:

1. **Problem** — Give learners a simple real-world question.
2. **Concept** — Explain what the mathematical concept measures or transforms.
3. **Formula** — Write the formula and explain every symbol.
4. **Manual calculation** — Use 3–5 values and solve it without Python.
5. **Python implementation** — Open `main.py` and map each mathematical step to code.
6. **Interpretation** — Explain what the output means in the scenario.
7. **Variation** — Change the inputs and ask learners to predict the output.
8. **Limitation** — Explain when the concept should *not* be blindly used.

A particularly useful comparison for beginners is **mean vs median**: use a salary dataset with one
very large salary and show how the mean moves dramatically while the median remains representative
of the center. For vector algebra, contrast **dot product** (weighted combination/similarity/projection)
with **cross product** (3-D perpendicular direction). For matrices, contrast `A * B` with `A @ B`.
For regression, connect **y = mx + c → residuals → MSE/MAE → R²** as one continuous story.
