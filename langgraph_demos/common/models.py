from langchain_ollama import ChatOllama, OllamaEmbeddings

LLAMA_MODEL = "llama3.1:8b"
QWEN_MODEL = "qwen3:0.6b"
EMBED_MODEL = "nomic-embed-text"

def llama(temperature=0):
    return ChatOllama(model=LLAMA_MODEL, temperature=temperature)

def qwen(temperature=0):
    return ChatOllama(model=QWEN_MODEL, temperature=temperature)

def embeddings():
    return OllamaEmbeddings(model=EMBED_MODEL)
