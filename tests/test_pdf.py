from app.processing.pdf_loader import extract_pdf_text

pdf_path = "documents/sample.pdf"

text = extract_pdf_text(pdf_path)

print(text[:2000])