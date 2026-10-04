import os
import sys
from langchain_postgres import PGVector
from common import load_documents, embeddings, answer

CONNECTION = os.getenv(
    "PGVECTOR_URL",
    "postgresql+psycopg://raguser:ragpass@localhost:5432/ragdb",
)
COLLECTION = "go_concurrency_demo"


def main():
    question = " ".join(sys.argv[1:]) or "explain template package in go"
    embedder = embeddings()

    store = PGVector(
        embeddings=embedder,
        collection_name=COLLECTION,
        connection=CONNECTION,
        use_jsonb=True,
    )

    # For a reproducible demo, rebuild the collection each run.
    # In production, ingestion and querying should normally be separate processes.
    try:
        store.delete_collection()
    except Exception:
        pass
    store.create_collection()
    store.add_documents(load_documents())

    retrieved = store.similarity_search(question, k=3)

    print("\nRetrieved chunks:")
    for doc in retrieved:
        print(f"- chunk={doc.metadata.get('chunk')} source={doc.metadata.get('source')}")

    print("\nAnswer:")
    print(answer(question, retrieved))


if __name__ == "__main__":
    main()
