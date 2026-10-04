from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:0.6b", temperature=0)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a concise software engineering trainer."),
        ("human", "Explain {topic} to a {level} developer. /no_think"),
       # {"human", "Give me {num_of} questions and answers about {topic} in csv format"}
    ]
)
chain = prompt | llm
print(chain.invoke({"topic": "Go channels", "level": "beginner"}).content)
