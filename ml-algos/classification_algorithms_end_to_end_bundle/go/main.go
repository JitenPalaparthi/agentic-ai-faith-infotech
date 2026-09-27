package main

// Run after generating models/random_forest.onnx.
// One common Go ONNX Runtime binding is github.com/yalue/onnxruntime_go.
// The exact shared-library setup is platform dependent.

import (
    "fmt"
    ort "github.com/yalue/onnxruntime_go"
)

func main() {
    ort.SetSharedLibraryPath("libonnxruntime.so")
    if err := ort.InitializeEnvironment(); err != nil { panic(err) }
    defer ort.DestroyEnvironment()

    // Order MUST match Python training:
    // monthly_spend, tenure_months, support_calls, usage_hours_week,
    // late_payments, satisfaction_score, num_products, discount_percent
    inputData := []float32{145, 12, 7, 18, 5, 3, 2, 5}
    input, _ := ort.NewTensor(ort.NewShape(1, 8), inputData)
    defer input.Destroy()

    // skl2onnx classifiers commonly expose label + probabilities.
    // Inspect the generated model in Netron / Python ONNX Runtime if output
    // names/types differ for your runtime version.
    fmt.Println("Input tensor ready:", input.GetData())
    fmt.Println("Load random_forest.onnx with ONNX Runtime and execute session.")
}
