import chromadb

from app.rag.embeddings import generate_embeddings


client = chromadb.PersistentClient(
    path="vector_db"
)

collection = client.get_or_create_collection(
    name="documents"
)


def store_chunks(chunks):
    embeddings = generate_embeddings(chunks)

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=ids
    )

    print(f"{len(chunks)} chunks stored successfully.")