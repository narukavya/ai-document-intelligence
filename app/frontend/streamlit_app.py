import os
import sys
import streamlit as st

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
)

from app.backend.process_document import process_document
from app.rag.qa_chain import ask_question

st.set_page_config(
    page_title="AI Document Intelligence",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Document Intelligence System")
st.markdown(
    "Upload a PDF or DOCX document and ask questions using RAG + Gemini."
)

# Initialize session state
if "processed" not in st.session_state:
    st.session_state.processed = False

uploaded_file = st.file_uploader(
    "Upload PDF or DOCX",
    type=["pdf", "docx"]
)

if uploaded_file and not st.session_state.processed:

    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Processing document..."):

        chunks = process_document(
            uploaded_file.name
        )

    st.session_state.processed = True

    st.success(
        f"✅ Document processed successfully! {chunks} chunks created."
    )

if st.session_state.processed:

    question = st.text_input(
        "Ask a question about the document"
    )

    if st.button("Get Answer"):

        if question.strip():

            with st.spinner(
                "Generating answer..."
            ):

                answer = ask_question(
                    question
                )

            st.subheader("Answer")

            st.write(answer)

        else:
            st.warning(
                "Please enter a question."
            )