from app.processing.docx_loader import extract_docx_text

docx_path = "documents/sample.docx"

text = extract_docx_text(docx_path)

print(text)
