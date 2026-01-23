from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from app.config import settings

# Create database engine
engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False} 
    if "sqlite" in settings.database_url else {}
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()


class Translation(Base):
    __tablename__ = "translations"
    
    id = Column(Integer, primary_key=True, index=True)
    english_word = Column(String(100), index=True, nullable=False)
    yoruba_word = Column(String(100), nullable=False)
    part_of_speech = Column(String(50))
    example_sentence = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime, 
        default=datetime.utcnow, 
        onupdate=datetime.utcnow
    )


class Proverb(Base):
    __tablename__ = "proverbs"
    
    id = Column(Integer, primary_key=True, index=True)
    yoruba_text = Column(Text, nullable=False)
    english_translation = Column(Text, nullable=False)
    meaning = Column(Text)
    category = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)


class ToneMarking(Base):
    __tablename__ = "tone_markings"
    
    id = Column(Integer, primary_key=True, index=True)
    original_text = Column(Text, nullable=False)
    tone_marked_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
