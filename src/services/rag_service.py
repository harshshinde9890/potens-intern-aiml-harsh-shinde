from typing import Dict, List

from src.retrieval.retriever import Retriever
from src.llm.gemini import GeminiLLM
from src.prompts.prompts import RAG_PROMPT


class RAGService:
    """
    Main RAG service that retrieves relevant document chunks,
    generates answers using Gemini, and returns citations.
    """

    def __init__(self):
        self.retriever = Retriever()
        self.llm = GeminiLLM().get_llm()

    def ask(self, question: str, k: int = 4) -> Dict:
        """
        Answer a user question using Retrieval-Augmented Generation (RAG).

        Returns:
            {
                "answer": "...",
                "citations": [
                    {
                        "source": "...",
                        "page": 1,
                        "snippet": "..."
                    }
                ]
            }
        """

        # Retrieve relevant documents
        documents = self.retriever.similarity_search(
            query=question,
            k=k
        )

        if not documents:
            return {
                "answer": "I couldn't find the answer in the provided documents.",
                "citations": []
            }

        context = ""
        citations: List[dict] = []

        for doc in documents:

            source = doc.metadata.get("source", "Unknown")
            page = doc.metadata.get("page", "Unknown")

            snippet = doc.page_content[:250].replace("\n", " ")

            citations.append(
                {
                    "source": source,
                    "page": page,
                    "snippet": snippet
                }
            )

            context += f"""
Source: {source}
Page: {page}

Content:
{doc.page_content}

----------------------------------------
"""

        prompt = RAG_PROMPT.format(
            context=context,
            question=question
        )

        response = self.llm.invoke(prompt)

        return {
            "answer": response.content,
            "citations": citations
        }