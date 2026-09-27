using Microsoft.ML.OnnxRuntime;
using Microsoft.ML.OnnxRuntime.Tensors;
using var session = new InferenceSession("../linear_regression_model.onnx");
var input = new DenseTensor<float>(new[] { 1, 4 });
input[0, 0] = 1800; input[0, 1] = 3; input[0, 2] = 5; input[0, 3] = 8;
var inputs = new[] { NamedOnnxValue.CreateFromTensor("X", input) };
using var results = session.Run(inputs);
var prediction = results.First(x => x.Name == "variable").AsTensor<float>().ToArray()[0];
Console.WriteLine($"Predicted price: {prediction:F2} lakhs");
