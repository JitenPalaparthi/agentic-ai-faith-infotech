"""15 — Feature leakage: one of the most important ML lessons."""
import pandas as pd

df = pd.DataFrame({
    "customer_id": [1, 2, 3],
    "visits_before_prediction": [5, 20, 10],
    "bought": [0, 1, 0],
    # Imagine this was recorded only AFTER the prediction point:
    "payment_completed_after_prediction": [0, 1, 0]
})

print(df)

print("""
Suppose our task is to predict `bought`.

GOOD:
visits_before_prediction
because it existed before prediction.

LEAKY:
payment_completed_after_prediction
because it became known after the prediction point and practically reveals outcome.

Golden question:
"Would I know this feature at the exact moment the prediction is made?"

If not, do not use it.
""")
