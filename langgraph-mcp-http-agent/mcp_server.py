from mcp.server.mcpserver import MCPServer

mcp = MCPServer(
    "Calculator HTTP MCP Server",
    instructions="Calculator tools for arithmetic operations."
)

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@mcp.tool()
def percentage(value: float, percent: float) -> float:
    """Calculate percent percent of value."""
    return value * percent / 100.0

if __name__ == "__main__":
    print("Starting MCP Streamable HTTP server")
    print("Endpoint: http://127.0.0.1:8000/mcp")
    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=8000,
        stateless_http=True,
        json_response=True,
    )
