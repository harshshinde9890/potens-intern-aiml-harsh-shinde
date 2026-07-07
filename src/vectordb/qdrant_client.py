from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

from config import (
    QDRANT_URL,
    QDRANT_API_KEY,
    COLLECTION_NAME,
)


class QdrantManager:
    """
    Handles connection and collection management for Qdrant.
    """

    def __init__(self):
        self.url = QDRANT_URL
        self.api_key = QDRANT_API_KEY
        self.collection_name = COLLECTION_NAME

        self.client = QdrantClient(
            url=self.url,
            api_key=self.api_key,
        )

    def create_collection(self, vector_size: int):
        """
        Create the collection if it doesn't already exist.
        """

        collections = self.client.get_collections().collections

        collection_names = [collection.name for collection in collections]

        if self.collection_name in collection_names:
            print(f"Collection '{self.collection_name}' already exists.")
            return

        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE,
            ),
        )

        print(f"Collection '{self.collection_name}' created successfully.")

    def delete_collection(self):
        """
        Delete the collection if it exists.
        Useful during development.
        """

        collections = self.client.get_collections().collections

        collection_names = [collection.name for collection in collections]

        if self.collection_name not in collection_names:
            print(f"Collection '{self.collection_name}' does not exist.")
            return

        self.client.delete_collection(
            collection_name=self.collection_name
        )

        print(f"Collection '{self.collection_name}' deleted successfully.")

    def collection_exists(self):
        """
        Check whether the collection exists.
        """

        collections = self.client.get_collections().collections

        collection_names = [collection.name for collection in collections]

        return self.collection_name in collection_names

    def get_client(self):
        return self.client

    def get_url(self):
        return self.url

    def get_api_key(self):
        return self.api_key

    def get_collection_name(self):
        return self.collection_name