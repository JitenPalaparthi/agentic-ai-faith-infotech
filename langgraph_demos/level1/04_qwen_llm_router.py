from typing_extensions import TypedDict, Literal
from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:0.6b", temperature=0)

class State(TypedDict):
    question: str
    category: str
    answer: str

def classify(state: State):
    prompt = """Classify the question into exactly one word:
technical, billing, general.
Return only the category.

Question: """ + state["question"]
    category = llm.invoke(prompt).content.strip().lower()
    if "technical" in category:
        category = "technical"
    elif "billing" in category:
        category = "billing"
    else:
        category = "general"
    return {"category": category}

def choose(state: State):
    return state["category"]

def technical(state: State):
    return {"answer": "TECHNICAL TEAM: " + llm.invoke("Answer briefly: " + state["question"]).content}

def billing(state: State):
    return {"answer": "BILLING TEAM: Please check the billing/account details for this request."}

def general(state: State):
    return {"answer": "GENERAL TEAM: " + llm.invoke("Answer briefly: " + state["question"]).content}

g = StateGraph(State)
g.add_node("classify", classify)
g.add_node("technical", technical)
g.add_node("billing", billing)
g.add_node("general", general)
g.add_edge(START, "classify")
g.add_conditional_edges("classify", choose,
                        {"technical": "technical", "billing": "billing", "general": "general"})
for node in ["technical", "billing", "general"]:
    g.add_edge(node, END)
app = g.compile()

for q in ["Why is my Python API returning 500?", "Why was I charged twice?", "Who are you?"]:
    print("\nQUESTION:", q)
    print(app.invoke({"question": q, "category": "", "answer": ""}))
