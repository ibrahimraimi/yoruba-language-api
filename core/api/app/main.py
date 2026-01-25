from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
import structlog
import uuid

from app.routes import translations, proverbs, tone_marking
from app.database import engine, Base
from app.config import settings
from app.logging_config import configure_logging
from app.telemetry import setup_telemetry

# Initialize logging immediately
configure_logging()
logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("startup_event", message="Initializing database tables")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown
    await engine.dispose()
    logger.info("shutdown_event", message="Database engine disposed")


app = FastAPI(
    title="Yoruba API",
    description="A cultural and educational API for the Yoruba language",
    version="1.0.0",
    lifespan=lifespan
)

# Setup Telemetry (Tracing)
setup_telemetry(app)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request ID Middleware
@app.middleware("http")
async def add_request_id_header(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    
    # Bind request_id to structlog context
    structlog.contextvars.clear_contextvars()
    structlog.contextvars.bind_contextvars(request_id=request_id)
    
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response

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
    logger.info("root_endpoint_accessed")
    return {
        "message": "Welcome to Yoruba API",
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
    return {"status": "healthy", "service": "yoruba-api"}


@app.get("/config")
async def get_config():
    """Get current configuration (without sensitive data)"""
    logger.warning("config_accessed", user_warning="Sensitive endpoint")
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
