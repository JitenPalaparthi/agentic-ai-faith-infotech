# Run after: pip install -r ../requirements.txt
import joblib
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

model = joblib.load('../logistic_regression_model.pkl')
initial_type = [('float_input', FloatTensorType([None, 5]))]
onnx_model = convert_sklearn(model, initial_types=initial_type, options={id(model.named_steps['model']): {'zipmap': False}})
with open('../logistic_regression_model.onnx', 'wb') as f:
    f.write(onnx_model.SerializeToString())
print('Created ../logistic_regression_model.onnx')
