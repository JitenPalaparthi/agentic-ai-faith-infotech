import asyncio
import sys
from mcp import Client, StdioServerParameters
from mcp.types import TextContent

async def main():
    server = StdioServerParameters(
        command=sys.executable,
        args=["mcp_server.py"],
    )

    async with Client(server) as client:
        print("Protocol:", client.protocol_version)

        listed = await client.list_tools()
        print("\nTools discovered from MCP server:")
        for tool in listed.tools:
            print(f"- {tool.name}: {tool.description}")

        result = await client.call_tool(
            "multiply",
            {"a": 25, "b": 18},
        )

        print("\nDirect MCP call: multiply(25, 18)")
        if result.structured_content is not None:
            print(result.structured_content)
        else:
            for block in result.content:
                if isinstance(block, TextContent):
                    print(block.text)

if __name__ == "__main__":
    asyncio.run(main())
