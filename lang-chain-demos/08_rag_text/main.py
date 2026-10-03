from pathlib import Path

from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = Path("knowledge.txt").read_text()
docs = RecursiveCharacterTextSplitter(chunk_size=350, chunk_overlap=50).split_documents(
    [Document(page_content=text)]
)
emb = OllamaEmbeddings(model="qwen3-embedding:0.6b")
store = InMemoryVectorStore(emb)
store.add_documents(docs)
retriever = store.as_retriever(search_kwargs={"k": 3})
llm = ChatOllama(model="qwen3:0.6b", temperature=0)
prompt = ChatPromptTemplate.from_template(
    "Answer only from this context. If absent, say you do not know.\n\nContext:\n{context}\n\nQuestion: {question} /no_think"
)
chain = prompt | llm | StrOutputParser()
question = input("Question: ")
hits = retriever.invoke(question)
context = "\n\n".join(d.page_content for d in hits)
print(chain.invoke({"context": context, "question": question}))
