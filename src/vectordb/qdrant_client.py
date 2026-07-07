from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

from config import (
    QDRANT_URL,
    QDRANT_API_KEY,
    COLLECTION_NAME,
)


class QdrantManager:

    def __init__(self):

        self.client = QdrantClient(
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY,
        )

    def create_collection(self, vector_size: int):

        collections = self.client.get_collections().collections

        names = [collection.name for collection in collections]

        if COLLECTION_NAME in names:
            print(f"Collection '{COLLECTION_NAME}' already exists.")
            return

        self.client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE,
            ),
        )

        print(f"Collection '{COLLECTION_NAME}' created successfully.")

    def get_client(self):
        return self.client