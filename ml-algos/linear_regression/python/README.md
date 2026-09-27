python3 -m venv .venv

# for windows
python -m venv .venv

source .venv/bin/activate 

# for windows
source .venv/Scripts/activate

pip install numpy scikit-learn onnxruntime

python infer_onnx.py
python infer_pickle.py
