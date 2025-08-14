# Yoruba Language API

A cultural and educational API for the Yoruba language, built with FastAPI. This API provides endpoints for translations, proverbs, tone marking, and more — designed for both learners and developers who want to integrate Yoruba into their apps.

---

## 📌 Features

- ✅ English ↔ Yoruba dictionary with example sentences
- ✅ Proverb & idiom retrieval with categories
- ✅ Tone marking for Yoruba text (diacritics)
- ✅ Random proverb generator
- ✅ JSON responses for easy integration with apps and bots
- 🔄 Word of the Day (planned)
- 🔄 Audio pronunciations (planned)

---

## 🛠 Tech Stack

- **Backend**: FastAPI 0.104.1
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Data Validation**: Pydantic 2.5.0
- **ORM**: SQLAlchemy 2.0.23
- **Environment Management**: Python venv + python-dotenv
- **Testing**: pytest + httpx

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### 1. Clone and Navigate

```bash
git clone https://github.com/ibrahimraimi/yoruba-language-api
cd yoruba-language-api
```

### 2. Activate Virtual Environment

```bash
# On Linux/Mac:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
DATABASE_URL=sqlite:///./yoruba.db
API_KEY=yourapikey123
DEBUG=true
```

### 5. Initialize the Database

```bash
python scripts/init_db.py
```

### 6. Run the Development Server

```bash
# Option 1: Using the startup script
python run.py

# Option 2: Using uvicorn directly
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 7. Access the API

- **API Base URL**: http://127.0.0.1:8000
- **Interactive API Docs**: http://127.0.0.1:8000/docs
- **Alternative API Docs**: http://127.0.0.1:8000/redoc

---

## 📂 Project Structure

```
yoruba-language-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Configuration settings
│   ├── database.py          # Database models and connection
│   ├── schemas.py           # Pydantic request/response schemas
│   ├── routes/              # API route handlers
│   │   ├── __init__.py
│   │   ├── translations.py  # Translation endpoints
│   │   ├── proverbs.py      # Proverb endpoints
│   │   └── tone_marking.py  # Tone marking endpoints
│   └── services/            # Business logic
│       ├── __init__.py
│       └── tone_service.py  # Tone marking service
├── scripts/
│   └── init_db.py           # Database initialization script
├── tests/                   # Test files
├── requirements.txt         # Python dependencies
├── run.py                  # Startup script
├── SETUP.md                # Detailed setup guide
└── README.md               # This file
```

---

## 🔗 API Endpoints

### Translations

- `GET /api/v1/translate?word={word}&lang=yo` - Translate English to Yoruba
- `GET /api/v1/translations` - Get all translations (paginated)
- `POST /api/v1/translations` - Create new translation
- `GET /api/v1/translations/{id}` - Get specific translation
- `PUT /api/v1/translations/{id}` - Update translation
- `DELETE /api/v1/translations/{id}` - Delete translation

### Proverbs

- `GET /api/v1/proverbs` - Get all proverbs (paginated)
- `GET /api/v1/proverbs/random` - Get random proverb
- `GET /api/v1/proverbs/{id}` - Get specific proverb
- `POST /api/v1/proverbs` - Create new proverb

### Tone Marking

- `POST /api/v1/tone-mark` - Add tone marks to Yoruba text
- `GET /api/v1/tone-mark/history` - Get tone marking history

---

## 📝 Example Usage

### 1. Translate English → Yoruba

```bash
curl "http://127.0.0.1:8000/api/v1/translate?word=love&lang=yo"
```

**Response:**

```json
{
  "english_word": "love",
  "yoruba_word": "ifẹ́",
  "part_of_speech": "noun",
  "example_sentence": "I love you → Mo nífẹ́ rẹ",
  "id": 1,
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00"
}
```

### 2. Get a Random Yoruba Proverb

```bash
curl http://127.0.0.1:8000/api/v1/proverbs/random
```

**Response:**

```json
{
  "yoruba_text": "Ìwà l'ẹ̀wà",
  "english_translation": "Character is beauty",
  "meaning": "A good character is more important than physical appearance.",
  "category": "character",
  "id": 1,
  "created_at": "2024-01-01T00:00:00"
}
```

### 3. Tone Marking for Yoruba Text

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/tone-mark" \
     -H "Content-Type: application/json" \
     -d '{"text": "Omo mi"}'
```

**Response:**

```json
{
  "original": "Omo mi",
  "tone_marked": "Ọmọ mi"
}
```

---

## 🧪 Testing

Run the test suite:

```bash
pytest tests/
```

Run specific tests:

```bash
pytest tests/test_main.py -v
```

---

## 🗄️ Database

The API uses SQLite by default for development. The database is automatically created and populated with sample data when you run:

```bash
python scripts/init_db.py
```

**Sample Data Includes:**

- 10 common English-Yoruba translations
- 5 traditional Yoruba proverbs
- Tone marking examples

**Reset Database:**

```bash
rm yoruba.db
python scripts/init_db.py
```

---

## 🔧 Configuration

Key configuration options in `.env`:

| Variable       | Description                | Default                 |
| -------------- | -------------------------- | ----------------------- |
| `DATABASE_URL` | Database connection string | `sqlite:///./yoruba.db` |
| `API_KEY`      | API authentication key     | `yourapikey123`         |
| `DEBUG`        | Enable debug mode          | `true`                  |

---

## 🚀 Deployment

### Development

```bash
python run.py
```

### Production

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Docker (Coming Soon)

```bash
docker build -t yoruba-language-api .
docker run -p 8000:8000 yoruba-language-api
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Use conventional commit messages

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💡 Roadmap

### Phase 1 (Current) ✅

- [x] Basic API structure
- [x] Translation endpoints
- [x] Proverb endpoints
- [x] Tone marking service
- [x] SQLite database
- [x] Basic testing

### Phase 2 (Next) 🔄

- [ ] Word of the Day endpoint
- [ ] Search functionality
- [ ] User authentication
- [ ] Rate limiting
- [ ] PostgreSQL support

### Phase 3 (Future) 🔮

- [ ] Speech-to-text API for Yoruba
- [ ] Yoruba spell-checker endpoint
- [ ] Telegram/WhatsApp bot integration
- [ ] Mobile app SDK
- [ ] Audio pronunciation files

---

## 🆘 Support & Troubleshooting

### Common Issues

1. **Import errors**: Ensure virtual environment is activated and dependencies are installed
2. **Database errors**: Run `python scripts/init_db.py` to initialize the database
3. **Port conflicts**: Change port in `run.py` or kill processes using port 8000

### Getting Help

- Check the [SETUP.md](SETUP.md) for detailed setup instructions
- Review the API documentation at `/docs`
- Check the logs for error messages
- Create an issue in the project repository

---

## 🙏 Acknowledgments

- Yoruba language experts and native speakers
- FastAPI community for the excellent framework
- Contributors and beta testers

---

**Made with ❤️ for the Yoruba language and culture**
