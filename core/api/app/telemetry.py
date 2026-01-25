from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import Resource
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.instrumentation.asyncpg import AsyncPGInstrumentor
from app.database import engine

def setup_telemetry(app: FastAPI):
    """Configure OpenTelemetry instrumentation."""
    
    # Define resource (service name, version)
    resource = Resource.create({
        "service.name": "yoruba-api",
        "service.version": "1.0.0",
    })

    # Set up TracerProvider
    provider = TracerProvider(resource=resource)
    
    # Configure Exporter (defaulting to localhost if not set)
    # This expects an OTLP collector endpoint (e.g., http://localhost:4318/v1/traces)
    # You can configure attributes via standard OTel env vars like OTEL_EXPORTER_OTLP_ENDPOINT
    processor = BatchSpanProcessor(OTLPSpanExporter())
    provider.add_span_processor(processor)
    
    trace.set_tracer_provider(provider)

    # Instrument FastAPI
    FastAPIInstrumentor.instrument_app(app, tracer_provider=provider)

    # Instrument SQLAlchemy
    SQLAlchemyInstrumentor().instrument(
        engine=engine.sync_engine,
        tracer_provider=provider
    )
    
    # Instrument AsyncPG (if used directly, but good to have)
    AsyncPGInstrumentor().instrument(tracer_provider=provider)
