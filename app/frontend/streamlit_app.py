import os
import sys
import streamlit as st

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
)

from app.backend.process_document import process_document
from app.backend.summary_service import summarize_document
from app.rag.qa_chain import ask_question
from app.backend.entity_service import (
    get_document_entities
)

from app.backend.information_service import (
    get_information
)

st.set_page_config(
    page_title="AI Document Intelligence",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Document Intelligence System")

st.markdown(
    "Upload a PDF or DOCX document and ask questions using RAG + Gemini."
)

# Session State
if "processed" not in st.session_state:
    st.session_state.processed = False

if "current_file" not in st.session_state:
    st.session_state.current_file = None

# Upload section
uploaded_file = st.file_uploader(
    "Upload PDF or DOCX",
    type=["pdf", "docx"]
)

if uploaded_file:

    # New file uploaded
    if st.session_state.current_file != uploaded_file.name:

        st.session_state.current_file = uploaded_file.name
        st.session_state.processed = False

    # Process document only once
    if not st.session_state.processed:

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

# Document Analysis Section
if st.session_state.processed:

    st.markdown("---")
    st.subheader("📊 Document Analysis")

    # Summary Button
    if st.button("📝 Generate Summary"):

        with st.spinner("Generating summary..."):

            summary = summarize_document(
                uploaded_file.name
            )

        st.subheader("📋 Document Summary")

        st.markdown(summary)

    st.markdown("---")

    question = st.text_input(
        "Ask a question about the document"
    )

    if st.button("🔍 Get Answer"):

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

    if st.button("🔍 Extract Entities"):

        entities = get_document_entities(
            uploaded_file.name
        )

        st.subheader("👤 People")
        st.write(entities["PERSON"])

        st.subheader("📧 Emails")
        st.write(entities["EMAIL"])

        st.subheader("🏢 Organizations")
        st.write(entities["ORG"])

        st.subheader("📍 Locations")
        st.write(entities["GPE"])

        st.subheader("📅 Dates")
        st.write(entities["DATE"])

    if st.button("🧠 Extract Key Information"):

        with st.spinner(
            "Extracting information..."
        ):

            info = get_information(
                uploaded_file.name
            )

        st.subheader(
            "📋 Key Information"
        )

        st.markdown(info)