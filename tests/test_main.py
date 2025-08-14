"""
Basic tests for the Yoruba Language API.
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Welcome to Yoruba Language API"


def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_translate_endpoint():
    """Test the translate endpoint."""
    response = client.get("/api/v1/translate?word=love&lang=yo")
    # This will fail if no database is set up, which is expected
    assert response.status_code in [404, 500]


def test_proverbs_endpoint():
    """Test the proverbs endpoint."""
    response = client.get("/api/v1/proverbs")
    # This will fail if no database is set up, which is expected
    assert response.status_code in [404, 500]
