import joblib
from skl2onnx import to_onnx
import numpy as np
model=joblib.load("models/kmeans_pipeline.pkl")
sample=np.zeros((1,5),dtype=np.float32)
onnx_model=to_onnx(model,sample,target_opset=15)
with open("models/kmeans_pipeline.onnx","wb") as f: f.write(onnx_model.SerializeToString())
print("Created models/kmeans_pipeline.onnx")
