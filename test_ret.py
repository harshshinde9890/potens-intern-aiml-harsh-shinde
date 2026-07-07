from src.retrieval.retriever import Retriever

retriever = Retriever()

documents = retriever.similarity_search(
    query="What is the employee Attendance policy?",
    k=3
)

print("=" * 70)

for i, doc in enumerate(documents, start=1):

    print(f"\nResult {i}")
    print("-" * 70)

    print("Source :", doc.metadata.get("source"))
    print("Page   :", doc.metadata.get("page"))

    print("\nContent\n")
    print(doc.page_content[:500])

    print("=" * 70)