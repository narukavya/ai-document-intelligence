from app.rag.gemini_client import generate_response
from app.rag.retriever import retrieve

def ask_question(question):

    results = retrieve(question)

    context = "\n".join(
        results["documents"][0]
    )

    prompt = f"""
You are an AI Document Assistant.

Answer ONLY from the provided context.

If the answer is not present in the context,
say "Information not found in document."

Context:
{context}

Question:
{question}
"""

    return generate_response(prompt)