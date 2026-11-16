from app.rag.chunker import chunk_text

sample_text = "Artificial Intelligence " * 100

chunks = chunk_text(sample_text)

print(f"Number of chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print(chunk[:100])