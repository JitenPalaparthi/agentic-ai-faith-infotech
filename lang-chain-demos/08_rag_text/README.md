# RAG over Local Text

Split a local document, embed it, retrieve relevant chunks and answer using qwen3:0.6b.

## Prerequisites

1. Install and start Ollama.
2. Pull the chat model: `ollama pull qwen3:0.6b`
3. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Before running, also execute: `ollama pull qwen3-embedding:0.6b`.

## Run

```bash
python main.py
```

## Learning objective

Split a local document, embed it, retrieve relevant chunks and answer using qwen3:0.6b.
