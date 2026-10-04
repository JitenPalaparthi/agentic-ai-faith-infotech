from pathlib import Path
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

doc_path = Path(__file__).parent / "documents" / "company_policy.txt"
text = doc_path.read_text()

splitter = RecursiveCharacterTextSplitter(chunk_size=350, chunk_overlap=50)
docs = splitter.split_documents([Document(page_content=text)])

embeddings = OllamaEmbeddings(model="nomic-embed-text")
store = FAISS.from_documents(docs, embeddings)
llm = ChatOllama(model="llama3.1:8b", temperature=0)

question = input("Ask about company policy: ")
hits = store.similarity_search(question, k=3)
context = "\n\n".join(d.page_content for d in hits)

prompt = f"""Answer ONLY from the context below.
If the answer is not present, say: "I don't have enough information in the provided documents."

CONTEXT:
{context}

QUESTION:
{question}
"""
print("\nANSWER:\n", llm.invoke(prompt).content)
