from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.config import settings

# Create async database engine
engine = create_async_engine(
    settings.database_url,
    echo=settings.debug,
)

# Create async session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)

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


# Dependency to get async database session
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
