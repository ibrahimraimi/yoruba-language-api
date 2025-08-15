# 🌍 Yoruba Language API

A comprehensive API for English-Yoruba translations, proverbs, and tone marking with AI-powered translation capabilities.

## ✨ Features

- ✅ English ↔ Yoruba dictionary with 10,000+ translations
- ✅ AI-powered translations using OpenAI GPT-4o
- ✅ Yoruba proverbs collection
- ✅ Tone marking service for Yoruba text
- ✅ RESTful API with comprehensive documentation
- ✅ Docker containerization
- ✅ CI/CD pipeline with GitHub Actions
- ✅ Kubernetes deployment ready
- 🔄 Rate limiting and security features
- 🔄 Caching and performance optimization

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Docker and Docker Compose
- PostgreSQL (for production)
- OpenAI API key (for AI translations)

### Local Development

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/yoruba-language-api.git
   cd yoruba-language-api
   ```

2. **Set up virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # For development tools
   ```

4. **Environment setup**

   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Initialize database**

   ```bash
   python scripts/init_db.py
   ```

6. **Run the server**
   ```bash
   python run.py
   # Or use uvicorn directly
   uvicorn app.main:app --reload
   ```

### Docker Development

1. **Build and run with Docker Compose**

   ```bash
   # Start all services (API, PostgreSQL, Redis, Nginx)
   docker-compose up -d

   # View logs
   docker-compose logs -f api

   # Stop services
   docker-compose down
   ```

2. **Build Docker image manually**
   ```bash
   docker build -t yoruba-language-api .
   docker run -p 8000:8000 yoruba-language-api
   ```

### Using Makefile

```bash
# View all available commands
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

## 🐳 Docker

### Production Dockerfile

The application includes a production-ready Dockerfile with:

- Multi-stage build for optimization
- Non-root user for security
- Health checks
- Minimal base image (Python 3.11 slim)

### Docker Compose

Full-stack development environment with:

- **API**: FastAPI application
- **PostgreSQL**: Primary database
- **Redis**: Caching layer
- **Nginx**: Reverse proxy with SSL

### Kubernetes Deployment

Production-ready Kubernetes manifests in `k8s/`:

- Deployment with 3 replicas
- Service and Ingress configuration
- ConfigMaps and Secrets
- Health checks and resource limits
- SSL/TLS termination

## 🔄 CI/CD Pipeline

### GitHub Actions Workflows

1. **CI Pipeline** (`ci.yml`)

   - Linting and code formatting
   - Security checks (bandit, safety)
   - Unit tests across Python versions
   - Integration tests
   - Docker image building
   - Automated deployment

2. **Release Pipeline** (`release.yml`)
   - Triggered on version tags
   - Docker image publishing
   - GitHub releases
   - Asset uploads

### Automated Checks

- **Code Quality**: flake8, black, isort, mypy
- **Security**: bandit, safety
- **Testing**: pytest with coverage
- **Formatting**: Pre-commit hooks
- **Dependencies**: Security updates

### Pre-commit Hooks

Automated code quality checks:

```bash
# Install pre-commit hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

## 🗄️ Database

### Models

- **Translation**: English-Yoruba word pairs
- **Proverb**: Yoruba proverbs with meanings
- **ToneMarking**: Tone marking history and analysis

### Seeding

Populate with 10,000 translations:

```bash
# Generate translations dataset
python scripts/generate_translations.py

# Seed database (if script exists)
python scripts/seed_database.py
```

### Database Management

```bash
# Reset database
make db-reset

# Database shell
make db-shell

# View database status
make status
```

## 🔧 Configuration

### Environment Variables

| Variable         | Description                        | Default                 |
| ---------------- | ---------------------------------- | ----------------------- |
| `DATABASE_URL`   | Database connection string         | `sqlite:///./yoruba.db` |
| `API_KEY`        | API authentication key             | Required                |
| `OPENAI_API_KEY` | OpenAI API key for AI translations | Optional                |
| `AI_MODEL`       | OpenAI model to use                | `gpt-4o`                |
| `DEBUG`          | Enable debug mode                  | `false`                 |
| `HOST`           | Server host                        | `0.0.0.0`               |
| `PORT`           | Server port                        | `8000`                  |
| `CORS_ORIGINS`   | Allowed CORS origins               | `*`                     |

### Production Settings

```bash
# Production environment file
cp .env.example .env.prod

# Production Docker build
make prod-build
make prod-run
```

## 🧪 Testing

### Test Commands

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test categories
pytest -m "unit"
pytest -m "integration"

# Run linting
make lint

# Run security checks
make security
```

### Test Structure

- **Unit Tests**: `tests/test_*.py`
- **Integration Tests**: API endpoint testing
- **Mock Services**: AI service mocking for testing

## 📚 API Endpoints

### Core Endpoints

- `GET /` - API information
- `GET /health` - Health check
- `GET /config` - Configuration details

### Translations

- `GET /api/v1/translations` - List all translations
- `GET /api/v1/translations/{id}` - Get specific translation
- `POST /api/v1/translations` - Create new translation
- `PUT /api/v1/translations/{id}` - Update translation
- `DELETE /api/v1/translations/{id}` - Delete translation
- `GET /api/v1/translate?word={word}&use_ai={true/false}` - Translate word
- `POST /api/v1/translate` - Translate with POST request

### AI Translation

- `GET /api/v1/ai/status` - Check AI service availability
- `GET /api/v1/translate?use_ai=true` - Use AI for translation

### Proverbs

- `GET /api/v1/proverbs` - List all proverbs
- `GET /api/v1/proverbs/random` - Get random proverb
- `POST /api/v1/proverbs` - Add new proverb

### Tone Marking

- `POST /api/v1/tone-mark` - Add tone marks to text
- `GET /api/v1/tone-mark` - Get tone marking history
- `POST /api/v1/tone-mark/analyze` - Analyze text for tone marking

## 🚀 Deployment

### Docker Deployment

```bash
# Production build
docker build -t yoruba-language-api:prod .

# Run with environment file
docker run -d \
  --name yoruba-api \
  -p 8000:8000 \
  --env-file .env.prod \
  yoruba-language-api:prod
```

### Kubernetes Deployment

```bash
# Create namespace
kubectl create namespace yoruba-api

# Apply configurations
kubectl apply -f k8s/

# Check status
kubectl get all -n yoruba-api
```

### Environment-Specific Deployments

- **Development**: Local Docker Compose
- **Staging**: Automated deployment on main branch
- **Production**: Manual deployment with approval

## 🔒 Security Features

- API key authentication
- CORS configuration
- Rate limiting
- Input validation
- SQL injection prevention
- XSS protection headers
- Non-root Docker containers
- Kubernetes security contexts

## 📊 Monitoring & Health

- Health check endpoints
- Prometheus metrics (planned)
- Structured logging
- Error tracking with Sentry
- Performance monitoring

## 🤝 Contributing

### Development Workflow

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

### Code Standards

- Follow PEP 8 style guide
- Use type hints
- Write comprehensive tests
- Update documentation
- Run pre-commit hooks

### Testing Guidelines

- Maintain >80% test coverage
- Include unit and integration tests
- Mock external dependencies
- Test error conditions

## 📈 Roadmap

### Completed ✅

- Core API structure
- Database models and schemas
- Translation endpoints
- AI translation integration
- Tone marking service
- Docker containerization
- CI/CD pipeline
- Kubernetes manifests

### In Progress 🔄

- Performance optimization
- Caching implementation
- Advanced search features

### Planned 📋

- User authentication system
- Translation memory
- Community contributions
- Mobile app
- Advanced analytics
- Multi-language support

## 🆘 Support & Troubleshooting

### Common Issues

1. **Database Connection Errors**

   - Check `DATABASE_URL` in `.env`
   - Ensure database service is running
   - Verify network connectivity

2. **AI Translation Failures**

   - Check `OPENAI_API_KEY` is valid
   - Verify API quota and billing
   - Check network connectivity

3. **Docker Issues**
   - Ensure Docker daemon is running
   - Check port conflicts
   - Verify image builds successfully

### Getting Help

- Check the [Issues](https://github.com/yourusername/yoruba-language-api/issues) page
- Review [Discussions](https://github.com/yourusername/yoruba-language-api/discussions)
- Create detailed bug reports with logs

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for AI translation capabilities
- FastAPI community for the excellent framework
- Yoruba language experts and contributors
- Open source community for tools and libraries

---

**Made with ❤️ for the Yoruba language community**
