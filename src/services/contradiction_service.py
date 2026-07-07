from src.retrieval.retriever import Retriever
from src.llm.gemini import GeminiLLM


class ContradictionService:
    """
    Compare two documents on a given topic and determine
    whether they contradict each other.
    """

    def __init__(self):
        self.retriever = Retriever()
        self.llm = GeminiLLM().get_llm()

    def compare(
        self,
        topic: str,
        document_1: str,
        document_2: str,
        k: int = 3
    ):

        docs = self.retriever.similarity_search(
            query=topic,
            k=10
        )

        doc1_context = ""
        doc2_context = ""

        citations = []

        for doc in docs:

            source = doc.metadata.get("source", "")

            page = doc.metadata.get("page", 0)

            snippet = doc.page_content[:250]

            if source == document_1:

                doc1_context += doc.page_content + "\n\n"

                citations.append(
                    {
                        "source": source,
                        "page": page,
                        "snippet": snippet
                    }
                )

            elif source == document_2:

                doc2_context += doc.page_content + "\n\n"

                citations.append(
                    {
                        "source": source,
                        "page": page,
                        "snippet": snippet
                    }
                )

        prompt = f"""
You are an expert document comparison assistant.

Topic:
{topic}

Document A
------------
{doc1_context}

Document B
------------
{doc2_context}

Tasks

1. Determine whether these documents contradict each other regarding the topic.

2. Answer either:
- Contradiction Found
or
- No Contradiction

3. Explain your reasoning.

4. Mention the important differences.

If there is insufficient information, clearly say so.
"""

        response = self.llm.invoke(prompt)

        return {
            "result": response.content,
            "citations": citations
        }