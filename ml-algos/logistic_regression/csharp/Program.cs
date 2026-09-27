using Microsoft.ML.OnnxRuntime;
using Microsoft.ML.OnnxRuntime.Tensors;

using var session = new InferenceSession("../logistic_regression_model.onnx");
var input = new DenseTensor<float>(new[] { 1, 5 });
float[] values = { 18.0f, 760.0f, 0.18f, 8.0f, 12.0f };
for (int i = 0; i < values.Length; i++) input[0, i] = values[i];
var inputs = new List<NamedOnnxValue> { NamedOnnxValue.CreateFromTensor("float_input", input) };
using var results = session.Run(inputs);
foreach (var r in results) Console.WriteLine($"{r.Name}: {r.Value}");
