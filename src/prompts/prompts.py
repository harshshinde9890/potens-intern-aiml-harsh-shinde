from langchain_core.prompts import ChatPromptTemplate


RAG_PROMPT = ChatPromptTemplate.from_template(
    """
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not found in the context, reply:

"I couldn't find the answer in the provided documents."

Context:
{context}

Question:
{question}

Instructions:
- Give a clear answer.
- Do not make up information.
- Mention citations at the end.
- Use bullet points whenever suitable.

Answer:
"""
)