from app.processing.document_loader import load_document
from app.processing.text_cleaner import clean_text

from app.extraction.information_extractor import (
    extract_information
)


def get_information(file_path):

    text = load_document(file_path)

    text = clean_text(text)

    return extract_information(
        text[:3000]
    )