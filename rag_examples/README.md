# RAG: In-Memory Vectors + PostgreSQL/pgvector

Two small, runnable Retrieval-Augmented Generation examples using LangChain + Ollama:

1. `in_memory_rag.py` — embeddings are Python/Numpy objects in RAM.
2. `pgvector_rag.py` — embeddings are persisted in PostgreSQL using pgvector.

Both use:
- Generator: `qwen3:0.6b`
- Embeddings: `nomic-embed-text`
- Local inference: Ollama
- Sample knowledge: `data/go.txt`

## Architecture

Question -> embedding -> vector similarity search -> top chunks -> prompt context -> Qwen -> answer

The in-memory version computes cosine similarity directly with NumPy so you can see the mechanics clearly. The PostgreSQL version uses LangChain's `PGVector` integration.

## 1. Prerequisites

Install Python 3.11+ and Docker Desktop / Docker Engine.

Install Ollama, start it, then pull both models:

```bash
ollama pull qwen3:0.6b
ollama pull nomic-embed-text
```

Check:

```bash
ollama list
```

## 2. Create Python environment

From this project directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell activation:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 3. Run the in-memory RAG example

```bash
python in_memory_rag.py "What is a goroutine?"
```

Try:

```bash
python in_memory_rag.py "How do channels synchronize goroutines?"
python in_memory_rag.py "What causes a data race?"
```

### What happens

1. `data/go.txt` is loaded.
2. Paragraphs become chunks.
3. `nomic-embed-text` converts every chunk to a vector.
4. The question becomes another vector.
5. NumPy cosine similarity ranks chunks.
6. Top 3 chunks are inserted into the prompt.
7. `qwen3:0.6b` generates an answer from that context.

The vectors disappear when the Python process exits.

## 4. Start PostgreSQL + pgvector

```bash
docker compose up -d
```

Verify:

```bash
docker compose ps
```

Optional database check:

```bash
docker compose exec postgres psql -U raguser -d ragdb -c "CREATE EXTENSION IF NOT EXISTS vector;"
docker compose exec postgres psql -U raguser -d ragdb -c "SELECT extname FROM pg_extension WHERE extname='vector';"
```

## 5. Run PostgreSQL/pgvector RAG

```bash
python pgvector_rag.py "What is select used for?"
```

The default connection is:

```text
postgresql+psycopg://raguser:ragpass@localhost:5432/ragdb
```

Override it if needed:

```bash
export PGVECTOR_URL='postgresql+psycopg://raguser:ragpass@localhost:5432/ragdb'
python pgvector_rag.py "What is a mutex?"
```

## 6. Inspect PostgreSQL

```bash
docker compose exec postgres psql -U raguser -d ragdb
```

Inside psql:

```sql
\dx
\dt
SELECT * FROM langchain_pg_collection;
SELECT COUNT(*) FROM langchain_pg_embedding;
```

Exit with `\q`.

## 7. Stop PostgreSQL

Keep data:

```bash
docker compose down
```

Delete PostgreSQL volume/data too:

```bash
docker compose down -v
```

## Key difference

| In-memory | PostgreSQL + pgvector |
|---|---|
| Vectors live in RAM | Vectors live in PostgreSQL |
| Lost after process exits | Persistent |
| Excellent for learning/tests | Better basis for persistent applications |
| Direct NumPy cosine similarity | Database vector similarity search |
| No DB required | Requires PostgreSQL + pgvector |

## Production note

The pgvector demo deliberately deletes/recreates its LangChain collection on every run to make classroom execution repeatable. A production application should separate **ingestion/indexing** from **query/retrieval**, avoid re-embedding unchanged documents, add stable document IDs and metadata, and choose an appropriate pgvector index/search strategy for its scale.

## Project files

```text
rag_examples/
├── README.md
├── requirements.txt
├── docker-compose.yml
├── common.py
├── in_memory_rag.py
├── pgvector_rag.py
└── data/
    └── go.txt
```
