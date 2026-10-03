from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers. Use this for multiplication."""
    return a * b

@tool
def get_service_status(name: str) -> str:
    """Get demo status for a named microservice."""
    return {"payment": "UP", "inventory": "DOWN"}.get(name.lower(), "UNKNOWN")

model = ChatOllama(model="qwen3:0.6b", temperature=0)
agent = create_agent(model=model, tools=[multiply, get_service_status], system_prompt="Use tools when they can answer the request. Keep answers short.")
result = agent.invoke({"messages": [{"role": "user", "content": "Use the multiplication tool to calculate 17 times 23."}]})
print(result["messages"][-1].content)
