import numpy as np, onnxruntime as ort
session=ort.InferenceSession('../linear_regression_model.onnx')
x=np.array([[1800,3,5,8]],dtype=np.float32)
y=session.run(None, {'float_input':x})
print('Predicted price (lakhs):', float(np.asarray(y[0]).reshape(-1)[0]))
