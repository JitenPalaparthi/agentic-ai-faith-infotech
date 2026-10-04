import os
import psycopg
from dotenv import load_dotenv
from typing import Annotated, Literal
from typing_extensions import TypedDict

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/companydb",
)
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b")


# ------------------------------------------------------------
# 1. LANGGRAPH STATE
# ------------------------------------------------------------
# Every node receives this state.
# add_messages appends new messages instead of replacing the list.
class State(TypedDict):
    messages: Annotated[list, add_messages]


# ------------------------------------------------------------
# 2. TOOL
# ------------------------------------------------------------
@tool
def execute_sql(query: str) -> str:
    """
    Execute a read-only PostgreSQL SELECT query.

    The database has an employees table with these columns:
    id, name, department, salary, city.

    Use this tool whenever employee data must be retrieved.
    """
    cleaned = query.strip()

    # Deliberately simple safety check for a teaching demo.
    # Production systems should use a DB role with SELECT-only privileges too.
    if not cleaned.lower().startswith("select"):
        return "Rejected: only SELECT queries are allowed."

    # Prevent multiple statements in this simple demo.
    if ";" in cleaned.rstrip(";"):
        return "Rejected: multiple SQL statements are not allowed."

    try:
        with psycopg.connect(DATABASE_URL) as conn:
            # A read-only transaction adds another guardrail.
            conn.execute("SET TRANSACTION READ ONLY")

            with conn.cursor() as cursor:
                cursor.execute(cleaned)
                rows = cursor.fetchall()

                if cursor.description is None:
                    return "Query returned no tabular result."

                columns = [column.name for column in cursor.description]

                if not rows:
                    return f"Columns: {columns}\nRows: []"

                return f"Columns: {columns}\nRows: {rows}"

    except Exception as exc:
        # Returning the error lets the LLM inspect it and potentially retry.
        return f"PostgreSQL error: {exc}"


tools = [execute_sql]


# ------------------------------------------------------------
# 3. LLM + TOOL BINDING
# ------------------------------------------------------------
llm = ChatOllama(
    model=OLLAMA_MODEL,
    temperature=0,
)

# This exposes the tool schema/name/description to the LLM.
# The LLM decides whether it wants to request a tool call.
llm_with_tools = llm.bind_tools(tools)


SYSTEM_PROMPT = """
You are a PostgreSQL SQL agent.

Database schema:

employees(
    id INTEGER,
    name VARCHAR,
    department VARCHAR,
    salary NUMERIC,
    city VARCHAR
)

Rules:
- When a question requires employee data, use execute_sql.
- Generate PostgreSQL-compatible SQL.
- Only generate SELECT statements.
- Never INSERT, UPDATE, DELETE, DROP, ALTER, TRUNCATE or CREATE.
- After receiving tool results, answer in simple human-readable language.
- If a query fails, inspect the error and, when reasonable, correct the SELECT
  query and call the tool again.
"""


# ------------------------------------------------------------
# 4. AGENT NODE
# ------------------------------------------------------------
def agent_node(state: State):
    """Ask the LLM what to do next."""
    response = llm_with_tools.invoke(
        [SystemMessage(content=SYSTEM_PROMPT)] + state["messages"]
    )
    return {"messages": [response]}


# ------------------------------------------------------------
# 5. TOOL NODE
# ------------------------------------------------------------
# ToolNode looks at the AIMessage tool_calls and executes the requested tool.
tool_node = ToolNode(tools)


# ------------------------------------------------------------
# 6. CONDITIONAL ROUTER
# ------------------------------------------------------------
def should_continue(state: State) -> Literal["tools", "end"]:
    """
    If the LLM requested a tool, route to ToolNode.
    Otherwise the LLM has produced the final answer.
    """
    last_message = state["messages"][-1]

    if getattr(last_message, "tool_calls", None):
        return "tools"

    return "end"


# ------------------------------------------------------------
# 7. BUILD THE LANGGRAPH
# ------------------------------------------------------------
builder = StateGraph(State)

builder.add_node("agent", agent_node)
builder.add_node("tools", tool_node)

builder.add_edge(START, "agent")

builder.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        "end": END,
    },
)

# After a tool executes, send its ToolMessage back to the LLM.
builder.add_edge("tools", "agent")

graph = builder.compile()


# ------------------------------------------------------------
# 8. COMMAND-LINE CHAT
# ------------------------------------------------------------
def print_trace(result):
    """Print the messages so students can see the agent/tool loop."""
    print("\n--- LangGraph trace ---")

    for i, message in enumerate(result["messages"], start=1):
        kind = message.__class__.__name__
        print(f"\n[{i}] {kind}")

        tool_calls = getattr(message, "tool_calls", None)
        if tool_calls:
            print("Tool calls:")
            for call in tool_calls:
                print(f"  {call}")

        if getattr(message, "content", None):
            print(message.content)

    print("\n-----------------------")


def main():
    print("LangGraph + PostgreSQL SQL Agent")
    print(f"Ollama model: {OLLAMA_MODEL}")
    print("Type 'exit' to stop.")
    print("\nTry:")
    print("  Who has the highest salary?")
    print("  Show all Engineering employees.")
    print("  What is the average salary by department?")
    print("  How many employees are in Hyderabad?")

    while True:
        question = input("\nYou: ").strip()

        if question.lower() in {"exit", "quit"}:
            break

        if not question:
            continue

        result = graph.invoke(
            {"messages": [HumanMessage(content=question)]}
        )

        print_trace(result)
        print("\nAgent:", result["messages"][-1].content)


if __name__ == "__main__":
    main()
