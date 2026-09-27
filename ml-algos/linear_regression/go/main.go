package main

import (
	"fmt"

	ort "github.com/yalue/onnxruntime_go"
)

func main() {
	//ort.SetSharedLibraryPath("./onnxruntime/lib/libonnxruntime.so") // adjust for OS
	ort.SetSharedLibraryPath(
		"./lib/libonnxruntime.dylib",
	)
	if err := ort.InitializeEnvironment(); err != nil {
		panic(err)
	}
	defer ort.DestroyEnvironment()
	input, err := ort.NewTensor(ort.NewShape(1, 4), []float32{1800, 3, 5, 8})
	if err != nil {
		panic(err)
	}
	defer input.Destroy()
	output, err := ort.NewEmptyTensor[float32](ort.NewShape(1, 1))
	if err != nil {
		panic(err)
	}
	defer output.Destroy()
	session, err := ort.NewAdvancedSession("../linear_regression_model.onnx", []string{"X"}, []string{"variable"}, []ort.Value{input}, []ort.Value{output}, nil)
	if err != nil {
		panic(err)
	}
	defer session.Destroy()
	if err = session.Run(); err != nil {
		panic(err)
	}
	fmt.Printf("Predicted price: %.2f lakhs\n", output.GetData()[0])
}
