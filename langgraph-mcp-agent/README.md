# LangGraph + MCP Client/Server + Ollama Agent

This teaching demo deliberately separates **MCP**, **LLM tool selection**, and
**LangGraph orchestration**.

## Architecture

```text
User
 |
 v
LangGraph: agent node (Qwen)
 |
 | LLM requests a tool?
 +---- no ------------------------> END
 |
 yes
 v
LangGraph: tools node
 |
 v
MCP Client
 |
 | call_tool(...)
 v
MCP Server
 |  add
 |  subtract
 |  multiply
 |  divide
 v
MCP result
 |
 v
ToolMessage
 |
 +-------------------------------> agent node
                                      |
                                      v
                                  final answer
```

## Responsibilities

| Part | Responsibility |
|---|---|
| Qwen / LLM | Chooses which available tool to request |
| LangGraph | Controls the agent -> tool -> agent loop |
| MCP Client | Discovers and invokes MCP capabilities |
| MCP Server | Owns and implements the actual tools |

**MCP is not the agent.** It is the standardized boundary between a capability
provider (server) and a consumer (client/host).

## Files

```text
mcp_server.py       # MCP server with four calculator tools
mcp_client_demo.py  # pure MCP test: no LLM, no LangGraph
agent.py            # MCP client + Qwen + explicit LangGraph agent
requirements.txt
.env.example
README.md
```

## 1. Setup

Python 3.11+ is recommended.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## 2. Check Ollama before running the agent

```bash
ollama list
```

`.env` defaults to:

```text
OLLAMA_MODEL=qwen3:4b
```

The model name must exactly match an installed Ollama model. Change `.env` if
you already have another tool-capable model.

If needed:

```bash
ollama pull qwen3:4b
```

## 3. Understand the MCP server

`mcp_server.py` creates the server:

```python
from mcp.server import MCPServer

mcp = MCPServer("Calculator MCP Server")
```

A normal Python function becomes an MCP tool:

```python
@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b
```

The name, docstring and type hints become discoverable tool metadata/schema.

`mcp.run()` uses stdio by default. There is no HTTP port in this demo. The MCP
client launches the server as a child process and talks through stdin/stdout.

## 4. First test MCP without AI

Run:

```bash
python mcp_client_demo.py
```

This is important because it proves MCP does not require an LLM.

The client connects:

```python
async with Client(server) as client:
```

It discovers capabilities:

```python
listed = await client.list_tools()
```

Then directly calls one:

```python
await client.call_tool(
    "multiply",
    {"a": 25, "b": 18},
)
```

Conceptually:

```text
MCP Client
   |
   | list_tools()
   v
MCP Server
   |
   +--> add
   +--> subtract
   +--> multiply
   +--> divide

MCP Client
   |
   | call_tool("multiply", {"a":25,"b":18})
   v
MCP Server
   |
   v
multiply(25,18)
   |
   v
450
```

## 5. Run the LangGraph agent

```bash
python agent.py
```

Try:

```text
What is 25 * 18?
Add 100 and 55.
Divide 144 by 12.
What is (10 + 5) * 3?
```

## 6. Dynamic tool discovery

`agent.py` does not manually implement the calculator operations.

It asks the MCP server:

```python
listed = await mcp_client.list_tools()
```

The MCP server returns tool definitions including names, descriptions and input
schemas.

The demo converts each MCP definition into a LangChain `StructuredTool` adapter:

```python
tools = [
    mcp_tool_to_langchain(mcp_client, tool)
    for tool in listed.tools
]
```

The adapter's implementation simply forwards the call through MCP:

```python
result = await mcp_client.call_tool(mcp_tool.name, kwargs)
```

The real calculator implementation remains in `mcp_server.py`.

## 7. How does Qwen know the tools?

This line matters:

```python
llm_with_tools = llm.bind_tools(tools)
```

Conceptually Qwen is told:

```text
Available:
add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)
```

It sees the schemas and descriptions, not the MCP server's Python
implementation.

## 8. Who chooses multiply?

Question:

```text
What is 25 * 18?
```

Qwen may emit a structured tool call:

```text
name: multiply
arguments:
  a: 25
  b: 18
```

Therefore the **LLM chooses the tool**.

LangGraph's router only checks whether a tool call exists:

```python
def should_continue(state):
    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tools"

    return "end"
```

The router does not decide between `multiply` and `divide`.

## 9. LangGraph

The graph is intentionally explicit:

```python
builder = StateGraph(State)

builder.add_node("agent", agent_node)
builder.add_node("tools", tool_node)

builder.add_edge(START, "agent")

builder.add_conditional_edges(
    "agent",
    should_continue,
    {"tools": "tools", "end": END},
)

builder.add_edge("tools", "agent")

graph = builder.compile()
```

So:

```text
              +-------------------+
              |                   |
              v                   |
START ---> agent ---> tools ------+
             |
             | no tool call
             v
            END
```

## 10. Full execution for "25 * 18"

```text
HumanMessage
"What is 25 * 18?"
       |
       v
agent node / Qwen
       |
       | AIMessage tool call:
       | multiply(a=25,b=18)
       v
tools node
       |
       v
MCP Client
       |
       | call_tool("multiply", ...)
       v
MCP Server
       |
       | multiply(25,18)
       v
450
       |
       v
MCP Client
       |
       v
ToolMessage("450")
       |
       v
agent node / Qwen
       |
       | "25 × 18 = 450."
       v
router
       |
       | no new tool call
       v
END
```

For `(10 + 5) * 3`, the model may make multiple calls. The graph can loop:

```text
agent -> add -> agent -> multiply -> agent -> END
```

That is a useful demonstration of why an agent is different from a fixed
single-tool workflow.

## 11. Inspect the MCP server

With the environment activated:

```bash
mcp dev mcp_server.py
```

The MCP development command can open the MCP Inspector. The Inspector requires
Node.js/npx. It lets you inspect and invoke tools independently of LangGraph.

## 12. Recommended teaching sequence

1. Open `mcp_server.py`: "This machine/process provides capabilities."
2. Run `mcp_client_demo.py`: "MCP works without an LLM."
3. Show `list_tools()`: "The client discovers tools dynamically."
4. Show `llm.bind_tools(tools)`: "The LLM now knows the available interfaces."
5. Open the LangGraph construction: "The graph controls the loop."
6. Ask `What is 25 * 18?`.
7. Show the printed `HumanMessage -> AIMessage(tool call) -> ToolMessage ->
   AIMessage` trace.

This separates three concepts that are often incorrectly treated as one:
**MCP protocol, LLM tool calling, and LangGraph orchestration**.
