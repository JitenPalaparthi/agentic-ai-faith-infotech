import onnxruntime as ort

session = ort.InferenceSession("../logistic_regression_model.onnx")

print("=== INPUTS ===")
for inp in session.get_inputs():
    print("Name :", inp.name)
    print("Type :", inp.type)
    print("Shape:", inp.shape)
    print()

print("=== OUTPUTS ===")
for out in session.get_outputs():
    print("Name :", out.name)
    print("Type :", out.type)
    print("Shape:", out.shape)
    print()
