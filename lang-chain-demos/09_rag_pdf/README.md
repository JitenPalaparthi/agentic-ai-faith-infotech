# PDF RAG

Load a PDF, chunk it, build an in-memory vector index and ask grounded questions.

## Prerequisites

1. Install and start Ollama.
2. Pull the chat model: `ollama pull qwen3:0.6b`
3. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

For RAG, also execute: `ollama pull qwen3-embedding:0.6b`.

## Run

```bash
python main.py /path/to/document.pdf
```

## Learning objective

Load a PDF, chunk it, build an in-memory vector index and ask grounded questions.
