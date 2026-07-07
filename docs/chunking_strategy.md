# Chunking Strategy

## Overview

This project uses a Retrieval-Augmented Generation (RAG) pipeline for document-based question answering.

Before documents are stored in the vector database, they are split into smaller chunks. Chunking improves retrieval accuracy by ensuring that only the most relevant sections of a document are embedded and searched.

---

# Chunking Method

The project uses:

- RecursiveCharacterTextSplitter
- LangChain Text Splitter

This splitter preserves sentence boundaries whenever possible while maintaining overlapping context between chunks.

---

# Configuration

| Parameter | Value |
|-----------|------|
| Chunk Size | 1000 characters |
| Chunk Overlap | 200 characters |
| Separator Strategy | Recursive |
| Embedding Model | BAAI/bge-small-en-v1.5 |
| Vector Database | Qdrant |

---

# Why RecursiveCharacterTextSplitter?

RecursiveCharacterTextSplitter was selected because it:

- Preserves semantic meaning
- Avoids cutting sentences abruptly
- Maintains contextual continuity
- Produces consistent chunk sizes
- Improves retrieval quality

---

# Chunking Workflow

PDF Documents
        │
        ▼
Load using PyPDFLoader
        │
        ▼
Extract Text
        │
        ▼
RecursiveCharacterTextSplitter
(Chunk Size = 1000)
(Overlap = 200)
        │
        ▼
Multiple Document Chunks
        │
        ▼
Generate Embeddings
(BAAI/bge-small-en-v1.5)
        │
        ▼
Store in Qdrant

---

# Example

Original Text

```
The Exit Policy ensures a smooth separation process for employees.
Employees are required to submit resignation through the HR portal.
The HR department verifies all documents before final settlement.
```

Chunk 1

```
The Exit Policy ensures a smooth separation process for employees.
Employees are required to submit resignation through the HR portal.
```

Chunk 2

```
Employees are required to submit resignation through the HR portal.
The HR department verifies all documents before final settlement.
```

Notice that the overlapping sentence appears in both chunks, preserving context.

---

# Benefits

This chunking strategy provides:

- Better semantic search
- Higher retrieval accuracy
- Reduced hallucinations
- Better citation quality
- Improved answer relevance
- Faster similarity search

---

# Integration with RAG

The chunking process is part of the document ingestion pipeline:

PDF Files
→ Load Documents
→ Chunk Documents
→ Generate Embeddings
→ Store in Qdrant
→ Similarity Search
→ Gemini 2.5 Flash
→ Final Answer with Citations

---

# Final Configuration

| Component | Technology |
|------------|------------|
| Loader | PyPDFLoader |
| Chunker | RecursiveCharacterTextSplitter |
| Chunk Size | 1000 |
| Chunk Overlap | 200 |
| Embedding Model | BAAI/bge-small-en-v1.5 |
| Vector Database | Qdrant |
| LLM | Gemini 2.5 Flash |