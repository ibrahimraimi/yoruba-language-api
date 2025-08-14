# Yoruba Language API

A cultural and educational API for the Yoruba language, built with FastAPI. This API provides endpoints for translations, proverbs, tone marking, and more — designed for both learners and developers who want to integrate Yoruba into their apps.

---

## 📌 Features

- ✅ English ↔ Yoruba dictionary with example sentences
- ✅ Proverb & idiom retrieval with categories
- ✅ Tone marking for Yoruba text (diacritics)
- ✅ Random proverb generator
- ✅ **🤖 AI-powered translations using OpenAI GPT-4o**
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
- **🤖 AI Integration**: OpenAI GPT-4o API

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- OpenAI API key (for AI translations)

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

# OpenAI API for AI translations
OPENAI_API_KEY=your_openai_api_key_here
AI_MODEL=gpt-4o
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

## 🤖 AI Translation Feature

The API now includes **AI-powered translations** using OpenAI's GPT-4o model. This feature provides:

- **Context-aware translations** from English to Yoruba
- **Automatic tone marking** with proper diacritics
- **Part-of-speech tagging** and example sentences
- **Auto-caching** in the database to reduce API costs
- **Fallback to database** when AI is unavailable

### Using AI Translation

#### GET Request with AI

```bash
curl "http://127.0.0.1:8000/api/v1/translate?word=happiness&lang=yo&use_ai=true"
```

#### POST Request with AI

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/translate" \
     -H "Content-Type: application/json" \
     -d '{"word": "wisdom", "lang": "yo", "use_ai": true}'
```

#### AI Translation Response

```json
{
  "english_word": "wisdom",
  "yoruba_word": "ọgbọ́n",
  "part_of_speech": "noun",
  "example_sentence": "Wisdom comes with age → Ọgbọ́n ńbọ̀ pẹ̀lú ọjọ́",
  "id": 15,
  "created_at": "2024-01-01T12:00:00",
  "updated_at": "2024-01-01T12:00:00",
  "source": "ai"
}
```

### AI Service Status

Check if AI translation is available:

```bash
curl "http://127.0.0.1:8000/api/v1/ai/status"
```

Response:

```json
{
  "available": true,
  "model": "gpt-4o"
}
```

### Testing AI Translation

#### Test with Mock Service (No API Key Required)

```bash
python test_mock_ai.py
```

#### Test with Real OpenAI API

```bash
python test_ai_translation.py
```

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
│   │   ├── translations.py  # Translation endpoints (with AI)
│   │   ├── proverbs.py      # Proverb endpoints
│   │   └── tone_marking.py  # Tone marking endpoints
│   └── services/            # Business logic
│       ├── __init__.py
│       ├── tone_service.py  # Tone marking service
│       ├── ai_translation_service.py  # 🤖 OpenAI integration
│       └── mock_ai_service.py         # 🎭 Mock AI for testing
├── scripts/
│   └── init_db.py           # Database initialization
├── tests/                   # Test files
├── requirements.txt         # Python dependencies
├── run.py                  # Startup script
├── SETUP.md                # Detailed setup guide
├── test_ai_translation.py  # 🤖 AI translation tests
├── test_mock_ai.py         # 🎭 Mock AI tests
└── README.md               # This file
```

---

## 🔗 API Endpoints

### Translations

- `GET /api/v1/translate?word={word}&lang=yo&use_ai={bool}` - Translate English to Yoruba (with optional AI)
- `POST /api/v1/translate` - Translate using POST method
- `GET /api/v1/translations` - Get all translations (paginated)
- `POST /api/v1/translations` - Create new translation
- `GET /api/v1/translations/{id}` - Get specific translation
- `PUT /api/v1/translations/{id}` - Update translation
- `DELETE /api/v1/translations/{id}` - Delete translation
- `GET /api/v1/ai/status` - Check AI translation service status

### Proverbs

- `GET /api/v1/proverbs` - Get all proverbs (paginated)
- `GET /api/v1/proverbs/random` - Get random proverb
- `GET /api/v1/proverbs/{id}` - Get specific proverb
- `POST /api/v1/proverbs` - Create new proverb

### Tone Marking

- `POST /api/v1/tone-mark` - Add tone marks to Yoruba text
- `POST /api/v1/tone-mark/analyze` - Analyze Yoruba text
- `GET /api/v1/tone-mark/history` - Get tone marking history

---

## 📝 Example Usage

### 1. Basic Translation (Database Only)

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
  "updated_at": "2024-01-01T00:00:00",
  "source": "database"
}
```

### 2. AI-Powered Translation

```bash
curl "http://127.0.0.1:8000/api/v1/translate?word=happiness&lang=yo&use_ai=true"
```

**Response:**

```json
{
  "english_word": "happiness",
  "yoruba_word": "ayọ̀",
  "part_of_speech": "noun",
  "example_sentence": "Happiness is important → Ayọ̀ ṣe pàtàkì",
  "id": 16,
  "created_at": "2024-01-01T12:00:00",
  "updated_at": "2024-01-01T12:00:00",
  "source": "ai"
}
```

### 3. Get a Random Yoruba Proverb

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

### 4. Tone Marking for Yoruba Text

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/tone-mark" \
     -H "Content-Type: application/json" \
     -d '{"text": "Omo mi"}'
```

**Response:**

```json
{
  "original_text": "Omo mi",
  "tone_marked_text": "Ọmọ mi"
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

### AI Translation Tests

Test AI translation with mock service:

```bash
python test_mock_ai.py
```

Test AI translation with OpenAI API:

```bash
python test_ai_translation.py
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

| Variable         | Description                        | Default                 |
| ---------------- | ---------------------------------- | ----------------------- |
| `DATABASE_URL`   | Database connection string         | `sqlite:///./yoruba.db` |
| `API_KEY`        | API authentication key             | `yourapikey123`         |
| `DEBUG`          | Enable debug mode                  | `true`                  |
| `OPENAI_API_KEY` | OpenAI API key for AI translations | `None`                  |
| `AI_MODEL`       | OpenAI model to use                | `gpt-4o`                |

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
- [x] **🤖 AI-powered translations**

### Phase 2 (Next) 🔄

- [ ] Word of the Day endpoint
- [ ] Search functionality
- [ ] User authentication
- [ ] Rate limiting
- [ ] PostgreSQL support
- [ ] **🤖 Enhanced AI features (context, cultural notes)**

### Phase 3 (Future) 🔮

- [ ] Speech-to-text API for Yoruba
- [ ] Yoruba spell-checker endpoint
- [ ] Telegram/WhatsApp bot integration
- [ ] Mobile app SDK
- [ ] Audio pronunciation files
- [ ] **🤖 Multi-language AI support**

---

## 🆘 Support & Troubleshooting

### Common Issues

1. **Import errors**: Ensure virtual environment is activated and dependencies are installed
2. **Database errors**: Run `python scripts/init_db.py` to initialize the database
3. **Port conflicts**: Change port in `run.py` or kill processes using port 8000
4. **AI translation errors**: Check OpenAI API key and quota limits

### Getting Help

- Check the [SETUP.md](SETUP.md) for detailed setup instructions
- Review the API documentation at `/docs`
- Check the logs for error messages
- Create an issue in the project repository

---

## 🙏 Acknowledgments

- Yoruba language experts and native speakers
- FastAPI community for the excellent framework
- OpenAI for providing the AI translation capabilities
- Contributors and beta testers

---

**Made with ❤️ for the Yoruba language and culture**

**Powered by 🤖 OpenAI GPT-4o for intelligent translations**
