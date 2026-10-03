import os
import psycopg
from langchain_core.messages import SystemMessage
from langchain_ollama import ChatOllama
from langchain_postgres import PostgresChatMessageHistory

user = os.getenv("POSTGRES_USER", "langchain")
password = os.getenv("POSTGRES_PASSWORD", "langchain")
database = os.getenv("POSTGRES_DB", "langchain")
host = os.getenv("POSTGRES_HOST", "localhost")
port = os.getenv("POSTGRES_PORT", "5432")

database_url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

llm = ChatOllama(
    model="qwen3:0.6b",
    temperature=0,
    base_url=ollama_url,
)

connection = psycopg.connect(database_url)
table_name = "chat_history"

PostgresChatMessageHistory.create_tables(connection, table_name)

# Keep the same UUID to continue the same conversation.
session_id = "550e8400-e29b-41d4-a716-446655440000"

history = PostgresChatMessageHistory(
    table_name,
    session_id,
    sync_connection=connection,
)

if not history.messages:
    history.add_message(SystemMessage(content="You are a concise Go tutor."))

print("\nLangChain + PostgreSQL + Ollama")
print("Session:", session_id)
print("Type 'exit' to stop.\n")

try:
    while True:
        question = input("YOU: ").strip()
        if question.lower() in {"exit", "quit"}:
            break

        history.add_user_message(question)
        answer = llm.invoke(history.messages)
        history.add_ai_message(answer.content)

        print("\nAI:", answer.content, "\n")
finally:
    connection.close()
