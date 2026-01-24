# Yoruba API

The Yoruba API is a comprehensive platform for English-Yoruba translations, cultural proverbs, and linguistic services. It leverages modern asynchronous web frameworks and artificial intelligence to provide high-quality language processing capabilities.

## Repository Overview

This project is structured as a monorepo to support core services, infrastructure, and future web applications.

### Core Modules

- **core/api**: The main FastAPI application providing the RESTful interface.
- **core/scripts**: Utility scripts for database management and data generation.

### Infrastructure

- **infra/docker**: Containerization configurations for local and production environments.
- **infra/k8s**: Kubernetes manifests for high-availability deployments.
- **infra/nginx**: Reverse proxy and SSL configurations.

### Documentation

Detailed documentation is available in the `web/docs/` directory:

- [Project Features](web/docs/FEATURES.md): Detailed breakdown of capabilities.
- [Setup Guide](web/docs/SETUP.md): Instructions for local development and run commands.
- [About the Project](web/docs/ABOUT.md): Mission overview and project scope.
- [AI Implementation](web/docs/AI_FEATURE_SUMMARY.md): Technical details on the GPT-4o integration.
- [CI/CD and Docker](web/docs/CI_CD_SETUP.md): Guide to deployment pipelines and containerization.

## Quick Start

### Prerequisites

- Python 3.8+
- Docker (optional, for containerized development)

### One-Command Setup

The root directory contains a Makefile that orchestrates common tasks.

```bash
# Install dependencies
make install

# Initialize database
make db-init

# Start server
make run
```

The API will be accessible at http://127.0.0.1:8000 with interactive documentation at /docs.

## Development and Verification

To ensure code quality and system reliability, use the following commands:

```bash
# Run test suite
make test

# Perform linting
make lint

# Run security checks
make security
```

---

_Yoruba API is an open-source initiative dedicated to preserving and empowering the Yoruba language in the digital age._
