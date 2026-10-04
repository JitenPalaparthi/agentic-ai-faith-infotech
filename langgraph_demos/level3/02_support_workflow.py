from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:0.6b", temperature=0)

class State(TypedDict):
    issue: str
    category: str
    resolution: str

def classify(state: State):
    out = llm.invoke(
        "Classify as exactly billing, technical, or account. Only output one word. Issue: " + state["issue"]
    ).content.lower()
    category = "billing" if "billing" in out else "account" if "account" in out else "technical"
    return {"category": category}

def route(state: State):
    return state["category"]

def billing(state: State):
    return {"resolution": "Billing workflow: verify invoice and payment history."}

def technical(state: State):
    return {"resolution": "Technical workflow: collect logs and reproduce the error."}

def account(state: State):
    return {"resolution": "Account workflow: verify identity before account changes."}

g = StateGraph(State)
g.add_node("classify", classify)
g.add_node("billing", billing)
g.add_node("technical", technical)
g.add_node("account", account)
g.add_edge(START, "classify")
g.add_conditional_edges("classify", route,
                        {"billing": "billing", "technical": "technical", "account": "account"})
for n in ["billing", "technical", "account"]:
    g.add_edge(n, END)
app = g.compile()

print(app.invoke({"issue": "I was charged twice this month", "category": "", "resolution": ""}))
