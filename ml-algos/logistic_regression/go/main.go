package main

import (
    "fmt"
    ort "github.com/yalue/onnxruntime_go"
)

func main() {
    ort.SetSharedLibraryPath("./onnxruntime/lib/libonnxruntime.so")
    if err := ort.InitializeEnvironment(); err != nil { panic(err) }
    defer ort.DestroyEnvironment()

    input, _ := ort.NewTensor(ort.NewShape(1, 5), []float32{18.0, 760.0, 0.18, 8.0, 12.0})
    defer input.Destroy()
    label, _ := ort.NewEmptyTensor[int64](ort.NewShape(1))
    defer label.Destroy()
    probabilities, _ := ort.NewEmptyTensor[float32](ort.NewShape(1, 2))
    defer probabilities.Destroy()

    session, err := ort.NewAdvancedSession("../logistic_regression_model.onnx",
        []string{"float_input"}, []string{"label", "probabilities"},
        []ort.ArbitraryTensor{input}, []ort.ArbitraryTensor{label, probabilities}, nil)
    if err != nil { panic(err) }
    defer session.Destroy()
    if err := session.Run(); err != nil { panic(err) }
    fmt.Println("Predicted class:", label.GetData()[0])
    fmt.Println("P(class 0), P(class 1):", probabilities.GetData())
}
