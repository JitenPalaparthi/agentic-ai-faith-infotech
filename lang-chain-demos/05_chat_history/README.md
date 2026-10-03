# Conversation History

Maintain multi-turn state explicitly with InMemoryChatMessageHistory.

## Prerequisites

1. Install and start Ollama.
2. Pull the chat model: `ollama pull qwen3:0.6b`
3. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```



## Run

```bash
python main.py
```

## Learning objective

Maintain multi-turn state explicitly with InMemoryChatMessageHistory.
