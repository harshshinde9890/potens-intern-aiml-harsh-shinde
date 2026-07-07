from fastapi import FastAPI

from src.api.routes import router

app = FastAPI(
    title="Potens Document Q&A API",
    version="1.0.0",
    description="RAG-based Document Question Answering System"
)

app.include_router(router)