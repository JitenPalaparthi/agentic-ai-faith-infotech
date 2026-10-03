# LangChain + Qwen3 0.6B — 10 Runnable Projects

All generation uses Ollama model `qwen3:0.6b`. Projects 8–10 additionally use `qwen3-embedding:0.6b` for embeddings because retrieval requires an embedding model.

## Projects

1. Basic LLM invocation
2. Prompt templates
3. LCEL and output parsing
4. Structured output with Pydantic
5. Multi-turn chat history
6. LangChain tools
7. Tool-calling agent
8. RAG over local text
9. PDF RAG
10. Persistent mini RAG CLI with Chroma

## Global setup

```bash
ollama pull qwen3:0.6b
ollama pull qwen3-embedding:0.6b   # needed for 08-10
```

Each directory is standalone and has its own README and requirements.txt. Run commands from inside that project's directory.

> Note: `qwen3:0.6b` is intentionally tiny. It is excellent for local demonstrations, but tool selection and strict structured output can be less reliable than larger models. The examples constrain prompts and temperature accordingly.

python3 -m venv .venv

source .venv/bin/activate
