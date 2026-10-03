# LangChain PostgreSQL Chat History + Ollama

A small runnable example showing persistent LangChain chat history using PostgreSQL,
with a local Qwen model served by Ollama.

## Prerequisites

- Docker + Docker Compose
- Ollama installed on the host

## 1. Download the model

```bash
ollama pull qwen3:0.6b
```

Make sure Ollama is running:

```bash
ollama serve
```

## 2. Build

```bash
docker compose build
```

## 3. Start PostgreSQL

```bash
docker compose up -d postgres
```

## 4. Run the chat application

```bash
docker compose run --rm app
```

Try:

```text
My project is called PaymentService. Remember that. /no_think
```

Then:

```text
What is my project called? /no_think
```

Type `exit`, start the app again, and ask the second question again.
The conversation survives because it is stored in PostgreSQL.

## Inspect PostgreSQL

```bash
docker exec -it langchain-postgres psql -U langchain -d langchain
```

Inside psql:

```sql
SELECT id, session_id, message, created_at
FROM chat_history
ORDER BY id;
```

Exit psql:

```text
\q
```

## Reset everything

```bash
docker compose down -v
```

This removes the PostgreSQL volume and therefore the saved history.

## Architecture

```text
User
  |
  v
Python / LangChain
  |
  +---- PostgresChatMessageHistory ----> PostgreSQL
  |
  +---- ChatOllama --------------------> Ollama / Qwen3
```

This example demonstrates persistent chat history, not vector/RAG memory.
