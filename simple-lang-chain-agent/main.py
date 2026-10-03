from langchain.agents import create_agent
from langchain.tools import tool
from langchain_ollama import ChatOllama


# =========================================================
# 1. TOOLS
# =========================================================

@tool
def add(a: int, b: int) -> int:
    """Add two integer numbers."""

    print(f"\n[TOOL] add({a}, {b})")

    return a + b


@tool
def subtract(a: int, b: int) -> int:
    """Subtract the second integer from the first integer."""

    print(f"\n[TOOL] subtract({a}, {b})")

    return a - b


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integer numbers."""

    print(f"\n[TOOL] multiply({a}, {b})")

    return a * b


@tool
def divide(a: float, b: float) -> float:
    """Divide the first number by the second number."""

    print(f"\n[TOOL] divide({a}, {b})")

    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


# =========================================================
# 2. CREATE LOCAL LLM
# =========================================================

model = ChatOllama(
    model="qwen3:0.6b",

    # Ollama running inside Docker and exposed
    # to the host on port 11434
    base_url="http://localhost:11434",

    # Useful for deterministic mathematical operations
    temperature=0,
)


# =========================================================
# 3. CREATE LANGCHAIN AGENT
# =========================================================

agent = create_agent(
    model=model,

    tools=[
        add,
        subtract,
        multiply,
        divide,
    ],

    system_prompt=(
        "You are a helpful mathematical assistant. "
        "Use the provided mathematical tools whenever "
        "a calculation is required. "
        "Do not perform arithmetic yourself when an "
        "appropriate tool is available."
    ),
)


# =========================================================
# 4. ASK AGENT
# =========================================================

def ask_agent(question: str) -> None:

    print("\n" + "=" * 60)
    print("AGENT EXECUTION")
    print("=" * 60)

    try:

        # Streaming lets us observe each step of
        # the agent execution.
        for event in agent.stream(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": question,
                    }
                ]
            },

            # Return the complete agent state
            # after every execution step.
            stream_mode="values",
        ):

            messages = event.get("messages", [])

            if not messages:
                continue

            # Last message represents the newest
            # event in the agent execution.
            message = messages[-1]

            message.pretty_print()

    except Exception as error:

        print("\nAgent execution failed:")
        print(error)


# =========================================================
# 5. MAIN APPLICATION
# =========================================================

def main():

    print()
    print("=" * 60)
    print("LANGCHAIN + QWEN3 + OLLAMA AGENT")
    print("=" * 60)

    print()
    print("LLM:")
    print("  qwen3:4b")

    print()
    print("Ollama:")
    print("  http://localhost:11434")

    print()
    print("Available tools:")
    print("  1. add")
    print("  2. subtract")
    print("  3. multiply")
    print("  4. divide")

    print()
    print("Example questions:")
    print("  Add 10 and 22")
    print("  Multiply 25 and 8")
    print("  Divide 100 by 5")
    print("  Add 10 and 22 and then multiply the result by 5")

    print()
    print("Type 'exit' or 'quit' to stop.")
    print()

    # -----------------------------------------------------
    # Interactive loop
    # -----------------------------------------------------

    while True:

        try:

            question = input("You: ").strip()

            # Exit application
            if question.lower() in ["exit", "quit"]:
                print()
                print("Goodbye!")
                break

            # Ignore empty input
            if not question:
                continue

            # Send question to agent
            ask_agent(question)

            print()

        except KeyboardInterrupt:

            print("\n\nGoodbye!")
            break

        except EOFError:

            print("\n\nGoodbye!")
            break


# =========================================================
# 6. PROGRAM ENTRY POINT
# =========================================================

if __name__ == "__main__":
    main()
