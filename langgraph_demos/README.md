# LangGraph Local MacBook Demos

Small classroom-friendly LangGraph demos using Ollama. No cloud API key is required.

## Models

- `llama3.1:8b` — main LLM and tool demos
- `qwen3:0.6b` — lightweight routing/tool comparison
- `nomic-embed-text` — local RAG embeddings

## 1. Install Ollama

Install Ollama for macOS, then run:

```bash
ollama pull llama3.1:8b
ollama pull qwen3:0.6b
ollama pull nomic-embed-text
ollama list
```

Make sure Ollama is running.

## 2. Python environment

Python 3.11 or 3.12 is recommended.

```bash
cd langgraph_macbook_demos
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 3. Run demos

### Level 1: workflows

```bash
python level1/01_hello_graph.py
python level1/02_state_pipeline.py
python level1/03_conditional_graph.py
python level1/04_qwen_llm_router.py
```

### Level 2: tools / agents

```bash
python level2/01_calculator_agent.py
python level2/02_employee_tool_agent.py
python level2/03_qwen_calculator_agent.py
```

### Level 3: state and memory

```bash
python level3/01_conversation_memory.py
python level3/02_support_workflow.py
python level3/03_travel_state.py
```

### Level 4: RAG

```bash
python level4_rag/01_basic_rag.py
python level4_rag/02_langgraph_rag.py
```

Try these RAG questions:

- How many paid leave days do employees get?
- What is the laptop reimbursement limit?
- Can employees work remotely five days per week?
- What is the food reimbursement limit?
- Does the company provide free gym membership?

The last question is deliberately absent from the document.

## Teaching sequence

1. `01_hello_graph.py`: START -> node -> END
2. `02_state_pipeline.py`: nodes update shared state
3. `03_conditional_graph.py`: conditional edges
4. `04_qwen_llm_router.py`: LLM makes a routing decision
5. `01_calculator_agent.py`: LLM chooses a tool; ToolNode executes it
6. `02_employee_tool_agent.py`: retrieval via a normal Python tool
7. `03_qwen_calculator_agent.py`: compare a tiny Qwen model
8. `01_conversation_memory.py`: thread-scoped checkpointed state
9. `02_support_workflow.py`: LLM classification + deterministic workflows
10. `03_travel_state.py`: structured application state
11. `01_basic_rag.py`: retrieve -> augment -> generate
12. `02_langgraph_rag.py`: explicit RAG graph

## Important classroom distinction

- The LLM decides semantically whether/which tool to call.
- LangGraph controls nodes, edges, state, loops, and execution.
- `ToolNode` executes the selected Python tool.
- RAG retrieves relevant external context before generation.
