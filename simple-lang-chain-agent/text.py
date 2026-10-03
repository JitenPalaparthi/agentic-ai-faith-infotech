from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="qwen3:0.6b",
    base_url="http://localhost:11434",
    temperature=0,
)


print("Starting Qwen...")


for chunk in llm.stream("Say hello in one sentence"):

    if chunk.content:
        print(chunk.content, end="", flush=True)


print("\nDONE")
