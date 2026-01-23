# CI/CD and Docker Setup Guide

This document provides a comprehensive guide to the CI/CD pipeline and Docker containerization setup for the Yoruba Language API.

## Docker Setup

### Production Dockerfile

The Dockerfile is located in `infra/docker/` and is optimized for production use:

- **Base Image**: Python 3.11 slim for minimal size.
- **Security**: Non-root user execution.
- **Health Checks**: Built-in health monitoring.
- **Multi-stage**: Optimized build process.
- **Dependencies**: Minimal system packages.

### Docker Compose

The root `infra/docker-compose.yml` provides a full-stack development environment:

- **PostgreSQL**: Primary data store.
- **Redis**: Caching layer.
- **API**: FastAPI application.
- **Nginx**: Reverse proxy with SSL.

### Quick Start with Docker

From the root directory:

```bash
# Start all services
make docker-run

# View logs
make logs

# Stop services
make docker-stop

# Clean up volumes
make docker-clean
```

### Manual Docker Commands

```bash
# Build image
docker build -f infra/docker/Dockerfile -t yoruba-language-api .

# Run container
docker run -p 8000:8000 yoruba-language-api
```

## CI/CD Pipeline

### GitHub Actions Workflows

Found in `.github/workflows/`:

#### 1. CI Pipeline (ci.yml)

- **Triggers**: Push to main/develop, Pull Requests.
- **Jobs**:
  - Lint: Code quality checks (flake8, black, isort).
  - Security: Security vulnerability scanning (bandit, safety).
  - Test: Unit and integration tests.
  - Build: Docker image creation verification.

#### 2. Release Pipeline (release.yml)

- **Triggers**: Version tags (v\*).
- **Features**: Docker image publishing, GitHub releases.

### Automated Quality Checks

Run these locally using the root Makefile:

- **Code Quality**: `make lint`, `make format`.
- **Security**: `make security`.
- **Testing**: `make test`, `make coverage`.

### Pre-commit Hooks

Automated code quality enforcement:

```bash
# Install hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

## Deployment

### Environment-Specific Configurations

- **Development**: Local Docker Compose with SQLite.
- **Staging**: Automated deployment on the main branch to a production-like environment.
- **Production**: Manual deployment with approval using Kubernetes manifests in `infra/k8s/`.

### Deployment Commands

```bash
# Kubernetes deployment
kubectl create namespace yoruba-api
kubectl apply -f infra/k8s/

# Check status
kubectl get all -n yoruba-api
```

## Troubleshooting

### Debug Commands

Using the root Makefile:

- `make shell`: Access container shell.
- `make logs`: View application logs.
- `make status`: Check service status.
- `make db-shell`: Access database shell.

---

**This setup provides a production-ready, scalable, and maintainable infrastructure for the Yoruba Language API.**
