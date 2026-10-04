from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:0.6b", temperature=0)
response = llm.invoke(
    "Explain goroutines in Go in three simple bullet points. /no_think"
)
print(response.content)
print(type(response))
print(response.content)
print(response.id)
print(response.name)
print(response.additional_kwargs)
print(response.response_metadata)
print("----> Tool Calls:")
print(response.tool_calls)
print(response.invalid_tool_calls)
print(response.usage_metadata)
