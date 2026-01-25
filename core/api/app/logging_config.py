import logging
import sys
import structlog
from app.config import settings

def configure_logging():
    """Configure structured logging with structlog."""
    
    # Processors applied to all events
    processors = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.dev.set_exc_info,
        structlog.processors.TimeStamper(fmt="iso"),
    ]

    # Renderer selection based on debug mode
    if settings.debug:
        # Dev: Colorful console output
        processors.extend([
            structlog.dev.ConsoleRenderer()
        ])
    else:
        # Prod: JSON output
        processors.extend([
            structlog.processors.dict_tracebacks,
            structlog.processors.JSONRenderer()
        ])

    structlog.configure(
        processors=processors,
        logger_factory=structlog.PrintLoggerFactory(),
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
        cache_logger_on_first_use=True,
    )

    # Redirect standard logging to structlog
    logging.basicConfig(format="%(message)s", stream=sys.stdout, level=logging.INFO)
    
    # Quiet noisy libraries
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.error").setLevel(logging.WARNING)
