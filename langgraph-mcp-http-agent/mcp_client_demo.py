import asyncio
import os
from dotenv import load_dotenv
from mcp import Client
from mcp.types import TextContent

load_dotenv()
MCP_URL = os.getenv("MCP_URL", "http://127.0.0.1:8000/mcp")

async def main():
    print(f"Connecting to {MCP_URL}")

    async with Client(MCP_URL) as client:
        print("Connected.")
        print("Protocol version:", client.protocol_version)

        result = await client.list_tools()

        print("\nTools discovered:")
        for tool in result.tools:
            print(f"  - {tool.name}: {tool.description}")

        print("\nCalling multiply(a=25, b=18)...")
        response = await client.call_tool(
            "multiply",
            {"a": 25, "b": 18},
        )

        if response.structured_content is not None:
            print("Result:", response.structured_content)
        else:
            texts = [
                block.text
                for block in response.content
                if isinstance(block, TextContent)
            ]
            print("Result:", "\n".join(texts))

if __name__ == "__main__":
    asyncio.run(main())
