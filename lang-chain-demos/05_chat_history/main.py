from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import SystemMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:0.6b", temperature=0)
history = InMemoryChatMessageHistory()
history.add_message(SystemMessage(content="You are a concise Go tutor."))

for question in ["My project is called PaymentService. Remember that. /no_think", "What is my project called? /no_think"]:
    history.add_user_message(question)
    answer = llm.invoke(history.messages)
    history.add_ai_message(answer.content)
    print("USER:", question)
    print("AI:", answer.content, "\n")
