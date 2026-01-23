# Configuration
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

.PHONY: help build run stop clean test lint format docker-build docker-run docker-stop docker-clean docker-push

# Default target
help:
	@echo "Yoruba Language API - Available Commands:"
	@echo ""
	@echo "Development:"
	@echo "  install     Install Python dependencies"
	@echo "  test        Run tests"
	@echo "  lint        Run linting checks"
	@echo "  format      Format code with black and isort"
	@echo "  run         Run the API server locally"
	@echo "  db-init     Initialize the database"
	@echo ""
	@echo "Docker:"
	@echo "  docker-build    Build Docker image"
	@echo "  docker-run      Run with Docker Compose"
	@echo "  docker-stop     Stop Docker Compose services"
	@echo "  docker-clean    Clean up Docker containers and volumes"
	@echo "  docker-push     Push Docker image to registry"
	@echo ""
	@echo "CI/CD:"
	@echo "  ci-check    Run all CI checks locally"
	@echo "  security    Run security checks"
	@echo "  coverage    Run tests with coverage report"

# Development commands
install:
	$(PIP) install -r core/api/requirements.txt
	$(PIP) install -r core/api/requirements-dev.txt

test:
	PYTHONPATH=core/api $(PYTHON) -m pytest tests/ -v --cov=core/api/app --cov-report=html

lint:
	$(PYTHON) -m flake8 core/api/app/ tests/ --max-line-length=79
	$(PYTHON) -m black --check core/api/app/ tests/
	$(PYTHON) -m isort --check-only core/api/app/ tests/
	PYTHONPATH=core/api $(PYTHON) -m mypy core/api/app/ --ignore-missing-imports

format:
	$(PYTHON) -m black core/api/app/ tests/
	$(PYTHON) -m isort core/api/app/ tests/

run:
	PYTHONPATH=core/api $(PYTHON) -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

db-init:
	PYTHONPATH=core/api $(PYTHON) core/scripts/init_db.py

# Docker commands
docker-build:
	docker build -f infra/docker/Dockerfile -t yoruba-language-api:latest .

docker-run:
	docker-compose -f infra/docker-compose.yml up -d

docker-stop:
	docker-compose -f infra/docker-compose.yml down

docker-clean:
	docker-compose -f infra/docker-compose.yml down -v --remove-orphans
	docker system prune -f
	docker volume prune -f

docker-push:
	docker tag yoruba-language-api:latest $(DOCKER_USERNAME)/yoruba-language-api:latest
	docker push $(DOCKER_USERNAME)/yoruba-language-api:latest

# CI/CD commands
ci-check: lint test security

security:
	$(PYTHON) -m bandit -r core/api/app/ -f json -o bandit-report.json
	$(PYTHON) -m safety check

coverage:
	PYTHONPATH=core/api $(PYTHON) -m pytest tests/ -v --cov=core/api/app --cov-report=xml --cov-report=html
	@echo "Coverage report generated in htmlcov/"

# Database commands
db-reset:
	docker-compose -f infra/docker-compose.yml down -v
	docker-compose -f infra/docker-compose.yml up -d postgres
	sleep 5
	PYTHONPATH=core/api $(PYTHON) core/scripts/init_db.py

# Production commands
prod-build:
	docker build -f infra/docker/Dockerfile -t yoruba-language-api:prod --target production .

prod-run:
	docker run -d \
		--name yoruba-api-prod \
		-p 8000:8000 \
		--env-file .env.prod \
		yoruba-language-api:prod

# Utility commands
logs:
	docker-compose -f infra/docker-compose.yml logs -f api

shell:
	docker-compose -f infra/docker-compose.yml exec api bash

db-shell:
	docker-compose -f infra/docker-compose.yml exec postgres psql -U yoruba_user -d yoruba_api

# Health checks
health:
	curl -f http://localhost:8000/health || echo "API is not healthy"

status:
	docker-compose -f infra/docker-compose.yml ps
