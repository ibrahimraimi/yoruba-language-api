from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class TranslationBase(BaseModel):
    english_word: str
    yoruba_word: str
    part_of_speech: Optional[str] = None
    example_sentence: Optional[str] = None


class TranslationCreate(TranslationBase):
    pass


class TranslationResponse(TranslationBase):
    id: int
    created_at: datetime
    updated_at: datetime
    source: Optional[str] = "database"  # database, ai, or ai_fallback
    
    class Config:
        from_attributes = True


class AITranslationResponse(BaseModel):
    word: str
    translation: str
    part_of_speech: str
    example: str
    source: str = "ai"
    model: Optional[str] = None


class ProverbBase(BaseModel):
    yoruba_text: str
    english_translation: str
    meaning: Optional[str] = None
    category: Optional[str] = None


class ProverbCreate(ProverbBase):
    pass


class ProverbResponse(ProverbBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True


class ToneMarkingRequest(BaseModel):
    text: str


class ToneMarkingResponse(BaseModel):
    original_text: str
    tone_marked_text: str


class WordOfTheDayResponse(BaseModel):
    word: str
    translation: str
    part_of_speech: str
    example: str


class RandomProverbResponse(BaseModel):
    proverb: str
    translation: str
    meaning: str


class SearchResponse(BaseModel):
    results: List[TranslationResponse]
    total: int
    page: int
    per_page: int


class TranslationRequest(BaseModel):
    word: str
    lang: str = "yo"  # Default to Yoruba
    use_ai: bool = False  # Whether to use AI if not in database
