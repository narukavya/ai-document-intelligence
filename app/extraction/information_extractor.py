from app.rag.gemini_client import generate_response


def extract_information(text):

    prompt = f"""
Extract the following details from the document.

Return in this format:

Name:
Email:
Phone:
Education:
Skills:
Certifications:

Document:

{text[:3000]}
"""

    return generate_response(prompt)