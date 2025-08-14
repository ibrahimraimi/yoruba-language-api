from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db, Translation
from app.schemas import TranslationCreate, TranslationResponse

router = APIRouter()


@router.get("/translate", response_model=TranslationResponse)
async def translate_word(
    word: str = Query(..., description="English word to translate"),
    lang: str = Query("yo", description="Target language (yo for Yoruba)"),
    db: Session = Depends(get_db)
):
    """Translate an English word to Yoruba"""
    if lang.lower() != "yo":
        raise HTTPException(
            status_code=400, 
            detail="Only Yoruba (yo) translation is supported"
        )
    
    translation = db.query(Translation).filter(
        Translation.english_word.ilike(f"%{word}%")
    ).first()
    
    if not translation:
        raise HTTPException(
            status_code=404, 
            detail=f"Translation for '{word}' not found"
        )
    
    return translation


@router.post("/translations", response_model=TranslationResponse)
async def create_translation(
    translation: TranslationCreate,
    db: Session = Depends(get_db)
):
    """Create a new translation"""
    db_translation = Translation(**translation.dict())
    db.add(db_translation)
    db.commit()
    db.refresh(db_translation)
    return db_translation


@router.get("/translations", response_model=List[TranslationResponse])
async def get_all_translations(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    """Get all translations with pagination"""
    translations = db.query(Translation).offset(skip).limit(limit).all()
    return translations
