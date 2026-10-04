from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import MessagesState
from langgraph.checkpoint.memory import InMemorySaver

llm = ChatOllama(model="llama3.1:8b", temperature=0)

def chat(state: MessagesState):
    return {"messages": [llm.invoke(state["messages"])]}

g = StateGraph(MessagesState)
g.add_node("chat", chat)
g.add_edge(START, "chat")
g.add_edge("chat", END)
app = g.compile(checkpointer=InMemorySaver())

config = {"configurable": {"thread_id": "class-demo"}}

r1 = app.invoke({"messages": [("user", "My favorite programming language is Go.")]}, config)
print("1:", r1["messages"][-1].content)

r2 = app.invoke({"messages": [("user", "What is my favorite programming language?")]}, config)
print("2:", r2["messages"][-1].content)
