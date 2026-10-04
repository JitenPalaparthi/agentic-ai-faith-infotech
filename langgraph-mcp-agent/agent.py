import asyncio
import json
import os
import sys
from typing import Annotated, Literal

from dotenv import load_dotenv
from typing_extensions import TypedDict
from mcp import Client, StdioServerParameters
from mcp.types import TextContent

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import StructuredTool
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

load_dotenv()
MODEL = os.getenv("OLLAMA_MODEL", "qwen3:4b")

class State(TypedDict):
    messages: Annotated[list, add_messages]

def mcp_tool_to_langchain(mcp_client: Client, mcp_tool) -> StructuredTool:
    """Create a LangChain-facing adapter whose implementation calls MCP."""

    async def call_mcp_tool(**kwargs):
        result = await mcp_client.call_tool(mcp_tool.name, kwargs)

        if result.is_error:
            texts = [
                block.text for block in result.content
                if isinstance(block, TextContent)
            ]
            return "MCP tool error: " + " ".join(texts)

        if result.structured_content is not None:
            return json.dumps(result.structured_content)

        texts = [
            block.text for block in result.content
            if isinstance(block, TextContent)
        ]
        return "\n".join(texts)

    return StructuredTool.from_function(
        coroutine=call_mcp_tool,
        name=mcp_tool.name,
        description=mcp_tool.description or f"MCP tool: {mcp_tool.name}",
        args_schema=mcp_tool.input_schema,
    )

async def run_agent():
    # MCP CLIENT: launches/connects to the MCP server.
    server = StdioServerParameters(
        command=sys.executable,
        args=["mcp_server.py"],
    )

    async with Client(server) as mcp_client:
        # Dynamic MCP tool discovery.
        listed = await mcp_client.list_tools()

        print("\nMCP tools discovered:")
        for tool in listed.tools:
            print(f"  - {tool.name}: {tool.description}")

        # Adapt discovered MCP schemas to tools the LLM can see.
        tools = [
            mcp_tool_to_langchain(mcp_client, tool)
            for tool in listed.tools
        ]
        tools_by_name = {tool.name: tool for tool in tools}

        # LLM: decides which available tool to request.
        llm = ChatOllama(model=MODEL, temperature=0)
        llm_with_tools = llm.bind_tools(tools)

        system = SystemMessage(
            content=(
                "You are a calculator agent. "
                "Use the available tools for arithmetic. "
                "Do not calculate arithmetic yourself when a suitable tool exists. "
                "After receiving tool results, answer clearly and briefly."
            )
        )

        # LANGGRAPH NODE 1: the agent/brain.
        async def agent_node(state: State):
            response = await llm_with_tools.ainvoke(
                [system] + state["messages"]
            )
            return {"messages": [response]}

        # LANGGRAPH NODE 2: executes the tool requested by the LLM.
        # The selected tool is only an adapter; it calls the MCP server.
        async def tool_node(state: State):
            ai_message = state["messages"][-1]
            tool_messages = []

            for call in ai_message.tool_calls:
                name = call["name"]
                args = call["args"]
                call_id = call["id"]

                tool = tools_by_name.get(name)

                if tool is None:
                    content = f"Unknown tool: {name}"
                else:
                    try:
                        content = await tool.ainvoke(args)
                    except Exception as exc:
                        content = f"Tool execution error: {exc}"

                tool_messages.append(
                    ToolMessage(content=str(content), tool_call_id=call_id)
                )

            return {"messages": tool_messages}

        # Router only checks whether the LLM requested a tool.
        # It does NOT decide which tool should be used.
        def should_continue(state: State) -> Literal["tools", "end"]:
            last_message = state["messages"][-1]
            if isinstance(last_message, AIMessage) and last_message.tool_calls:
                return "tools"
            return "end"

        # Explicit LangGraph.
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

        print("\nLangGraph + MCP Agent")
        print(f"Ollama model: {MODEL}")
        print("Type 'exit' to stop.")
        print("\nTry:")
        print("  What is 25 * 18?")
        print("  Add 100 and 55.")
        print("  Divide 144 by 12.")
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

            print("\n--- LangGraph trace ---")
            for message in result["messages"]:
                print(f"\n{message.__class__.__name__}")
                calls = getattr(message, "tool_calls", None)
                if calls:
                    print("tool_calls =", calls)
                if getattr(message, "content", None):
                    print(message.content)

            print("\n-----------------------")
            print("Agent:", result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(run_agent())
