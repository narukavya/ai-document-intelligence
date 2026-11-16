from app.rag.gemini_client import generate_response


def generate_summary(text):

    prompt = f"""
    Create a professional summary of the following document.

    Document:
    {text}
    """

    return generate_response(prompt)