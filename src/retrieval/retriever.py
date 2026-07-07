from langchain_qdrant import QdrantVectorStore

from src.embeddings.embedding_model import EmbeddingModel
from src.vectordb.qdrant_client import QdrantManager


class Retriever:

    def __init__(self):

        self.embedding_model = EmbeddingModel().get_embedding_model()

        self.manager = QdrantManager()

        self.vector_store = QdrantVectorStore(
            client=self.manager.get_client(),
            collection_name=self.manager.get_collection_name(),
            embedding=self.embedding_model,
        )

    def get_retriever(self, k: int = 4):
        """
        Returns a LangChain retriever.
        """

        return self.vector_store.as_retriever(
            search_kwargs={
                "k": k
            }
        )

    def similarity_search(self, query: str, k: int = 4):
        """
        Returns the top-k most relevant documents.
        """

        return self.vector_store.similarity_search(
            query=query,
            k=k
        )