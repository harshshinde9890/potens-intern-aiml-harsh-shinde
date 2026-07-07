from src.loaders.pdf_loader import PDFLoader

loader = PDFLoader("data/documents")

documents = loader.load_documents()

print("=" * 60)
print(f"Total Pages Loaded : {len(documents)}")
print("=" * 60)

print(documents[0].metadata)
print(documents[0].page_content[:500])