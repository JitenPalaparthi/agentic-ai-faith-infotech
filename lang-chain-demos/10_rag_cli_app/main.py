import argparse
from pathlib import Path
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

DB = "./chroma_db"
EMBED = "qwen3-embedding:0.6b"
CHAT = "qwen3:0.6b"

def load(path: str):
    p = Path(path)
    if p.suffix.lower() == ".pdf": return PyPDFLoader(str(p)).load()
    return TextLoader(str(p), encoding="utf-8").load()

def ingest(path: str):
    docs = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=120).split_documents(load(path))
    db = Chroma(collection_name="training", persist_directory=DB, embedding_function=OllamaEmbeddings(model=EMBED))
    ids = db.add_documents(docs)
    print(f"Indexed {len(ids)} chunks into {DB}")

def ask(question: str):
    db = Chroma(collection_name="training", persist_directory=DB, embedding_function=OllamaEmbeddings(model=EMBED))
    hits = db.similarity_search(question, k=4)
    context = "\n\n".join(f"SOURCE={d.metadata.get('source','?')} PAGE={d.metadata.get('page','?')}\n{d.page_content}" for d in hits)
    prompt = ChatPromptTemplate.from_template("You are a grounded assistant. Answer only from context; otherwise say you do not know.\nCONTEXT:\n{context}\nQUESTION: {question} /no_think")
    answer = (prompt | ChatOllama(model=CHAT, temperature=0) | StrOutputParser()).invoke({"context": context, "question": question})
    print("\nANSWER\n", answer)
    print("\nRETRIEVED SOURCES")
    for i,d in enumerate(hits,1): print(i, d.metadata)

parser=argparse.ArgumentParser()
sub=parser.add_subparsers(dest="cmd", required=True)
p1=sub.add_parser("ingest"); p1.add_argument("path")
p2=sub.add_parser("ask"); p2.add_argument("question")
a=parser.parse_args()
ingest(a.path) if a.cmd=="ingest" else ask(a.question)
