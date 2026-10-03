import sys
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore

pdf = sys.argv[1] if len(sys.argv) > 1 else "sample.pdf"
pages = PyPDFLoader(pdf).load()
docs = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=100).split_documents(pages)
store = InMemoryVectorStore(OllamaEmbeddings(model="qwen3-embedding:0.6b"))
store.add_documents(docs)
retriever = store.as_retriever(search_kwargs={"k": 4})
llm = ChatOllama(model="qwen3:0.6b", temperature=0)
prompt = ChatPromptTemplate.from_template("Use only the supplied PDF excerpts. Cite page numbers when metadata contains them.\nContext:\n{context}\nQuestion: {question} /no_think")
chain = prompt | llm | StrOutputParser()
q = input("Question: ")
hits = retriever.invoke(q)
context = "\n\n".join(f"[page {d.metadata.get('page', '?')}] {d.page_content}" for d in hits)
print(chain.invoke({"context": context, "question": q}))
