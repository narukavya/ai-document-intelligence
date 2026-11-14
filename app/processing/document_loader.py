import os

from app.processing.pdf_loader import extract_pdf_text
from app.processing.docx_loader import extract_docx_text


def load_document(file_path):
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_pdf_text(file_path)

    elif extension == ".docx":
        return extract_docx_text(file_path)

    else:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )
