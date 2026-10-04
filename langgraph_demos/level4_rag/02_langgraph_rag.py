from pathlib import Path
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = (Path(__file__).parent / "documents" / "company_policy.txt").read_text()
docs = RecursiveCharacterTextSplitter(chunk_size=350, chunk_overlap=50).split_documents(
    [Document(page_content=text)]
)
store = FAISS.from_documents(docs, OllamaEmbeddings(model="nomic-embed-text"))
llm = ChatOllama(model="llama3.1:8b", temperature=0)

class RAGState(TypedDict):
    question: str
    context: str
    answer: str

def retrieve(state: RAGState):
    hits = store.similarity_search(state["question"], k=3)
    return {"context": "\n\n".join(d.page_content for d in hits)}

def generate(state: RAGState):
    prompt = f"""Use only this context:
{state['context']}

Question: {state['question']}
If the context does not contain the answer, say you do not have enough information.
"""
    return {"answer": llm.invoke(prompt).content}

g = StateGraph(RAGState)
g.add_node("retrieve", retrieve)
g.add_node("generate", generate)
g.add_edge(START, "retrieve")
g.add_edge("retrieve", "generate")
g.add_edge("generate", END)
app = g.compile()

for q in [
    "What is the maximum laptop reimbursement?",
    "Does the company provide a free gym membership?"
]:
    result = app.invoke({"question": q, "context": "", "answer": ""})
    print("\nQ:", q, "\nA:", result["answer"])
