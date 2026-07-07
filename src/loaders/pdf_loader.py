from pathlib import Path
from typing import List

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


class PDFLoader:
    """
    Loads all PDF files from a directory and preserves metadata
    such as filename and page number for citations.
    """

    def __init__(self, documents_path: str):
        self.documents_path = Path(documents_path)

    def load_documents(self) -> List[Document]:
        documents = []

        pdf_files = sorted(self.documents_path.glob("*.pdf"))

        if not pdf_files:
            raise FileNotFoundError(
                f"No PDF files found in {self.documents_path}"
            )

        print(f"\nFound {len(pdf_files)} PDF files.\n")

        for pdf in pdf_files:

            print(f"Loading: {pdf.name}")

            loader = PyPDFLoader(str(pdf))

            pages = loader.load()

            for page in pages:
                page.metadata["source"] = pdf.name
                page.metadata["page"] = page.metadata.get("page", 0) + 1

            documents.extend(pages)

        print(f"\nLoaded {len(documents)} pages successfully.\n")

        return documents