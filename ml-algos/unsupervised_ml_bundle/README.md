# Unsupervised ML — 10,000 Record Teaching Bundle

This project demonstrates two unsupervised-learning use cases on synthetic customer data.

**Algorithms**
- K-Means: discovers customer segments without a target/label column.
- Isolation Forest: detects unusual customers/outliers without supervised class labels.

## Dataset
`data/customers_10000.csv` contains exactly 10,000 rows. Features used for learning: age, annual_income, spending_score, monthly_visits, monthly_purchases. `customer_id` is an identifier and is deliberately excluded. `synthetic_anomaly` exists only so the generated teaching data can be inspected; the models do NOT train on it.

## Setup
```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run
```bash
python train.py
python predict_pickle.py
python visualize.py
python convert_kmeans_to_onnx.py
python predict_onnx.py
```

## Included pre-trained artifacts
- `models/kmeans_pipeline.pkl`
- `models/isolation_forest_pipeline.pkl`
- `outputs/predictions_10000.csv`
- `outputs/metrics.txt`

## ONNX note
The K-Means pipeline has a straightforward `skl2onnx` conversion path, so `convert_kmeans_to_onnx.py` creates `models/kmeans_pipeline.onnx`. Isolation Forest converter support can vary by `skl2onnx`/opset version; the Pickle pipeline is included as the reliable executable artifact for that model. The requirements include ONNX Runtime so you can inspect inputs/outputs and run inference.

## Important teaching point
K-Means cluster IDs (0, 1, 2, 3) are arbitrary identifiers, not class meanings or quality rankings. Interpret a cluster by examining its centroid/feature profile. Isolation Forest returns `1` for an inlier and `-1` for an anomaly.

Current generated metric: K-Means silhouette score = 0.3790.
