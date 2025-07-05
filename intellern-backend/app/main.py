from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import logging

from app.config.settings import get_settings
from app.config.logging import setup_logging
from app.api.v1.router import api_router
from app.api.middleware.cors import setup_cors
from app.core.exceptions import AppException

setup_logging()
logger = logging.getLogger(__name__)

settings = get_settings()

app = FastAPI(
    title="Intellern API",
    description="A powerful AI-powered learning assistant with RAG capabilities",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
)

setup_cors(app)

app.include_router(api_router, prefix="/api/v1")

@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message, "details": exc.details}
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}

@app.get("/")
async def root():
    return {"message": "Intellern API", "version": "1.0.0"}

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )