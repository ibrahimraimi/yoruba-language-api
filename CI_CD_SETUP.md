# 🚀 CI/CD & Docker Setup Guide

This document provides a comprehensive guide to the CI/CD pipeline and Docker containerization setup for the Yoruba Language API.

## 🐳 Docker Setup

### Production Dockerfile

The `Dockerfile` is optimized for production use:

- **Base Image**: Python 3.11 slim for minimal size
- **Security**: Non-root user execution
- **Health Checks**: Built-in health monitoring
- **Multi-stage**: Optimized build process
- **Dependencies**: Minimal system packages

### Docker Compose

Full-stack development environment with:

```yaml
services:
  postgres: # PostgreSQL database
  redis: # Caching layer
  api: # FastAPI application
  nginx: # Reverse proxy with SSL
```

### Quick Start with Docker

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f api

# Stop services
docker-compose down

# Clean up volumes
docker-compose down -v
```

### Docker Commands

```bash
# Build image
docker build -t yoruba-language-api .

# Run container
docker run -p 8000:8000 yoruba-language-api

# Test Docker setup
python scripts/test_docker.py
```

## 🔄 CI/CD Pipeline

### GitHub Actions Workflows

#### 1. CI Pipeline (`ci.yml`)

**Triggers**: Push to main/develop, Pull Requests

**Jobs**:

- **Lint**: Code quality checks
- **Security**: Security vulnerability scanning
- **Test**: Unit tests across Python versions
- **Integration**: API endpoint testing
- **Build**: Docker image creation
- **Deploy**: Staging/Production deployment

#### 2. Release Pipeline (`release.yml`)

**Triggers**: Version tags (v\*)

**Features**:

- Docker image publishing
- GitHub releases
- Asset management

### Automated Quality Checks

#### Code Quality

- **flake8**: PEP 8 compliance
- **black**: Code formatting
- **isort**: Import sorting
- **mypy**: Type checking

#### Security

- **bandit**: Security linting
- **safety**: Dependency vulnerability scanning

#### Testing

- **pytest**: Test framework
- **Coverage**: Code coverage reporting
- **Integration**: API endpoint testing

### Pre-commit Hooks

Automated code quality enforcement:

```bash
# Install hooks
pre-commit install

# Run manually
pre-commit run --all-files

# Run specific hooks
pre-commit run black
pre-commit run flake8
```

## 🚀 Deployment

### Environment-Specific Configurations

#### Development

- Local Docker Compose
- SQLite database
- Debug mode enabled

#### Staging

- Automated deployment on main branch
- PostgreSQL database
- Production-like environment

#### Production

- Manual deployment with approval
- Kubernetes orchestration
- High availability setup

### Kubernetes Deployment

Production-ready manifests in `k8s/`:

```yaml
# Deployment
- 3 replicas for high availability
- Resource limits and requests
- Health checks and readiness probes
- Security contexts

# Service & Ingress
- Load balancing
- SSL/TLS termination
- Rate limiting
- Security headers
```

### Deployment Commands

```bash
# Kubernetes deployment
kubectl create namespace yoruba-api
kubectl apply -f k8s/

# Check status
kubectl get all -n yoruba-api

# View logs
kubectl logs -f deployment/yoruba-language-api -n yoruba-api
```

## 🛠 Development Tools

### Makefile Commands

```bash
# View all commands
make help

# Development
make install      # Install dependencies
make test         # Run tests
make lint         # Run linting
make format       # Format code
make run          # Run server locally

# Docker
make docker-build # Build Docker image
make docker-run   # Start with Docker Compose
make docker-stop  # Stop Docker Compose
make docker-clean # Clean up Docker resources

# CI/CD
make ci-check     # Run all CI checks locally
make security     # Run security checks
make coverage     # Run tests with coverage
```

### Development Dependencies

Additional tools in `requirements-dev.txt`:

- **Testing**: pytest, pytest-cov, pytest-asyncio
- **Quality**: flake8, black, isort, mypy
- **Security**: bandit, safety
- **Documentation**: mkdocs, mkdocs-material
- **Development**: pre-commit, ipython, ipdb

## 🔧 Configuration

### Environment Variables

| Variable         | Description                | Default                 |
| ---------------- | -------------------------- | ----------------------- |
| `DATABASE_URL`   | Database connection string | `sqlite:///./yoruba.db` |
| `API_KEY`        | API authentication key     | Required                |
| `OPENAI_API_KEY` | OpenAI API key             | Optional                |
| `AI_MODEL`       | OpenAI model               | `gpt-4o`                |
| `DEBUG`          | Debug mode                 | `false`                 |
| `HOST`           | Server host                | `0.0.0.0`               |
| `PORT`           | Server port                | `8000`                  |

### Docker Environment

```bash
# Development
docker-compose up -d

# Production
docker run --env-file .env.prod yoruba-language-api
```

## 📊 Monitoring & Health

### Health Checks

- **Application**: `/health` endpoint
- **Docker**: Built-in health checks
- **Kubernetes**: Liveness and readiness probes

### Logging

- Structured logging format
- Docker log aggregation
- Kubernetes log management

### Metrics (Planned)

- Prometheus metrics
- Grafana dashboards
- Performance monitoring

## 🔒 Security Features

### Docker Security

- Non-root user execution
- Minimal base image
- Security scanning in CI/CD
- Dependency vulnerability checks

### Kubernetes Security

- Security contexts
- Network policies
- RBAC configuration
- Secret management

### API Security

- API key authentication
- Rate limiting
- CORS configuration
- Input validation

## 🧪 Testing Strategy

### Test Types

1. **Unit Tests**: Individual function testing
2. **Integration Tests**: API endpoint testing
3. **Security Tests**: Vulnerability scanning
4. **Performance Tests**: Load testing (planned)

### Test Commands

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific categories
pytest -m "unit"
pytest -m "integration"

# Run security checks
make security
```

### Test Environment

- Isolated test database
- Mock external services
- CI/CD integration
- Coverage reporting

## 📈 Performance & Optimization

### Docker Optimization

- Multi-stage builds
- Layer caching
- Minimal dependencies
- Alpine-based images

### Application Optimization

- Database connection pooling
- Redis caching (planned)
- Async request handling
- Resource limits

### Monitoring

- Performance metrics
- Resource usage tracking
- Error rate monitoring
- Response time analysis

## 🚨 Troubleshooting

### Common Issues

#### Docker Issues

```bash
# Check Docker status
docker info

# View container logs
docker logs <container_name>

# Check resource usage
docker stats
```

#### CI/CD Issues

```bash
# Run checks locally
make ci-check

# Check GitHub Actions logs
# View workflow runs in GitHub
```

#### Kubernetes Issues

```bash
# Check pod status
kubectl get pods -n yoruba-api

# View pod logs
kubectl logs <pod_name> -n yoruba-api

# Check events
kubectl get events -n yoruba-api
```

### Debug Commands

```bash
# Docker debugging
make shell          # Access container shell
make logs           # View application logs
make status         # Check service status

# Database debugging
make db-shell       # Access database shell
make health         # Check API health
```

## 📚 Additional Resources

### Documentation

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

### Best Practices

- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Kubernetes Best Practices](https://kubernetes.io/docs/concepts/configuration/)
- [CI/CD Best Practices](https://www.atlassian.com/continuous-delivery/principles)

### Community

- [FastAPI Community](https://github.com/tiangolo/fastapi)
- [Docker Community](https://www.docker.com/community)
- [Kubernetes Community](https://kubernetes.io/community/)

---

**This setup provides a production-ready, scalable, and maintainable infrastructure for the Yoruba Language API.**
