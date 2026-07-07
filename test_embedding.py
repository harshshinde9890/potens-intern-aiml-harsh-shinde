from src.embeddings.embedding_model import EmbeddingModel

embedding_model = EmbeddingModel().get_embedding_model()

embedding = embedding_model.embed_query(
    "What is Retrieval Augmented Generation?"
)

print(type(embedding))
print(len(embedding))