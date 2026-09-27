import json
from pathlib import Path

from google.protobuf import descriptor_pb2, descriptor_pool, message_factory

R = Path("/mnt/data/linear_regression_bundle")
m = json.loads((R / "model_metrics.json").read_text())
fd = descriptor_pb2.FileDescriptorProto()
fd.name = "mini_onnx.proto"
fd.package = "onnx"


def msg(name):
    x = fd.message_type.add()
    x.name = name
    return x


def fld(M, n, num, typ, label=1, type_name=None):
    f = M.field.add()
    f.name = n
    f.number = num
    f.type = typ
    f.label = label
    if type_name:
        f.type_name = type_name
    return f


# protobuf type numbers: double1 float2 int64=3 string=9 message=11
D = msg("Dimension")
fld(D, "dim_value", 1, 3)
S = msg("TensorShapeProto")
fld(S, "dim", 1, 11, 3, ".onnx.Dimension")
TT = msg("TensorTypeProto")
fld(TT, "elem_type", 1, 3)
fld(TT, "shape", 2, 11, 1, ".onnx.TensorShapeProto")
TP = msg("TypeProto")
fld(TP, "tensor_type", 1, 11, 1, ".onnx.TensorTypeProto")
VI = msg("ValueInfoProto")
fld(VI, "name", 1, 9)
fld(VI, "type", 2, 11, 1, ".onnx.TypeProto")
A = msg("AttributeProto")
fld(A, "name", 1, 9)
fld(A, "f", 2, 2)
fld(A, "i", 3, 3)
fld(A, "s", 4, 12)
fld(A, "floats", 7, 2, 3)
fld(A, "ints", 8, 3, 3)
fld(A, "type", 20, 3)
N = msg("NodeProto")
fld(N, "input", 1, 9, 3)
fld(N, "output", 2, 9, 3)
fld(N, "name", 3, 9)
fld(N, "op_type", 4, 9)
fld(N, "attribute", 5, 11, 3, ".onnx.AttributeProto")
fld(N, "domain", 7, 9)
G = msg("GraphProto")
fld(G, "node", 1, 11, 3, ".onnx.NodeProto")
fld(G, "name", 2, 9)
fld(G, "input", 11, 11, 3, ".onnx.ValueInfoProto")
fld(G, "output", 12, 11, 3, ".onnx.ValueInfoProto")
O = msg("OperatorSetIdProto")
fld(O, "domain", 1, 9)
fld(O, "version", 2, 3)
M = msg("ModelProto")
fld(M, "ir_version", 1, 3)
fld(M, "producer_name", 2, 9)
fld(M, "domain", 4, 9)
fld(M, "model_version", 5, 3)
fld(M, "graph", 7, 11, 1, ".onnx.GraphProto")
fld(M, "opset_import", 8, 11, 3, ".onnx.OperatorSetIdProto")
pool = descriptor_pool.DescriptorPool()
pool.Add(fd)
Model = message_factory.GetMessageClass(pool.FindMessageTypeByName("onnx.ModelProto"))
model = Model()
model.ir_version = 8
model.producer_name = "ChatGPT training bundle"
model.model_version = 1
op = model.opset_import.add()
op.domain = "ai.onnx.ml"
op.version = 1
# input/output
inp = model.graph.input.add()
inp.name = "float_input"
inp.type.tensor_type.elem_type = 1
inp.type.tensor_type.shape.dim.add().dim_value = 1
inp.type.tensor_type.shape.dim.add().dim_value = 4
out = model.graph.output.add()
out.name = "variable"
out.type.tensor_type.elem_type = 1
out.type.tensor_type.shape.dim.add().dim_value = 1
out.type.tensor_type.shape.dim.add().dim_value = 1
model.graph.name = "LinearRegressionHousePrice"
n = model.graph.node.add()
n.input.append("float_input")
n.output.append("variable")
n.name = "LinearRegressor"
n.op_type = "LinearRegressor"
n.domain = "ai.onnx.ml"
a = n.attribute.add()
a.name = "coefficients"
a.floats.extend(m["coefficients"])
a.type = 6
a = n.attribute.add()
a.name = "intercepts"
a.floats.append(m["intercept"])
a.type = 6
a = n.attribute.add()
a.name = "targets"
a.i = 1
a.type = 2
(R / "linear_regression_model.onnx").write_bytes(model.SerializeToString())
print("onnx bytes", (R / "linear_regression_model.onnx").stat().st_size)
