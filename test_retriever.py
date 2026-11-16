from app.rag.retriever import retrieve

results = retrieve(
    "What is Machine Learning?"
)

print(results["documents"])