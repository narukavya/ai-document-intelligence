from app.processing.text_cleaner import clean_text

sample_text = """
AI      Document Intelligence


System       for         processing documents.
"""

cleaned_text = clean_text(sample_text)

print(cleaned_text)
