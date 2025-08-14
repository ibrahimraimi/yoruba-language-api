from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn

from app.routes import translations, proverbs, tone_marking
from app.database import engine, Base
from app.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown
    pass


app = FastAPI(
    title="Yoruba Language API",
    description="A cultural and educational API for the Yoruba language",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(
    translations.router, 
    prefix="/api/v1", 
    tags=["translations"]
)
app.include_router(
    proverbs.router, 
    prefix="/api/v1", 
    tags=["proverbs"]
)
app.include_router(
    tone_marking.router, 
    prefix="/api/v1", 
    tags=["tone-marking"]
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Yoruba Language API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "translations": "/api/v1/translate",
            "proverbs": "/api/v1/proverbs",
            "tone_marking": "/api/v1/tone-mark"
        }
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "yoruba-language-api"}


@app.get("/config")
async def get_config():
    """Get current configuration (without sensitive data)"""
    return {
        "debug": settings.debug,
        "host": settings.host,
        "port": settings.port,
        "database_url": (
            settings.database_url.split("://")[0] + "://***"
        ),  # Hide full DB URL
        "has_openai_key": bool(settings.openai_api_key),
        "ai_model": settings.ai_model
    }


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", 
        host=settings.host, 
        port=settings.port, 
        reload=settings.debug
    )
