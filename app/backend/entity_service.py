from app.processing.document_loader import load_document
from app.processing.text_cleaner import clean_text
from app.extraction.entity_extractor import (
    extract_entities
)


def get_document_entities(file_path):

    text = load_document(file_path)

    text = clean_text(text)

    return extract_entities(text)
