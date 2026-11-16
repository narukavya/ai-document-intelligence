from app.rag.embeddings import generate_embeddings

chunks = [
    "Artificial Intelligence is transforming industries.",
    "Machine Learning helps computers learn patterns."
]

embeddings = generate_embeddings(chunks)

print("Shape:")
print(embeddings.shape)

print("\nFirst 10 values:")
print(embeddings[0][:10])