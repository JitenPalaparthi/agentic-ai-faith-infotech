from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    text: str
    upper: str
    word_count: int

def uppercase(state: State):
    return {"upper": state["text"].upper()}

def count_words(state: State):
    return {"word_count": len(state["text"].split())}

g = StateGraph(State)
g.add_node("uppercase", uppercase)
g.add_node("count_words", count_words)
g.add_edge(START, "uppercase")
g.add_edge("uppercase", "count_words")
g.add_edge("count_words", END)
app = g.compile()

print(app.invoke({"text": "LangGraph makes workflows explicit", "upper": "", "word_count": 0}))
