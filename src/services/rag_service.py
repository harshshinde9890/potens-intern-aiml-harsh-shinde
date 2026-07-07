from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from src.retrieval.retriever import Retriever
from src.llm.gemini import GeminiLLM
from src.prompts.prompts import RAG_PROMPT


class RAGService:

    def __init__(self):

        self.retriever = Retriever()

        self.llm = GeminiLLM().get_llm()

        self.parser = StrOutputParser()

    def format_docs(self, docs):

        context = []

        for doc in docs:

            source = doc.metadata.get("source", "Unknown")

            page = doc.metadata.get("page", "Unknown")

            context.append(
                f"""
Source : {source}
Page : {page}

Content:
{doc.page_content}
"""
            )

        return "\n\n".join(context)

    def build_chain(self):

        retriever = self.retriever.get_retriever()

        chain = (

            {
                "context": retriever | self.format_docs,
                "question": RunnablePassthrough()
            }

            | RAG_PROMPT

            | self.llm

            | self.parser

        )

        return chain

    def ask(self, question: str):

        chain = self.build_chain()

        return chain.invoke(question)