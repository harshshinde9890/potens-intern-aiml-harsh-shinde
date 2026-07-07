from fastapi import APIRouter, HTTPException
from src.services.contradiction_service import ContradictionService
from src.api.schemas import (
    AskRequest,
    AskResponse,
    Citation,
    ContradictRequest,
    ContradictResponse,
)

from src.services.rag_service import RAGService

router = APIRouter()

rag_service = RAGService()

contradiction_service = ContradictionService()


@router.get("/")
def root():
    return {
        "message": "Potens Document Q&A API"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.post("/ask", response_model=AskResponse)
def ask_question(request: AskRequest):

    try:

        result = rag_service.ask(request.question)

        return AskResponse(
            answer=result["answer"],
            citations=[
                Citation(**citation)
                for citation in result["citations"]
            ]
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
@router.post("/contradict",response_model=ContradictResponse)
def contradict(request: ContradictRequest):

    try:

        result = contradiction_service.compare(
            topic=request.topic,
            document_1=request.document_1,
            document_2=request.document_2,
        )

        return ContradictResponse(
            result=result["result"],
            citations=[
                Citation(**citation)
                for citation in result["citations"]
            ]
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )