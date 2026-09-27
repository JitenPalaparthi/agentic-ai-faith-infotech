import numpy as np
import onnxruntime as ort
session = ort.InferenceSession('../logistic_regression_model.onnx')
x = np.array([[18.0, 760.0, 0.18, 8.0, 12.0]], dtype=np.float32)
outputs = session.run(None, {'float_input': x})
print('Class:', outputs[0][0])
print('Probabilities:', outputs[1][0])
