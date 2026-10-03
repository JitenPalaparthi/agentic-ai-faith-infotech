import numpy as np
import onnxruntime as ort
session=ort.InferenceSession("models/kmeans_pipeline.onnx",providers=["CPUExecutionProvider"] )
print("INPUTS")
for x in session.get_inputs(): print(x.name,x.type,x.shape)
print("OUTPUTS")
for x in session.get_outputs(): print(x.name,x.type,x.shape)
sample=np.array([[29,48000,82,8,11]],dtype=np.float32)
outputs=session.run(None,{session.get_inputs()[0].name:sample})
for meta,value in zip(session.get_outputs(),outputs): print(meta.name, value)
