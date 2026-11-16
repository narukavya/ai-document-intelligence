from app.rag.vector_store import collection
from app.rag.embeddings import generate_embeddings


def retrieve(query, n_results=3):

    query_embedding = generate_embeddings(
        [query]
    )[0]

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results
    )

    return results