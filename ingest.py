from src.loaders.pdf_loader import PDFLoader
from src.chunking.text_splitter import DocumentChunker
from src.embeddings.embedding_model import EmbeddingModel
from src.vectordb.qdrant_client import QdrantManager

from langchain_qdrant import QdrantVectorStore

from config import COLLECTION_NAME


def main():

    print("=" * 60)
    print("Loading Documents...")
    print("=" * 60)

    loader = PDFLoader("data/documents")
    documents = loader.load_documents()

    print("=" * 60)
    print("Chunking Documents...")
    print("=" * 60)

    chunker = DocumentChunker()

    chunks = chunker.split_documents(documents)

    print("=" * 60)
    print("Loading Embedding Model...")
    print("=" * 60)

    embedding_model = EmbeddingModel().get_embedding_model()

    vector_size = len(
        embedding_model.embed_query("test")
    )

    print(f"Embedding Dimension : {vector_size}")

    print("=" * 60)
    print("Connecting Qdrant...")
    print("=" * 60)

    manager = QdrantManager()

    manager.create_collection(vector_size)

    client = manager.get_client()

    print("=" * 60)
    print("Uploading Documents...")
    print("=" * 60)

    QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embedding_model,
        url=manager.get_url(),
        api_key=manager.get_api_key(),
        collection_name=COLLECTION_NAME,
    )

    print("\nIndexing Completed Successfully!")


if __name__ == "__main__":
    main()