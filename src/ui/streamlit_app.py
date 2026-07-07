import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Potens Document Q&A",
    page_icon="📄",
    layout="wide",
)

st.title("📄 Document Q&A with Citations")
st.caption("Document Question Answering ")

st.sidebar.title("🏢 HR–IT FAQ Chatbot")

st.sidebar.markdown("""
### 📌 About

This AI-powered chatbot helps employees quickly find answers from company HR and IT policy documents.

### 🎯 Features

- 📄 Ask questions about HR & IT documents
- 🤖 AI-generated answers using RAG
- 📚 Source citations with page numbers
- ⚡ Fast semantic search
- 🔍 Powered by Qdrant Vector Database

---

### 🛠 Tech Stack

- **Backend:** FastAPI
- **Frontend:** Streamlit
- **LLM:** Gemini 2.5 Flash
- **Embeddings:** BAAI/bge-small-en-v1.5
- **Vector DB:** Qdrant
- **Framework:** LangChain


Developed for the **Potens Internship Assignment 2026**.
""")

question = st.text_area(
    "Ask your question",
    height=150,
    placeholder="Example: What is the Exit Policy?"
)

if st.button("🔍 Ask Question", use_container_width=True):

    if question.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Searching documents..."):

        response = requests.post(
            f"{API_URL}/ask",
            json={"question": question}
        )

    if response.status_code != 200:
        st.error(response.text)
        st.stop()

    result = response.json()

    st.success("Answer")

    st.write(result["answer"])

    st.divider()

    st.subheader("📚 Citations")

    shown = set()

    for citation in result["citations"]:

        key = (
            citation["source"],
            citation["page"]
        )

        if key in shown:
            continue

        shown.add(key)

        with st.expander(
            f'{citation["source"]} | Page {citation["page"]}'
        ):

            st.write(citation["snippet"])