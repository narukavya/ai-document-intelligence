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
from app.backend.entity_service import get_document_entities
from app.backend.information_service import get_information
from app.rag.qa_chain import ask_question

st.set_page_config(
    page_title="AI Document Intelligence",
    page_icon="📄",
    layout="wide"
)

# -------------------------
# Session State
# -------------------------

if "processed" not in st.session_state:
    st.session_state.processed = False

if "current_file" not in st.session_state:
    st.session_state.current_file = None

# -------------------------
# Header
# -------------------------

st.title("📄 AI Document Intelligence System")

st.markdown("""
Analyze documents using:

- 📝 AI Summarization
- 👤 Entity Extraction
- 🧠 Information Extraction
- 🔍 RAG Question Answering
""")

# -------------------------
# Sidebar
# -------------------------

with st.sidebar:

    st.header("📂 Upload Document")

    st.warning(
        "Only one document can be processed at a time. Uploading a new document will replace the current document."
    )

    uploaded_file = st.file_uploader(
        "Upload PDF or DOCX",
        type=["pdf", "docx"]
    )

    if uploaded_file:

        st.success(uploaded_file.name)

        st.caption(
            f"Size: {round(uploaded_file.size / 1024, 2)} KB"
        )

        if st.session_state.current_file != uploaded_file.name:

            st.session_state.current_file = uploaded_file.name
            st.session_state.processed = False

        if not st.session_state.processed:

            with open(uploaded_file.name, "wb") as f:
                f.write(uploaded_file.getbuffer())

            with st.spinner(
                "Processing document..."
            ):

                chunks = process_document(
                    uploaded_file.name
                )

            st.session_state.processed = True

            st.success(
                f"{chunks} chunks created"
            )

# -------------------------
# Main Content
# -------------------------

if st.session_state.processed:

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📝 Summary",
            "👤 Entities",
            "🧠 Information",
            "🔍 Q&A"
        ]
    )

    # ---------------------
    # Summary
    # ---------------------

    with tab1:

        if st.button(
            "Generate Summary",
            key="summary_btn"
        ):

            with st.spinner(
                "Generating summary..."
            ):

                summary = summarize_document(
                    uploaded_file.name
                )

            st.markdown(summary)

    # ---------------------
    # Entity Extraction
    # ---------------------

    with tab2:

        if st.button(
            "Extract Entities",
            key="entity_btn"
        ):

            entities = get_document_entities(
                uploaded_file.name
            )

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("👤 People")

                st.write(
                    entities["PERSON"]
                )

                st.subheader("📧 Emails")

                st.write(
                    entities["EMAIL"]
                )

            with col2:

                st.subheader("🏢 Organizations")

                st.write(
                    entities["ORG"]
                )

                st.subheader("📅 Dates")

                st.write(
                    entities["DATE"]
                )

    # ---------------------
    # Information Extraction
    # ---------------------

    with tab3:

        if st.button(
            "Extract Information",
            key="info_btn"
        ):

            with st.spinner(
                "Extracting information..."
            ):

                info = get_information(
                    uploaded_file.name
                )

            st.text_area(
                "Key Information",
                info,
                height=350
            )

    # ---------------------
    # Question Answering
    # ---------------------

    with tab4:

        question = st.text_input(
            "Ask a question about the document"
        )

        if st.button(
            "Get Answer",
            key="qa_btn"
        ):

            if question.strip():

                with st.spinner(
                    "Generating answer..."
                ):

                    answer = ask_question(
                        question
                    )

                st.subheader(
                    "Answer"
                )

                st.write(answer)

            else:

                st.warning(
                    "Please enter a question."
                )