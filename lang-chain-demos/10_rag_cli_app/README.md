# Mini Production-Style RAG CLI

Persistent Chroma index, ingestion command, query command, source display and configuration.

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
python main.py ingest /path/to/document.pdf
python main.py ask "What does the document say about concurrency?"
```

## Learning objective

Persistent Chroma index, ingestion command, query command, source display and configuration.
