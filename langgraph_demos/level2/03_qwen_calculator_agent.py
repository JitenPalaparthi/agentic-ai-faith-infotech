from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START
from langgraph.graph.message import MessagesState
from langgraph.prebuilt import ToolNode, tools_condition

@tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@tool
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@tool
def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

tools = [add, subtract, multiply, divide]
llm = ChatOllama(model="qwen3:0.6b", temperature=0).bind_tools(tools)

def assistant(state: MessagesState):
    return {"messages": [llm.invoke(state["messages"])]}

g = StateGraph(MessagesState)
g.add_node("assistant", assistant)
g.add_node("tools", ToolNode(tools))
g.add_edge(START, "assistant")
g.add_conditional_edges("assistant", tools_condition)
g.add_edge("tools", "assistant")
app = g.compile()

result = app.invoke({"messages": [("user", "Add 45 and 18, then tell me the result.")]})
for m in result["messages"]:
    print(type(m).__name__, ":", getattr(m, "content", ""))
    if getattr(m, "tool_calls", None):
        print("  TOOL CALLS:", m.tool_calls)
