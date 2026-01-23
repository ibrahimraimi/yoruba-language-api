from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db, Translation
from app.schemas import (
    TranslationCreate, 
    TranslationResponse, 
    TranslationRequest
)
from app.services.ai_translation_service import (
    translate_to_yoruba, 
    is_ai_available
)

router = APIRouter()


@router.get("/translate", response_model=TranslationResponse)
async def translate_word(
    word: str = Query(..., description="English word to translate"),
    lang: str = Query("yo", description="Target language (yo for Yoruba)"),
    use_ai: bool = Query(
        False, 
        description="Use AI translation if not in database"
    ),
    db: Session = Depends(get_db)
):
    """Translate an English word to Yoruba"""
    if lang.lower() != "yo":
        raise HTTPException(
            status_code=400, 
            detail="Only Yoruba (yo) translation is supported"
        )
    
    # First, try to find in database
    translation = db.query(Translation).filter(
        Translation.english_word.ilike(f"%{word}%")
    ).first()
    
    if translation:
        # Return database result
        return TranslationResponse(
            english_word=translation.english_word,
            yoruba_word=translation.yoruba_word,
            part_of_speech=translation.part_of_speech,
            example_sentence=translation.example_sentence,
            id=translation.id,
            created_at=translation.created_at,
            updated_at=translation.updated_at,
            source="database"
        )
    
    # If not in database and AI is requested
    if use_ai and is_ai_available():
        try:
            # Get AI translation
            ai_result = translate_to_yoruba(word)
            
            # Save AI translation to database for future use
            db_translation = Translation(
                english_word=ai_result['word'],
                yoruba_word=ai_result['translation'],
                part_of_speech=ai_result['part_of_speech'],
                example_sentence=ai_result['example']
            )
            db.add(db_translation)
            db.commit()
            db.refresh(db_translation)
            
            # Return AI result
            return TranslationResponse(
                english_word=db_translation.english_word,
                yoruba_word=db_translation.yoruba_word,
                part_of_speech=db_translation.part_of_speech,
                example_sentence=db_translation.example_sentence,
                id=db_translation.id,
                created_at=db_translation.created_at,
                updated_at=db_translation.updated_at,
                source="ai"
            )
            
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"AI translation failed: {str(e)}"
            )
    
    # If AI is not available or not requested
    if use_ai and not is_ai_available():
        raise HTTPException(
            status_code=503,
            detail="AI translation service is not available. Check OpenAI API key."
        )
    
    # Word not found and AI not requested
    raise HTTPException(
        status_code=404, 
        detail=(
            f"Translation for '{word}' not found. "
            "Try setting use_ai=true for AI translation."
        )
    )


@router.post("/translate", response_model=TranslationResponse)
async def translate_word_post(
    request: TranslationRequest,
    db: Session = Depends(get_db)
):
    """Translate an English word to Yoruba using POST method"""
    return await translate_word(
        word=request.word,
        lang=request.lang,
        use_ai=request.use_ai,
        db=db
    )


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
    
    return TranslationResponse(
        english_word=db_translation.english_word,
        yoruba_word=db_translation.yoruba_word,
        part_of_speech=db_translation.part_of_speech,
        example_sentence=db_translation.example_sentence,
        id=db_translation.id,
        created_at=db_translation.created_at,
        updated_at=db_translation.updated_at,
        source="database"
    )


@router.get("/translations", response_model=List[TranslationResponse])
async def get_all_translations(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    """Get all translations with pagination"""
    translations = db.query(Translation).offset(skip).limit(limit).all()
    
    return [
        TranslationResponse(
            english_word=t.english_word,
            yoruba_word=t.yoruba_word,
            part_of_speech=t.part_of_speech,
            example_sentence=t.example_sentence,
            id=t.id,
            created_at=t.created_at,
            updated_at=t.updated_at,
            source="database"
        )
        for t in translations
    ]


@router.get("/ai/status")
async def get_ai_status():
    """Check if AI translation service is available"""
    return {
        "available": is_ai_available(),
        "model": "gpt-4o" if is_ai_available() else None
    }
