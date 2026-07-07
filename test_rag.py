from src.services.rag_service import RAGService

rag = RAGService()

question = "What is the employee referral policy?"

answer = rag.ask(question)

print("\n")
print("=" * 80)
print(answer)
print("=" * 80)