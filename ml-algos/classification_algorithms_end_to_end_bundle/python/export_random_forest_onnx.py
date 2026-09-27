# Install first:
# pip install skl2onnx onnx onnxruntime
#
# This example exports Random Forest. Tree-based sklearn models are especially
# convenient for ONNX because no StandardScaler is required here.
import joblib
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

model = joblib.load("../models/03_random_forest.pkl")
initial_type = [("float_input", FloatTensorType([None, 8]))]
onnx_model = convert_sklearn(model, initial_types=initial_type, target_opset=17)

with open("../models/random_forest.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

print("Created ../models/random_forest.onnx")
