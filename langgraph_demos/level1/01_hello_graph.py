from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    name: str
    message: str

def greet(state: State):
    return {"message": f"Hello {state['name']}! Welcome to LangGraph."}

graph = StateGraph(State)
graph.add_node("greet", greet)
graph.add_edge(START, "greet")
graph.add_edge("greet", END)
app = graph.compile()

print(app.invoke({"name": "JP", "message": ""}))
