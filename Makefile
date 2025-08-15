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
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test:
	pytest tests/ -v --cov=app --cov-report=html

lint:
	flake8 app/ tests/ --max-line-length=79
	black --check app/ tests/
	isort --check-only app/ tests/
	mypy app/ --ignore-missing-imports

format:
	black app/ tests/
	isort app/ tests/

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

db-init:
	python scripts/init_db.py

# Docker commands
docker-build:
	docker build -t yoruba-language-api:latest .

docker-run:
	docker-compose up -d

docker-stop:
	docker-compose down

docker-clean:
	docker-compose down -v --remove-orphans
	docker system prune -f
	docker volume prune -f

docker-push:
	docker tag yoruba-language-api:latest $(DOCKER_USERNAME)/yoruba-language-api:latest
	docker push $(DOCKER_USERNAME)/yoruba-language-api:latest

# CI/CD commands
ci-check: lint test security

security:
	bandit -r app/ -f json -o bandit-report.json
	safety check

coverage:
	pytest tests/ -v --cov=app --cov-report=xml --cov-report=html
	@echo "Coverage report generated in htmlcov/"

# Database commands
db-reset:
	docker-compose down -v
	docker-compose up -d postgres
	sleep 5
	python scripts/init_db.py

# Production commands
prod-build:
	docker build -t yoruba-language-api:prod --target production .

prod-run:
	docker run -d \
		--name yoruba-api-prod \
		-p 8000:8000 \
		--env-file .env.prod \
		yoruba-language-api:prod

# Utility commands
logs:
	docker-compose logs -f api

shell:
	docker-compose exec api bash

db-shell:
	docker-compose exec postgres psql -U yoruba_user -d yoruba_api

# Health checks
health:
	curl -f http://localhost:8000/health || echo "API is not healthy"

status:
	docker-compose ps
