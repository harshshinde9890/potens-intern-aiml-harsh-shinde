from typing import List

from pydantic import BaseModel


class AskRequest(BaseModel):
    question: str


class Citation(BaseModel):
    source: str
    page: int
    snippet: str


class AskResponse(BaseModel):
    answer: str
    citations: List[Citation]


class ContradictRequest(BaseModel):
    topic: str
    document_1: str
    document_2: str


class ContradictResponse(BaseModel):
    result: str
    citations: List[Citation]