from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START
from langgraph.graph.message import MessagesState
from langgraph.prebuilt import ToolNode, tools_condition

EMPLOYEES = {
    101: {"name": "Ravi", "department": "Engineering", "location": "Hyderabad"},
    102: {"name": "Anita", "department": "Finance", "location": "Bengaluru"},
}

@tool
def get_employee(employee_id: int) -> dict:
    """Get employee details using an employee ID."""
    return EMPLOYEES.get(employee_id, {"error": "employee not found"})

tools = [get_employee]
llm = ChatOllama(model="llama3.1:8b", temperature=0).bind_tools(tools)

def agent(state: MessagesState):
    return {"messages": [llm.invoke(state["messages"])]}

g = StateGraph(MessagesState)
g.add_node("agent", agent)
g.add_node("tools", ToolNode(tools))
g.add_edge(START, "agent")
g.add_conditional_edges("agent", tools_condition)
g.add_edge("tools", "agent")
app = g.compile()

result = app.invoke({"messages": [("user", "Where does employee 101 work and which department?")]})
print(result["messages"][-1].content)
