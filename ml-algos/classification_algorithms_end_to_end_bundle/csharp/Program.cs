using Microsoft.ML.OnnxRuntime;
using Microsoft.ML.OnnxRuntime.Tensors;

class Program
{
    static void Main()
    {
        // Order must exactly match the Python feature order.
        float[] values = {145f, 12f, 7f, 18f, 5f, 3f, 2f, 5f};

        using var session = new InferenceSession("../models/random_forest.onnx");
        var tensor = new DenseTensor<float>(values, new[] {1, 8});

        // Confirm the exported input name using session.InputMetadata.
        string inputName = session.InputMetadata.Keys.First();
        var inputs = new[] { NamedOnnxValue.CreateFromTensor(inputName, tensor) };

        using var results = session.Run(inputs);
        foreach (var result in results)
            Console.WriteLine($"{result.Name}: {result.Value}");
    }
}
