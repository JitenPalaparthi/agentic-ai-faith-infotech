from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

prompt = ChatPromptTemplate.from_template("Give exactly 5 interview questions about {topic}. /no_think")
llm = ChatOllama(model="qwen3:0.6b", temperature=0)
chain = prompt | llm | StrOutputParser()
print(chain.invoke({"topic": "Go concurrency"}))
