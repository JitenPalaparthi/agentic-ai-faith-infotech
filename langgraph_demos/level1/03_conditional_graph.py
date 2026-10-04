from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    number: int
    result: str

def route(state: State):
    return "even" if state["number"] % 2 == 0 else "odd"

def even_node(state: State):
    return {"result": f"{state['number']} is even"}

def odd_node(state: State):
    return {"result": f"{state['number']} is odd"}

g = StateGraph(State)
g.add_node("even", even_node)
g.add_node("odd", odd_node)
g.add_conditional_edges(START, route, {"even": "even", "odd": "odd"})
g.add_edge("even", END)
g.add_edge("odd", END)
app = g.compile()

for n in [10, 7]:
    print(app.invoke({"number": n, "result": ""}))
