## 🏗️ Architecture 1: Document Ingestion & Indexing Pipeline

```text
                   ┌───────────────────────┐
                   │   HR & IT PDF Files   │
                   └──────────┬────────────┘
                              │
                              ▼
                   ┌───────────────────────┐
                   │     PDF Loader        │
                   │    (PyPDFLoader)      │
                   └──────────┬────────────┘
                              │
                              ▼
                   ┌───────────────────────┐
                   │ Document Chunking     │
                   │ RecursiveCharacter    │
                   │ TextSplitter          │
                   └──────────┬────────────┘
                              │
                              ▼
                   ┌───────────────────────┐
                   │ Generate Embeddings   │
                   │ BAAI/bge-small-en-v1.5│
                   └──────────┬────────────┘
                              │
                              ▼
                   ┌───────────────────────┐
                   │  Qdrant Vector DB     │
                   │ Store Vectors +       │
                   │ Metadata              │
                   └───────────────────────┘
```
## 🏗️ Architecture 2: Question Answering (RAG Pipeline)

```text
                     ┌───────────────────────┐
                     │      User Query       │
                     └──────────┬────────────┘
                                │
                                ▼
                     ┌───────────────────────┐
                     │ Generate Query        │
                     │ Embedding             │
                     │ (BAAI/bge-small)      │
                     └──────────┬────────────┘
                                │
                                ▼
                     ┌───────────────────────┐
                     │   Qdrant Vector DB    │
                     │ Similarity Search     │
                     └──────────┬────────────┘
                                │
                     Top-K Relevant Chunks
                                │
                                ▼
                     ┌───────────────────────┐
                     │ Build Context          │
                     │ + Source Metadata      │
                     └──────────┬────────────┘
                                │
                                ▼
                     ┌───────────────────────┐
                     │ Gemini 2.5 Flash LLM  │
                     │ Generate Response     │
                     └──────────┬────────────┘
                                │
                                ▼
                  ┌────────────────────────────────┐
                  │ Answer + Source Citations      │
                  │ (Document Name & Page Number)  │
                  └──────────┬─────────────────────┘
                             │
                             ▼
                    ┌───────────────────────┐
                    │ Streamlit Frontend    │
                    │ Display Final Answer  │
                    └───────────────────────┘
```