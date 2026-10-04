from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.1:8b", temperature=0)

class TravelState(TypedDict):
    destination: str
    budget: int
    days: int
    interests: list[str]
    itinerary: str

def planner(state: TravelState):
    prompt = f"""Create a concise demo itinerary.
Destination: {state['destination']}
Budget INR: {state['budget']}
Days: {state['days']}
Interests: {', '.join(state['interests'])}
"""
    return {"itinerary": llm.invoke(prompt).content}

g = StateGraph(TravelState)
g.add_node("planner", planner)
g.add_edge(START, "planner")
g.add_edge("planner", END)
app = g.compile()

print(app.invoke({
    "destination": "Kochi", "budget": 20000, "days": 3,
    "interests": ["food", "history"], "itinerary": ""
})["itinerary"])
