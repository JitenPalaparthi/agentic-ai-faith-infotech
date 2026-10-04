import asyncio
import json
import os
from typing import Annotated, Literal

from dotenv import load_dotenv
from typing_extensions import TypedDict
from mcp import Client
from mcp.types import TextContent

from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    ToolMessage,
)
from langchain_core.tools import StructuredTool
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

load_dotenv()

MCP_URL = os.getenv("MCP_URL", "http://127.0.0.1:8000/mcp")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3:4b")

class State(TypedDict):
    messages: Annotated[list, add_messages]

def make_langchain_tool(client: Client, mcp_tool) -> StructuredTool:
    """Adapt a remotely hosted MCP tool to a LangChain tool."""

    async def invoke_remote_mcp(**kwargs):
        response = await client.call_tool(mcp_tool.name, kwargs)

        if response.is_error:
            texts = [
                block.text for block in response.content
                if isinstance(block, TextContent)
            ]
            raise RuntimeError(" ".join(texts) or "MCP tool failed")

        if response.structured_content is not None:
            return json.dumps(response.structured_content)

        texts = [
            block.text for block in response.content
            if isinstance(block, TextContent)
        ]
        return "\n".join(texts)

    return StructuredTool.from_function(
        coroutine=invoke_remote_mcp,
        name=mcp_tool.name,
        description=mcp_tool.description or f"Remote MCP tool {mcp_tool.name}",
        args_schema=mcp_tool.input_schema,
    )

async def main():
    print(f"Connecting to MCP server: {MCP_URL}")

    # IMPORTANT:
    # Unlike stdio, this does NOT launch mcp_server.py.
    # A separate HTTP MCP server must already be running.
    async with Client(MCP_URL) as mcp_client:
        discovered = await mcp_client.list_tools()

        print("\nRemote MCP tools discovered:")
        for tool in discovered.tools:
            print(f"  - {tool.name}: {tool.description}")

        tools = [
            make_langchain_tool(mcp_client, tool)
            for tool in discovered.tools
        ]
        tools_by_name = {tool.name: tool for tool in tools}

        llm = ChatOllama(
            model=OLLAMA_MODEL,
            temperature=0,
        )
        llm_with_tools = llm.bind_tools(tools)

        system = SystemMessage(
            content=(
                "You are a calculator agent. "
                "Use the available tools whenever arithmetic is required. "
                "The tools are hosted on a remote MCP server. "
                "After receiving tool results, give a concise final answer."
            )
        )

        async def agent_node(state: State):
            response = await llm_with_tools.ainvoke(
                [system] + state["messages"]
            )
            return {"messages": [response]}

        async def tools_node(state: State):
            ai_message = state["messages"][-1]
            output = []

            for call in ai_message.tool_calls:
                name = call["name"]
                args = call["args"]
                call_id = call["id"]

                print(f"\n[LangGraph] LLM requested tool: {name}")
                print(f"[LangGraph] Arguments: {args}")
                print(f"[MCP Client] Sending request to {MCP_URL}")

                tool = tools_by_name.get(name)

                if tool is None:
                    content = f"Unknown tool: {name}"
                else:
                    try:
                        content = await tool.ainvoke(args)
                    except Exception as exc:
                        content = f"MCP tool error: {exc}"

                print(f"[MCP Client] Tool result: {content}")

                output.append(
                    ToolMessage(
                        content=str(content),
                        tool_call_id=call_id,
                    )
                )

            return {"messages": output}

        def route(state: State) -> Literal["tools", "end"]:
            last = state["messages"][-1]
            if isinstance(last, AIMessage) and last.tool_calls:
                return "tools"
            return "end"

        builder = StateGraph(State)
        builder.add_node("agent", agent_node)
        builder.add_node("tools", tools_node)
        builder.add_edge(START, "agent")
        builder.add_conditional_edges(
            "agent",
            route,
            {"tools": "tools", "end": END},
        )
        builder.add_edge("tools", "agent")
        graph = builder.compile()

        print("\n========================================")
        print(" LangGraph + HTTP MCP Agent")
        print("========================================")
        print("Ollama model:", OLLAMA_MODEL)
        print("MCP endpoint:", MCP_URL)
        print("Type exit to stop.")
        print("\nExamples:")
        print("  What is 25 * 18?")
        print("  Add 20 and 30.")
        print("  What is 15 percent of 800?")
        print("  What is (10 + 5) * 3?")

        while True:
            question = input("\nYou: ").strip()

            if question.lower() in {"exit", "quit"}:
                break
            if not question:
                continue

            result = await graph.ainvoke(
                {"messages": [HumanMessage(content=question)]}
            )

            print("\n--- Message trace ---")
            for message in result["messages"]:
                print(message.__class__.__name__)

                if getattr(message, "tool_calls", None):
                    print("  tool_calls:", message.tool_calls)

                if getattr(message, "content", None):
                    print(" ", message.content)

            print("---------------------")
            print("Agent:", result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())
