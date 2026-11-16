from app.processing.document_loader import load_document
from app.processing.text_cleaner import clean_text
from app.rag.chunker import chunk_text
from app.rag.vector_store import store_chunks


def process_document(file_path):

    text = load_document(file_path)

    text = clean_text(text)

    chunks = chunk_text(text)

    store_chunks(chunks)

    return len(chunks)