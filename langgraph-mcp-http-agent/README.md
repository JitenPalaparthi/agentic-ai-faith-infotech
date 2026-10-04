# LangGraph + MCP over Streamable HTTP + Ollama

A classroom-ready example showing a **real separately running MCP HTTP server**,
a plain MCP client, and a LangGraph agent using the same remote MCP tools.

## Architecture

```text
TERMINAL 2 / AGENT PROCESS                  TERMINAL 1 / SERVER PROCESS

User
 |
 v
LangGraph
 |
 v
Qwen / Ollama
 |
 | chooses a tool
 v
Tools Node
 |
 v
MCP Client
 |
 |       Streamable HTTP
 |       http://127.0.0.1:8000/mcp
 +----------------------------------------> MCP Server
                                             |
                                             +-- add
                                             +-- subtract
                                             +-- multiply
                                             +-- divide
                                             +-- percentage
                                             |
                                             v
                                           result
 |
 <--------------------------------------------+
 |
 v
ToolMessage -> Qwen -> final answer
```

Unlike the stdio version, **agent.py does not launch the server**.

The MCP server must already be running.

---

## 1. Requirements

- macOS/Linux
- Python 3.11+ recommended
- Ollama
- an Ollama model capable of tool calling

Check Python:

```bash
python3 --version
```

Check Ollama:

```bash
ollama --version
ollama list
```

---

## 2. Extract and enter the project

```bash
unzip langgraph-mcp-http-agent.zip
cd langgraph-mcp-http-agent
```

---

## 3. Create Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create `.env`:

```bash
cp .env.example .env
```

Default:

```text
MCP_URL=http://127.0.0.1:8000/mcp
OLLAMA_MODEL=qwen3:4b
```

Run:

```bash
ollama list
```

If your installed model has a different name, edit `OLLAMA_MODEL`.

For example:

```text
OLLAMA_MODEL=qwen3:8b
```

Only use that value if `ollama list` actually shows it.

---

# PART A — Run the MCP HTTP server

## 4. Terminal 1

Open Terminal 1:

```bash
cd langgraph-mcp-http-agent
source .venv/bin/activate
python mcp_server.py
```

The server listens on:

```text
http://127.0.0.1:8000/mcp
```

Leave Terminal 1 running.

This is now an independent network service.

```text
python mcp_server.py
        |
        v
MCPServer
        |
        v
Streamable HTTP
        |
        v
127.0.0.1:8000/mcp
```

The server uses:

```python
mcp.run(
    transport="streamable-http",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True,
)
```

`streamable-http` is the modern MCP HTTP transport.

---

# PART B — Test MCP without AI

## 5. Terminal 2

Open another terminal:

```bash
cd langgraph-mcp-http-agent
source .venv/bin/activate
python mcp_client_demo.py
```

The important line is:

```python
async with Client(
    "http://127.0.0.1:8000/mcp"
) as client:
```

Because the `Client` receives a URL, it uses Streamable HTTP.

The client does NOT execute:

```text
mcp_server.py
```

It connects to the already-running server.

It then executes:

```python
result = await client.list_tools()
```

You should see:

```text
add
subtract
multiply
divide
percentage
```

Then the demo calls:

```python
await client.call_tool(
    "multiply",
    {"a": 25, "b": 18}
)
```

Conceptually:

```text
mcp_client_demo.py

      |
      | HTTP
      | list_tools()
      v

http://127.0.0.1:8000/mcp

      |
      v

MCP Server

      |
      +-- add
      +-- subtract
      +-- multiply
      +-- divide
      +-- percentage
```

This proves MCP works without LangGraph and without an LLM.

---

# PART C — Run the LangGraph agent

## 6. Make sure Ollama is available

In Terminal 2:

```bash
ollama list
```

If required:

```bash
ollama pull qwen3:4b
```

Test:

```bash
ollama run qwen3:4b
```

Exit the interactive Ollama session when done.

---

## 7. Run agent.py

Terminal 1 must still contain:

```bash
python mcp_server.py
```

In Terminal 2:

```bash
python agent.py
```

Try:

```text
What is 25 * 18?
```

Then:

```text
What is 15 percent of 800?
```

Then:

```text
What is (10 + 5) * 3?
```

---

# What happens internally?

For:

```text
What is 25 * 18?
```

the flow is:

```text
HumanMessage
     |
     v
LangGraph agent node
     |
     v
Qwen
     |
     | tool call
     | multiply(a=25,b=18)
     v
LangGraph tools node
     |
     v
MCP Client
     |
     | HTTP POST / MCP protocol
     v
127.0.0.1:8000/mcp
     |
     v
MCP Server
     |
     v
multiply(25,18)
     |
     v
450
     |
     v
MCP Client
     |
     v
ToolMessage
     |
     v
Qwen
     |
     v
"25 × 18 = 450"
     |
     v
END
```

---

# Who is responsible for what?

## Qwen

Qwen decides:

```text
I need multiply.
```

It creates a structured tool call.

It does NOT directly execute the Python function.

## LangGraph

LangGraph controls:

```text
START
  |
  v
agent
  |
  +---- tool requested? ---- yes ---> tools
  |                                     |
  |                                     |
  |<------------------------------------+
  |
  no
  |
  v
 END
```

## MCP Client

The MCP client knows how to communicate with:

```text
http://127.0.0.1:8000/mcp
```

It discovers tools and sends tool-call requests.

## MCP Server

The MCP server owns the actual implementation:

```python
@mcp.tool()
def multiply(a: float, b: float) -> float:
    return a * b
```

---

# Important: this is not a REST API

You have an HTTP endpoint:

```text
http://127.0.0.1:8000/mcp
```

but MCP defines the protocol messages exchanged over that transport.

Do not think of it as:

```text
POST /multiply
POST /add
POST /divide
```

Instead, think:

```text
HTTP
  |
  v
MCP protocol
  |
  +-- initialize
  +-- tools/list
  +-- tools/call
  +-- ...
```

The tool name and arguments are carried inside MCP messages.

---

# STDIO versus HTTP

## STDIO version

```text
agent.py
   |
   | starts subprocess
   v
mcp_server.py
```

No port is required.

Best for local MCP integrations.

## This HTTP version

```text
agent.py
   |
   | network connection
   v
http://127.0.0.1:8000/mcp
   |
   v
separately running MCP server
```

The server can later run on another machine/container.

For example:

```text
Laptop
   |
   | HTTPS
   v
mcp.mycompany.com/mcp
```

The agent architecture remains conceptually the same.

---

# Troubleshooting

## Connection refused

If you see a connection error, make sure Terminal 1 is running:

```bash
python mcp_server.py
```

and `.env` contains:

```text
MCP_URL=http://127.0.0.1:8000/mcp
```

## Ollama model not found

Run:

```bash
ollama list
```

Copy the exact model name into `.env`.

## Port 8000 already in use

On macOS/Linux:

```bash
lsof -i :8000
```

Either stop the existing process or change the server port and `MCP_URL`
together.

## Test the layers separately

Always debug in this order:

```text
1. Start mcp_server.py

2. Run mcp_client_demo.py
      |
      +-- if this fails, problem is MCP/server/network

3. Check ollama list

4. Run agent.py
      |
      +-- if MCP demo works but agent fails,
          investigate Ollama/tool calling/LangGraph
```

This separation is one of the main advantages of the HTTP example.

---

# Useful classroom demonstration

Terminal 1:

```bash
python mcp_server.py
```

Terminal 2:

```bash
python mcp_client_demo.py
```

Explain:

```text
"No AI is involved yet."
```

Then:

```bash
python agent.py
```

Ask:

```text
What is 25 * 18?
```

Now explain:

```text
Qwen chose multiply
        ↓
LangGraph routed execution
        ↓
MCP Client made a network request
        ↓
separate MCP Server executed multiply
        ↓
result returned as ToolMessage
        ↓
Qwen generated final response
```

Finally, stop Terminal 1 with Ctrl+C and ask another question in `agent.py`.
The MCP call will fail because the remote capability provider is no longer
available. This visibly demonstrates that the agent and MCP server are
separate processes.
