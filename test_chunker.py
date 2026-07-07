from src.loaders.pdf_loader import PDFLoader
from src.chunking.text_splitter import DocumentChunker

loader = PDFLoader("data/documents")
documents = loader.load_documents()

chunker = DocumentChunker()

chunks = chunker.split_documents(documents)

print("=" * 60)
print(f"Total Chunks : {len(chunks)}")
print("=" * 60)

print(chunks[0].metadata)
print()
print(chunks[0].page_content)