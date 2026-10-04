import sys
import numpy as np
from common import load_documents, embeddings, answer


def cosine_similarity(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    return float(np.dot(a, b) / denom) if denom else 0.0


def main():
    question = " ".join(sys.argv[1:]) or "What is a goroutine?"
    docs = load_documents()
    embedder = embeddings()

    # In-memory vector store: vectors exist only in this Python process.
    vectors = embedder.embed_documents([d.page_content for d in docs])
    query_vector = embedder.embed_query(question)

    ranked = sorted(
        zip(docs, vectors),
        key=lambda item: cosine_similarity(query_vector, item[1]),
        reverse=True,
    )[:3]
    retrieved = [doc for doc, _ in ranked]

    print("\nRetrieved chunks:")
    for doc, vector in ranked:
        print(f"- chunk={doc.metadata['chunk']} score={cosine_similarity(query_vector, vector):.4f}")

    print("\nAnswer:")
    print(answer(question, retrieved))


if __name__ == "__main__":
    main()
