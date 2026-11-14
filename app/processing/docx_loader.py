from docx import Document


def extract_docx_text(docx_path):
    document = Document(docx_path)

    text = []

    for paragraph in document.paragraphs:
        text.append(paragraph.text)

    return "\n".join(text)