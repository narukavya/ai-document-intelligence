from app.processing.document_loader import load_document
from app.processing.text_cleaner import clean_text
from app.summarizer.summarizer import generate_summary


def summarize_document(file_path):

    text = load_document(file_path)

    text = clean_text(text)

    summary = generate_summary(text[:8000])

    return summary