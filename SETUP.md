# Yoruba Language API - Setup Guide

This guide will help you get the Yoruba Language API up and running on your local machine.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## Step 1: Clone and Navigate to Project

```bash
git clone <your-repo-url>
cd yoruba-language-api
```

## Step 2: Activate Virtual Environment

You already have a virtual environment set up. Activate it:

```bash
# On Linux/Mac:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
# Copy the example file
cp .env.example .env

# Or create manually with these contents:
DATABASE_URL=sqlite:///./yoruba.db
API_KEY=yourapikey123
DEBUG=true
```

## Step 5: Initialize the Database

```bash
python scripts/init_db.py
```

This will:

- Create the SQLite database
- Create all necessary tables
- Populate with sample translations and proverbs

## Step 6: Run the Application

### Option 1: Using the startup script

```bash
python run.py
```

### Option 2: Using uvicorn directly

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Step 7: Access the API

- **API Base URL**: http://127.0.0.1:8000
- **Interactive API Docs**: http://127.0.0.1:8000/docs
- **Alternative API Docs**: http://127.0.0.1:8000/redoc

## Testing the API

### Test the root endpoint:

```bash
curl http://127.0.0.1:8000/
```

### Test translation:

```bash
curl "http://127.0.0.1:8000/api/v1/translate?word=love&lang=yo"
```

### Test proverbs:

```bash
curl http://127.0.0.1:8000/api/v1/proverbs/random
```

### Test tone marking:

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/tone-mark" \
     -H "Content-Type: application/json" \
     -d '{"text": "Omo mi"}'
```

## Running Tests

```bash
pytest tests/
```

## Project Structure

```
yoruba-language-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── config.py            # Configuration settings
│   ├── database.py          # Database models and connection
│   ├── schemas.py           # Pydantic schemas
│   ├── routes/              # API route handlers
│   │   ├── __init__.py
│   │   ├── translations.py  # Translation endpoints
│   │   ├── proverbs.py      # Proverb endpoints
│   │   └── tone_marking.py  # Tone marking endpoints
│   └── services/            # Business logic
│       ├── __init__.py
│       └── tone_service.py  # Tone marking service
├── scripts/
│   └── init_db.py           # Database initialization
├── tests/                   # Test files
├── requirements.txt         # Python dependencies
├── run.py                  # Startup script
└── README.md               # Project documentation
```

## Troubleshooting

### Common Issues:

1. **Import errors**: Make sure you're in the virtual environment and dependencies are installed
2. **Database errors**: Run `python scripts/init_db.py` to initialize the database
3. **Port already in use**: Change the port in `run.py` or kill the process using port 8000

### Database Reset:

To reset the database:

```bash
rm yoruba.db
python scripts/init_db.py
```

## Next Steps

- Add more translations and proverbs to the database
- Implement additional features like audio pronunciations
- Add authentication and rate limiting
- Deploy to production

## Support

If you encounter any issues, check the logs or create an issue in the project repository.
