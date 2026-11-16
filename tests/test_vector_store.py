from app.rag.chunker import chunk_text
from app.rag.vector_store import store_chunks

text = """
Artificial Intelligence is transforming businesses.
Machine Learning helps identify patterns.
Generative AI is becoming increasingly popular.
""" * 50

chunks = chunk_text(text)

store_chunks(chunks)